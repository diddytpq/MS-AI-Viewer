import sys
import os
from pathlib import Path

from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QLabel, QWidget, QDialog, QListWidgetItem
from PySide6.QtGui import QImage, QPixmap, QPainter, QPen, QColor, QPolygon, QBrush, QFont, QStandardItem, QStandardItemModel, QIcon, QWheelEvent
from PySide6.QtCore import QEvent, Qt, QThread, Signal, QRect, QPoint, QTimer, QDate, QUrl, QSize
from PySide6 import QtCore
from ui.login_ui import Ui_Dialog
from ui.main_ui import Ui_MainWindow


from utils_ai_setting_window import open_ai_setting_window
from utils_search_window import open_search_window
from utils_schedule_window import open_schedule_window
from utils_labeling_window import open_labeling_window


import socket
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
                self.main_window = MainWindow(user_info = receive_data["user_info"], host = self.HOST, port = self.PORT)
                self.main_window.show()
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

class MainWindow(QMainWindow):
    def __init__(self, user_info, host, port):
        super(MainWindow, self).__init__()
        self.ui_main = Ui_MainWindow()
        self.setWindowTitle("MS-AI")
        self.ui_main.setupUi(self)
        self.user_info = user_info
        self.open_labeling_window = False
        self.HOST = host
        self.PORT = port

        # self.ui_main.camera_page_detect_area_table.setColumnWidth(0, 60)

        self.init_GUI_setup()
        self.ui_main.stackedWidget.setCurrentIndex(0)

        # time.sleep(1)

        # self.showMaximized()
        # 윈도우 플래그 설정: 최대화 버튼 활성화
        # self.setWindowState(Qt.WindowNoState)
        # self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowMaximizeButtonHint | Qt.WindowMinimizeButtonHint)

        self.ui_main.sever_login_bnt.clicked.connect(self.login_NVR)

        #종료 버튼 활성화
        self.ui_main.shutdown_bnt.clicked.connect(self.shutdown)
        # 카메라 리스트 표 간격 설정
        self.ui_main.camera_list_table.setColumnWidth(0, 30)
        self.ui_main.camera_list_table.setColumnWidth(1, 40)
        self.ui_main.camera_list_table.setColumnWidth(2, 175)
        # self.ui_main.camera_list_table.setColumnWidth(3, 60)

        #우측 상단 버튼 활성화
        self.ui_main.alarm_search_bnt.clicked.connect(lambda click, instance = self : open_search_window(click, instance))
        self.ui_main.camera_schedule_bnt.clicked.connect(lambda click, instance = self : open_schedule_window(click, instance))
        self.ui_main.labeling_bnt.clicked.connect(lambda click, instance = self : open_labeling_window(click, instance))
        self.ui_main.camera_refresh_bnt.clicked.connect(self.live_refresh_live_viewer)
        # self.ui_main.camera_schedule_bnt.clicked.connect(lambda: open_schedule_window(self))

        ##카메라 페이지 영상 뷰어 생성
        self.ui_main.camera_page_viewer.hide()
        self.ui_main.camera_page_viewer = Plot_Camera_Viewer(self.ui_main.camera_page)
        self.ui_main.camera_page_viewer.setObjectName(u"camera_page_viewer")
        self.ui_main.camera_page_viewer.setMinimumSize(QSize(472, 331))
        self.ui_main.camera_page_viewer.setStyleSheet(u"border: 1px solid rgb(255, 255, 255);\n"
                                                "background-color: rgba(255, 255, 255, 0);")
        self.ui_main.camera_page_viewer.setScaledContents(False)
        self.ui_main.verticalLayout_10.addWidget(self.ui_main.camera_page_viewer)

        ##카메라 리스트 및 카메라 속성 리스트
        self.ui_main.camera_list_table.itemSelectionChanged.connect(self.camera_page_display_selected_row)

        self.ui_main.camera_info_name_input.installEventFilter(self)# 이벤트 필터 설치
        self.ui_main.camera_info_ip_input.installEventFilter(self)  # 이벤트 필터 설치
        self.ui_main.camera_info_id_input.installEventFilter(self)  # 이벤트 필터 설치
        self.ui_main.camera_info_pw_input.installEventFilter(self)  # 이벤트 필터 설치

        #카메라 속성 변경 버튼
        self.ui_main.camera_add_bn.hide()
        self.ui_main.camera_remove_bn.hide()
        # self.ui_main.camera_add_bn.clicked.connect(self.add_camera_info)
        # self.ui_main.camera_remove_bn.clicked.connect(self.del_camera_info)

        ##주요 메인 메뉴 버튼 설정
        self.ui_main.live_bnt.clicked.connect(self.switch_main_display_to_live)
        self.ui_main.camera_bnt.clicked.connect(self.switch_main_display_to_camera)
        self.ui_main.setting_bnt.clicked.connect(self.switch_main_display_to_setting)
        self.ui_main.admin_bnt.clicked.connect(self.switch_main_display_to_admin)

        ##카메라 페이지 설정
        self.ui_main.camera_page_name_box.currentTextChanged.connect(self.camera_page_display_camera_and_detect_area_list)
        self.ui_main.camera_page_detect_add_bnt.clicked.connect(self.camera_page_add_detect_type)
        self.ui_main.camera_page_detect_area_del_bnt.clicked.connect(self.camera_page_del_detect_area)

        self.ui_main.camera_page_detect_area_table.itemClicked.connect(self.camera_page_update_camera_page_viewer_roi)
        self.ui_main.camera_page_viewer.clicked.connect(self.camera_page_add_detect_area_point)

        # self.ui_main.camera_page_person_conf_slider.sliderReleased.connect(self.set_person_conf_value)
        self.ui_main.camera_page_person_conf_slider.valueChanged.connect(self.set_person_conf_value)
        
        self.ui_main.camera_page_person_conf_value.valueChanged.connect(self.set_person_conf_slider)

        # 지능형 활성화 버튼 
        self.ui_main.camera_page_ai_bnt.clicked.connect(lambda click, instance = self : open_ai_setting_window(click, instance))

        # 설정 메뉴
        self.ui_main.setting_user_setting_bnt.clicked.connect(self.switch_setting_display_to_user_setting)

        self.ui_main.setting_user_id_input.installEventFilter(self)# 이벤트 필터 설치
        self.ui_main.setting_user_pw_input.installEventFilter(self)  # 이벤트 필터 설치
        self.ui_main.setting_user_new_pw_input.installEventFilter(self)  # 이벤트 필터 설
        self.ui_main.setting_user_new_pw_input2.installEventFilter(self)  # 이벤트 필터 설치
        self.ui_main.setting_email_id_input.installEventFilter(self)  # 이벤트 필터 설치
        self.ui_main.setting_email_pw_input.installEventFilter(self)  # 이벤트 필터 설치
        self.ui_main.setting_receive_email_id_input.installEventFilter(self)  # 이벤트 필터 설치
        self.ui_main.admin_pw_input.installEventFilter(self)  # 이벤트 필터 설치
        
        self.ui_main.setting_user_save_bnt.clicked.connect(self.setting_change_user_info)
        self.ui_main.setting_alarm_bnt.clicked.connect(self.switch_setting_display_to_notice_stting)
        self.ui_main.setting_ai_bnt.clicked.connect(self.switch_setting_display_to_ai_stting)


        self.ui_main.setting_email_save_bnt.clicked.connect(self.change_email_info)
        self.ui_main.setting_email_active_bnt.clicked.connect(self.change_setting_info)
        self.ui_main.setting_popup_alarm_active_bnt.clicked.connect(self.change_setting_info)
        self.ui_main.setting_popup_alarm_cnt.currentIndexChanged.connect(self.change_setting_info)

        self.ui_main.setting_video_save_alarm_active_bnt.clicked.connect(self.change_setting_info)
        self.ui_main.setting_event_video_storage_period.currentIndexChanged.connect(self.change_setting_info)
        self.ui_main.setting_detect_bbox_active_bnt.clicked.connect(self.change_setting_info)
        self.ui_main.setting_detect_label_active_bnt.clicked.connect(self.change_setting_info)

        # admin 메뉴
        self.ui_main.admin_page_bnt.clicked.connect(self.login_admin_page)
        self.ui_main.admin_license_bnt.clicked.connect(self.switch_admin_license_page)
        self.ui_main.admin_fn_permission_bnt.clicked.connect(self.switch_admin_fn_permission_page)

        self.ui_main.license_add_bnt.clicked.connect(self.move_active_license_list)
        self.ui_main.license_remove_bnt.clicked.connect(self.move_non_license_camera_list)

        self.ui_main.license_save_bnt.clicked.connect(self.save_admin_info)

        self.ui_main.admin_pw_input.returnPressed.connect(self.login_admin_page)
        
