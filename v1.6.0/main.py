import sys
import os
from pathlib import Path
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QLabel, QWidget, QDialog, QListWidgetItem, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout, QSystemTrayIcon, QMenu
from PySide6.QtGui import QImage, QPixmap, QWheelEvent, QIcon, QAction
from PySide6.QtCore import QEvent, Qt, QThread, Signal, QRect, QPoint, QTimer, QDate, QUrl, QSize, QItemSelection
from PySide6 import QtCore
from ui.ui_login import Ui_Dialog
from ui.ui_main import Ui_MainWindow


from ui.utils_ai_setting_window import open_ai_setting_window
from ui.utils_schedule_window import open_schedule_window
from ui.utils_object_setting_window import open_object_setting_window
from ui.utils_search_window import open_search_window
from ui.utils_labeling_window import open_labeling_window
import numpy as np

import socket
import json
import requests
from requests.auth import HTTPBasicAuth
import threading
import base64
import cv2
import re

from utils import (Connect_Camera, Plot_Camera_Viewer, FadeOutWindow, NotificationManager,
                  Eng2kor, Kor2eng, load_info, save_info, 
                  print_error, check_nvidia_gpu)
import time
from datetime import datetime, timedelta
import traceback
import gc
import math

NOTICE_DURATION = {
    0: 3000,
    1: 5000,
    2: 10000,
    3: 60000,
    4: -1,
}

FIRST_NOTICE = True

