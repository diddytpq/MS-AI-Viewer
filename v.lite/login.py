import sys
import os
from pathlib import Path

from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QLabel, QWidget, QDialog, QListWidgetItem, QPushButton, QHBoxLayout, QVBoxLayout
from PySide6.QtGui import QImage, QPixmap, QWheelEvent
from PySide6.QtCore import QEvent, Qt, QThread, Signal, QRect, QPoint, QTimer, QDate, QUrl, QSize, QItemSelection
from PySide6 import QtCore

import numpy as np

import socket
import json
import requests
from multiprocessing import Process

import time
from datetime import datetime, timedelta
import traceback
import gc

from ui import login_ui
from utils import FadeOutWindow, Plot_Camera_Viewer, Connect_Camera, load_info, save_info

from main import MainWindow
from ui.main_ui import Ui_MainWindow
from ui.window_object_setting import open_object_setting_window

Kor2eng = {
    "침입": "Intrusion",
    "배회": "Loitering",
    "쓰러짐": "Falldown",
    "방화": "Fire",
    "싸움": "Fight",
}

Eng2kor = {
    "Intrusion": "침입",
    "Loitering": "배회",
    "Falldown": "쓰러짐",
    "Fire": "방화",
    "Fight": "싸움",
}


class LoginWindow(QMainWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()
        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : start login window")
        # self.client_ip = requests.get("https://api.ipify.org?format=text").text
        self.client_ip = "127.0.0.1"
        self.local_ip = self.client_ip


        # with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        #     s.connect(("8.8.8.8", 80))
        #     self.local_ip = s.getsockname()[0]

        self.ui_login = login_ui.Ui_login_windows()

        self.setWindowTitle("MS-AI")
        self.ui_login.setupUi(self)
        self.ui_login.login_bn.clicked.connect(self.check_login)

        self.setup_event_filters()
        self.ai_sever_info_path = os.path.join(os.getcwd(), "ai_sever_info.json")

        # AI 서버 정보 로드
        try:
            with open(self.ai_sever_info_path, "r", encoding="UTF-8") as f:
                self.ai_server_info = json.load(f)

            self.ui_login.ai_server_ip_input.setText(self.ai_server_info.get("ai_server_ip", ""))
            self.ui_login.ai_server_port_input.setText(self.ai_server_info.get("ai_server_port", ""))
        except FileNotFoundError:
            print("AI server info file not found. Using default values.")
            self.ai_server_info = {"ai_server_ip": "", "ai_server_port": ""}

    def setup_event_filters(self):
        # 이벤트 필터 설치
        event_filters = [
            self.ui_login.id_input,
            self.ui_login.pw_input,
            self.ui_login.ai_server_ip_input,
            self.ui_login.ai_server_port_input,
        ]
        for filter in event_filters:
            filter.installEventFilter(self)

    def eventFilter(self, obj, event):
        if event.type() in (QEvent.FocusIn, QEvent.FocusOut):
            color = "green" if event.type() == QEvent.FocusIn else "rgb(36, 39, 44)"
            if obj == self.ui_login.id_input:
                self.set_line_style(self.ui_login.id_line, color)
            elif obj == self.ui_login.pw_input:
                self.set_line_style(self.ui_login.pw_line, color)
            elif obj == self.ui_login.ai_server_ip_input:
                self.set_line_style(self.ui_login.ai_server_ip_line, color)
            elif obj == self.ui_login.ai_server_port_input:
                self.set_line_style(self.ui_login.ai_server_port_line, color)

        return super().eventFilter(obj, event)

    def set_line_style(self, line_widget, color):
        # 라인 스타일 변경
        line_widget.setStyleSheet(f"background-color: {color}")
        
    def keyPressEvent(self, event):
        if event.key() in (Qt.Key_Enter, Qt.Key_Return):  # Enter 키 또는 Return 키를 눌렀을 경우
            self.check_login()

    def check_login(self):
        try:
            print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : Try login")

            # 로그인 데이터 준비
            # data = {"msg" : 
            #             {"id" : self.ui_login.id_input.text(), 
            #             "password" : self.ui_login.pw_input.text(),
            #             "client_ip" : self.client_ip,
            #             "client_local_ip" : self.local_ip
            #             }
            #         }
            
            # url = f'http://{self.ui_login.ai_server_ip_input.text()}:{self.ui_login.ai_server_port_input.text()}/login'

            # receive_data = requests.post(url, json=data, timeout=3).json()

            if self.ui_login.id_input.text() == "admin" and self.ui_login.pw_input.text() == "admin":
                receive_data = "로그인 성공"
                self.handle_successful_login(receive_data)
            else:
                receive_data = "로그인 실패"
                print(receive_data)
                self.create_fade_out_msg(msg=receive_data["data"])

        except Exception as e:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            tb = traceback.format_exc()
            print(f"Error occurred at {current_time}: {e}\n{tb}", file=sys.stderr)

    def handle_successful_login(self, receive_data):
        # 로그인 성공 처리
        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : succese login")

        self.close()

        self.main_window = MainWindow(user_info="admin", 
                                      host=self.ui_login.ai_server_ip_input.text(), 
                                      port=self.ui_login.ai_server_port_input.text(),
                                      client_ip = f"{self.client_ip}@{self.local_ip}")
        self.main_window.show()
        # self.create_fade_out_msg(msg="login")
        self.save_ai_server_info()

    def save_ai_server_info(self):
        # AI 서버 정보 저장
        with open(self.ai_sever_info_path, "w", encoding="UTF-8") as f:
            self.ai_server_info["ai_server_ip"] = self.ui_login.ai_server_ip_input.text()
            self.ai_server_info["ai_server_port"] = self.ui_login.ai_server_port_input.text()
            f.write(json.dumps(self.ai_server_info))

    def create_fade_out_msg(self, msg="None"):
            if not hasattr(self, 'fadeout_window') or not self.fadeout_window.isVisible():
                self.fadeout_window = FadeOutWindow(self, msg)

                main_window_rect = self.geometry()
                fadeout_window_rect = self.fadeout_window.geometry()
                self.fadeout_window.move(
                    main_window_rect.left() + (main_window_rect.width() - fadeout_window_rect.width()) // 2,
                    main_window_rect.top() + (main_window_rect.height() - fadeout_window_rect.height() * 1.7)
                )

            self.fadeout_window.show()


class MainWindow(QMainWindow):
    def __init__(self, user_info, host, port, client_ip):
        super(MainWindow, self).__init__()
        self.ui_main = Ui_MainWindow()
        self.setWindowTitle("MS-AI")
        self.ui_main.setupUi(self)
        self.user_info = user_info
        self.HOST = host
        self.PORT = port
        self.client_ip = client_ip
        self.camera_edit_permission = False
        self.camera_page_worker = None


        self.admin_info_temp = load_info(host=self.HOST,port=self.PORT,file_name="admin_info")
        self.setting_info_temp = load_info(host=self.HOST, port=self.PORT, file_name="setting_info")
        self.login_info_temp = load_info(host=self.HOST, port=self.PORT, file_name="login_info")
        self.camera_info_dict_temp = load_info(host=self.HOST, port=self.PORT, file_name="camera_info")

        self.ui_main.server_ip_input.setText(self.camera_info_dict_temp["ip"])
        self.ui_main.server_id_input.setText(self.camera_info_dict_temp["id"])
        self.ui_main.server_pw_input.setText(self.camera_info_dict_temp["pw"])

        self.ui_main.server_login_bnt.clicked.connect(self.connect_camera_bnt)
        self.ui_main.camera_page_detect_add_bnt.clicked.connect(self.camera_page_add_detect_type)
        self.ui_main.camera_page_object_setting_bnt.clicked.connect(lambda click, instance = self : open_object_setting_window(click, instance))
        self.ui_main.camera_page_detect_area_del_bnt.clicked.connect(self.camera_page_del_detect_area)
        self.ui_main.camera_page_ai_bnt.clicked.connect(self.run_ms_ai)
        self.ui_main.shutdown_bnt.clicked.connect(self.shutdown) #종료 버튼 활성화


        self.setup_camera_viewer()

    def create_fade_out_msg(self, std_window=None, msg="None"):
            try:
                if not hasattr(self, 'fadeout_window') or not self.fadeout_window.isVisible():
                    self.fadeout_window = FadeOutWindow(self, msg)

                    if std_window is None:
                        main_window_rect = self.geometry()
                        fadeout_window_rect = self.fadeout_window.geometry()
                        self.fadeout_window.move(
                            main_window_rect.left() + (main_window_rect.width() - fadeout_window_rect.width()) // 2,
                            main_window_rect.top() + (main_window_rect.height() - fadeout_window_rect.height()) * 4 // 5
                        )
                    else:
                        # Always keep the fadeout window on top
                        self.fadeout_window.setWindowFlags(self.fadeout_window.windowFlags() | Qt.WindowStaysOnTopHint)
                        main_window_rect = std_window.geometry()
                        fadeout_window_rect = self.fadeout_window.geometry()
                        self.fadeout_window.move(
                            main_window_rect.left() + (main_window_rect.width() - fadeout_window_rect.width()) // 2,
                            main_window_rect.top() + (main_window_rect.height() - fadeout_window_rect.height()) * 4 // 5
                        )
                        # Ensure it is above the schedule_window
                        # self.fadeout_window.raise_()
                        # self.fadeout_window.activateWindow()

                self.fadeout_window.show()
                # self.fadeout_window.raise_()          # Bring the window to the front
                # self.fadeout_window.activateWindow()  # Focus the window

            except Exception as e:
                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                tb = traceback.format_exc()
                print(f"Error occurred at {current_time}: {e}\n{tb}", file=sys.stderr)

    def setup_camera_viewer(self):
        print("setup camera viewer")
        self.ui_main.camera_page_viewer.hide()
        self.ui_main.camera_page_viewer = Plot_Camera_Viewer(self.ui_main.ai_camera_page)
        self.ui_main.camera_page_viewer.setObjectName(u"camera_page_viewer")
        self.ui_main.camera_page_viewer.setMinimumSize(QSize(472, 331))
        self.ui_main.camera_page_viewer.setStyleSheet(u"border: 1px solid rgb(119, 118, 123);\n"
                                                "background-color: rgba(255, 255, 255, 0);")
        self.ui_main.camera_page_viewer.setScaledContents(True)
        self.ui_main.verticalLayout_10.addWidget(self.ui_main.camera_page_viewer)
        self.ui_main.camera_page_viewer.clicked.connect(self.camera_page_add_detect_area_point)

    def camera_page_add_detect_area_point(self, point): #마우스 클릭으로 생성된 포인트를 viewer에 표시
        try:
            if self.camera_edit_permission:
                print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : camera_page_add_detect_area_point")
                camera_name = "main"
                select_index = self.ui_main.camera_page_detect_area_table.selectionModel().selectedRows()

                if select_index:  # 선택된 행이 있다면
                    select_row = select_index[0].row()

                    if point.x() == -1 :
                        if len(self.camera_info_dict_temp["detect_info"][select_row]) > 1:
                            self.camera_info_dict_temp["detect_info"][select_row].pop()

                        else: pass
                    else:
                        self.camera_info_dict_temp["detect_info"][select_row].append([point.x()/ self.ui_main.camera_page_viewer.width(), 
                                                                                                point.y()/self.ui_main.camera_page_viewer.height()])

                    self.ui_main.camera_page_viewer.set_point(self.camera_info_dict_temp["detect_info"][select_row][1:], [self.ui_main.camera_page_viewer.width(), self.ui_main.camera_page_viewer.height()])

                    gray_point_list = []
                    if self.camera_info_dict_temp["AI"] == False:
                        for index, value in enumerate(self.camera_info_dict_temp["detect_info"]):
                            # 현재 인덱스가 제외할 인덱스 목록에 없으면 결과 리스트에 추가
                            if index != select_row:
                                gray_point_list.append(value[1:])

                    self.ui_main.camera_page_viewer.set_gray_point(gray_point_list)
            
        except Exception as e:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            tb = traceback.format_exc()
            print(f"Error occurred at {current_time}: {e}\n{tb}", file=sys.stderr)

    def camera_page_add_detect_type(self):
        try:
            if self.camera_edit_permission:
                print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : camera_page_add_detect_type")
                detect_type = self.ui_main.camera_page_camera_event_box.currentText()

                detect_type = Kor2eng[detect_type]

                #add_detect_type
                if detect_type in ["Intrusion", "Loitering", "Falldown", "Fire", "Fight"]:
                    self.camera_info_dict_temp["detect_info"].append([detect_type])

                    print(self.camera_info_dict_temp)

                    for i in range(7):
                        self.camera_info_dict_temp["detect_schedule"][str(i)][detect_type] = [[0, 24]]


                self.reset_detect_area_list(self.camera_info_dict_temp["detect_info"])

                lastRow = self.ui_main.camera_page_detect_area_table.rowCount() - 1  
                if lastRow >= 0:
                    # 마지막 행의 첫 번째 셀을 현재 셀로 설정
                    self.ui_main.camera_page_detect_area_table.setCurrentCell(lastRow, 0)
                else:
                    self.create_fade_out_msg(msg="테이블이 비어 있습니다.")
                    

                gray_point_list = []
                if self.camera_info_dict_temp["AI"] == False:
                    for index, value in enumerate(self.camera_info_dict_temp["detect_info"]):
                        # 현재 인덱스가 제외할 인덱스 목록에 없으면 결과 리스트에 추가
                        gray_point_list.append(value[1:])

                self.ui_main.camera_page_viewer.reset_green_area()
                self.ui_main.camera_page_viewer.set_gray_point(gray_point_list)

                save_info(host=self.HOST, port=self.PORT, file_name="camera_info", info = self.camera_info_dict_temp)

            else:
                print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : Not allow camera page edit permission")
                self.create_fade_out_msg(msg = "수정 권한이 없습니다.")

        except Exception as e:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            tb = traceback.format_exc()
            print(f"Error occurred at {current_time}: {e}\n{tb}", file=sys.stderr)

    def camera_page_del_detect_area(self):
            try:
                if self.camera_edit_permission:
                    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : camera_page_del_detect_area")

                    select_index = self.ui_main.camera_page_detect_area_table.selectionModel().selectedRows()
                    if select_index:  # 선택된 행이 있다면
                        select_row = select_index[0].row()
                        del self.camera_info_dict_temp["detect_info"][select_row]

                    self.reset_detect_area_list(self.camera_info_dict_temp["detect_info"])
                    self.ui_main.camera_page_viewer.reset_green_area()

                    save_info(host=self.HOST, port=self.PORT, file_name="camera_info", info = self.camera_info_dict_temp)

                else:
                    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : Not allow camera page edit permission")
                    self.create_fade_out_msg(msg ="수정 권한이 없습니다.")

            except Exception as e:
                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                tb = traceback.format_exc()
                print(f"Error occurred at {current_time}: {e}\n{tb}", file=sys.stderr)

    def reset_detect_area_list(self, camera_detect_info):
        self.ui_main.camera_page_detect_area_table.setRowCount(0)

        for detect_type_list in camera_detect_info:
            detect_type_text = Eng2kor[detect_type_list[0]]

            row_position = self.ui_main.camera_page_detect_area_table.rowCount()
            self.ui_main.camera_page_detect_area_table.insertRow(row_position)
            text = QTableWidgetItem(detect_type_text)
            text.setTextAlignment(Qt.AlignCenter)
            text.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled)
            self.ui_main.camera_page_detect_area_table.setItem(row_position, 0, text)

    def connect_camera_bnt(self):
        ip = self.ui_main.server_ip_input.text()
        id = self.ui_main.server_id_input.text()
        pw = self.ui_main.server_pw_input.text()

        pipe = f"rtsp://{id}:{pw}@{ip}:554/stream1"
        print(pipe)

        if self.camera_page_worker is not None:
            self.camera_page_worker.stop()
            del self.camera_page_worker
            self.camera_page_worker = None


        self.camera_page_worker = Connect_Camera(pipe = pipe)
        self.camera_page_worker.ImageUpdated.connect(lambda image, viewer=self.ui_main.camera_page_viewer: self.ShowCamera(viewer, image))
        self.camera_page_worker.start()

        self.camera_info_dict_temp["ip"] = self.ui_main.server_ip_input.text()
        self.camera_info_dict_temp["id"] = self.ui_main.server_id_input.text()
        self.camera_info_dict_temp["pw"] = self.ui_main.server_pw_input.text()

        save_info(host=self.HOST, port=self.PORT, file_name="camera_info", info = self.camera_info_dict_temp)

        self.camera_edit_permission = True

        self.reset_detect_area_list(self.camera_info_dict_temp["detect_info"])

    @QtCore.Slot()
    def ShowCamera(self, view, frame: QImage) -> None:
        # frame = frame.scaled(view.width(), view.height(), Qt.IgnoreAspectRatio, Qt.FastTransformation)
        view.setPixmap(QPixmap.fromImage(frame))

    def shutdown(self):
        QApplication.instance().quit()
        if self.camera_page_worker is not None:
            self.camera_page_worker.stop()
            del self.camera_page_worker
        # self.stop_camera_page_worker()
        # self.stop_live_page_worker()
        # self.return_camera_page_permission()

    def run_ms_ai(self):
        save_info(host=self.HOST, port=self.PORT, file_name="camera_info", info = self.camera_info_dict_temp)

        data = {"msg" : "ms_ai"}
        url = f'http://{self.HOST}:{self.PORT}/run_ms_ai'
        receive_data = requests.post(url, json=data).json()

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
            
            # input("Press Enter to close...")  # 실행 후 입력을 기다림
            pass
    
if __name__ == "__main__":
        main()