#---------------------------------------------------------------------------------------------------------#
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

    def set_person_conf_value(self):
        try:
            # ret, camera_info_dict, camera_info_ori = self.load_camera_info(reset=False, connect_nvr = self.check_nvr_login())
            # ret, camera_info_dict = self.load_camera_info()


            self.ui_main.camera_page_person_conf_value.setValue(self.ui_main.camera_page_person_conf_slider.value())
            camera_name = self.ui_main.camera_page_name_box.currentText()

            self.camera_info_dict_temp[camera_name]["Conf"] = self.ui_main.camera_page_person_conf_value.value()
            # save_info(host=self.HOST, port=self.PORT, file_name="camera_info", info=self.camera_info_dict_temp)

        except Exception as e:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            tb = traceback.format_exc()
            print(f"Error occurred at {current_time}: {e}\n{tb}", file=sys.stderr)

    def set_person_conf_slider(self):
        try:
            # ret, camera_info_dict, camera_info_ori = self.load_camera_info(reset=False, connect_nvr = self.check_nvr_login())
            # ret, camera_info_dict = self.load_camera_info()


            self.ui_main.camera_page_person_conf_slider.setValue(self.ui_main.camera_page_person_conf_value.value())
            camera_name = self.ui_main.camera_page_name_box.currentText()

            self.camera_info_dict_temp[camera_name]["Conf"] = self.ui_main.camera_page_person_conf_value.value()
            # save_info(host=self.HOST, port=self.PORT, file_name="camera_info", info=self.camera_info_dict_temp)

        except Exception as e:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            tb = traceback.format_exc()
            print(f"Error occurred at {current_time}: {e}\n{tb}", file=sys.stderr)

    def shutdown(self):
        QApplication.instance().quit()
        for worker in self.camera_worker_dict.values():
            worker.stop()
            del worker

        if self.camera_page_worker != None :
            self.camera_page_worker.stop()
            del self.camera_page_worker

        # data = {"msg" : ""}
        # url = f'http://{self.HOST}:{self.PORT}/logout'
        # receive_data = requests.put(url, json=data).json()

        # sys.exit()
    
    def save_admin_info(self):
        try:
            save_info(host=self.HOST, port=self.PORT, file_name="admin_info", info=self.admin_info_temp)
            self.create_fade_out_msg(msg="save lisence")

        except Exception as e:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            tb = traceback.format_exc()
            print(f"Error occurred at {current_time}: {e}\n{tb}", file=sys.stderr)

    def login_admin_page(self):
        try:
            if "0512" == self.ui_main.admin_pw_input.text():
                self.switch_main_display_to_admin_2()
                self.switch_admin_license_page()

            else:
                self.create_fade_out_msg(msg="Invalid PW")
        except Exception as e:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            tb = traceback.format_exc()
            print(f"Error occurred at {current_time}: {e}\n{tb}", file=sys.stderr)

    def start_camera_connect_status_timer(self):
        if self.timer is not None :
            self.timer.stop()
            del self.timer
        self.check_camera_connect_status()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.check_camera_connect_status)

        #누적된 알람 초기화
        data = {"msg" : str(" ")}
        url = f'http://{self.HOST}:{self.PORT}/get-alarm-info'
        receive_data = requests.get(url, json=data).json()
        
        self.timer.timeout.connect(self.Notification_status)

        self.timer.start(1000)  # 타이머 시작 5초에 한번씩

    def start_camera_refresh_timer(self):
        if self.camera_connect_timer is not None :
            self.camera_connect_timer.stop()
            del self.camera_connect_timer

        self.camera_connect_timer = QTimer(self)
        self.camera_connect_timer.timeout.connect(self.live_refresh_live_viewer)

        self.camera_connect_timer.start(600000)  # 타이머 시작

    def change_setting_info(self):
        try:
            self.setting_info_temp = load_info(host=self.HOST, port=self.PORT, file_name="setting_info")

            self.setting_info_temp["EMAIL"]["active"] = 1 if self.ui_main.setting_email_active_bnt.isChecked() else 0
            self.setting_info_temp["NOTICE"]["active"] = 1 if self.ui_main.setting_popup_alarm_active_bnt.isChecked() else 0
            self.setting_info_temp["VIDEO_SAVE"]["active"] = 1 if self.ui_main.setting_video_save_alarm_active_bnt.isChecked() else 0
            self.setting_info_temp["DETECT"]["Bbox"] = 1 if self.ui_main.setting_detect_bbox_active_bnt.isChecked() else 0
            self.setting_info_temp["DETECT"]["Label"] = 1 if self.ui_main.setting_detect_label_active_bnt.isChecked() else 0

            for worker in self.camera_worker_dict.values():
                if self.setting_info_temp["DETECT"]["Bbox"] == 1:
                    worker.plot_bbox = True
                else: worker.plot_bbox = False

                if self.setting_info_temp["DETECT"]["Label"] == 1:
                    worker.plot_label = True
                else: worker.plot_label = False

            # self.camera_page_worker.plot_bbox = self.setting_info["DETECT"]["Bbox"]
            # self.camera_page_worker.plot_label = self.setting_info["DETECT"]["Label"]

            if self.ui_main.setting_video_save_alarm_active_bnt.isChecked():
                self.ui_main.setting_event_video_storage_period.setEnabled(True)
                self.setting_info_temp["VIDEO_SAVE"]["period"] = self.storage_period[self.ui_main.setting_event_video_storage_period.currentIndex()]

            else:
                self.ui_main.setting_event_video_storage_period.setEnabled(False)

            if self.ui_main.setting_popup_alarm_active_bnt.isChecked():
                self.ui_main.setting_popup_alarm_cnt.setEnabled(True)
                self.setting_info_temp["NOTICE"]["cnt"] = self.ui_main.setting_popup_alarm_cnt.currentIndex() + 1

            else:
                self.ui_main.setting_popup_alarm_cnt.setEnabled(False)


            save_info(host=self.HOST, port=self.PORT, file_name="setting_info", info=self.setting_info_temp)

            # self.start_timer()

        except Exception as e:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            tb = traceback.format_exc()
            print(f"Error occurred at {current_time}: {e}\n{tb}", file=sys.stderr)

    def change_email_info(self):
        try:
            self.setting_info_temp = load_info(host=self.HOST,port=self.PORT,file_name="setting_info")

            self.setting_info_temp["EMAIL"]["sender"] = self.ui_main.setting_email_id_input.text()
            self.setting_info_temp["EMAIL"]["PW"] = self.ui_main.setting_email_pw_input.text()
            self.setting_info_temp["EMAIL"]["TO"] = self.ui_main.setting_receive_email_id_input.text()

            save_info(host=self.HOST, port=self.PORT, file_name="setting_info", info=self.setting_info_temp)

        except Exception as e:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            tb = traceback.format_exc()
            print(f"Error occurred at {current_time}: {e}\n{tb}", file=sys.stderr)

    def check_camera_viewer_click(self, viewer):
        if viewer.click_count >= 1:
            self.switch_main_display_to_camera()
            self.set_button_style('camera')
            self.ui_main.stackedWidget.setCurrentIndex(1)
            index = self.ui_main.camera_page_name_box.findText(viewer.camera_name)
            self.ui_main.camera_page_name_box.setCurrentIndex(index)

            # for worker in self.camera_worker_list:
            #     worker.stop()
            #     del worker

            for camera_name, camera_viewer in self.camera_view_list.items():
                camera_viewer.click_count = 0

    def setting_change_user_info(self):
        try:
            data = {"username" : self.ui_main.setting_user_id_input.text(), 
                    "password" : self.ui_main.setting_user_pw_input.text(),
                    "new_password" : self.ui_main.setting_user_new_pw_input.text(),
                    "new_password2" : self.ui_main.setting_user_new_pw_input2.text(),
                    }
            url = f'http://{self.HOST}:{self.PORT}/login_chg'
            receive_data = requests.post(url, json=data).json()

            self.create_fade_out_msg(msg=receive_data["message"])

        except Exception as e:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            tb = traceback.format_exc()
            print(f"Error occurred at {current_time}: {e}\n{tb}", file=sys.stderr)

    def camera_page_del_detect_area(self):
        try:
            # ret, self.camera_info_dict_temp = self.load_camera_info(reset=False)

            camera_name = self.ui_main.camera_page_name_box.currentText()

            select_index = self.ui_main.camera_page_detect_area_table.selectionModel().selectedRows()
            if select_index:  # 선택된 행이 있다면
                select_row = select_index[0].row()
                del self.camera_info_dict_temp[camera_name]["detect_info"][select_row]

            self.reset_detect_area_list(self.camera_info_dict_temp[camera_name]["detect_info"])
            self.ui_main.camera_page_viewer.reset_green_area()
            # save_info(host=self.HOST, port=self.PORT, file_name="camera_info", info=self.camera_info_dict_temp)

            # cmd = {"msg" : ["change_camera_info"]}
            # receive_data = socket_communication(self.HOST, self.PORT, cmd, on_data_received)
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


    def camera_page_update_camera_page_viewer_roi(self, item):
        try:
            # ret, camera_info_dict = self.load_camera_info()
            
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
            # self.ui_main.camera_page_viewer.set_gray_point(gray_point_list, [self.ui_main.camera_page_viewer.width(), self.ui_main.camera_page_viewer.height()])
            self.ui_main.camera_page_viewer.set_gray_point(gray_point_list)

        except Exception as e:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            tb = traceback.format_exc()
            print(f"Error occurred at {current_time}: {e}\n{tb}", file=sys.stderr)

    def camera_page_add_detect_type(self):
        try:
            # ret, camera_info_dict = self.load_camera_info()

            camera_name = self.ui_main.camera_page_name_box.currentText()
            detect_type = self.ui_main.camera_page_camera_event_box.currentText()

            detect_type = Kor2eng(detect_type)

            if detect_type == "Intrusion" :
                self.camera_info_dict_temp[camera_name]["detect_info"].append(["Intrusion"])

            elif detect_type == "Loitering" :
                self.camera_info_dict_temp[camera_name]["detect_info"].append(["Loitering"])

            elif detect_type == "Falldown" :
                self.camera_info_dict_temp[camera_name]["detect_info"].append(["Falldown"])

            elif detect_type == "Fire" :
                self.camera_info_dict_temp[camera_name]["detect_info"].append(["Fire"])

            elif detect_type == "Fight" :
                self.camera_info_dict_temp[camera_name]["detect_info"].append(["Fight"])

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
            # self.ui_main.camera_page_viewer.set_gray_point(gray_point_list, [self.ui_main.camera_page_viewer.width(), self.ui_main.camera_page_viewer.height()])
            self.ui_main.camera_page_viewer.set_gray_point(gray_point_list)
            # save_info(host=self.HOST, port=self.PORT, file_name="camera_info", info=self.camera_info_dict_temp)

            # cmd = {"msg" : ["change_camera_info"]}
            # receive_data = socket_communication(self.HOST, self.PORT, cmd, on_data_received)
        except Exception as e:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            tb = traceback.format_exc()
            print(f"Error occurred at {current_time}: {e}\n{tb}", file=sys.stderr)

    def camera_page_add_detect_area_point(self, point): #마우스 클릭으로 생성된 포인트를 viewer에 표시
        try:
            # ret, camera_info_dict = self.load_camera_info()
            
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

                # self.ui_main.camera_page_viewer.set_gray_point(gray_point_list, [self.ui_main.camera_page_viewer.width(), self.ui_main.camera_page_viewer.height()])
                self.ui_main.camera_page_viewer.set_gray_point(gray_point_list)
            # save_info(host=self.HOST, port=self.PORT, file_name="camera_info", info=self.camera_info_dict_temp)
            # cmd = {"msg" : ["change_camera_info"]}
            # receive_data = socket_communication(self.HOST, self.PORT, cmd, on_data_received)
        except Exception as e:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            tb = traceback.format_exc()
            print(f"Error occurred at {current_time}: {e}\n{tb}", file=sys.stderr)

    def camera_page_display_camera_and_detect_area_list(self, camera_name):
        try:
            # ret, camera_info_dict = self.load_camera_info()
            # setting_info = load_info(host=self.HOST, port=self.PORT, file_name="setting_info")
            # login_info = load_info(host=self.HOST, port=self.PORT, file_name="login_info")

            nvr_id = self.login_info_temp["NVR"]["ID"]
            nvr_pw = self.login_info_temp["NVR"]["PW"]
            nvr_ip = self.login_info_temp["NVR"]["IP"]

            # 선택된 카메라 인덱스에 해당하는 이미지를 QLabel에 표시
            if self.camera_page_worker != None :
                self.camera_page_worker.stop()
                del self.camera_page_worker
                self.camera_page_worker = None

            if camera_name in self.camera_info_dict_temp.keys():
                camera_info = self.camera_info_dict_temp[camera_name]
                camera_num = camera_info["Num"]

                pipe = f"{nvr_id}:{nvr_pw}@{nvr_ip}/normal{camera_num}"

                self.camera_page_worker = Connect_Camera(pipe = pipe,
                                                        host=self.HOST, 
                                                        port=self.PORT, 
                                                        camera_name = camera_info["Name"], 
                                                        # camera_num=camera_info["Num"], 
                                                        roi_thickness = 2,
                                                        plot_bbox=self.setting_info_temp["DETECT"]["Bbox"],
                                                        plot_label=self.setting_info_temp["DETECT"]["Label"],
                                                        viewer = self.ui_main.camera_page_viewer)

                self.camera_page_worker.ImageUpdated.connect(lambda image, viewer=self.ui_main.camera_page_viewer: self.ShowCamera(viewer, image))
                self.camera_page_worker.start()

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

                self.ui_main.camera_page_person_conf_value.setValue(camera_info["Conf"])
                self.ui_main.camera_page_person_conf_slider.setValue(camera_info["Conf"])

            else:
                # 유효하지 않은 인덱스 처리
                # print("선택된 카메라 인덱스가 범위를 벗어났습니다.")
                # self.create_fade_out_msg(msg="선택된 카메라 인덱스가 범위를 벗어났습니다.")
                pass
                
        except Exception as e:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            tb = traceback.format_exc()
            print(f"Error occurred at {current_time}: {e}\n{tb}", file=sys.stderr)

    def reset_detect_area_list(self, camera_detect_info):
        self.ui_main.camera_page_detect_area_table.setRowCount(0)

        for detect_type_list in camera_detect_info:
            detect_type_text = Eng2kor(detect_type_list[0])

            # for roi in roi_list:
            row_position = self.ui_main.camera_page_detect_area_table.rowCount()
            self.ui_main.camera_page_detect_area_table.insertRow(row_position)
            text = QTableWidgetItem(detect_type_text)
            text.setTextAlignment(Qt.AlignCenter)
            text.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled)
            self.ui_main.camera_page_detect_area_table.setItem(row_position, 0, text)

            # roi_text = str(roi_list)
            # text = QTableWidgetItem(roi_text)
            # text.setTextAlignment(Qt.AlignCenter)
            # text.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled)
            # self.ui_main.camera_page_detect_area_table.setItem(row_position, 1, text)

    def live_refresh_live_viewer(self):
        try:
            print("refresh live viwer")
            for worker in self.camera_worker_dict.values():
                worker.stop()
                del worker
                gc.collect()

            self.connect_live_page_camera()
            print("finish refresh live viwer")

        except Exception as e:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            tb = traceback.format_exc()
            print(f"Error occurred at {current_time}: {e}\n{tb}", file=sys.stderr)

    def connect_live_page_camera(self, reset=False):
        try:
            ret, self.camera_info_dict_temp = self.load_camera_info(reset=reset, connect_nvr=self.check_nvr_login())

            self.camera_worker_dict = {}
            setting_info_temp = load_info(host=self.HOST, port=self.PORT, file_name="setting_info")
            login_info = load_info(host=self.HOST, port=self.PORT, file_name="login_info")
            nvr_id = login_info["NVR"]["ID"]
            nvr_pw = login_info["NVR"]["PW"]
            nvr_ip = login_info["NVR"]["IP"]

            cameras_grouped = {}
            camera_viewers = {}
            thread_index = 0

            for idx, (camera_name, camera_info) in enumerate(self.camera_info_dict_temp.items()):
                if len(camera_info["IP"]):
                    camera_num = camera_info["Num"]
                    pipe = f"{nvr_id}:{nvr_pw}@{nvr_ip}/normal{camera_num}"
                    viewer = self.camera_view_list[camera_name]

                    if thread_index not in cameras_grouped:
                        cameras_grouped[thread_index] = {}
                        camera_viewers[thread_index] = {}

                    cameras_grouped[thread_index][camera_name] = {
                        'pipe': pipe,
                        'roi_thickness': setting_info_temp["DETECT"]["Bbox"],
                        'ai_active': camera_info["AI"],
                        'back_url': f"http://{self.HOST}:{self.PORT}/get-camera-info"
                    }
                    camera_viewers[thread_index][camera_name] = viewer

                    if len(cameras_grouped[thread_index]) >= 1:
                        thread_index += 1

            for idx, cameras in cameras_grouped.items():
                worker = Connect_Camera_Group(cameras=cameras, 
                                              host=self.HOST, 
                                              port=self.PORT, 
                                              viewers=camera_viewers[idx],
                                              viewers_widget=self.ui_main.live_page,
                                              settings={"plot_bbox": setting_info_temp["DETECT"]["Bbox"],
                                                        "plot_label": setting_info_temp["DETECT"]["Label"]},
                                                
                                                )
                worker.ImageUpdated.connect(self.ShowCamera_Group)
                worker.start()
                self.camera_worker_dict[f"worker_{idx}"] = worker

        except Exception as e:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            tb = traceback.format_exc()
            print(f"Error occurred at {current_time}: {e}\n{tb}", file=sys.stderr)

    def find_in_first_column(self, text):
        # 첫 번째 열에서 특정 문자를 포함한 행의 인덱스를 반환
        for row in range(self.ui_main.camera_list_table.rowCount()):
            item = self.ui_main.camera_list_table.item(row, 2)  # 첫 번째 열의 항목 가져오기
            if item is not None and text in item.text():
                return row
        return None

    def check_camera_connect_status(self):
        try:
            for worker in self.camera_worker_dict.values():
                for camera_name, flag in worker.camera_connect_flag.items():
                    row_index = self.find_in_first_column(camera_name)
                    if row_index is not None:
                        if flag:
                            label = QLabel()
                            # pixmap = QPixmap("./images/ico_video_on.svg").scaled(24, 24, Qt.KeepAspectRatio)
                            pixmap = QPixmap(u":/newPrefix/ui/images/ico_video_on.svg").scaled(24, 24, Qt.KeepAspectRatio)

                            label.setPixmap(pixmap)
                            label.setAlignment(Qt.AlignCenter)
                            self.ui_main.camera_list_table.setCellWidget(row_index, 0, label)
                        else:
                            label = QLabel()
                            # pixmap = QPixmap("./images/ico_video_off.svg").scaled(24, 24, Qt.KeepAspectRatio)
                            pixmap = QPixmap(u":/newPrefix/ui/images/ico_video_off.svg").scaled(24, 24, Qt.KeepAspectRatio)

                            label.setPixmap(pixmap)
                            label.setAlignment(Qt.AlignCenter)
                            self.ui_main.camera_list_table.setCellWidget(row_index, 0, label)

        except Exception as e:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            tb = traceback.format_exc()
            print(f"Error occurred at {current_time}: {e}\n{tb}", file=sys.stderr)

    @QtCore.Slot()
    def ShowCamera(self, view, frame: QImage) -> None:
        # frame = frame.scaled(view.width(), view.height(), Qt.IgnoreAspectRatio, Qt.FastTransformation)
        view.setPixmap(QPixmap.fromImage(frame))
        
    @QtCore.Slot()
    def ShowCamera_Group(self, camera_name: str, frame: QImage) -> None:
        viewer = self.camera_view_list[camera_name]
        viewer.setPixmap(QPixmap.fromImage(frame))

    def on_data_received(self, data):
        receive_data = json.loads(data)
        return receive_data["msg"]

    def set_button_style(self, active_button):
        # 모든 버튼을 기본 스타일로 설정
        default_style = "color: white; border: 1px solid rgba(191, 64, 64, 0); background-color: rgba(191, 64, 64, 0);"
        active_style = "color: green; border: 1px solid rgba(191, 64, 64, 0); background-color: rgba(191, 64, 64, 0);"
        
        buttons = {
            'live': self.ui_main.live_bnt,
            'camera': self.ui_main.camera_bnt,
            'setting': self.ui_main.setting_bnt,
            'admin': self.ui_main.admin_bnt
        }
        
        for key, button in buttons.items():
            button.setStyleSheet(active_style if key == active_button else default_style)

    def switch_main_display_to_live(self):
        try:
            self.set_button_style('live')
            self.ui_main.stackedWidget.setCurrentIndex(0)
            self.ui_main.camera_refresh_bnt.show()

            # self.connect_live_page_camera()

            if self.camera_page_worker != None :
                self.camera_page_worker.stop()
                del self.camera_page_worker
                self.camera_page_worker = None

            save_info(host=self.HOST, port=self.PORT, file_name="camera_info", info=self.camera_info_dict_temp)
            # self.live_refresh_live_viewer()
        except Exception as e:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            tb = traceback.format_exc()
            print(f"Error occurred at {current_time}: {e}\n{tb}", file=sys.stderr)


    def switch_main_display_to_camera(self):
        try:
            self.set_button_style('camera')
            self.ui_main.stackedWidget.setCurrentIndex(1)
            self.camera_page_display_camera_and_detect_area_list(camera_name=self.ui_main.camera_page_name_box.currentText())

            self.ui_main.camera_refresh_bnt.hide()

            self.ui_main.camera_page_camera_event_box.clear()
            # admin_info = load_info(host=self.HOST,port=self.PORT,file_name="admin_info")

            ret, self.camera_info_dict_temp = self.load_camera_info()
            self.admin_info_temp = load_info(host=self.HOST,port=self.PORT,file_name="admin_info")
            self.setting_info_temp = load_info(host=self.HOST, port=self.PORT, file_name="setting_info")
            self.login_info_temp = load_info(host=self.HOST, port=self.PORT, file_name="login_info")

            # if self.camera_worker_dict != None :
            #     for worker in self.camera_worker_dict.values():
            #         worker.stop()
            #         del worker

            for detect_type in self.admin_info_temp["LICENSE"]:
                if self.admin_info_temp["LICENSE"][detect_type] == 1:
                    self.ui_main.camera_page_camera_event_box.addItems([Eng2kor(detect_type)])

        except Exception as e:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            tb = traceback.format_exc()
            print(f"Error occurred at {current_time}: {e}\n{tb}", file=sys.stderr)


    def switch_main_display_to_setting(self):
        try:
            self.set_button_style('setting')
            self.ui_main.stackedWidget.setCurrentIndex(2)
            self.ui_main.setting_stack_widget.setCurrentIndex(0)


            self.ui_main.setting_user_id_input.clear()
            self.ui_main.setting_user_pw_input.clear()
            self.ui_main.setting_user_new_pw_input.clear()
            self.ui_main.setting_user_new_pw_input2.clear()

            # if self.camera_page_worker != None :
            #     self.camera_page_worker.stop()
            #     del self.camera_page_worker
            #     self.camera_page_worker = None

            save_info(host=self.HOST, port=self.PORT, file_name="camera_info", info=self.camera_info_dict_temp)
            self.setting_info_temp = load_info(host=self.HOST, port=self.PORT, file_name="setting_info")

            self.update_setting()

        except Exception as e:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            tb = traceback.format_exc()
            print(f"Error occurred at {current_time}: {e}\n{tb}", file=sys.stderr)



    # def switch_main_display_to_server(self):
    #     self.set_button_style('server')
    #     self.ui_main.stackedWidget.setCurrentIndex(3)
        self.ui_main.camera_refresh_bnt.hide()

        if self.camera_page_worker != None :
            self.camera_page_worker.stop()
            del self.camera_page_worker
            self.camera_page_worker = None

        # for worker in self.camera_worker_list:
        #     worker.stop()
        #     del worker

    def switch_main_display_to_admin(self):
        try:
            self.set_button_style('admin')
            self.ui_main.stackedWidget.setCurrentIndex(3)
            self.ui_main.camera_refresh_bnt.hide()

            self.ui_main.admin_pw_input.clear()

            if self.camera_page_worker != None :
                self.camera_page_worker.stop()
                del self.camera_page_worker
                self.camera_page_worker = None

            save_info(host=self.HOST, port=self.PORT, file_name="camera_info", info=self.camera_info_dict_temp)

        except Exception as e:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            tb = traceback.format_exc()
            print(f"Error occurred at {current_time}: {e}\n{tb}", file=sys.stderr)

        # for worker in self.camera_worker_list:
        #     worker.stop()
        #     del worker

    def switch_main_display_to_admin_2(self):
        self.set_button_style('admin')
        self.ui_main.stackedWidget.setCurrentIndex(4)

    def switch_setting_display_to_user_setting(self):
        try:
            self.setting_info_temp = load_info(host=self.HOST, port=self.PORT, file_name="setting_info")

            self.ui_main.setting_stack_widget.setCurrentIndex(1)
            self.ui_main.setting_user_id_input.clear()
            self.ui_main.setting_user_pw_input.clear()
            self.ui_main.setting_user_new_pw_input.clear()
            self.ui_main.setting_user_new_pw_input2.clear()

        except Exception as e:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            tb = traceback.format_exc()
            print(f"Error occurred at {current_time}: {e}\n{tb}", file=sys.stderr)

    def change_ai_info(self):
        weight_name = self.ui_main.setting_setting_ai_weight_box.currentText()
        print("change ",weight_name)

        self.setting_info_temp["AI"]["Weight"] = weight_name

        save_info(host=self.HOST, port=self.PORT, file_name="setting_info", info=self.setting_info_temp)

    def change_zeroshot_info(self):
        self.setting_info_temp["AI"]["ZeroShot"] = 1 if self.setting_info_temp["AI"]["ZeroShot"] == 0 else 0
    def change_auto_label_info(self):
        self.setting_info_temp["AI"]["AutoLabel"] = 1 if self.setting_info_temp["AI"]["AutoLabel"] == 0 else 0


    def switch_setting_display_to_ai_stting(self):
        try:
            self.ui_main.setting_setting_ai_weight_box.clear()
            # weight_path = os.path.join(os.getcwd(), "back", "weight", "yolo")
            # weight_list = sorted(os.listdir(weight_path))

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


            self.ui_main.setting_ai_setting_save_bnt.clicked.connect(self.change_ai_info)


        except Exception as e:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            tb = traceback.format_exc()
            print(f"Error occurred at {current_time}: {e}\n{tb}", file=sys.stderr)


    def switch_setting_display_to_notice_stting(self):
        try:
            self.ui_main.setting_stack_widget.setCurrentIndex(0)

        except Exception as e:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            tb = traceback.format_exc()
            print(f"Error occurred at {current_time}: {e}\n{tb}", file=sys.stderr)

    # def setting_switch_schedule_setting(self):
    #     self.ui_main.setting_stack_widget.setCurrentIndex(2)

    def switch_admin_license_page(self):
        try:
            self.ui_main.stackedWidget_2.setCurrentIndex(0)
            self.reset_admin_license_list()

        except Exception as e:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            tb = traceback.format_exc()
            print(f"Error occurred at {current_time}: {e}\n{tb}", file=sys.stderr)

    def switch_admin_fn_permission_page(self):
        try:
            self.ui_main.stackedWidget_2.setCurrentIndex(1)

        except Exception as e:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            tb = traceback.format_exc()
            print(f"Error occurred at {current_time}: {e}\n{tb}", file=sys.stderr)

    def camera_page_display_selected_row(self):
        try:
            # ret, camera_info_dict, camera_info_ori = self.load_camera_info()
            ret, self.camera_info_dict_temp = self.load_camera_info()


            selected_indexes = self.ui_main.camera_list_table.selectedIndexes()
            if selected_indexes:
                selected_row = selected_indexes[0].row()  # 선택된 셀의 행 인덱스
                camera_name = self.ui_main.camera_list_table.item(selected_row, 2).text()
                
                # data = self.camera_info_dict[camera_name]
                data = self.camera_info_dict_temp[camera_name]

                self.ui_main.camera_info_name_input.setText(data["Name"])
                self.ui_main.camera_info_ip_input.setText(data["IP"])
                self.ui_main.camera_info_id_input.setText(data["ID"])
                self.ui_main.camera_info_pw_input.setText(data["PW"])

        except Exception as e:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            tb = traceback.format_exc()
            print(f"Error occurred at {current_time}: {e}\n{tb}", file=sys.stderr)

    def add_camera_info(self):
        try:
            if len(self.ui_main.camera_info_name_input.text()) and len(self.ui_main.camera_info_ip_input.text()) and len(self.ui_main.camera_info_id_input.text()) and len(self.ui_main.camera_info_pw_input.text()):
                camera_name = self.ui_main.camera_info_name_input.text()
                self.camera_info_dict_temp[camera_name] =  {"Name" : str(self.ui_main.camera_info_name_input.text()), 
                                                            "IP" : str(self.ui_main.camera_info_ip_input.text()),
                                                            "ID" : str(self.ui_main.camera_info_id_input.text()),
                                                            "PW" : str(self.ui_main.camera_info_pw_input.text()),
                                                            "detect_info" : [],
                                                            "AI" : False,
                                                            }

                row_position = self.ui_main.camera_list_table.rowCount()
                self.ui_main.camera_list_table.insertRow(row_position)

                # 새 행에 데이터 채우기
                text = QTableWidgetItem(str(self.camera_info_dict_temp[camera_name]["Name"]))
                text.setTextAlignment(Qt.AlignCenter)
                text.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled)
                self.ui_main.camera_list_table.setItem(row_position, 1, text)

                # text = QTableWidgetItem(str(self.camera_info_dict_temp[camera_name]["Group"]))
                # text.setTextAlignment(Qt.AlignCenter)
                # text.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled)
                # self.ui_main.camera_list_table.setItem(row_position, 1, text)
                
                text = QTableWidgetItem(str(self.camera_info_dict_temp[camera_name]["IP"]))
                text.setTextAlignment(Qt.AlignCenter)
                text.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled)
                self.ui_main.camera_list_table.setItem(row_position, 2, text)

        except Exception as e:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            tb = traceback.format_exc()
            print(f"Error occurred at {current_time}: {e}\n{tb}", file=sys.stderr)

    def load_camera_info(self, reset = False, connect_nvr = True):
        login_info = load_info(host=self.HOST, port=self.PORT, file_name="login_info")

        data = {"ip" : login_info["NVR"]["IP"], "id" : login_info["NVR"]["ID"], "pw" : login_info["NVR"]["PW"], "reset" : reset}
        url = f'http://{self.HOST}:{self.PORT}/load_camera_info'
        receive_data = requests.post(url, json=data).json()
        camera_info_dict = {}

        if connect_nvr and receive_data["success"] == True:
            # self.create_fade_out_msg(msg="init camera")
            camera_info_dict = receive_data["data"]

            return receive_data["success"], camera_info_dict
        
        return receive_data["success"], camera_info_dict

    def live_camera_viewer_setup(self, reset = False, connect_nvr = True):
        try:
            self.camera_view_list = {}
            ret, self.camera_info_dict_temp = self.load_camera_info(reset, connect_nvr)

            if connect_nvr and ret == True:
                # disconnect_camera_id = []

                # for camera in camera_info_ori["cameras"]:
                #     if camera["connected"] == False:
                #         disconnect_camera_id.append(camera["id"])

                for camera_name, camera_info in self.camera_info_dict_temp.items():
                    # if len(str(camera_info["IP"])) == 0 or camera_info["Num"] in disconnect_camera_id:
                        # num = camera_info["Num"]
                        # self.camera_view_list[camera_name] = Livepage_view(getattr(self.ui_main, 
                        #                                                            f"camera_view_{num}"), 
                        #                                                            camera_name = camera_name, 
                        #                                                            camera_num = str(camera_info["Num"]), 
                        #                                                             stackedWidget = self.ui_main.stackedWidget)
                        # row = num // 4
                        # col = num % 4
                        
                        # self.ui_main.gridLayout_2.addWidget(self.camera_view_list[camera_name], row, col, 1, 1)
                        # continue

                    row_position = self.ui_main.camera_list_table.rowCount()
                    self.ui_main.camera_list_table.insertRow(row_position)

                    # 새 행에 데이터 채우기
                    label = QLabel()
                    # pixmap = QPixmap("./images/ico_video_off.svg").scaled(24, 24, Qt.KeepAspectRatio)
                    pixmap = QPixmap(u":/newPrefix/ui/images/ico_video_off.svg").scaled(24, 24, Qt.KeepAspectRatio)

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
                    # text.setFont(self.font)  
                    
                    self.ui_main.camera_list_table.setItem(row_position, 3, text)

                    # self.ui_main.camera_page_name_box.addItems([str(camera_num)])
                    self.ui_main.camera_page_name_box.addItems([str(camera_info["Name"])])

                    # if reset == False:
                    num = camera_info["Num"]

                    #Live 카메라 뷰어 setup
                    if camera_name not in self.camera_view_list.keys():
                        self.camera_view_list[camera_name] = Livepage_view(getattr(self.ui_main, 
                                                                                    f"camera_view_{num}"), 
                                                                                    camera_name = camera_name, 
                                                                                    camera_num = str(camera_info["Num"]), 
                                                                                    stackedWidget = self.ui_main.stackedWidget)
                        
                        self.camera_view_list[camera_name].doubleClicked.connect(self.check_camera_viewer_click)
                        # camera_viewer.setPixmap(QPixmap(u"images/ico_video_off.svg"))
                        self.camera_view_list[camera_name].setPixmap(QPixmap(u":/newPrefix/ui/images/ico_video_off.svg"))
                        self.camera_view_list[camera_name].setAlignment(Qt.AlignCenter)

                    getattr(self.ui_main, f"camera_view_{num}").hide()
                    # getattr(self.ui_main, f"camera_view_{num}").deleteLater()
                    num -= 1
                    row = num // 4
                    col = num % 4

                    self.ui_main.gridLayout_2.addWidget(self.camera_view_list[camera_name], row, col, 1, 1)
            else:
                self.camera_info_dict_temp = {}
                self.create_fade_out_msg(msg="Disconnect NVR")

        except Exception as e:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            tb = traceback.format_exc()
            print(f"Error occurred at {current_time}: {e}\n{tb}", file=sys.stderr)
            self.create_fade_out_msg(msg=f"Error occurred at {current_time}: {e} {sys.stderr}")


    def del_camera_info(self):
        try:
            selected_indexes = self.ui_main.camera_list_table.selectedIndexes()
            if selected_indexes:
                selected_row = selected_indexes[0].row()  # 선택된 셀의 행 인덱스
                camera_num = self.ui_main.camera_list_table.item(selected_row, 1).text()
                self.ui_main.camera_list_table.removeRow(selected_row)

                # del self.camera_info_dict[camera_num]
                del self.camera_info_dict_temp[camera_num]

        except Exception as e:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            tb = traceback.format_exc()
            print(f"Error occurred at {current_time}: {e}\n{tb}", file=sys.stderr)

    def eventFilter(self, obj, event):
        self.input_field_styles = {
            self.ui_main.camera_info_name_input: self.ui_main.camera_info_name_line,
            self.ui_main.camera_info_ip_input: self.ui_main.camera_info_ip_line,
            self.ui_main.camera_info_id_input: self.ui_main.camera_info_id_line,
            self.ui_main.camera_info_pw_input: self.ui_main.camera_info_pw_line,
            self.ui_main.setting_user_id_input: self.ui_main.setting_user_id_input_line,
            self.ui_main.setting_user_pw_input: self.ui_main.setting_user_pw_input_line,
            self.ui_main.setting_user_new_pw_input: self.ui_main.setting_user_new_pw_input_line,
            self.ui_main.setting_user_new_pw_input2: self.ui_main.setting_user_new_pw_input2_line,
            self.ui_main.setting_email_id_input: self.ui_main.setting_email_id_input_line,
            self.ui_main.setting_email_pw_input: self.ui_main.setting_email_pw_input_line,
            self.ui_main.setting_receive_email_id_input:self.ui_main.setting_receive_email_id_input_line,
            self.ui_main.admin_pw_input: self.ui_main.admin_pw_input_line
        }

        if obj in self.input_field_styles:
            line_edit = self.input_field_styles[obj]
            if event.type() == QEvent.FocusIn:
                line_edit.setStyleSheet("background-color: green")
            elif event.type() == QEvent.FocusOut:
                line_edit.setStyleSheet("background-color: rgb(36, 39, 44)")

        if isinstance(event, QWheelEvent):
            try:
                if obj == self.search_ui.time_day_start_input or obj == self.search_ui.time_day_end_input:
                    return True  # 휠 이벤트 무시
            except: pass

        return super().eventFilter(obj, event)

    def login_NVR(self):
        login_info = load_info(host=self.HOST, port=self.PORT, file_name="login_info")

        login_info["NVR"]["IP"] = self.ui_main.server_ip_input.text()
        login_info["NVR"]["ID"] = self.ui_main.server_id_input.text()
        login_info["NVR"]["PW"] = self.ui_main.server_pw_input.text()

        self.ui_main.camera_list_table.setRowCount(0)
        self.ui_main.camera_page_name_box.clear()

        for worker in self.camera_worker_dict.values():
            worker.stop()
            del worker
        
        save_info(host=self.HOST, port=self.PORT, file_name="login_info", info=login_info)
        self.init_GUI_setup(reset=True)
    
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
    
    def create_fade_out_msg(self, msg="None"):
        try:
            if not hasattr(self, 'fadeout_window') or not self.fadeout_window.isVisible():
                self.fadeout_window = FadeOutWindow(self, msg)
                main_window_rect = self.geometry()
                fadeout_window_rect = self.fadeout_window.geometry()
                self.fadeout_window.move(
                    main_window_rect.left() + (main_window_rect.width() - fadeout_window_rect.width()) // 2,
                    main_window_rect.top() + (main_window_rect.height() - fadeout_window_rect.height()) * 4 // 5
                )

            self.fadeout_window.show()
        except Exception as e:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            tb = traceback.format_exc()
            print(f"Error occurred at {current_time}: {e}\n{tb}", file=sys.stderr)

    def Save_video_and_Notification_alarm_and_Send_mail(self):
        try:
            data = {"msg" : str(" ")}

            url = f'http://{self.HOST}:{self.PORT}/get-status-info'
            receive_data = requests.get(url, json=data).json()

            if len(receive_data["data"]):
                for camera_name, alarm_list in receive_data["data"].items():
                    for alarm in alarm_list:
                        # if self.setting_info_temp["VIDEO_SAVE"]["active"]:
                        #     timer = threading.Timer(5, self.start_delayed_video_save, args=(camera_name, alarm))
                        #     timer.start()

                        #     self.video_storage_manage()

                        if self.setting_info_temp["NOTICE"]["active"]:
                            self.fadeout_in_window = FadeOutInWindow(self, camera_name, alarm, self.alarm_window_num)
                            main_window_rect = self.geometry()
                            fadeout_in_window_rect = self.fadeout_in_window.geometry()
                            self.fadeout_in_window.move(
                                main_window_rect.left() + (main_window_rect.width() - fadeout_in_window_rect.width()) // 2,
                                main_window_rect.top() + (main_window_rect.height() - fadeout_in_window_rect.height()) * 4 // 5
                            )

                            self.fadeout_in_window.show()
                            self.alarm_window_num += 1

                            self.fadeout_in_window_list.append(self.fadeout_in_window)

                            if len(self.fadeout_in_window_list) > self.setting_info_temp["NOTICE"]["cnt"]:
                                self.fadeout_in_window_list[0].close()
                                self.fadeout_in_window_list.pop(0)

                        if self.setting_info_temp["EMAIL"]["active"]:
                            thread = threading.Thread(target=send_email_alarm, args=(self.camera_worker_dict, alarm, self.setting_info_temp["EMAIL"]["se nder"], self.setting_info_temp["EMAIL"]["PW"],  self.setting_info_temp["EMAIL"]["TO"], camera_name))
                            thread.start()

        except Exception as e:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            tb = traceback.format_exc()
            print(f"Error occurred at {current_time}: {e}\n{tb}", file=sys.stderr)

    def Notification_status(self):
        try:
            data = {"msg" : str(" ")}

            url = f'http://{self.HOST}:{self.PORT}/get-status-info'
            receive_data = requests.get(url, json=data).json()

            if self.setting_info_temp["NOTICE"]["active"]:
                if len(receive_data["data"]):
                    for camera_name, alarm_list in receive_data["data"].items():
                        print(alarm_list)
                        for alarm in alarm_list:
                            print(alarm)
                            if self.setting_info_temp["NOTICE"]["active"] and len(alarm):
                                self.fadeout_in_window = FadeOutInWindow(self, camera_name, alarm, self.alarm_window_num)
                                main_window_rect = self.geometry()
                                fadeout_in_window_rect = self.fadeout_in_window.geometry()
                                self.fadeout_in_window.move(
                                    main_window_rect.left() + (main_window_rect.width() - fadeout_in_window_rect.width()) // 2,
                                    main_window_rect.top() + (main_window_rect.height() - fadeout_in_window_rect.height()) * 4 // 5
                                )

                                self.fadeout_in_window.show()
                                self.alarm_window_num += 1

                                self.fadeout_in_window_list.append(self.fadeout_in_window)

                                if len(self.fadeout_in_window_list) > self.setting_info_temp["NOTICE"]["cnt"]:
                                    self.fadeout_in_window_list[0].close()
                                    self.fadeout_in_window_list.pop(0)

            self.ui_main.connected_user_label_2.setText(str(receive_data["user_num"]))

        except Exception as e:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            tb = traceback.format_exc()
            print(f"Error occurred at {current_time}: {e}\n{tb}", file=sys.stderr)


    def check_nvr_login(self):
        login_info = load_info(host=self.HOST, port=self.PORT, file_name="login_info")

        data = {"msg" : {"ip" : login_info["NVR"]["IP"], 
                        "pw" : login_info["NVR"]["PW"],
                        "id" : login_info["NVR"]["ID"]}}
            
        url = f'http://{self.HOST}:{self.PORT}/login_nvr'
        receive_data = requests.post(url, json=data).json()

        if receive_data["success"]:
            return True
        else:
            self.create_fade_out_msg(msg=receive_data["message"])
            return False

    def init_GUI_setup(self, reset=False):
        self.fadeout_in_window_list = []
        self.storage_period = {30 : 0, 60 : 1, 90 : 2, 
                               0 : 30, 1 : 60, 2 : 90}

        self.alarm_window_num = 0
        self.camera_page_worker = None
        self.search_page_worker = None
        self.timer = None
        self.camera_connect_timer = None

        # 어두운 레이어 위젯 생성
        self.dark_layer = QWidget(self)
        self.dark_layer.setGeometry(QRect(0,0,9999,9999))
        self.dark_layer.setStyleSheet("background-color: rgba(0, 0, 0, 178);")  # 70% 투명도
        self.dark_layer.hide()  # 기본적으로 숨김

        self.admin_info_temp = load_info(host=self.HOST,port=self.PORT,file_name="admin_info")
        self.setting_info_temp = load_info(host=self.HOST, port=self.PORT, file_name="setting_info")
        self.login_info_temp = load_info(host=self.HOST, port=self.PORT, file_name="login_info")

        # 상단 NVR 서버 정보 입력
        self.ui_main.server_ip_input.setText(self.login_info_temp["NVR"]["IP"])
        self.ui_main.server_id_input.setText(self.login_info_temp["NVR"]["ID"])
        self.ui_main.server_pw_input.setText(self.login_info_temp["NVR"]["PW"])

        # 지능형 프로그램 구동 상태 아이콘 설정
        self.ui_main.camera_page_ai_active_label.hide()
        self.ui_main.camera_page_ai_active_icon.hide()

        if self.user_info == "user":
            # self.ui_main.tab_backgournd.setGeometry(-20, -20, 501, 71)
            self.ui_main.tab_partion_3.hide()
            self.ui_main.admin_bnt.hide()

        # if reset:
        #     self.live_refresh_live_viewer()

        self.update_setting()

        self.live_camera_viewer_setup()

        ##live 페이지 카메라 연결
        self.connect_live_page_camera(reset = reset)

        self.start_camera_connect_status_timer()
        self.start_camera_refresh_timer()

    def update_setting(self):
        setting_info_temp = load_info(host=self.HOST, port=self.PORT, file_name="setting_info")
        self.ui_main.setting_email_active_bnt.setChecked(setting_info_temp["EMAIL"]["active"])  #알람 정보 이메일 전송 기능 활성화 여부

        self.ui_main.setting_email_id_input.setText(setting_info_temp["EMAIL"]["sender"]) #이메일 전송 송신 ID 
        self.ui_main.setting_email_pw_input.setText(setting_info_temp["EMAIL"]["PW"]) #이메일 전송 송신 Password
        self.ui_main.setting_receive_email_id_input.setText(setting_info_temp["EMAIL"]["TO"]) # 이베일 전송 수신 ID

        self.ui_main.setting_popup_alarm_active_bnt.setChecked(setting_info_temp["NOTICE"]["active"]) # 알람 발생시 프로그램 팝업알림 기능 활성화 여부
        self.ui_main.setting_video_save_alarm_active_bnt.setChecked(setting_info_temp["VIDEO_SAVE"]["active"]) # 알람 발생 영상 저장 기능 활성화 여부

        self.ui_main.setting_detect_bbox_active_bnt.setChecked(setting_info_temp["DETECT"]["Bbox"]) # 지능형 검출 결과 BBOX 출력 여부
        self.ui_main.setting_detect_label_active_bnt.setChecked(setting_info_temp["DETECT"]["Label"]) # 지능형 검출 결과 class 출력 여부

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

    def closeEvent(self, event):
        # 창이 닫힐 때 실행되는 코드
        if self.camera_page_worker != None :
            self.camera_page_worker.stop()
            del self.camera_page_worker

        for worker in self.camera_worker_dict.values():
            worker.stop()
            del worker

        data = {"msg" : ""}
        url = f'http://{self.HOST}:{self.PORT}/logout'
        receive_data = requests.put(url, json=data).json()
        event.accept()  # 또는 event.ignore()로 닫히지 않게 할 수 있음


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