class LoginWindow(QMainWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()
        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : start login window")
        
        try:
            self.client_ip = requests.get("https://api.ipify.org?format=text").text

            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                s.connect(("8.8.8.8", 80))
                self.local_ip = s.getsockname()[0]
        except :
            self.client_ip = "127.0.0.1"
            self.local_ip = "127.0.0.1"

        self.ui_login = Ui_Dialog()

        self.setWindowTitle("MS-AI")
        self.ui_login.setupUi(self)
        # self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
        self.ui_login.login_bn.clicked.connect(self.check_login)
        # self.setGeometry(200, 200, 1280, 720)

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
            data = {"msg" : 
                        {"id" : self.ui_login.id_input.text(), 
                        "password" : self.ui_login.pw_input.text(),
                        "client_ip" : self.client_ip,
                        "client_local_ip" : self.local_ip
                        }
                    }
            
            url = f'http://{self.ui_login.ai_server_ip_input.text()}:{self.ui_login.ai_server_port_input.text()}/login'

            try:
                receive_data = requests.post(url, json=data, timeout=3).json()
            except Exception as e:
                self.create_fade_out_msg(msg="지능형 서버 상태를 확인해주세요.")
                return

            if receive_data["success"]:
                self.handle_successful_login(receive_data)


        except Exception as e:
            print_error(e)

    def handle_successful_login(self, receive_data):
        # 로그인 성공 처리
        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : succese login")

        self.close()
        self.main_window = MainWindow(user_info=receive_data["user_info"], 
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

    def create_fade_out_msg(self, std_window=None, msg="None"):
        try:
            if not hasattr(self, 'fadeout_window') or not self.fadeout_window.isVisible():
                # std_window가 제공되면 해당 윈도우를 parent로 사용, 아니면 self 사용
                parent_window = std_window if std_window is not None else self
                self.fadeout_window = FadeOutWindow(parent_window, msg)
                # 항상 최상위에 표시되도록 설정
                self.fadeout_window.setWindowFlags(self.fadeout_window.windowFlags() | Qt.WindowStaysOnTopHint)

                if std_window is None:
                    main_window_rect = self.geometry()
                    fadeout_window_rect = self.fadeout_window.geometry()
                    self.fadeout_window.move(
                        main_window_rect.left() + (main_window_rect.width() - fadeout_window_rect.width()) // 2,
                        main_window_rect.top() + (main_window_rect.height() - fadeout_window_rect.height()) * 4 // 5
                    )
                else:
                    main_window_rect = std_window.geometry()
                    fadeout_window_rect = self.fadeout_window.geometry()
                    self.fadeout_window.move(
                        main_window_rect.left() + (main_window_rect.width() - fadeout_window_rect.width()) // 2,
                        main_window_rect.top() + (main_window_rect.height() - fadeout_window_rect.height()) * 4 // 5
                    )

            self.fadeout_window.show()
            self.fadeout_window.raise_()          # 윈도우를 최상위로 올림
            self.fadeout_window.activateWindow()  # 윈도우를 활성화

        except Exception as e:
            print_error(e)


class MainWindow(QMainWindow):
    def __init__(self, user_info, host, port, client_ip):
        super(MainWindow, self).__init__()
        self.ui_main = Ui_MainWindow()
        self.setWindowTitle("MS-AI")
        self.ui_main.setupUi(self)
        self.user_info = user_info
        self.open_labeling_window = False
        self.HOST = host
        self.PORT = port
        self.client_ip = client_ip

        # 커스텀 알림 관리자 초기화
        self.notification_manager = NotificationManager(on_click_callback=self.on_notification_clicked_handler)

        self.setup_init_GUI()
        self.setup_slot_connect()
        self.setup_event_filters()

        self.switch_main_display_to_camera()

        self.before_active_window = None
        # self.active_window_timer = QTimer(self)
        # self.active_window_timer.timeout.connect(self.check_window_active)
        # self.active_window_timer.start(1000)  # Check every 1 second

        # self.showMaximized()
        # 윈도우 플래그 설정: 최대화 버튼 활성화
        # self.setWindowState(Qt.WindowNoState)
        # self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMaximizeButtonHint | Qt.WindowMinimizeButtonHint)

        # self.change_live_page_camera_fps(10)

#---------------------------------------------------------------------------------------------------------#
    def connect_camera_page_camera(self, camera_name = None, tray_notify=False):
        try:
            self.stop_camera_page_worker()

            print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : connect_camera_page_camera")
            if camera_name == None:
                camera_name = self.ui_main.camera_page_name_box.currentText()

            nvr_id = self.login_info_temp["NVR"]["ID"]
            nvr_pw = self.login_info_temp["NVR"]["PW"]
            nvr_ip = self.login_info_temp["NVR"]["IP"]

            if camera_name in self.camera_info_dict_temp.keys():
                camera_info = self.camera_info_dict_temp[camera_name]
                camera_num = camera_info["Num"]

                
                if check_nvidia_gpu(): pipe = f"{nvr_id}:{nvr_pw}@{nvr_ip}/video{camera_num}"
                else:pipe = f"{nvr_id}:{nvr_pw}@{nvr_ip}/video{camera_num}"

                
                if tray_notify:
                    live_viewer_blcok_active = False
                    # 10초 타이머 설정하여 다시 연결
                    QTimer.singleShot(10000, lambda: self.connect_camera_page_camera(camera_name))
                else:
                    live_viewer_blcok_active = self.admin_info_temp["FN_PERMISSION"]["live_viewer_block_active"]

                self.camera_page_worker = Connect_Camera(pipe = pipe,
                                                        host=self.HOST, 
                                                        port=self.PORT, 
                                                        camera_name = camera_info["Name"], 
                                                        # camera_num=camera_info["Num"], 
                                                        roi_thickness = 2,
                                                        plot_bbox=self.setting_info_temp["DETECT"]["Bbox"],
                                                        plot_label=self.setting_info_temp["DETECT"]["Label"],
                                                        plot_roi = self.setting_info_temp["DETECT"]["Roi"],
                                                        viewer = self.ui_main.camera_page_viewer,
                                                        live_viewer_blcok_active = live_viewer_blcok_active)

                self.camera_page_worker.ImageUpdated.connect(lambda image, viewer=self.ui_main.camera_page_viewer: self.ShowCamera(viewer, image))
                self.camera_page_worker.start()

            else:
                print("선택된 카메라는 존재하지 않습니다.")
                
        except Exception as e:
            print_error(e)

    def save_admin_info(self):
        try:
            self.ui_main.setting_notion_widget.show() if self.admin_info_temp["FN_PERMISSION"]["sms_active"] == 1 else self.ui_main.setting_notion_widget.hide()
            self.ui_main.setting_self_labeling_widget.show() if self.admin_info_temp["FN_PERMISSION"]["self_labeling_active"] == 1 else self.ui_main.setting_self_labeling_widget.hide()

            # 텍스트를 정수로 변환하여 저장
            self.admin_info_temp["LICENSE"]["allow_camera_num"] = int(self.ui_main.license_camera_allow_num_input.text())
            self.admin_info_temp["FN_PERMISSION"]["sms_allow_phone_num"] = int(self.ui_main.admin_sms_alarm_allow_phone_num_input.text())
            

            save_info(host=self.HOST, port=self.PORT, file_name="admin_info", info=self.admin_info_temp)
            self.create_fade_out_msg(msg="save admin info")

        except Exception as e:
            print_error(e)

    def login_admin_page(self):
        try:
            data = {"msg" : str(self.ui_main.admin_pw_input.text())}
            url = f'http://{self.HOST}:{self.PORT}/login_admin_page'
            receive_data = requests.post(url, json=data).json()

            if receive_data["msg"] == True:
                self.switch_main_display_to_admin_2()
                self.ui_main.stackedWidget_2.setCurrentIndex(0)

                self.reset_admin_license_list()
            else:
                self.create_fade_out_msg(msg="Invalid PW")

        except Exception as e:
            print_error(e)

    def start_camera_connect_status_timer(self):
        self.camera_alarm_info_dict = {}
        self.last_notification_info = None  # 최근 알림 정보 저장 (카메라 이름, 시간)

        if self.camera_connect_timer is not None :
            self.camera_connect_timer.stop()
            del self.camera_connect_timer
        self.check_camera_connect_status()

        self.camera_connect_timer = QTimer(self)
        self.camera_connect_timer.timeout.connect(self.check_camera_connect_status)

        self.camera_connect_timer.start(5000)  # 타이머 시작 5초에 한번씩

    def notify(self, title, message, camera_name=None, alarm_time=None):
        """커스텀 알림 표시"""
        # 최근 알림 정보 저장
        self.last_notification_info = {
            "camera_name": camera_name,
            "alarm_time": alarm_time
        }
        # 커스텀 알림 매니저를 통해 알림 표시
        notification_data = {
            "camera_name": camera_name,
            "alarm_time": alarm_time
        }

        duration = self.setting_info_temp["NOTICE"]["duration"]
        # self.notification_manager.show(title, message, notification_data, duration=10000)
        self.notification_manager.show(title, message, notification_data, duration=NOTICE_DURATION[duration])


    def change_setting_info(self):
        try:
            print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : change_setting_info")
            self.setting_info_temp = load_info(host=self.HOST, port=self.PORT, file_name="setting_info")

            self.setting_info_temp["DETECT"]["Bbox"] = int(self.ui_main.setting_detect_bbox_active_bnt.isChecked())
            self.setting_info_temp["DETECT"]["Label"] = int(self.ui_main.setting_detect_label_active_bnt.isChecked())
            self.setting_info_temp["DETECT"]["Roi"] = int(self.ui_main.setting_detect_roi_active_bnt.isChecked())

            self.camera_page_worker.plot_bbox = self.setting_info_temp["DETECT"]["Bbox"] == 1
            self.camera_page_worker.plot_label = self.setting_info_temp["DETECT"]["Label"] == 1
            self.camera_page_worker.plot_roi = self.setting_info_temp["DETECT"]["Roi"] == 1

            if self.ui_main.setting_notice_phone_active_bnt.isChecked():
                self.setting_info_temp["SMS"]["active"] = 1
            else:
                self.setting_info_temp["SMS"]["active"] = 0

            if self.ui_main.setting_event_pop_up_active_bnt.isChecked():
                self.setting_info_temp["NOTICE"]["active"] = 1
            else:
                self.setting_info_temp["NOTICE"]["active"] = 0

            self.setting_info_temp["NOTICE"]["duration"] = self.ui_main.setting_event_pop_up_duration_box.currentIndex()

            self.create_fade_out_msg(msg="설정이 저장되었습니다")
            save_info(host=self.HOST, port=self.PORT, file_name="setting_info", info=self.setting_info_temp)

        except Exception as e:
            print_error(e)

    def check_camera_viewer_click(self, viewer):
        if viewer.click_count >= 1:
            self.switch_main_display_to_camera()
            self.set_button_style('camera')
            self.ui_main.stackedWidget.setCurrentIndex(1)
            index = self.ui_main.camera_page_name_box.findText(viewer.camera_name)
            self.ui_main.camera_page_name_box.setCurrentIndex(index)

            for camera_name, camera_viewer in self.camera_view_list.items():
                camera_viewer.click_count = 0


    def setting_change_user_info(self):
        try:
            print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : setting_change_user_info")

            data = {"username" : self.ui_main.setting_user_id_input.text(), 
                    "password" : self.ui_main.setting_user_pw_input.text(),
                    "new_password" : self.ui_main.setting_user_new_pw_input.text(),
                    "new_password2" : self.ui_main.setting_user_new_pw_input2.text(),
                    }

            url = f'http://{self.HOST}:{self.PORT}/login_info_chg'
            receive_data = requests.post(url, json=data).json()

            self.create_fade_out_msg(msg=receive_data["message"])

        except Exception as e:
            print_error(e)


    def move_active_license_list(self):
        try:
            selected_items = self.ui_main.non_active_license_list.selectedItems()
            selected_texts = [item.text() for item in selected_items]

            for detect_type in selected_texts:
                self.admin_info_temp["LICENSE"]["detect_type"][Kor2eng(detect_type)] = 1

            self.reset_admin_license_list()
        except Exception as e:
            print_error(e)

    def move_non_license_camera_list(self):
        try:
            selected_items = self.ui_main.active_license_list.selectedItems()
            selected_texts = [item.text() for item in selected_items]

            for detect_type in selected_texts:
                self.admin_info_temp["LICENSE"]["detect_type"][Kor2eng(detect_type)] = 0

            self.reset_admin_license_list()
        except Exception as e:
            print_error(e)

    def reset_admin_license_list(self):
        try:
            self.ui_main.non_active_license_list.clear()
            self.ui_main.active_license_list.clear()

            # 카메라 번호에 대한 체크박스를 생성하고 레이아웃에 추가
            for detect_type, active_flag in self.admin_info_temp["LICENSE"]["detect_type"].items():
                item = QListWidgetItem(Eng2kor(detect_type))
                item.setTextAlignment(Qt.AlignCenter)

                self.ui_main.active_license_list.addItem(item) if active_flag == 1 else self.ui_main.non_active_license_list.addItem(item)
        
            self.ui_main.license_camera_allow_num_input.setText(str(self.admin_info_temp["LICENSE"]["allow_camera_num"]))

        except Exception as e:
            print_error(e)

    def camera_page_update_camera_page_viewer_roi(self, item):
        try:
            print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : camera_page_update_roi")
            row = item.row()  # 클릭한 아이템의 행 인덱스
            row_data = []
            camera_num = self.ui_main.camera_page_name_box.currentText()
            self.ui_main.camera_page_viewer.set_point(self.camera_info_dict_temp[camera_num]["detect_info"][row][1:], [self.ui_main.camera_page_viewer.width(), self.ui_main.camera_page_viewer.height()])

            gray_point_list = []
            if self.camera_info_dict_temp[camera_num]["AI"] == False:
                for index, value in enumerate(self.camera_info_dict_temp[camera_num]["detect_info"]):
                    # 현재 인덱스가 제외할 인덱스 목록에 없으면 결과 리스트에 추가
                    if index != row:
                        gray_point_list.append(value[1:])
            self.ui_main.camera_page_viewer.set_gray_point(gray_point_list)

            save_info(host=self.HOST, port=self.PORT, file_name="camera_info", info=self.camera_info_dict_temp)

        except Exception as e:
            print_error(e)

    def camera_page_add_detect_type(self):
        try:
            print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : camera_page_add_detect_type")
            camera_name = self.ui_main.camera_page_name_box.currentText()
            detect_type = self.ui_main.camera_page_camera_event_box.currentText()

            detect_type = Kor2eng(detect_type)

            #add_detect_type
            if detect_type in ["Intrusion", "Loitering", "Falldown", "Fire", "Fight", "Trash"]:
                self.camera_info_dict_temp[camera_name]["detect_info"].append([detect_type])

                for i in range(7):
                    self.camera_info_dict_temp[camera_name]["detect_schedule"][str(i)][detect_type] = [[0, 24]]


            self.reset_detect_area_list(self.camera_info_dict_temp[camera_name]["detect_info"])

            lastRow = self.ui_main.camera_page_detect_area_table.rowCount() - 1  
            if lastRow >= 0:
                # 마지막 행의 첫 번째 셀을 현재 셀로 설정
                self.ui_main.camera_page_detect_area_table.setCurrentCell(lastRow, 0)
            else:
                self.create_fade_out_msg(msg="테이블이 비어 있습니다.")
                

            gray_point_list = []
            if self.camera_info_dict_temp[camera_name]["AI"] == False:
                for index, value in enumerate(self.camera_info_dict_temp[camera_name]["detect_info"]):
                    # 현재 인덱스가 제외할 인덱스 목록에 없으면 결과 리스트에 추가
                    gray_point_list.append(value[1:])

            self.ui_main.camera_page_viewer.reset_green_area()
            self.ui_main.camera_page_viewer.set_gray_point(gray_point_list)

            save_info(host=self.HOST, port=self.PORT, file_name="camera_info", info=self.camera_info_dict_temp)



        except Exception as e:
            print_error(e)

    def camera_page_add_detect_area_point(self, point): #마우스 클릭으로 생성된 포인트를 viewer에 표시
        try:
            print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : camera_page_add_detect_area_point")
            camera_num = self.ui_main.camera_page_name_box.currentText()
            select_index = self.ui_main.camera_page_detect_area_table.selectionModel().selectedRows()

            if select_index:  # 선택된 행이 있다면
                select_row = select_index[0].row()

                if point.x() == -1 :
                    if len(self.camera_info_dict_temp[camera_num]["detect_info"][select_row]) > 1:
                        self.camera_info_dict_temp[camera_num]["detect_info"][select_row].pop()

                    else: pass
                else:
                    self.camera_info_dict_temp[camera_num]["detect_info"][select_row].append([point.x()/ self.ui_main.camera_page_viewer.width(), 
                                                                                            point.y()/self.ui_main.camera_page_viewer.height()])

                self.ui_main.camera_page_viewer.set_point(self.camera_info_dict_temp[camera_num]["detect_info"][select_row][1:], [self.ui_main.camera_page_viewer.width(), self.ui_main.camera_page_viewer.height()])

                gray_point_list = []
                if self.camera_info_dict_temp[camera_num]["AI"] == False:
                    for index, value in enumerate(self.camera_info_dict_temp[camera_num]["detect_info"]):
                        # 현재 인덱스가 제외할 인덱스 목록에 없으면 결과 리스트에 추가
                        if index != select_row:
                            gray_point_list.append(value[1:])

                self.ui_main.camera_page_viewer.set_gray_point(gray_point_list)

                save_info(host=self.HOST, port=self.PORT, file_name="camera_info", info=self.camera_info_dict_temp)

        except Exception as e:
            print_error(e)

    def camera_page_del_detect_area(self):
        try:
            print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : camera_page_del_detect_area")
            camera_name = self.ui_main.camera_page_name_box.currentText()

            select_index = self.ui_main.camera_page_detect_area_table.selectionModel().selectedRows()
            if select_index:  # 선택된 행이 있다면
                select_row = select_index[0].row()
                del self.camera_info_dict_temp[camera_name]["detect_info"][select_row]

            self.reset_detect_area_list(self.camera_info_dict_temp[camera_name]["detect_info"])
            self.ui_main.camera_page_viewer.reset_green_area()

            save_info(host=self.HOST, port=self.PORT, file_name="camera_info", info=self.camera_info_dict_temp)

        except Exception as e:
            print_error(e)

    def reset_detect_area_list(self, camera_detect_info):
        self.ui_main.camera_page_detect_area_table.setRowCount(0)

        for detect_type_list in camera_detect_info:
            detect_type_text = Eng2kor(detect_type_list[0])

            row_position = self.ui_main.camera_page_detect_area_table.rowCount()
            self.ui_main.camera_page_detect_area_table.insertRow(row_position)
            text = QTableWidgetItem(detect_type_text)
            text.setTextAlignment(Qt.AlignCenter)
            text.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled)
            self.ui_main.camera_page_detect_area_table.setItem(row_position, 0, text)

    def set_camera_page_viewer(self, camera_name = None):
        try:
            if camera_name == None:
                camera_name = self.ui_main.camera_page_name_box.currentText()

            if camera_name in self.camera_info_dict_temp.keys():
                camera_info = self.camera_info_dict_temp[camera_name]
                self.reset_detect_area_list(camera_info["detect_info"])
                self.ui_main.camera_page_viewer.reset()

                gray_point_list = []

                if camera_info["AI"] == False:
                    for index, value in enumerate(self.camera_info_dict_temp[camera_name]["detect_info"]):
                        # 현재 인덱스가 제외할 인덱스 목록에 없으면 결과 리스트에 추가
                        gray_point_list.append(value[1:])
                    self.ui_main.camera_page_ai_active_label.hide()
                    self.ui_main.camera_page_ai_active_icon.hide()
                    self.camera_page_worker.ai_active = False
                else:
                    self.ui_main.camera_page_ai_active_label.show()
                    self.ui_main.camera_page_ai_active_icon.show()
                    self.camera_page_worker.ai_active = True

                self.ui_main.camera_page_viewer.set_gray_point(gray_point_list)

        except Exception as e:
            print_error(e)

    def find_in_first_column(self, text):
        # 첫 번째 열에서 특정 문자를 포함한 행의 인덱스를 반환
        for row in range(self.ui_main.camera_list_table.rowCount()):
            item = self.ui_main.camera_list_table.item(row, 2)  # 첫 번째 열의 항목 가져오기
            if item is not None and text in item.text():
                return row
        return None

    def check_camera_connect_status(self):
        global FIRST_NOTICE
        try:
            on_camera_pix = QPixmap(u":/ui/ui/images/ico_video_on.svg").scaled(24, 24, Qt.KeepAspectRatio)
            off_camera_pix = QPixmap(u":/ui/ui/images/ico_video_off.svg").scaled(24, 24, Qt.KeepAspectRatio)

            url = f'http://{self.HOST}:{self.PORT}/get-camera-connect_status'
            data = {"msg" : {"ip" : self.login_info_temp["NVR"]["IP"], 
                        "pw" : self.login_info_temp["NVR"]["PW"],
                        "id" : self.login_info_temp["NVR"]["ID"]}}

            receive_data = requests.get(url, json=data).json()

            if receive_data["success"] == True:
                # 카메라 연결 상태 아이콘 변경경
                camera_connect_status_dict = receive_data["data"]
                for camera_name, flag in camera_connect_status_dict.items():
                    row_index = self.find_in_first_column(camera_name)
                    if row_index is not None:
                        label = QLabel()
                        label.setAlignment(Qt.AlignCenter)
                        if flag: label.setPixmap(on_camera_pix)
                        else: label.setPixmap(off_camera_pix)
                        self.ui_main.camera_list_table.setCellWidget(row_index, 0, label)

                # 지능형 알림 수신 및 알림 팝업 발생
                if self.setting_info_temp["NOTICE"]["active"] == 1:
                    events = receive_data.get("alarm_info_data", {}).get("events", [])
                    
                    # 첫 실행 시 알림 발생 방지
                    if FIRST_NOTICE:
                        FIRST_NOTICE = False
                        # 기존 이벤트 정보만 저장하고 알림은 표시하지 않음
                        device_to_name = {}
                        for camera_name, camera_info in self.camera_info_dict_temp.items():
                            if "Num" in camera_info:
                                # 서버 device ID는 camera Num보다 1 작음
                                device_to_name[camera_info["Num"] - 1] = camera_name
                        
                        # 카메라별로 이벤트를 그룹화
                        camera_events = {}
                        for event in events:
                            device_ids = event.get("devices", [])
                            if not device_ids:
                                continue
                            
                            device_id = device_ids[0]
                            camera_name = device_to_name.get(device_id)
                            
                            if not camera_name:
                                continue
                            
                            if camera_name not in camera_events:
                                camera_events[camera_name] = []
                            
                            timestamp = event.get("timestamp", 0)
                            event_type = event.get("type", 0)
                            micro_ai = event.get("micro_ai", {})
                            ai_type = micro_ai.get("type", 0)
                            ai_object = micro_ai.get("object", 0)
                            alarm_time = datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")
                            
                            alarm_data = {
                                "timestamp": timestamp,
                                "event_type": event_type,
                                "ai_type": ai_type,
                                "ai_object": ai_object,
                                "alarm_time": alarm_time
                            }
                            camera_events[camera_name].append(alarm_data)
                        
                        # 각 카메라별로 최신 10개만 저장
                        for camera_name, event_list in camera_events.items():
                            # timestamp 기준으로 정렬 (최신순)
                            event_list.sort(key=lambda x: x["timestamp"], reverse=True)
                            # 최신 10개만 저장
                            self.camera_alarm_info_dict[camera_name] = event_list[:10]
                        
                        return
                    
                    # device ID를 카메라 이름으로 매핑하는 딕셔너리 생성
                    device_to_name = {}
                    for camera_name, camera_info in self.camera_info_dict_temp.items():
                        if "Num" in camera_info:
                            # 서버 device ID는 camera Num보다 1 작음
                            device_to_name[camera_info["Num"] - 1] = camera_name
                    
                    # STEP 1: 모든 이벤트를 파싱하고 카메라별로 그룹화
                    camera_new_events = {}  # 카메라별 신규 이벤트만 저장
                    
                    for event in events:
                        # 이벤트에서 카메라 ID 추출
                        device_ids = event.get("devices", [])
                        if not device_ids:
                            continue
                        
                        device_id = device_ids[0]  # 첫 번째 device ID 사용
                        camera_name = device_to_name.get(device_id)
                        
                        if not camera_name:
                            continue
                        
                        # 이벤트 정보 추출
                        timestamp = event.get("timestamp", 0)
                        event_type = event.get("type", 0)
                        micro_ai = event.get("micro_ai", {})
                        ai_type = micro_ai.get("type", 0)
                        ai_object = micro_ai.get("object", 0)
                        
                        # timestamp를 시간 문자열로 변환
                        alarm_time = datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")
                        
                        alarm_data = {
                            "timestamp": timestamp,
                            "event_type": event_type,
                            "ai_type": ai_type,
                            "ai_object": ai_object,
                            "alarm_time": alarm_time
                        }
                        
                        # 카메라별 알람 정보 초기화
                        if camera_name not in self.camera_alarm_info_dict:
                            self.camera_alarm_info_dict[camera_name] = []
                        
                        # STEP 2: 기존 timestamp와 비교하여 신규 이벤트만 필터링
                        existing_timestamps = {alarm.get("timestamp") for alarm in self.camera_alarm_info_dict[camera_name]}
                        
                        if timestamp not in existing_timestamps:
                            # 신규 이벤트만 별도로 저장
                            if camera_name not in camera_new_events:
                                camera_new_events[camera_name] = []
                            camera_new_events[camera_name].append(alarm_data)

                            print(camera_name)
                            print(alarm_data)
                    
                    ALARM_TYPE_DIC = {2 : "침입", 1 : "배회", 6 : "쓰러짐", 4 : "방화", 7 : "싸움", 5 : "무단투기"}
                    
                    for camera_name, new_events_list in camera_new_events.items():
                        # 신규 이벤트를 저장
                        for alarm_data in new_events_list:
                            self.camera_alarm_info_dict[camera_name].append(alarm_data)
                        
                        # 알람 리스트가 10개를 넘으면 오래된 것 제거
                        if len(self.camera_alarm_info_dict[camera_name]) > 10:
                            # timestamp 기준으로 정렬하여 최신 10개만 유지
                            self.camera_alarm_info_dict[camera_name].sort(key=lambda x: x["timestamp"], reverse=True)
                            self.camera_alarm_info_dict[camera_name] = self.camera_alarm_info_dict[camera_name][:10]
                        
                        # STEP 4: 신규 이벤트에 대해서만 알림 표시
                        for alarm_data in new_events_list:
                            ai_type = alarm_data["ai_type"]
                            alarm_time = alarm_data["alarm_time"]
                            alarm_type = ALARM_TYPE_DIC.get(ai_type, f"이벤트 감지 (타입: {ai_type})")
                            
                            title = f"{camera_name} 카메라"
                            message = f"{alarm_type}\n{alarm_time}\n(클릭하여 자세히 보기)"
                            self.notify(title, message, camera_name=camera_name, alarm_time=alarm_time)


        except Exception as e:
            print_error(e)

    @QtCore.Slot()
    def ShowCamera(self, view, frame: QImage) -> None:
        # frame = frame.scaled(view.width(), view.height(), Qt.IgnoreAspectRatio, Qt.FastTransformation)
        view.setPixmap(QPixmap.fromImage(frame))
        
    @QtCore.Slot()
    def ShowCamera_Group(self, camera_name: str, frame: QImage) -> None:
        try:
            viewer = self.camera_view_list[camera_name]
            viewer.setPixmap(QPixmap.fromImage(frame))
        except:
            pass
    def set_button_style(self, active_button):
        # 모든 버튼을 기본 스타일로 설정
        default_style = "color: white; border: 1px solid rgba(191, 64, 64, 0); background-color: rgba(191, 64, 64, 0);"
        active_style = "color: green; border: 1px solid rgba(191, 64, 64, 0); background-color: rgba(191, 64, 64, 0);"
        
        buttons = {
            'camera': self.ui_main.camera_bnt,
            'setting': self.ui_main.setting_bnt,
            'admin': self.ui_main.admin_bnt,
        }
        
        for key, button in buttons.items():
            button.setStyleSheet(active_style if key == active_button else default_style)

    def stop_camera_page_worker(self):
        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : stop camera page camera")

        if self.camera_page_worker != None :
            self.camera_page_worker.stop()
            del self.camera_page_worker
            self.camera_page_worker = None

    def switch_main_display_to_camera(self, tray_notify=False):
        try:
            self.set_button_style('camera')
            self.ui_main.stackedWidget.setCurrentIndex(0)
            self.ui_main.camera_page_camera_event_box.clear()

            ret, self.camera_info_dict_temp = self.load_camera_info()
            self.admin_info_temp = load_info(host=self.HOST,port=self.PORT,file_name="admin_info")
            self.setting_info_temp = load_info(host=self.HOST, port=self.PORT, file_name="setting_info")
            self.login_info_temp = load_info(host=self.HOST, port=self.PORT, file_name="login_info")

            if self.admin_info_temp["FN_PERMISSION"]["live_viewer_block_active"] == 0:
                self.ui_main.camera_page_block_label.hide()
            else:
                self.ui_main.camera_page_block_label.show()

            self.connect_camera_page_camera(camera_name=self.ui_main.camera_page_name_box.currentText(), tray_notify=tray_notify)
            self.set_camera_page_viewer(camera_name=self.ui_main.camera_page_name_box.currentText())

            for detect_type in self.admin_info_temp["LICENSE"]["detect_type"]:
                if self.admin_info_temp["LICENSE"]["detect_type"][detect_type] == 1:
                    self.ui_main.camera_page_camera_event_box.addItems([Eng2kor(detect_type)])

        except Exception as e:
            print_error(e)

    def switch_main_display_to_setting(self):
        try:
            save_info(host=self.HOST, port=self.PORT, file_name="camera_info", info=self.camera_info_dict_temp)

            self.set_button_style('setting')
            self.ui_main.stackedWidget.setCurrentIndex(1)

            self.ui_main.setting_user_id_input.clear()
            self.ui_main.setting_user_id_input.setText(self.user_info)
            self.ui_main.setting_user_pw_input.clear()
            self.ui_main.setting_user_new_pw_input.clear()
            self.ui_main.setting_user_new_pw_input2.clear()

            # self.stop_camera_page_worker()

            self.setting_info_temp = load_info(host=self.HOST, port=self.PORT, file_name="setting_info")

            self.update_setting()


        except Exception as e:
            print_error(e)

    def switch_main_display_to_admin(self):
        try:
            save_info(host=self.HOST, port=self.PORT, file_name="camera_info", info=self.camera_info_dict_temp)

            self.set_button_style('admin')
            self.ui_main.stackedWidget.setCurrentIndex(2)

            self.ui_main.admin_pw_input.clear()


        except Exception as e:
            print_error(e)

    def switch_main_display_to_admin_2(self):
        self.set_button_style('admin')
        self.ui_main.stackedWidget.setCurrentIndex(3)

        self.admin_info_temp = load_info(host=self.HOST, port=self.PORT, file_name="admin_info")

        self.reset_admin_license_list()
        self.reset_admin_fn_list()

    def save_ai_setting_info(self):
        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : AI Setting Save")

        weight_name = self.ui_main.setting_setting_ai_weight_box.currentText()
        self.setting_info_temp["AI"]["Weight"] = weight_name

        if self.ui_main.setting_self_training_auto_labeling_bnt.isChecked():
            self.setting_info_temp["AI"]["AutoLabel"] = 1
        else:
            self.setting_info_temp["AI"]["AutoLabel"] = 0

        self.setting_info_temp["AI"]["ZeroShot"] = 1 if self.ui_main.setting_self_training_zeroshot_bnt.isChecked() else 0

        self.setting_info_temp["AI"]["AutoLabel_StartTime"] = self.ui_main.setting_auto_label_time_start_box.currentText()
        self.setting_info_temp["AI"]["AutoLabel_EndTime"] = self.ui_main.setting_auto_label_time_end_box.currentText()

        save_info(host=self.HOST, port=self.PORT, file_name="setting_info", info=self.setting_info_temp)
        self.create_fade_out_msg(msg="지능형 엔진 설정이 저장되었습니다")

    def change_zeroshot_info(self):
        self.setting_info_temp["AI"]["ZeroShot"] = 1 if self.setting_info_temp["AI"]["ZeroShot"] == 0 else 0
    def change_auto_label_info(self):
        self.setting_info_temp["AI"]["AutoLabel"] = 1 if self.setting_info_temp["AI"]["AutoLabel"] == 0 else 0

    def load_camera_info(self, reset = False):
        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : load_camera_info")
        
        login_info = load_info(host=self.HOST, port=self.PORT, file_name="login_info")

        data = {"ip" : login_info["NVR"]["IP"], "id" : login_info["NVR"]["ID"], "pw" : login_info["NVR"]["PW"], "reset" : reset}
        url = f'http://{self.HOST}:{self.PORT}/load_camera_info'
        receive_data = requests.post(url, json=data).json()
        camera_info_dict = {}

        if receive_data["success"] == True:
            # self.create_fade_out_msg(msg="init camera")
            camera_info_dict = receive_data["data"]

            return receive_data["success"], camera_info_dict
        
        return receive_data["success"], camera_info_dict

    def camera_list_setup(self, reset = False):
        try:
            print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : camera list setup")

            self.camera_view_list = {}
            self.camera_img_temp = {}
            self.connect_nvr_flag, self.camera_info_dict_temp = self.load_camera_info(reset)

            if self.connect_nvr_flag == True:
                for camera_name, camera_info in self.camera_info_dict_temp.items():
                    row_position = self.ui_main.camera_list_table.rowCount()
                    self.ui_main.camera_list_table.insertRow(row_position)

                    # 새 행에 데이터 채우기
                    label = QLabel()
                    pixmap = QPixmap(":/ui/ui/images/ico_video_off.svg").scaled(24, 24, Qt.KeepAspectRatio)

                    label.setPixmap(pixmap)
                    label.setAlignment(Qt.AlignCenter)
                    self.ui_main.camera_list_table.setCellWidget(row_position, 0, label)

                    text = QTableWidgetItem(str(camera_info["Num"]))
                    text.setTextAlignment(Qt.AlignCenter)
                    text.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled)
                    # text.setFont(self.font)  
                    
                    self.ui_main.camera_list_table.setItem(row_position, 1, text)

                    text = QTableWidgetItem(str(camera_info["Name"]))
                    text.setTextAlignment(Qt.AlignCenter)
                    text.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled)
                    # text.setFont(self.font)  
                    
                    self.ui_main.camera_list_table.setItem(row_position, 2, text)

                    text = QTableWidgetItem(str(camera_info["IP"]))
                    text.setTextAlignment(Qt.AlignCenter)
                    text.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled)
                    
                    self.ui_main.camera_list_table.setItem(row_position, 3, text)

                    self.ui_main.camera_page_name_box.addItems([str(camera_info["Name"])])

            else:
                self.camera_info_dict_temp = {}
                self.create_fade_out_msg(msg="Disconnect NVR")

        except Exception as e:
            print_error(e)

    def del_camera_info(self):
        try:
            print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : del_camera_info")

            selected_indexes = self.ui_main.camera_list_table.selectedIndexes()
            if selected_indexes:
                selected_row = selected_indexes[0].row()  # 선택된 셀의 행 인덱스
                camera_num = self.ui_main.camera_list_table.item(selected_row, 1).text()
                self.ui_main.camera_list_table.removeRow(selected_row)

                # del self.camera_info_dict[camera_num]
                del self.camera_info_dict_temp[camera_num]

        except Exception as e:
            print_error(e)
            
    def eventFilter(self, obj, event):
        self.input_field_styles = {
            self.ui_main.setting_user_pw_input: self.ui_main.setting_user_pw_input_line,
            self.ui_main.setting_user_new_pw_input: self.ui_main.setting_user_new_pw_input_line,
            self.ui_main.setting_user_new_pw_input2: self.ui_main.setting_user_new_pw_input2_line,
            self.ui_main.admin_pw_input: self.ui_main.admin_pw_input_line,
            self.ui_main.admin_sms_alarm_allow_phone_num_input: self.ui_main.admin_sms_alarm_allow_phone_num_input_line,
            self.ui_main.license_camera_allow_num_input: self.ui_main.license_camera_allow_num_input_line,
        }

        if obj in self.input_field_styles:
            line_edit = self.input_field_styles[obj]
            if event.type() == QEvent.FocusIn:
                line_edit.setStyleSheet("background-color: green")
            elif event.type() == QEvent.FocusOut:
                line_edit.setStyleSheet("background-color: rgb(36, 39, 44)")

        return super().eventFilter(obj, event)

    def login_NVR(self):
        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : try login NVR")

        login_info = load_info(host=self.HOST, port=self.PORT, file_name="login_info")

        login_info["NVR"]["IP"] = self.ui_main.server_ip_input.text()
        login_info["NVR"]["ID"] = self.ui_main.server_id_input.text()
        login_info["NVR"]["PW"] = self.ui_main.server_pw_input.text()

        self.ui_main.camera_list_table.setRowCount(0)
        self.ui_main.camera_page_name_box.clear()

        try:
            self.timer.stop()
        except:
            pass
        try:
            self.active_window_timer.stop()
        except:
            pass
        try:
            self.camera_connect_timer.stop()
        except:
            pass
        save_info(host=self.HOST, port=self.PORT, file_name="login_info", info=login_info)
        for camera_name, viewer in self.camera_view_list.items():
            pixmap = QPixmap(u":/ui/ui/images//camera_off.png")
            self.camera_view_list[camera_name].setAlignment(Qt.AlignCenter)
            viewer.setPixmap(pixmap)

        self.setup_init_GUI(reset=True)
    
    def create_fade_out_msg(self, std_window=None, msg="None"):
        try:
            if not hasattr(self, 'fadeout_window') or not self.fadeout_window.isVisible():
                # std_window가 제공되면 해당 윈도우를 parent로 사용, 아니면 self 사용
                parent_window = std_window if std_window is not None else self
                self.fadeout_window = FadeOutWindow(parent_window, msg)
                # 항상 최상위에 표시되도록 설정
                self.fadeout_window.setWindowFlags(self.fadeout_window.windowFlags() | Qt.WindowStaysOnTopHint)

                if std_window is None:
                    main_window_rect = self.geometry()
                    fadeout_window_rect = self.fadeout_window.geometry()
                    self.fadeout_window.move(
                        main_window_rect.left() + (main_window_rect.width() - fadeout_window_rect.width()) // 2,
                        main_window_rect.top() + (main_window_rect.height() - fadeout_window_rect.height()) * 4 // 5
                    )
                else:
                    main_window_rect = std_window.geometry()
                    fadeout_window_rect = self.fadeout_window.geometry()
                    self.fadeout_window.move(
                        main_window_rect.left() + (main_window_rect.width() - fadeout_window_rect.width()) // 2,
                        main_window_rect.top() + (main_window_rect.height() - fadeout_window_rect.height()) * 4 // 5
                    )

            self.fadeout_window.show()
            self.fadeout_window.raise_()          # 윈도우를 최상위로 올림
            self.fadeout_window.activateWindow()  # 윈도우를 활성화

        except Exception as e:
            print_error(e)

    def check_nvr_login(self):
        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : check_nvr_login")

        login_info = load_info(host=self.HOST, port=self.PORT, file_name="login_info")
        data = {"msg" : {"ip" : login_info["NVR"]["IP"], 
                        "pw" : login_info["NVR"]["PW"],
                        "id" : login_info["NVR"]["ID"]}}
            
        url = f'http://{self.HOST}:{self.PORT}/login_nvr'
        receive_data = requests.post(url, json=data).json()

        if receive_data["success"]: return True
        else:
            self.create_fade_out_msg(msg=receive_data["message"])
            return False

    def show_confirmation_dialog(self):
        # 확인 창 생성
        self.confirm_dialog = QDialog(self)
        self.confirm_dialog.setWindowTitle("NVR login")
        self.confirm_dialog.setFixedSize(300, 150)
        # self.confirm_dialog.setWindowFlags(Qt.FramelessWindowHint)
        self.confirm_dialog.setWindowModality(Qt.ApplicationModal)

        mainWindowGeometry = self.frameGeometry()
        centerPoint = mainWindowGeometry.center() - self.rect().center()
        self.confirm_dialog.move(centerPoint.x(), centerPoint.y())

        # 확인 라벨
        label = QLabel("새로운 NVR 연결 시 \n 기존 설정 값이 초기화 됩니다.", self.confirm_dialog)
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("color: rgb(255, 255, 255);") 

        # 확인 및 취소 버튼
        ok_button = QPushButton("확인", self.confirm_dialog)
        ok_button.setStyleSheet("color: rgb(255, 255, 255); \n"
                            "background-color: rgb(30, 195, 55); \n"
                            "border-radius: 5px;") 
        cancel_button = QPushButton("취소", self.confirm_dialog)
        cancel_button.setStyleSheet("color: rgb(255, 255, 255);") 
        cancel_button.setStyleSheet("color: rgb(255, 255, 255); \n"
                                "background-color: rgb(36, 39, 44); \n"
                                "border-radius: 5px;") 

        # 버튼 클릭 이벤트 연결
        ok_button.clicked.connect(self.on_confirm)
        cancel_button.clicked.connect(self.confirm_dialog.close)

        # 레이아웃 설정
        button_layout = QHBoxLayout()
        button_layout.addWidget(ok_button)
        button_layout.addWidget(cancel_button)

        main_layout = QVBoxLayout(self.confirm_dialog)
        main_layout.addWidget(label)
        main_layout.addLayout(button_layout)

        self.confirm_dialog.show()  # 모달 창으로 실행

    def on_confirm(self):
        self.confirm_dialog.close()  # 확인 창 닫기
        self.login_NVR()  # login_NVR 함수 실행


    def setup_init_GUI(self, reset=False):
        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : setup main GUI")

        self.ui_main.stackedWidget.setCurrentIndex(0)

        #초기 변수 설정
        self.storage_period = {30: 0, 60: 1, 90: 2, 0: 30, 1: 60, 2: 90}
        self.camera_connect_timer = None
        self.camera_page_worker = None
        self.connect_nvr_flag = False

        # 카메라 리스트 테이블 설정
        self.ui_main.camera_list_table.setColumnWidth(0, 20)
        self.ui_main.camera_list_table.setColumnWidth(1, 35)
        self.ui_main.camera_list_table.setColumnWidth(2, 100)
        
        # 어두운 레이어 위젯 생성
        self.dark_layer = QWidget(self)
        self.dark_layer.setGeometry(QRect(0,0,9999,9999))
        self.dark_layer.setStyleSheet("background-color: rgba(0, 0, 0, 178);")  # 70% 투명도
        self.dark_layer.hide()  # 기본적으로 숨김

        # 초기 정보 로드
        self.admin_info_temp = load_info(host=self.HOST,port=self.PORT,file_name="admin_info")
        self.setting_info_temp = load_info(host=self.HOST, port=self.PORT, file_name="setting_info")
        self.login_info_temp = load_info(host=self.HOST, port=self.PORT, file_name="login_info")

        self.camera_img_temp = {} #camera_name : np.array(img)

        # 상단 NVR 서버 정보 입력
        self.ui_main.server_ip_input.setText(self.login_info_temp["NVR"]["IP"])
        self.ui_main.server_id_input.setText(self.login_info_temp["NVR"]["ID"])
        self.ui_main.server_pw_input.setText(self.login_info_temp["NVR"]["PW"])

        # 지능형 프로그램 구동 상태 아이콘 설정
        self.ui_main.camera_page_ai_active_label.hide()
        self.ui_main.camera_page_ai_active_icon.hide()

        if self.user_info != "admin":
            self.ui_main.tab_partion_4.hide()
            self.ui_main.admin_bnt.hide()

        #트레이 아이콘 설정
        self.tray_icon = QSystemTrayIcon(QIcon("ui/images/icon2.ico"), self)
        self.tray_icon.show()
        tray_menu = QMenu()
        restore_action = QAction("열기", self)
        restore_action.triggered.connect(self.open_main_window_tray)
        tray_menu.addAction(restore_action)
        quit_action = QAction("종료", self)
        quit_action.triggered.connect(QApplication.instance().quit)
        tray_menu.addAction(quit_action)
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()
        # self.tray_icon.activated.connect(self.__on_tray_activated)
        # 알림 메시지 클릭 시 검색 창 열기 (최근 알림 정보 사용)
        self.tray_icon.messageClicked.connect(self.on_notification_clicked)

        self.update_setting()

        self.camera_list_setup(reset = reset)#카메라 리스트에 카메라 정보 추가

        if self.connect_nvr_flag:
            self.update_camera_img_temp()
            self.start_camera_connect_status_timer()#NVR 카메라 연결상태 확인
            self.setup_camera_viewer()

        time.sleep(1)

    def open_main_window_tray(self, camera_name=None):
        """메인 창 열기"""
        self.showNormal()
        self.switch_main_display_to_camera()

        if camera_name is not None:
            self.ui_main.camera_page_name_box.setCurrentText(camera_name)

    def open_main_window_tray_notify(self, camera_name=None):
        """메인 창 열기"""
        self.showNormal()
        if camera_name is not None:
            self.ui_main.camera_page_name_box.setCurrentText(camera_name)
        self.switch_main_display_to_camera(tray_notify=True)

    def on_notification_clicked_handler(self, notification_data):
        """커스텀 알림 클릭 시 호출되는 핸들러"""
        camera_name = notification_data.get("camera_name")
        alarm_time = notification_data.get("alarm_time")
        print(f"클릭된 알림 - 카메라: {camera_name}, 시간: {alarm_time}")
        # 검색 창 열기
        self.open_main_window_tray_notify(camera_name = camera_name)

    def on_notification_clicked(self):
        """트레이 알림 메시지 클릭 시 호출되는 함수"""
        # 최근 알림 정보가 있으면 검색 창 열기
        if self.last_notification_info:
            camera_name = self.last_notification_info.get("camera_name")
            alarm_time = self.last_notification_info.get("alarm_time")
            print(f"클릭된 알림 - 카메라: {camera_name}, 시간: {alarm_time}")
            self.open_main_window_tray_notify(camera_name = camera_name)
        else:
            self.open_main_window_tray_notify()

    # def __on_tray_activated(self, reason):
    #     if reason == QSystemTrayIcon.DoubleClick:
    #         # 트레이 아이콘 더블 클릭 시 검색 창 열기
    #         self.open_main_window()
    #         # self.showNormal()
    #         # self.switch_main_display_to_camera()


    def update_camera_img_temp(self):
        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : update_camera_img_temp")

        data = {"msg" : {"ip" : self.login_info_temp["NVR"]["IP"], 
                        "pw" : self.login_info_temp["NVR"]["PW"],
                        "id" : self.login_info_temp["NVR"]["ID"]}}

        url = f'http://{self.HOST}:{self.PORT}/get_camera_img'
        receive_data = requests.post(url, json=data).json()

        # base64로 인코딩된 이미지 데이터를 numpy 배열로 변환
        self.camera_img_temp = {}
        if receive_data["success"]:
            for camera_name, img_base64 in receive_data["data"].items():
                if img_base64:  # 빈 문자열이 아닌 경우
                    try:
                        # base64 디코딩
                        img_bytes = base64.b64decode(img_base64)
                        # numpy 배열로 변환
                        nparr = np.frombuffer(img_bytes, np.uint8)
                        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
                        self.camera_img_temp[camera_name] = img
                    except Exception as e:
                        print(f"Failed to decode image for camera {camera_name}: {e}")
                        self.camera_img_temp[camera_name] = np.zeros((640, 480, 3), dtype=np.uint8)
                else:
                    self.camera_img_temp[camera_name] = np.zeros((640, 480, 3), dtype=np.uint8)

    def setup_camera_viewer(self):
        ##AI카메라 페이지 영상 뷰어 생성
        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : setup_camera_viewer")

        self.ui_main.camera_page_viewer.hide()
        self.ui_main.camera_page_viewer = Plot_Camera_Viewer(self.ui_main.camera_page)
        self.ui_main.camera_page_viewer.setObjectName(u"camera_page_viewer")
        self.ui_main.camera_page_viewer.setMinimumSize(QSize(472, 331))
        self.ui_main.camera_page_viewer.setStyleSheet(u"border: 1px solid rgb(119, 118, 123);\n"
                                                "background-color: rgba(255, 255, 255, 0);")
        self.ui_main.camera_page_viewer.setScaledContents(True)
        self.ui_main.ai_camera_page_verticalLayout.addWidget(self.ui_main.camera_page_viewer)
        self.ui_main.camera_page_viewer.clicked.connect(self.camera_page_add_detect_area_point)


    def setup_slot_connect(self):
        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : setup_QT_slot_connect")

        # self.ui_main.server_login_bnt.clicked.connect(self.login_NVR)
        self.ui_main.server_login_bnt.clicked.connect(self.show_confirmation_dialog)
        self.ui_main.shutdown_bnt.clicked.connect(self.shutdown) #종료 버튼 활성화

        #우측 상단 버튼 활성화
        self.ui_main.camera_schedule_bnt.clicked.connect(lambda click, instance = self : open_schedule_window(click, instance))
        self.ui_main.labeling_bnt.clicked.connect(lambda click, instance = self : open_labeling_window(click, instance))
        #주요 메인 메뉴 버튼 설정
        # self.ui_main.live_bnt.clicked.connect(self.switch_main_display_to_live)
        self.ui_main.camera_bnt.clicked.connect(self.switch_main_display_to_camera)
        self.ui_main.setting_bnt.clicked.connect(self.switch_main_display_to_setting)
        self.ui_main.admin_bnt.clicked.connect(self.switch_main_display_to_admin)
        self.ui_main.search_memu_bnt.clicked.connect(lambda click, instance = self : open_search_window(click, instance))

        ##카메라 페이지 설정
        self.ui_main.camera_page_name_box.currentTextChanged.connect(lambda: (self.connect_camera_page_camera(), self.set_camera_page_viewer()))
        self.ui_main.camera_page_detect_add_bnt.clicked.connect(self.camera_page_add_detect_type)
        self.ui_main.camera_page_detect_area_del_bnt.clicked.connect(self.camera_page_del_detect_area)
        self.ui_main.camera_page_object_setting_bnt.clicked.connect(lambda click, instance = self : open_object_setting_window(click, instance))
        self.ui_main.camera_page_detect_area_table.itemClicked.connect(self.camera_page_update_camera_page_viewer_roi)

        # 지능형 활성화 버튼 
        self.ui_main.camera_page_ai_bnt.clicked.connect(lambda click, instance = self : open_ai_setting_window(click, instance))

        # 설정 메뉴 버튼
        self.ui_main.setting_ai_setting_save_bnt.clicked.connect(self.save_ai_setting_info)
        self.ui_main.setting_user_save_bnt.clicked.connect(self.setting_change_user_info)
        self.ui_main.setting_detect_bbox_active_bnt.clicked.connect(self.change_setting_info)
        self.ui_main.setting_detect_label_active_bnt.clicked.connect(self.change_setting_info)
        self.ui_main.setting_detect_roi_active_bnt.clicked.connect(self.change_setting_info)
        self.ui_main.setting_notice_phone_save_bnt.clicked.connect(self.change_setting_info)
        self.ui_main.setting_notice_phone_add_bnt.clicked.connect(self.add_notice_phone_number)
        self.ui_main.setting_notice_phone_del_bnt.clicked.connect(self.del_notice_phone_number)
        self.ui_main.setting_event_pop_up_save_bnt.clicked.connect(self.change_setting_info)

        # admin 메뉴 버튼
        self.ui_main.admin_page_bnt.clicked.connect(self.login_admin_page)
        self.ui_main.admin_license_bnt.clicked.connect(lambda : (self.ui_main.stackedWidget_2.setCurrentIndex(0), self.reset_admin_license_list()))
        self.ui_main.admin_fn_permission_bnt.clicked.connect(lambda : (self.ui_main.stackedWidget_2.setCurrentIndex(1), self.reset_admin_fn_list()))
        self.ui_main.license_add_bnt.clicked.connect(self.move_active_license_list)
        self.ui_main.license_remove_bnt.clicked.connect(self.move_non_license_camera_list)
        self.ui_main.admin_self_labeling_fn_active_bnt.clicked.connect(self.change_self_labeling_fn)
        self.ui_main.admin_sms_alarm_fn_active_bnt.clicked.connect(self.change_sms_alarm_fn)
        self.ui_main.admin_live_viewer_block_bnt.clicked.connect(self.change_live_viewer_block_fn)
        self.ui_main.admin_fn_save_bnt.clicked.connect(self.save_admin_info)

        self.ui_main.license_save_bnt.clicked.connect(self.save_admin_info)

        self.ui_main.admin_pw_input.returnPressed.connect(self.login_admin_page)

        self.ui_main.camera_list_table.itemDoubleClicked.connect(self.double_click_camera_list_fn)
        self.ui_main.setting_notice_phone_list.itemClicked.connect(lambda: self.load_notion_detect_type_button_states())

    def reset_admin_fn_list(self):
        self.ui_main.admin_sms_alarm_fn_active_bnt.setChecked(self.admin_info_temp["FN_PERMISSION"]["sms_active"] == 1)
        self.ui_main.admin_self_labeling_fn_active_bnt.setChecked(self.admin_info_temp["FN_PERMISSION"]["self_labeling_active"] == 1)
        self.ui_main.admin_sms_alarm_allow_phone_num_input.setText(str(self.admin_info_temp["FN_PERMISSION"]["sms_allow_phone_num"]))
        self.ui_main.admin_live_viewer_block_bnt.setChecked(self.admin_info_temp["FN_PERMISSION"]["live_viewer_block_active"] == 1)

    def del_notice_phone_number(self):
        """전화번호 삭제 함수"""
        try:
            selected_items = self.ui_main.setting_notice_phone_list.selectedItems()
            
            if not selected_items:
                self.create_fade_out_msg(msg="삭제할 전화번호를 선택해주세요")
                return
            
            # 선택된 행의 인덱스를 수집 (역순으로 정렬)
            selected_rows = []
            selected_phones = []
            
            for item in selected_items:
                row = self.ui_main.setting_notice_phone_list.row(item)
                phone_number = item.text()
                selected_rows.append(row)
                selected_phones.append(phone_number)
            
            # setting_info_temp에서 전화번호 삭제
            for phone_number in selected_phones:
                if phone_number in self.setting_info_temp["SMS"]["USER"]:
                    del self.setting_info_temp["SMS"]["USER"][phone_number]
            
            # 서버에 저장
            save_info(host=self.HOST, port=self.PORT, file_name="setting_info", info=self.setting_info_temp)
            
            # QTableWidget에서 해당 행 제거 (역순으로 삭제하여 인덱스 문제 방지)
            for row in sorted(selected_rows, reverse=True):
                self.ui_main.setting_notice_phone_list.removeRow(row)
            
            self.create_fade_out_msg(msg="전화번호가 삭제되었습니다")
            print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : Deleted phone numbers: {selected_phones}")
            
        except Exception as e:
            print_error(e)

    def change_sms_alarm_fn(self):
        # sms_active 토글
        self.admin_info_temp["FN_PERMISSION"]["sms_active"] = 1 if self.admin_info_temp["FN_PERMISSION"]["sms_active"] == 0 else 0

    def change_self_labeling_fn(self):
        # self_labeling_active 토글
        self.admin_info_temp["FN_PERMISSION"]["self_labeling_active"] = 1 if self.admin_info_temp["FN_PERMISSION"]["self_labeling_active"] == 0 else 0
    def change_live_viewer_block_fn(self):
        # live_viewer_block_active 토글
        self.admin_info_temp["FN_PERMISSION"]["live_viewer_block_active"] = 1 if self.admin_info_temp["FN_PERMISSION"]["live_viewer_block_active"] == 0 else 0
    def double_click_camera_list_fn(self, item):
        try:
            print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : change_camera from table double click")
            
            # 더블클릭된 행에서 카메라 이름 가져오기
            row = item.row()
            camera_name_item = self.ui_main.camera_list_table.item(row, 2)  # 2번 컬럼이 카메라 이름
            
            if camera_name_item:
                camera_name = camera_name_item.text()

                # 카메라 페이지로 전환
                self.switch_main_display_to_camera()
                self.set_button_style('camera')
                self.ui_main.stackedWidget.setCurrentIndex(0)
                
                # 카메라 선택 변경 (이것이 자동으로 connect_camera_page_camera()와 set_camera_page_viewer()를 호출함)
                index = self.ui_main.camera_page_name_box.findText(camera_name)
                if index >= 0:
                    self.ui_main.camera_page_name_box.setCurrentIndex(index)
                
        except Exception as e:
            print_error(e)

    def setup_event_filters(self):
        # 이벤트 필터 설치
        event_filters = [
            self.ui_main.setting_user_id_input,
            self.ui_main.setting_user_pw_input,
            self.ui_main.setting_user_new_pw_input,
            self.ui_main.setting_user_new_pw_input2,
            self.ui_main.admin_pw_input,
            self.ui_main.admin_sms_alarm_allow_phone_num_input,
            self.ui_main.license_camera_allow_num_input,

        ]
        for filter in event_filters:
            filter.installEventFilter(self)


    def update_setting(self):
        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : setting update")

        setting_info_temp = load_info(host=self.HOST, port=self.PORT, file_name="setting_info")
        self.ui_main.setting_detect_bbox_active_bnt.setChecked(setting_info_temp["DETECT"]["Bbox"]) # 지능형 검출 결과 BBOX 출력 여부
        self.ui_main.setting_detect_label_active_bnt.setChecked(setting_info_temp["DETECT"]["Label"]) # 지능형 검출 결과 class 출력 여부
        self.ui_main.setting_detect_roi_active_bnt.setChecked(setting_info_temp["DETECT"]["Roi"]) # 지능형 검출 결과 class 출력 여부
        
        url = f'http://{self.HOST}:{self.PORT}/get_ai_weight_list'
        receive_data = requests.post(url, json={"msg" : {}}).json()
        self.ui_main.setting_setting_ai_weight_box.clear()

        for weight_name in receive_data["weight_list"]:
            self.ui_main.setting_setting_ai_weight_box.addItems([weight_name])

        self.ui_main.setting_self_training_zeroshot_bnt.setChecked(self.setting_info_temp["AI"]["ZeroShot"])
        self.ui_main.setting_self_training_auto_labeling_bnt.setChecked(self.setting_info_temp["AI"]["AutoLabel"])


        items_text = [self.ui_main.setting_setting_ai_weight_box.itemText(i) for i in range(self.ui_main.setting_setting_ai_weight_box.count())]

        if self.setting_info_temp["AI"]["Weight"] != 0:
            if self.setting_info_temp["AI"]["Weight"] in items_text:
                index_num = items_text.index(self.setting_info_temp["AI"]["Weight"])
                self.ui_main.setting_setting_ai_weight_box.setCurrentIndex(index_num)

        else:
            index_num = items_text.index("default")
            self.ui_main.setting_setting_ai_weight_box.setCurrentIndex(index_num)

        self.ui_main.setting_auto_label_time_start_box.setCurrentText(setting_info_temp["AI"]["AutoLabel_StartTime"])
        self.ui_main.setting_auto_label_time_end_box.setCurrentText(setting_info_temp["AI"]["AutoLabel_EndTime"])

        if self.admin_info_temp["FN_PERMISSION"]["sms_active"] == 1:
            self.ui_main.setting_notion_widget.show()
            self.ui_main.setting_partion_8.show()
        else:
            self.ui_main.setting_notion_widget.hide()
            self.ui_main.setting_partion_8.hide()

        if self.admin_info_temp["FN_PERMISSION"]["self_labeling_active"] == 1:
            self.ui_main.setting_self_labeling_widget.show()
            self.ui_main.setting_partion_4.show()
        else:
            self.ui_main.setting_self_labeling_widget.hide()
            self.ui_main.setting_partion_4.hide()

        if self.setting_info_temp["SMS"]["active"] == 1:
            self.ui_main.setting_notice_phone_active_bnt.setChecked(True)
        else:
            self.ui_main.setting_notice_phone_active_bnt.setChecked(False)

        if self.setting_info_temp["NOTICE"]["active"] == 1:
            self.ui_main.setting_event_pop_up_active_bnt.setChecked(True)
        else:
            self.ui_main.setting_event_pop_up_active_bnt.setChecked(False)

        self.ui_main.setting_event_pop_up_duration_box.setCurrentIndex(self.setting_info_temp["NOTICE"]["duration"])

        # QTableWidget의 모든 행 제거
        self.ui_main.setting_notice_phone_list.setRowCount(0)
        for user_phone, user_notice_detect_type in self.setting_info_temp["SMS"]["USER"].items():
            row = self.ui_main.setting_notice_phone_list.rowCount()
            self.ui_main.setting_notice_phone_list.insertRow(row)
            item = QTableWidgetItem(user_phone)
            item.setTextAlignment(Qt.AlignCenter)
            self.ui_main.setting_notice_phone_list.setItem(row, 0, item)

        # setting_notion_detect_type_widget의 기존 버튼들 제거 및 새로 생성
        self.update_notion_detect_type_buttons()

    def change_notice_phone_active_fn(self):
        if self.ui_main.setting_notice_phone_active_bnt.isChecked():
            self.setting_info_temp["SMS"]["active"] = 1
        else:
            self.setting_info_temp["SMS"]["active"] = 0
        self.change_setting_info()

    def add_notice_phone_number(self):
        """전화번호 추가 함수"""
        try:
            # 입력된 전화번호 가져오기
            phone_input = self.ui_main.setting_notice_phone_num_input.text().strip()
            
            if not phone_input:
                self.create_fade_out_msg(msg="전화번호를 입력해주세요")
                return

            # 최대 허용 전화번호 개수 체크
            current_phone_count = len(self.setting_info_temp["SMS"]["USER"])
            max_allowed = self.admin_info_temp["FN_PERMISSION"]["sms_allow_phone_num"]
            
            if current_phone_count >= max_allowed:
                self.create_fade_out_msg(msg=f"최대 전화번호 개수({max_allowed}개)를 초과했습니다")
                return
                
            # 전화번호 형식 검증 (정규표현식)
            # 1. XXX-XXXX-XXXX
            # 2. XXX.XXXX.XXXX
            # 3. XXXXXXXXXXX (11자리 숫자)
            pattern = r'^(\d{3}[-.]?\d{4}[-.]?\d{4})$'
            
            if not re.match(pattern, phone_input):
                self.create_fade_out_msg(msg="올바른 전화번호 형식이 아닙니다")
                return
            
            # 전화번호를 숫자만 추출 (구분자 제거)
            phone_number = re.sub(r'[-.]', '', phone_input)
            
            # 이미 존재하는 전화번호인지 확인
            if phone_number in self.setting_info_temp["SMS"]["USER"]:
                self.create_fade_out_msg(msg="이미 등록된 전화번호입니다")
                return
            
            # 모든 detect_type 가져오기
            detect_types_dict = {}
            for detect_type, active_flag in self.admin_info_temp["LICENSE"]["detect_type"].items():
                detect_types_dict[detect_type] = 0
            
            # 전화번호 추가
            self.setting_info_temp["SMS"]["USER"][phone_number] = detect_types_dict
            
            # 서버에 저장
            save_info(host=self.HOST, port=self.PORT, file_name="setting_info", info=self.setting_info_temp)
            
            # 테이블에 추가
            row = self.ui_main.setting_notice_phone_list.rowCount()
            self.ui_main.setting_notice_phone_list.insertRow(row)
            item = QTableWidgetItem(phone_number)
            item.setTextAlignment(Qt.AlignCenter)
            self.ui_main.setting_notice_phone_list.setItem(row, 0, item)
            
            # 입력 필드 초기화
            self.ui_main.setting_notice_phone_num_input.clear()
            
            self.create_fade_out_msg(msg="전화번호가 추가되었습니다")
            print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : Added phone number: {phone_number}")
            
        except Exception as e:
            print_error(e)

    def update_notion_detect_type_buttons(self):
        """알림 감지 타입 버튼들을 동적으로 생성"""
        try:
            # 기존 레이아웃의 모든 위젯 제거
            if self.ui_main.setting_notion_detect_type_widget.layout() is not None:
                layout = self.ui_main.setting_notion_detect_type_widget.layout()
                while layout.count():
                    item = layout.takeAt(0)
                    widget = item.widget()
                    if widget is not None:
                        widget.deleteLater()
                # 기존 레이아웃 삭제
                QWidget().setLayout(layout)
            
            # 새 그리드 레이아웃 생성
            grid_layout = QGridLayout(self.ui_main.setting_notion_detect_type_widget)
            grid_layout.setSpacing(10)
            grid_layout.setContentsMargins(0, 0, 0, 0)
            
            # 활성화된 detect_type 필터링
            active_detect_types = []
            for detect_type, active_flag in self.admin_info_temp["LICENSE"]["detect_type"].items():
                if active_flag == 1:
                    active_detect_types.append(detect_type)
            
            # 2열로 버튼 배치
            for index, detect_type in enumerate(active_detect_types):
                row = index // 2
                col = index % 2
                
                # 버튼 생성
                button = QPushButton(Eng2kor(detect_type))
                button.setCheckable(True)
                button.setMinimumSize(QSize(60, 35))
                button.setMaximumSize(QSize(60, 35))

                button.setStyleSheet(
                    "QPushButton {\n"
                    "    color: rgb(255, 255, 255);\n"
                    "    background-color: rgb(36, 39, 44);\n"
                    "    border-radius: 5px;\n"
                    "}\n"
                    "QPushButton:checked {\n"
                    "    background-color: rgb(30, 195, 55);\n"
                    "}"
                )
                
                # 버튼 클릭 이벤트 연결 (버튼 객체도 함께 전달)
                button.clicked.connect(lambda checked, dt=detect_type, btn=button: self.on_notion_detect_type_button_clicked(dt, checked, btn))
                
                # 그리드에 버튼 추가
                grid_layout.addWidget(button, row, col)
            
            # 버튼 생성 후 현재 선택된 전화번호의 설정 로드
            self.load_notion_detect_type_button_states()
            
            print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : notion detect type buttons updated")
            
        except Exception as e:
            print_error(e)

    def on_notion_detect_type_button_clicked(self, detect_type, checked, button):
        """알림 감지 타입 버튼 클릭 시 처리"""
        try:
            # 현재 선택된 전화번호 가져오기
            selected_items = self.ui_main.setting_notice_phone_list.selectedItems()
            
            if not selected_items:
                self.create_fade_out_msg(msg="전화번호를 선택해주세요")
                # 버튼 상태를 원래대로 되돌림
                button.setChecked(not checked)
                return
            
            # 선택된 행의 전화번호 가져오기
            selected_row = self.ui_main.setting_notice_phone_list.currentRow()
            phone_number = self.ui_main.setting_notice_phone_list.item(selected_row, 0).text()
            
            # setting_info_temp 업데이트
            if phone_number in self.setting_info_temp["SMS"]["USER"]:
                self.setting_info_temp["SMS"]["USER"][phone_number][detect_type] = 1 if checked else 0
                save_info(host=self.HOST, port=self.PORT, file_name="setting_info", info=self.setting_info_temp)
                print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : Updated {phone_number} - {detect_type}: {1 if checked else 0}")
            else:
                self.create_fade_out_msg(msg="전화번호 정보를 찾을 수 없습니다")
                # 버튼 상태를 원래대로 되돌림
                button.setChecked(not checked)
                
        except Exception as e:
            print_error(e)
            # 에러 발생 시에도 버튼 상태 복원
            button.setChecked(not checked)

    def load_notion_detect_type_button_states(self):
        """선택된 전화번호의 설정에 따라 버튼 상태 로드"""
        try:
            # 현재 선택된 전화번호 가져오기
            selected_row = self.ui_main.setting_notice_phone_list.currentRow()
            
            if selected_row < 0:
                return
            
            phone_number = self.ui_main.setting_notice_phone_list.item(selected_row, 0).text()
            
            # 전화번호가 존재하는지 확인
            if phone_number not in self.setting_info_temp["SMS"]["USER"]:
                return
            
            # 레이아웃에서 모든 버튼 가져오기
            layout = self.ui_main.setting_notion_detect_type_widget.layout()
            if layout is not None:
                for i in range(layout.count()):
                    button = layout.itemAt(i).widget()
                    if isinstance(button, QPushButton):
                        button_label = button.text()
                        detect_type = Kor2eng(button_label)
                        
                        # 버튼 상태 설정
                        if detect_type in self.setting_info_temp["SMS"]["USER"][phone_number]:
                            is_active = self.setting_info_temp["SMS"]["USER"][phone_number][detect_type] == 1
                            button.setChecked(is_active)
                        
        except Exception as e:
            print_error(e)


    def merge_intervals(self, intervals):
        # 시간 구간을 시작 시간 기준으로 정렬
        intervals.sort(key=lambda x: x[0])
        merged = []

        for current in intervals:
            # 병합된 리스트가 비어있지 않고 현재 구간이 마지막에 추가된 구간과 겹치는 경우
            if not merged or merged[-1][1] < current[0] - 1:
                # 겹치지 않는 경우, 새로운 구간으로 추가
                merged.append(current)
            else:
                # 현재 구간의 끝 시간이 마지막 구간의 끝 시간보다 클 경우 업데이트
                merged[-1][1] = max(merged[-1][1], current[1])
        
        return merged

    def keyPressEvent(self, event):
        # Alt + Enter 키를 감지
        if event.key() == Qt.Key_Enter and event.modifiers() & Qt.AltModifier:
            if self.isMaximized():
                self.showNormal()  # 최대화된 상태에서 복원
            else:
                self.showMaximized()  # 복원 상태에서 최대화

        # 일부 키보드에서는 Return 키가 Enter 키로 인식될 수 있으므로, Return 키도 처리
        elif event.key() == Qt.Key_Return and event.modifiers() & Qt.AltModifier:
            if self.isMaximized():
                self.showNormal()  # 최대화된 상태에서 복원
            else:
                self.showMaximized()  # 복원 상태에서 최대화

    def shutdown(self):
        # QApplication.instance().quit()
        self.stop_camera_page_worker()
        self.hide()
        self.tray_icon.showMessage("동작 중", "프로그램이 트레이에 최소화되었습니다.")

    def closeEvent(self, event):
        self.stop_camera_page_worker()

        self.hide()
        event.ignore()
    # def closeEvent(self, event):
    #     # 창이 닫힐 때 실행되는 코드

    #     data = {"msg" : str(self.client_ip)}
    #     url = f'http://{self.HOST}:{self.PORT}/logout'
    #     receive_data = requests.put(url, json=data).json()
    #     event.accept()  # 또는 event.ignore()로 닫히지 않게 할 수 있음

def generate_camera_grid(n):
    cols = math.ceil(math.sqrt(n))  # 열 개수
    rows = math.ceil(n / cols)  # 행 개수
    
    grid = [(r+1, c+1) for r in range(rows) for c in range(cols)][:n]  # 좌표 생성
    return grid


def main():
    try:
        # time.sleep(1)

        app = QApplication(sys.argv)
        window = LoginWindow()
        window.show()
        app.exec()

    except Exception as e:
            print_error(e)

    finally:
            
            # input("Press Enter to close...")  # 실행 후 입력을 기다림
            pass
    
if __name__ == "__main__":
        main()



