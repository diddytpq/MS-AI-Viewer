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
from requests.auth import HTTPBasicAuth
import threading

import time
from datetime import datetime, timedelta
import traceback
import gc
import cv2

from ui.main_ui import Ui_MainWindow
from utils import FadeOutWindow, Plot_Camera_Viewer, Connect_Camera, load_info, find_in_first_column, Eng2kor, Kor2eng, set_button_style, save_info

from ui.window_ai_setting import open_ai_setting_window
from ui.window_object_setting import open_object_setting_window
from ui.window_schedule import open_schedule_window
from ui.window_search import open_search_window


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
        self.camera_page_worker = None
        self.storage_period = {30: 0, 60: 1, 90: 2, 0: 30, 1: 60, 2: 90}

        self.camera_img_dict = {}


        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : setup main GUI")
        
        #초기 메뉴 0번으로 세팅
        self.ui_main.stackedWidget.setCurrentIndex(0)
        self.ui_main.camera_page_readmod_label.hide()
        self.ui_main.camera_page_readmod_icon.hide()

        # 카메라 리스트 테이블 설정
        self.ui_main.camera_list_table.setColumnWidth(0, 20)
        self.ui_main.camera_list_table.setColumnWidth(1, 35)
        self.ui_main.camera_list_table.setColumnWidth(2, 100)

        # 초기 정보 로드
        self.admin_info_temp = load_info(host=self.HOST,port=self.PORT,file_name="admin_info")
        self.setting_info_temp = load_info(host=self.HOST, port=self.PORT, file_name="setting_info")
        self.login_info_temp = load_info(host=self.HOST, port=self.PORT, file_name="login_info")

        # 상단 NVR 서버 정보 입력
        self.ui_main.server_ip_input.setText(self.login_info_temp["NVR"]["IP"])
        self.ui_main.server_id_input.setText(self.login_info_temp["NVR"]["ID"])
        self.ui_main.server_pw_input.setText(self.login_info_temp["NVR"]["PW"])
        
        # 상단 관리자 메뉴 숨기기
        if self.user_info != "admin":
            self.ui_main.tab_partion_3.hide()
            self.ui_main.admin_bnt.hide()

        #초기 설정 메뉴 버튼 값 세팅
        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : setting update")
        self.ui_main.setting_popup_alarm_active_bnt.setChecked(self.setting_info_temp["NOTICE"]["active"]) # 알람 발생시 프로그램 팝업알림 기능 활성화 여부
        self.ui_main.setting_video_save_alarm_active_bnt.setChecked(self.setting_info_temp["VIDEO_SAVE"]["active"]) # 알람 발생 영상 저장 기능 활성화 여부

        if self.ui_main.setting_video_save_alarm_active_bnt.isChecked():
            self.ui_main.setting_event_video_storage_period.setEnabled(True)
            self.ui_main.setting_event_video_storage_period.setCurrentIndex(self.storage_period[self.setting_info_temp["VIDEO_SAVE"]["period"]])
        else:
            self.ui_main.setting_event_video_storage_period.setEnabled(False)

        if self.ui_main.setting_popup_alarm_active_bnt.isChecked():
            self.ui_main.setting_popup_alarm_cnt.setEnabled(True)
            self.ui_main.setting_popup_alarm_cnt.setCurrentIndex(int(self.setting_info_temp["NOTICE"]["cnt"] - 1))
        else:
            self.ui_main.setting_popup_alarm_cnt.setEnabled(False)

        #NVR 연결 상태 및 연결된 카메라의 기존 설정 값 로드
        self.connect_nvr_flag, self.camera_info_dict_temp = self.load_camera_info(reset=False)

        if self.connect_nvr_flag:
            #카메라 리스트 채우기
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
                
                self.ui_main.camera_list_table.setItem(row_position, 1, text)

                text = QTableWidgetItem(str(camera_info["Name"]))
                text.setTextAlignment(Qt.AlignCenter)
                text.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled)
                
                self.ui_main.camera_list_table.setItem(row_position, 2, text)

                text = QTableWidgetItem(str(camera_info["IP"]))
                text.setTextAlignment(Qt.AlignCenter)
                text.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled)
                
                self.ui_main.camera_list_table.setItem(row_position, 3, text)

                #NVR에서 카메라 썸네일 이미지 불러오기
                auth = HTTPBasicAuth(self.login_info_temp["NVR"]["ID"], self.login_info_temp["NVR"]["PW"]) # NVR에 대한 ID / PW
                url = f'http://{self.login_info_temp["NVR"]["IP"]}/live/video{str(camera_info["Num"])}.jpg'
                response = requests.get(url,auth=auth, timeout= 1)
                image_bytes = np.frombuffer(response.content, dtype=np.uint8)
                frame = cv2.imdecode(image_bytes, cv2.IMREAD_COLOR)

                self.camera_img_dict[str(camera_info["Name"])] = frame

            self.start_camera_connect_status_timer()
            self.setup_camera_viewer()

        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : setup_QT_slot_connect")
        self.ui_main.server_login_bnt.clicked.connect(self.show_confirmation_dialog) #NVR 로그인 버튼 기능 활성화
        self.ui_main.shutdown_bnt.clicked.connect(self.shutdown) #종료 버튼 활성화

        #우측 상단 버튼 활성화
        self.ui_main.camera_schedule_bnt.clicked.connect(lambda click, instance = self : open_schedule_window(click, instance))
        # self.ui_main.labeling_bnt.clicked.connect(lambda click, instance = self : open_labeling_window(click, instance))

        self.ui_main.camera_list_table.itemDoubleClicked.connect(self.switch_main_display_to_camera)

        self.ui_main.camera_bnt.clicked.connect(self.switch_main_display_to_camera)
        self.ui_main.setting_bnt.clicked.connect(self.switch_main_display_to_setting)
        self.ui_main.admin_bnt.clicked.connect(self.switch_main_display_to_admin)
        self.ui_main.search_bnt.clicked.connect(lambda click, instance = self : open_search_window(click, instance))

        self.switch_main_display_to_camera()

        self.ui_main.camera_page_detect_add_bnt.clicked.connect(self.camera_page_add_detect_type)
        self.ui_main.camera_page_detect_area_del_bnt.clicked.connect(self.camera_page_del_detect_area)
        self.ui_main.camera_page_object_setting_bnt.clicked.connect(lambda click, instance = self : open_object_setting_window(click, instance))

        self.ui_main.camera_page_detect_area_table.itemClicked.connect(self.update_camera_page_viewer_roi)

        # 지능형 활성화 버튼 
        self.ui_main.camera_page_ai_bnt.clicked.connect(lambda click, instance = self : open_ai_setting_window(click, instance))

        self.ui_main.setting_user_setting_bnt.clicked.connect(self.switch_setting_display_to_user_setting)
        self.ui_main.setting_user_save_bnt.clicked.connect(self.setting_change_user_info)
        self.ui_main.setting_alarm_bnt.clicked.connect(self.switch_setting_display_to_alarm_setting)
        self.ui_main.setting_ai_bnt.clicked.connect(self.switch_setting_display_to_ai_stting)
        self.ui_main.setting_popup_alarm_active_bnt.clicked.connect(self.change_setting_info)
        self.ui_main.setting_popup_alarm_cnt.currentIndexChanged.connect(self.change_setting_info)
        self.ui_main.setting_video_save_alarm_active_bnt.clicked.connect(self.change_setting_info)
        self.ui_main.setting_event_video_storage_period.currentIndexChanged.connect(self.change_setting_info)

         # admin 메뉴 버튼
        self.ui_main.admin_page_bnt.clicked.connect(self.login_admin_page)
        self.ui_main.admin_license_bnt.clicked.connect(lambda : (self.ui_main.stackedWidget_2.setCurrentIndex(0), self.reset_admin_license_list()))
        self.ui_main.admin_fn_permission_bnt.clicked.connect(lambda : self.ui_main.stackedWidget_2.setCurrentIndex(1))
        self.ui_main.license_add_bnt.clicked.connect(self.move_active_license_list)
        self.ui_main.license_remove_bnt.clicked.connect(self.move_non_license_camera_list)
        self.ui_main.license_save_bnt.clicked.connect(self.save_admin_info)
        self.ui_main.admin_pw_input.returnPressed.connect(self.login_admin_page)

    def reset_admin_license_list(self):
        try:
            self.ui_main.non_active_license_list.clear()
            self.ui_main.active_license_list.clear()

            # 카메라 번호에 대한 체크박스를 생성하고 레이아웃에 추가
            for detect_type, active_flag in self.admin_info_temp["LICENSE"].items():
                item = QListWidgetItem(Eng2kor(detect_type))
                item.setTextAlignment(Qt.AlignCenter)

                self.ui_main.active_license_list.addItem(item) if active_flag == 1 else self.ui_main.non_active_license_list.addItem(item)
        
        except Exception as e:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            tb = traceback.format_exc()
            print(f"Error occurred at {current_time}: {e}\n{tb}", file=sys.stderr)

    def save_admin_info(self):
        try:
            save_info(host=self.HOST, port=self.PORT, file_name="admin_info", info=self.admin_info_temp)
            self.create_fade_out_msg(msg="save lisence")

        except Exception as e:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            tb = traceback.format_exc()
            print(f"Error occurred at {current_time}: {e}\n{tb}", file=sys.stderr)

    def move_active_license_list(self):
        try:
            selected_items = self.ui_main.non_active_license_list.selectedItems()
            selected_texts = [item.text() for item in selected_items]

            for detect_type in selected_texts:
                self.admin_info_temp["LICENSE"][Kor2eng(detect_type)] = 1

            self.reset_admin_license_list()
        except Exception as e:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            tb = traceback.format_exc()
            print(f"Error occurred at {current_time}: {e}\n{tb}", file=sys.stderr)

    def move_non_license_camera_list(self):
        try:
            selected_items = self.ui_main.active_license_list.selectedItems()
            selected_texts = [item.text() for item in selected_items]

            for detect_type in selected_texts:
                self.admin_info_temp["LICENSE"][Kor2eng(detect_type)] = 0

            self.reset_admin_license_list()
        except Exception as e:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            tb = traceback.format_exc()
            print(f"Error occurred at {current_time}: {e}\n{tb}", file=sys.stderr)

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
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            tb = traceback.format_exc()
            print(f"Error occurred at {current_time}: {e}\n{tb}", file=sys.stderr)

    def change_setting_info(self):
        try:
            print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : change_setting_info")
            self.setting_info_temp = load_info(host=self.HOST, port=self.PORT, file_name="setting_info")

            # self.setting_info_temp["EMAIL"]["active"] = int(self.ui_main.setting_email_active_bnt.isChecked())
            self.setting_info_temp["NOTICE"]["active"] = int(self.ui_main.setting_popup_alarm_active_bnt.isChecked())
            self.setting_info_temp["VIDEO_SAVE"]["active"] = int(self.ui_main.setting_video_save_alarm_active_bnt.isChecked())

            # for worker in self.live_page_worker_dict.values():
            #     worker.plot_bbox = self.setting_info_temp["DETECT"]["Bbox"] == 1
            #     worker.plot_label = self.setting_info_temp["DETECT"]["Label"] == 1
            #     worker.plot_roi = self.setting_info_temp["DETECT"]["Roi"] == 1

            # self.camera_page_worker.plot_bbox = self.setting_info_temp["DETECT"]["Bbox"] == 1
            # self.camera_page_worker.plot_label = self.setting_info_temp["DETECT"]["Label"] == 1
            # self.camera_page_worker.plot_roi = self.setting_info_temp["DETECT"]["Roi"] == 1


            video_save_active = self.ui_main.setting_video_save_alarm_active_bnt.isChecked()
            self.ui_main.setting_event_video_storage_period.setEnabled(video_save_active)
            if video_save_active:
                self.setting_info_temp["VIDEO_SAVE"]["period"] = self.storage_period[self.ui_main.setting_event_video_storage_period.currentIndex()]


            popup_alarm_active = self.ui_main.setting_popup_alarm_active_bnt.isChecked()
            self.ui_main.setting_popup_alarm_cnt.setEnabled(popup_alarm_active)
            if popup_alarm_active:
                self.setting_info_temp["NOTICE"]["cnt"] = self.ui_main.setting_popup_alarm_cnt.currentIndex() + 1


            save_info(host=self.HOST, port=self.PORT, file_name="setting_info", info=self.setting_info_temp)

        except Exception as e:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            tb = traceback.format_exc()
            print(f"Error occurred at {current_time}: {e}\n{tb}", file=sys.stderr)

    def switch_main_display_to_admin_2(self):
        set_button_style(self, 'admin')
        self.ui_main.stackedWidget.setCurrentIndex(3)

    def switch_setting_display_to_alarm_setting(self):
        self.ui_main.setting_alarm_bnt.setStyleSheet("""border-radius: 15px;
                                                        color: rgb(255, 255, 255);
                                                        background-color: rgb(30, 195, 55);
                                                        """)
            
        self.ui_main.setting_user_setting_bnt.setStyleSheet("""border-radius: 15px;
                                                    color: rgb(255, 255, 255);
                                                    background-color: rgb(36, 39, 44);
                                                    """)
        
        self.ui_main.setting_ai_bnt.setStyleSheet("""border-radius: 15px;
                                                    color: rgb(255, 255, 255);
                                                    background-color: rgb(36, 39, 44);
                                                    """)
        
        self.ui_main.setting_stack_widget.setCurrentIndex(0)

    def switch_setting_display_to_ai_stting(self):
        try:
            self.ui_main.setting_setting_ai_weight_box.clear()

            self.ui_main.setting_ai_bnt.setStyleSheet("""border-radius: 15px;
                                                        color: rgb(255, 255, 255);
                                                        background-color: rgb(30, 195, 55);
                                                        """)
            
            self.ui_main.setting_user_setting_bnt.setStyleSheet("""border-radius: 15px;
                                                        color: rgb(255, 255, 255);
                                                        background-color: rgb(36, 39, 44);
                                                        """)
            
            self.ui_main.setting_alarm_bnt.setStyleSheet("""border-radius: 15px;
                                                        color: rgb(255, 255, 255);
                                                        background-color: rgb(36, 39, 44);
                                                        """)

            url = f'http://{self.HOST}:{self.PORT}/get_ai_weight_list'
            receive_data = requests.post(url, json={"msg" : {}}).json()

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

            self.ui_main.setting_stack_widget.setCurrentIndex(2)

            self.ui_main.setting_self_training_auto_labeling_bnt.clicked.connect(self.change_auto_label_info)
            self.ui_main.setting_self_training_zeroshot_bnt.clicked.connect(self.change_zeroshot_info)
            self.ui_main.setting_ai_setting_save_bnt.clicked.connect(self.save_ai_setting_info)

        except Exception as e:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            tb = traceback.format_exc()
            print(f"Error occurred at {current_time}: {e}\n{tb}", file=sys.stderr)

    def save_ai_setting_info(self):
        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : AI Setting Save")

        weight_name = self.ui_main.setting_setting_ai_weight_box.currentText()
        self.setting_info_temp["AI"]["Weight"] = weight_name

        save_info(host=self.HOST, port=self.PORT, file_name="setting_info", info=self.setting_info_temp)
        self.create_fade_out_msg(msg="저장되었습니다")

    def change_zeroshot_info(self):
        self.setting_info_temp["AI"]["ZeroShot"] = 1 if self.setting_info_temp["AI"]["ZeroShot"] == 0 else 0
    def change_auto_label_info(self):
        self.setting_info_temp["AI"]["AutoLabel"] = 1 if self.setting_info_temp["AI"]["AutoLabel"] == 0 else 0


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
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            tb = traceback.format_exc()
            print(f"Error occurred at {current_time}: {e}\n{tb}", file=sys.stderr)

    def switch_setting_display_to_user_setting(self):
        try:
            self.ui_main.setting_user_setting_bnt.setStyleSheet("""border-radius: 15px;
                                                        color: rgb(255, 255, 255);
                                                        background-color: rgb(30, 195, 55);
                                                        """)
            
            self.ui_main.setting_ai_bnt.setStyleSheet("""border-radius: 15px;
                                                        color: rgb(255, 255, 255);
                                                        background-color: rgb(36, 39, 44);
                                                        """)
            
            self.ui_main.setting_alarm_bnt.setStyleSheet("""border-radius: 15px;
                                                        color: rgb(255, 255, 255);
                                                        background-color: rgb(36, 39, 44);
                                                        """)

            self.setting_info_temp = load_info(host=self.HOST, port=self.PORT, file_name="setting_info")

            self.ui_main.setting_stack_widget.setCurrentIndex(1)
            self.ui_main.setting_user_id_input.clear()
            self.ui_main.setting_user_id_input.setText(self.user_info)

            self.ui_main.setting_user_pw_input.clear()
            self.ui_main.setting_user_new_pw_input.clear()
            self.ui_main.setting_user_new_pw_input2.clear()

        except Exception as e:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            tb = traceback.format_exc()
            print(f"Error occurred at {current_time}: {e}\n{tb}", file=sys.stderr)

    def update_camera_page_viewer_roi(self, item):
        try:
            print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : camera_page_update_roi")
            row = item.row()  # 클릭한 아이템의 행 인덱스
            row_data = []
            camera_name = self.connect_camera_name
            self.ui_main.camera_page_viewer.set_point(self.camera_info_dict_temp[camera_name]["detect_info"][row][1:], [self.ui_main.camera_page_viewer.width(), self.ui_main.camera_page_viewer.height()])

            gray_point_list = []
            if self.camera_info_dict_temp[camera_name]["AI"] == False:
                for index, value in enumerate(self.camera_info_dict_temp[camera_name]["detect_info"]):
                    # 현재 인덱스가 제외할 인덱스 목록에 없으면 결과 리스트에 추가
                    if index != row:
                        gray_point_list.append(value[1:])
            self.ui_main.camera_page_viewer.set_gray_point(gray_point_list)

        except Exception as e:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            tb = traceback.format_exc()
            print(f"Error occurred at {current_time}: {e}\n{tb}", file=sys.stderr)

    def camera_page_del_detect_area(self):
        try:
            if self.camera_edit_permission:
                print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : camera_page_del_detect_area")
                camera_name = self.connect_camera_name

                select_index = self.ui_main.camera_page_detect_area_table.selectionModel().selectedRows()
                if select_index:  # 선택된 행이 있다면
                    select_row = select_index[0].row()
                    del self.camera_info_dict_temp[camera_name]["detect_info"][select_row]

                self.reset_detect_area_list(self.camera_info_dict_temp[camera_name]["detect_info"])
                self.ui_main.camera_page_viewer.reset_green_area()

            else:
                print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : Not allow camera page edit permission")
                self.create_fade_out_msg(msg ="수정 권한이 없습니다.")

        except Exception as e:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            tb = traceback.format_exc()
            print(f"Error occurred at {current_time}: {e}\n{tb}", file=sys.stderr)

    def camera_page_add_detect_type(self):
        try:
            if self.camera_edit_permission:
                print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : camera_page_add_detect_type")
                camera_name = self.connect_camera_name
                detect_type = self.ui_main.camera_page_camera_event_box.currentText()

                detect_type = Kor2eng(detect_type)

                #add_detect_type
                if detect_type in ["Intrusion", "Loitering", "Falldown", "Fire", "Fight"]:
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

            else:
                print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : Not allow camera page edit permission")
                self.create_fade_out_msg(msg = "수정 권한이 없습니다.")

        except Exception as e:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            tb = traceback.format_exc()
            print(f"Error occurred at {current_time}: {e}\n{tb}", file=sys.stderr)

    def switch_main_display_to_admin(self):
        try:
            save_info(host=self.HOST, port=self.PORT, file_name="camera_info", info=self.camera_info_dict_temp)

            set_button_style(self, 'admin')
            self.ui_main.stackedWidget.setCurrentIndex(2)

            self.ui_main.admin_pw_input.clear()

            # self.stop_camera_page_worker()
            # self.stop_live_page_worker()
            # self.change_live_page_camera_fps(1)

            # self.return_camera_page_permission()

        except Exception as e:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            tb = traceback.format_exc()
            print(f"Error occurred at {current_time}: {e}\n{tb}", file=sys.stderr)

    def switch_main_display_to_setting(self):
        try:
            save_info(host=self.HOST, port=self.PORT, file_name="camera_info", info=self.camera_info_dict_temp)

            set_button_style(self, 'setting')
            self.ui_main.stackedWidget.setCurrentIndex(1)
            self.ui_main.setting_stack_widget.setCurrentIndex(0)

            self.ui_main.setting_user_id_input.clear()
            self.ui_main.setting_user_pw_input.clear()
            self.ui_main.setting_user_new_pw_input.clear()
            self.ui_main.setting_user_new_pw_input2.clear()

            self.setting_info_temp = load_info(host=self.HOST, port=self.PORT, file_name="setting_info")

            self.update_setting()
            self.ui_main.setting_alarm_bnt.setStyleSheet("""border-radius: 15px;
                                                        color: rgb(255, 255, 255);
                                                        background-color: rgb(30, 195, 55);
                                                        """)
            
            self.ui_main.setting_ai_bnt.setStyleSheet("""border-radius: 15px;
                                                        color: rgb(255, 255, 255);
                                                        background-color: rgb(36, 39, 44);
                                                        """)
            
            self.ui_main.setting_user_setting_bnt.setStyleSheet("""border-radius: 15px;
                                                        color: rgb(255, 255, 255);
                                                        background-color: rgb(36, 39, 44);
                                                        """)

        except Exception as e:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            tb = traceback.format_exc()
            print(f"Error occurred at {current_time}: {e}\n{tb}", file=sys.stderr)

    def update_setting(self):
        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : setting update")

        setting_info_temp = load_info(host=self.HOST, port=self.PORT, file_name="setting_info")
        self.ui_main.setting_popup_alarm_active_bnt.setChecked(setting_info_temp["NOTICE"]["active"]) # 알람 발생시 프로그램 팝업알림 기능 활성화 여부
        self.ui_main.setting_video_save_alarm_active_bnt.setChecked(setting_info_temp["VIDEO_SAVE"]["active"]) # 알람 발생 영상 저장 기능 활성화 여부

        if self.ui_main.setting_video_save_alarm_active_bnt.isChecked():
            self.ui_main.setting_event_video_storage_period.setEnabled(True)
            self.ui_main.setting_event_video_storage_period.setCurrentIndex(self.storage_period[setting_info_temp["VIDEO_SAVE"]["period"]])
        
        else:
            self.ui_main.setting_event_video_storage_period.setEnabled(False)

        if self.ui_main.setting_popup_alarm_active_bnt.isChecked():
            self.ui_main.setting_popup_alarm_cnt.setEnabled(True)
            self.ui_main.setting_popup_alarm_cnt.setCurrentIndex(int(setting_info_temp["NOTICE"]["cnt"] - 1))
        
        else:
            self.ui_main.setting_popup_alarm_cnt.setEnabled(False)

    def switch_main_display_to_camera(self):
        try:
            set_button_style(self, 'camera')
            self.ui_main.stackedWidget.setCurrentIndex(0)

            self.ui_main.camera_page_camera_event_box.clear()

            data = {"msg" : ""}
            url = f'http://{self.HOST}:{self.PORT}/get_camera_page_permission'
            self.camera_edit_permission = requests.get(url, json=data).json()

            if self.camera_edit_permission:
                self.ui_main.camera_page_readmod_label.hide()
                self.ui_main.camera_page_readmod_icon.hide()

            else:
                self.ui_main.camera_page_readmod_label.show()
                self.ui_main.camera_page_readmod_icon.show()

            ret, self.camera_info_dict_temp = self.load_camera_info()
            self.admin_info_temp = load_info(host=self.HOST,port=self.PORT,file_name="admin_info")
            self.setting_info_temp = load_info(host=self.HOST, port=self.PORT, file_name="setting_info")
            self.login_info_temp = load_info(host=self.HOST, port=self.PORT, file_name="login_info")

            selected_indexes = self.ui_main.camera_list_table.selectedIndexes()

            if selected_indexes:
                selected_row = selected_indexes[0].row()  # 선택된 셀의 행 인덱스
                self.connect_camera_name = self.ui_main.camera_list_table.item(selected_row, 2).text()

                self.connect_camera_page_camera(camera_name=self.connect_camera_name)
                self.set_camera_page_viewer(camera_name=self.connect_camera_name)

            else:
                self.connect_camera_name = self.ui_main.camera_list_table.item(0, 2).text()

                self.connect_camera_page_camera(camera_name=self.connect_camera_name)
                self.set_camera_page_viewer(camera_name=self.connect_camera_name)

            for detect_type in self.admin_info_temp["LICENSE"]:
                if self.admin_info_temp["LICENSE"][detect_type] == 1:
                    self.ui_main.camera_page_camera_event_box.addItems([Eng2kor(detect_type)])

        except Exception as e:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            tb = traceback.format_exc()
            print(f"Error occurred at {current_time}: {e}\n{tb}", file=sys.stderr)

    def connect_camera_page_camera(self, camera_name = None):
        try:

            if self.camera_page_worker is not None:
                self.camera_page_worker.stop()
                del self.camera_page_worker

            print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : connect_camera_page_camera")

            nvr_id = self.login_info_temp["NVR"]["ID"]
            nvr_pw = self.login_info_temp["NVR"]["PW"]
            nvr_ip = self.login_info_temp["NVR"]["IP"]

            if camera_name in self.camera_info_dict_temp.keys():
                camera_info = self.camera_info_dict_temp[camera_name]
                camera_num = camera_info["Num"]

                
                pipe = f"rtsp://{nvr_id}:{nvr_pw}@{nvr_ip}/video{camera_num}"
                print(pipe)


                self.camera_page_worker = Connect_Camera(pipe = pipe)

                self.camera_page_worker.ImageUpdated.connect(lambda image, viewer=self.ui_main.camera_page_viewer: self.ShowCamera(viewer, image))
                self.camera_page_worker.start()

            else:
                # 유효하지 않은 인덱스 처리
                print("선택된 카메라 인덱스가 범위를 벗어났습니다.")
                self.create_fade_out_msg(msg="선택된 카메라 인덱스가 범위를 벗어났습니다.")
                pass
                
        except Exception as e:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            tb = traceback.format_exc()
            print(f"Error occurred at {current_time}: {e}\n{tb}", file=sys.stderr)

    def set_camera_page_viewer(self, camera_name = None):
        try:
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
                    # self.camera_page_worker.ai_active = False
                else:
                    self.ui_main.camera_page_ai_active_label.show()
                    self.ui_main.camera_page_ai_active_icon.show()
                    # self.camera_page_worker.ai_active = True

                self.ui_main.camera_page_viewer.set_gray_point(gray_point_list)

        except Exception as e:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            tb = traceback.format_exc()
            print(f"Error occurred at {current_time}: {e}\n{tb}", file=sys.stderr)

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

    ##지능형 카메라 설정 영상 뷰어 생성하는 함수
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
                camera_name = self.connect_camera_name
                select_index = self.ui_main.camera_page_detect_area_table.selectionModel().selectedRows()

                if select_index:  # 선택된 행이 있다면
                    select_row = select_index[0].row()

                    if point.x() == -1 :
                        if len(self.camera_info_dict_temp[camera_name]["detect_info"][select_row]) > 1:
                            self.camera_info_dict_temp[camera_name]["detect_info"][select_row].pop()

                        else: pass
                    else:
                        self.camera_info_dict_temp[camera_name]["detect_info"][select_row].append([point.x()/ self.ui_main.camera_page_viewer.width(), 
                                                                                                point.y()/self.ui_main.camera_page_viewer.height()])

                    self.ui_main.camera_page_viewer.set_point(self.camera_info_dict_temp[camera_name]["detect_info"][select_row][1:], [self.ui_main.camera_page_viewer.width(), self.ui_main.camera_page_viewer.height()])

                    gray_point_list = []
                    if self.camera_info_dict_temp[camera_name]["AI"] == False:
                        for index, value in enumerate(self.camera_info_dict_temp[camera_name]["detect_info"]):
                            # 현재 인덱스가 제외할 인덱스 목록에 없으면 결과 리스트에 추가
                            if index != select_row:
                                gray_point_list.append(value[1:])

                    self.ui_main.camera_page_viewer.set_gray_point(gray_point_list)
            
            else:
                print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : Not allow camera page edit permission")
                self.create_fade_out_msg(msg ="수정 권한이 없습니다.")


        except Exception as e:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            tb = traceback.format_exc()
            print(f"Error occurred at {current_time}: {e}\n{tb}", file=sys.stderr)
    

    #카메라 연결 상태를 주기적으로 확인하는 함수
    def start_camera_connect_status_timer(self):
        self.check_camera_connect_status()

        self.camera_connect_status_timer = QTimer(self)
        self.camera_connect_status_timer.timeout.connect(self.check_camera_connect_status)

        #누적된 알람 초기화
        data = {"msg" : str(" ")}
        url = f'http://{self.HOST}:{self.PORT}/get-alarm-info'
        receive_data = requests.get(url, json=data).json()
        
        self.camera_connect_status_timer.start(1000)  # 타이머 시작 n초에 한번씩

    #카메라 연결 상태를 표시하는 함수
    def check_camera_connect_status(self):
        try:
            on_camera_pix = QPixmap(u":/ui/ui/images/ico_video_on.svg").scaled(24, 24, Qt.KeepAspectRatio)
            off_camera_pix = QPixmap(u":/ui/ui/images/ico_video_off.svg").scaled(24, 24, Qt.KeepAspectRatio)

            data = {"msg" : {"ip" : self.login_info_temp["NVR"]["IP"], "id" : self.login_info_temp["NVR"]["ID"], "pw" : self.login_info_temp["NVR"]["PW"]}}
            url = f'http://{self.HOST}:{self.PORT}/get-camera-connect_status'
            receive_data = requests.get(url, json=data).json()

            if receive_data["success"] == True:
                camera_connect_status_dict = receive_data["data"]

                for camera_name, flag in camera_connect_status_dict.items():
                    row_index = find_in_first_column(self, camera_name)
                    if row_index is not None:
                        label = QLabel()

                        if flag: label.setPixmap(on_camera_pix)
                        else: label.setPixmap(off_camera_pix)

                        label.setAlignment(Qt.AlignCenter)
                        self.ui_main.camera_list_table.setCellWidget(row_index, 0, label)

        except Exception as e:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            tb = traceback.format_exc()
            print(f"Error occurred at {current_time}: {e}\n{tb}", file=sys.stderr)

    #NVR에 연결된 카메라 전체 정보를 가져오는 함수
    def load_camera_info(self, reset = False):
        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : load_camera_info")
        
        login_info = load_info(host=self.HOST, port=self.PORT, file_name="login_info")
        
        # 상단 NVR 서버 정보 입력
        data = {"ip" : login_info["NVR"]["IP"], "id" : login_info["NVR"]["ID"], "pw" : login_info["NVR"]["PW"], "reset" : reset}
        url = f'http://{self.HOST}:{self.PORT}/load_camera_info'
        receive_data = requests.post(url, json=data).json()
        camera_info_dict = {}

        if receive_data["success"] == True:
            # self.create_fade_out_msg(msg="init camera")
            camera_info_dict = receive_data["data"]

            return receive_data["success"], camera_info_dict
        
        return receive_data["success"], camera_info_dict
    

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
