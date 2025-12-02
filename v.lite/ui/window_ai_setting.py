import sys
import os
from pathlib import Path

from PySide6.QtWidgets import QDialog, QTableWidgetItem, QLabel, QToolButton, QVBoxLayout, QHBoxLayout, QSizePolicy, QWidget, QScrollArea
from datetime import datetime
from PySide6.QtCore import QDate, Qt, Signal, QRect, QSize
from PySide6.QtGui import  QImage, QPixmap, QFont

import requests
import resourece_rc

import numpy as np
import cv2
from requests.auth import HTTPBasicAuth

from ui.ai_setting_ui import Ui_Ai_Setting_Window
from utils import save_info, load_info

class Ai_Setting_Page_Viewer(QLabel):
    Checked = Signal(QLabel)
    def __init__(self, base_viewer, name_label, camera_name, _parent):
        super().__init__(base_viewer)

        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy2)

        self.setScaledContents(True)

        self.checked = False
        self.name_label = name_label

        self.frame_flag = False
        self._parent = _parent
        self.camera_name = camera_name

    def setChecked(self, checked):
        self.checked = checked
        self.updateStyle()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.setChecked(not self.checked)

    def enterEvent(self, event):
        if event.buttons() & Qt.LeftButton:
            self.setChecked(True)
            
    def updateStyle(self):
            if self.checked:
                if self.frame_flag:
                    self.setStyleSheet("""
                        QLabel {
                            border: 2px solid rgb(56, 188, 56);
                        }
                    """)

                    self.set_img(self.frame, 1)
                    self.name_label.setStyleSheet("""
                            QLabel {
                                        color: rgb(56, 188, 56);
                                        border: 1px solid rgb(56, 188, 56);
                                    }
                                """)
                    self._parent.camera_info_dict_temp[self.camera_name]["AI"] = True
            else:
                if self.frame_flag:
                    self.setStyleSheet("""
                        QLabel {
                            border: 1px solid rgb(119, 118, 123);
                        }
                    """)
                    self.set_img(self.frame, 0.5)
                    # self.ai_check_box.setPixmap(self.ai_off_img)
                    self.name_label.setStyleSheet("""
                            QLabel {
                                        color: rgb(255, 255, 255);
                                        border: 1px solid rgb(119, 118, 123);
                                    }
                                """)
                    self._parent.camera_info_dict_temp[self.camera_name]["AI"] = False

    def set_img(self, img, brightness = 1):
        self.frame_flag = True
        self.frame = img.copy()
        cv_image = self.frame.astype('float32')
        cv_image = cv_image * brightness
        cv_image = np.clip(cv_image, 0, 255)
        cv_image = cv_image.astype('uint8')

        height, width, channels = cv_image.shape
        # Calculate the number of bytes per line.
        bytes_per_line = width * channels
        # Convert image from BGR (cv2 default color format) to RGB (Qt default color format).
        cv_rgb_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)
        # print(cv_rgb_image.shape)
        # Convert the image to Qt format.
        qt_rgb_image = QImage(cv_rgb_image.data, width, height, bytes_per_line, QImage.Format_RGB888)

        self.setPixmap(QPixmap.fromImage(qt_rgb_image))


class AiSettingDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : open at setting window")
        self.ai_setting_ui = Ui_Ai_Setting_Window()
        self.ai_setting_ui.setupUi(self)
        self._parent = parent

        # 메인 윈도우의 중앙에 팝업 윈도우 위치 계산
        mainWindowGeometry = self._parent.frameGeometry()
        centerPoint = mainWindowGeometry.center() - self.rect().center()
        self.move(centerPoint.x(), centerPoint.y())

        self.ai_setting_camera_view_list = {}

        for camera_name, camera_info in self._parent.camera_info_dict_temp.items():
            num = str(camera_info["Num"])
            layout = getattr(self.ai_setting_ui, f"search_camera_view_layout_{num}")
            self.ai_setting_camera_view_list[camera_name] = Ai_Setting_Page_Viewer(base_viewer = getattr(self.ai_setting_ui, f"camera_view_{num}"), 
                                                                                name_label = getattr(self.ai_setting_ui, f"camera_view_name_{num}"),
                                                                                camera_name = camera_name, 
                                                                                _parent = self._parent)

            getattr(self.ai_setting_ui, f"camera_view_name_{num}").setText(camera_name)
            getattr(self.ai_setting_ui, f"camera_view_{num}").hide()
            layout.addWidget(self.ai_setting_camera_view_list[camera_name])

            if camera_name in self._parent.camera_info_dict_temp.keys():
                # auth = HTTPBasicAuth(self._parent.login_info_temp["NVR"]["ID"], self._parent.login_info_temp["NVR"]["PW"]) # NVR에 대한 ID / PW
                # url = f'http://{self._parent.login_info_temp["NVR"]["IP"]}/live/video{num}.jpg'
                # response = requests.get(url,auth=auth, timeout= 1)
                # image_bytes = np.frombuffer(response.content, dtype=np.uint8)
                # frame = cv2.imdecode(image_bytes, cv2.IMREAD_COLOR)

                frame = self._parent.camera_img_dict[camera_name]
                frame = cv2.resize(frame, (250, 140))
                
                self.ai_setting_camera_view_list[camera_name].set_img(frame, 0.5)

        self.ai_setting_ui.camera_save_bnt.clicked.connect(self.send_camera_info_and_close)
        self.ai_setting_ui.close_bnt.clicked.connect(self.cancel_ai_setting)
        self.ai_setting_ui.all_select_bnt.clicked.connect(self.select_camera)

        self.check_camera_viewer()

    def cancel_ai_setting(self):
        self._parent.camera_info_dict_temp = load_info(host=self._parent.HOST, port=self._parent.PORT, file_name="camera_info")
        self.close()

    def select_camera(self):
        all_check_flag = False
        for camera_name, camera_info in self.camera_info_dict_temp.items():
            if self.ai_setting_camera_view_list[camera_name].checked == False:
                self.ai_setting_camera_view_list[camera_name].setChecked(True)
                all_check_flag = True

        if all_check_flag == False:
            for camera_name, camera_info in self.camera_info_dict_temp.items():
                self.ai_setting_camera_view_list[camera_name].setChecked(False)

    def check_camera_viewer(self):
        for camera_name, camera_info in self._parent.camera_info_dict_temp.items():
            if len(camera_info["IP"]):
                if camera_info["AI"] == False:
                    self.ai_setting_camera_view_list[camera_name].setChecked(False)

                elif camera_info["AI"] == True:
                    self.ai_setting_camera_view_list[camera_name].setChecked(True)

    def send_camera_info_and_close(self):
        self.run_ms_ai()
        self.close()

    def run_ms_ai(self):
        save_info(host=self._parent.HOST, port=self._parent.PORT, file_name="camera_info", info=self._parent.camera_info_dict_temp)

        data = {"msg" : "ms_ai"}
        url = f'http://{self._parent.HOST}:{self._parent.PORT}/run_ms_ai'
        receive_data = requests.post(url, json=data).json()

        if self._parent.camera_info_dict_temp[self._parent.connect_camera_name]["AI"] == True:
            self._parent.ui_main.camera_page_viewer.reset()
            self._parent.ui_main.camera_page_ai_active_label.show()
            self._parent.ui_main.camera_page_ai_active_icon.show()
            if self._parent.camera_page_worker is not None:
                self._parent.camera_page_worker.ai_active = True

        else:
            self._parent.ui_main.camera_page_viewer.reset()
            self._parent.ui_main.camera_page_ai_active_label.hide()
            self._parent.ui_main.camera_page_ai_active_icon.hide()
            if self._parent.camera_page_worker is not None:
                self._parent.camera_page_worker.ai_active = False

def open_ai_setting_window(click, self):
    self.ai_setting_window = AiSettingDialog(self)
    self.ai_setting_window.show()