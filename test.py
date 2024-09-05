import sys
import os
from pathlib import Path

from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QLabel, QWidget, QDialog, QListWidgetItem
from PySide6.QtCore import QEvent, Qt, QThread, Signal, QRect, QPoint, QTimer, QDate, QUrl, QSize
from PySide6 import QtCore
from ui.login_ui import Ui_Dialog
from ui.main_ui import Ui_MainWindow

import json
import requests
from requests.auth import HTTPBasicAuth
import threading

from utils import (Connect_Camera, Plot_Camera_Viewer, FadeOutWindow, Livepage_view, FadeOutInWindow,
                  Eng2kor, Kor2eng, send_email_alarm, load_info, save_info, Connect_Camera_Group)
import time
from datetime import datetime, timedelta
import traceback
import gc

class LoginWindow(QMainWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.ui_login = Ui_Dialog()

        self.setWindowTitle("MS-AI")
        self.ui_login.setupUi(self)
        # self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
        self.ui_login.login_bn.clicked.connect(self.check_login)
        # self.setGeometry(200, 200, 1280, 720)

        self.ui_login.id_input.installEventFilter(self)  # 이벤트 필터 설치
        self.ui_login.pw_input.installEventFilter(self)  # 이벤트 필터 설치
        self.ui_login.ai_server_ip_input.installEventFilter(self)  # 이벤트 필터 설치
        self.ui_login.ai_server_port_input.installEventFilter(self)  # 이벤트 필터 설치

        self.ai_sever_info_path = os.path.join(os.getcwd(), "ai_sever_info.json")

        with open(self.ai_sever_info_path, "r", encoding="UTF-8") as f:
            self.ai_server_info = json.load(f)

        if len(self.ai_server_info["ai_server_ip"]):
            self.ui_login.ai_server_ip_input.setText(self.ai_server_info["ai_server_ip"])

        if len(self.ai_server_info["ai_server_port"]):
            self.ui_login.ai_server_port_input.setText(self.ai_server_info["ai_server_port"])
        
    def eventFilter(self, obj, event):
        if obj == self.ui_login.id_input:
            if event.type() == QEvent.FocusIn:  # 커서가 id_input에 들어가면
                self.ui_login.id_line.setStyleSheet("background-color: green")  # id_line을 초록색으로 변경
            elif event.type() == QEvent.FocusOut:  # 커서가 id_input에서 나가면
                self.ui_login.id_line.setStyleSheet("background-color: rgb(36, 39, 44)")  # id_line을 원래 색상으로 변경

        if obj == self.ui_login.pw_input:
            if event.type() == QEvent.FocusIn:  # 커서가 id_input에 들어가면
                self.ui_login.pw_line.setStyleSheet("background-color: green")  # id_line을 초록색으로 변경
            elif event.type() == QEvent.FocusOut:  # 커서가 id_input에서 나가면
                self.ui_login.pw_line.setStyleSheet("background-color: rgb(36, 39, 44)")  # id_line을 원래 색상으로 변경
        
        if obj == self.ui_login.ai_server_ip_input:
            if event.type() == QEvent.FocusIn:  # 커서가 id_input에 들어가면
                self.ui_login.ai_server_ip_line.setStyleSheet("background-color: green")  # id_line을 초록색으로 변경
            elif event.type() == QEvent.FocusOut:  # 커서가 id_input에서 나가면
                self.ui_login.ai_server_ip_line.setStyleSheet("background-color: rgb(36, 39, 44)")  # id_line을 원래 색상으로 변경

        if obj == self.ui_login.ai_server_port_input:
            if event.type() == QEvent.FocusIn:  # 커서가 id_input에 들어가면
                self.ui_login.ai_server_port_line.setStyleSheet("background-color: green")  # id_line을 초록색으로 변경
            elif event.type() == QEvent.FocusOut:  # 커서가 id_input에서 나가면
                self.ui_login.ai_server_port_line.setStyleSheet("background-color: rgb(36, 39, 44)")  # id_line을 원래 색상으로 변경
                
        return super().eventFilter(obj, event)
    
    def keyPressEvent(self, event):
            if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:  # Enter 키 또는 Return 키를 눌렀을 경우
                self.check_login()

    def check_login(self):
        try:
            data = {"msg" : {"id" : self.ui_login.id_input.text(), 
                            "password" : self.ui_login.pw_input.text()}}
            
            # receive_data = socket_communication(self.HOST, self.PORT, cmd, on_data_received)
            self.HOST = self.ui_login.ai_server_ip_input.text()
            self.PORT = self.ui_login.ai_server_port_input.text()
            url = f'http://{self.HOST}:{self.PORT}/login'

            # auth = HTTPBasicAuth(self.ui_login.id_input.text(), self.ui_login.pw_input.text())

            # receive_data = requests.post(url,auth=auth, json=data).json()
            print(url)
            receive_data = requests.post(url, json=data).json()

            if receive_data["success"]:
                self.close()
                
                # self.send_message(data = data)
                self.create_fade_out_msg(msg = "login")

                with open(self.ai_sever_info_path, "w", encoding="UTF-8") as f:
                    self.ai_server_info["ai_server_ip"] = self.ui_login.ai_server_ip_input.text()
                    self.ai_server_info["ai_server_port"] = self.ui_login.ai_server_port_input.text()

                    f.write(json.dumps(self.ai_server_info))
                
            else:
                print(receive_data)
                self.create_fade_out_msg(msg = receive_data["data"])
                
        except Exception as e:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            tb = traceback.format_exc()
            print(f"Error occurred at {current_time}: {e}\n{tb}", file=sys.stderr)

            # elif self.ui_login.id_input.text() == "user" and self.ui_login.pw_input.text() == "1234":
            #     self.main_window = MainWindow()
            #     self.main_window.show()
            #     self.close()
            #     print("사용자 로그인")

    def create_fade_out_msg(self, msg="None"):
            if not hasattr(self, 'fadeout_window') or not self.fadeout_window.isVisible():
                self.fadeout_window = FadeOutWindow(self, msg)

                main_window_rect = self.geometry()
                fadeout_window_rect = self.fadeout_window.geometry()
                self.fadeout_window.move(
                    main_window_rect.left() + (main_window_rect.width() - fadeout_window_rect.width()) // 2,
                    main_window_rect.top() + (main_window_rect.height() - fadeout_window_rect.height()) * 4 // 5
                )

            self.fadeout_window.show()



def main():
    try:
        # time.sleep(1)
        app = QApplication(sys.argv)
        window = LoginWindow()
        window.show()
        app.exec()

    except Exception as e:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            tb = traceback.format_exc()
            print(f"Error occurred at {current_time}: {e}\n{tb}", file=sys.stderr)
    finally:
            input("Press Enter to close...")  # 실행 후 입력을 기다림
    
if __name__ == "__main__":
        main()
