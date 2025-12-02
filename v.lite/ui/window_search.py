import sys
import os
from pathlib import Path

from PySide6.QtWidgets import QDialog, QTableWidgetItem, QLabel, QToolButton, QVBoxLayout, QHBoxLayout, QSizePolicy, QWidget, QScrollArea
from datetime import datetime
from PySide6.QtCore import QDate, Qt, Signal, QRect, QSize, QThread
from PySide6.QtGui import  QImage, QPixmap, QFont


import requests
from ui.search_ui import Ui_Search_window
import cv2
import numpy as np 
import base64
from io import BytesIO
import traceback
import time

import resourece_rc

color_map_num = {
    0 : "검정색" ,
    1 : "흰색" ,
    2 : "파랑색" ,
    3 : "갈색" ,
    4 : "초록색" ,
    5 : "회색" ,
    6 : "주황색",
    7 : "핑크색" ,
    8 : "빨강색" ,
    9 : "노랑색"
}

class Connect_Playback(QThread):
    # Signal emitted when a new image or a new frame is ready.
    ImageUpdated = Signal(QImage)

    def __init__(self, url, viewers_widget, play_fps = 30, roi_thickness = 1) -> None:
        super(Connect_Playback, self).__init__()
        # Declare and initialize instance variables.
        self.url = url
        self.__thread_active = True
        self.fps = 0
        self.disconnect_cnt = 0

        self.play_fps = int(play_fps)

        self.roi_thickness = roi_thickness
        self.viewers_widget = viewers_widget

    def run(self) -> None:
        while self.__thread_active:
            bytes_data = b''  # 스트리밍 데이터 저장할 바이트 버퍼

            for chunk in self.url.iter_content(chunk_size=1024):
                if not self.__thread_active:
                        break
                
                t0 = time.time()
                bytes_data += chunk

                # JPEG 이미지의 시작과 끝을 찾습니다.
                a = bytes_data.find(b'\xff\xd8')
                b = bytes_data.find(b'\xff\xd9')

                if a != -1 and b != -1:
                    jpg = bytes_data[a:b+2]
                    bytes_data = bytes_data[b+2:]

                    frame = cv2.resize(cv2.imdecode(np.frombuffer(jpg, dtype=np.uint8), cv2.IMREAD_COLOR), dsize=(self.viewers_widget.width(), self.viewers_widget.height()))
                    # frame = cv2.resize(self.jpeg.decode(np.frombuffer(jpg, dtype=np.uint8), cv2.IMREAD_COLOR), dsize=self.output_size)

                    height, width, channels = frame.shape
                    # Calculate the number of bytes per line.
                    bytes_per_line = width * channels
                    self.ImageUpdated.emit(QImage(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB).data, width, height, bytes_per_line, QImage.Format_RGB888))
                    # frame_num += 1
                    
                    sleep_time = max(0, (1 / self.play_fps) - (time.time() - t0))
                    time.sleep(sleep_time)
                        
            else:
                self.stop()

    def stop(self) -> None:
        self.__thread_active = False
        self.wait()

class ClickableSearchWidget(QWidget):
    def __init__(self, img_pixmap, label_info=None, video_info=None, parent=None, instance=None):
        super().__init__(parent)
        
        self._default_style = (
            "QWidget { "
            "border: 1px solid rgb(119, 118, 123); "
            "}"
        )
        self._selected_style = (
            "QWidget { "
            "border: 1px solid rgb(0, 255, 0); "
            "}"
        )

        if label_info is not None :
            if label_info["Hat"] == 0:
                hat_text = "착용"
            elif label_info["Hat"] == 1:
                hat_text = "미착용"
            else : hat_text = "확인불가"


            if label_info["Top"] == 0:
                top_text = "긴팔"
            elif label_info["Top"] == 1:
                top_text = "반팔"
            else : top_text = "확인불가"

            for i in label_info["TopColor"]:
                top_text += " " + color_map_num[i]

            if label_info["Bot"] == 0:
                bot_text = "긴바지"
            elif label_info["Bot"] == 1:
                bot_text = "반바지"
            else : bot_text = "확인불가"

            for i in label_info["BotColor"]:
                bot_text += " " + color_map_num[i]
            
            text = f"카메라 이름 : {video_info[0]}\n"\
                    + f"날짜 : {video_info[1]}\n"\
                    + f"시간 : {video_info[2]}\n"\
                    + f"모자 : {hat_text}\n"\
                    + f"상의 : {top_text}\n"\
                    + f"하의 : {bot_text}\n"\

        else:
            text = "검색 결과 없음"

                
        self.video_info = video_info
        self.instance = instance

        # Track selection state
        self._is_selected = False
        
        # Setup widget
        self.setMaximumSize(QSize(1068, 261))
        self.setStyleSheet(self._default_style)
        
        # Create layouts
        main_layout = QVBoxLayout(self)
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(-1, -1, -1, 0)

        horizontal_layout = QHBoxLayout()
        
        # Image label
        self.image_label = QLabel(self)
        self.image_label.setMinimumSize(QSize(1, 208))
        self.image_label.setMaximumSize(QSize(317, 16777215))
        self.image_label.setPixmap(img_pixmap)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.image_label.setScaledContents(False)
        
        # Text label
        self.text_label = QLabel(self)
        font = QFont()
        font.setFamilies(["Sans"])
        size_policy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        
        self.text_label.setSizePolicy(size_policy)
        self.text_label.setMinimumSize(QSize(82, 86))
        self.text_label.setMaximumSize(QSize(999, 16777215))
        # self.text_label.setStyleSheet("color: rgb(255, 255, 255); border-color: rgba(0, 0, 0, 0);")
        self.text_label.setStyleSheet("color: rgb(255, 255, 255);")

        if label_info is None :
            self.text_label.setAlignment(Qt.AlignCenter)  
        
        self.text_label.setText(text)
        
        if label_info is None :
            self.text_label.setAlignment(Qt.AlignCenter)  # 텍스트 가운데 정렬

        # Add widgets to layout
        horizontal_layout.addWidget(self.image_label)
        horizontal_layout.addWidget(self.text_label)
        main_layout.addLayout(horizontal_layout)
    
    def mousePressEvent(self, event):
        """Handle mouse press to toggle selection"""
        if self.video_info is not None:
            for par_label in self.instance.par_label_list:
                par_label._is_selected = False
                par_label._update_style()

            self._is_selected = not self._is_selected
            self._update_style()
            super().mousePressEvent(event)
    
    def mouseDoubleClickEvent(self, event):
        """Handle double-click event"""
        try:
            print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : play par video")

            if self.video_info is not None:
                if self.instance.search_page_worker is not None:
                    self.instance.search_page_worker.stop()  # 기존 쓰레드를 종료
                    self.instance.search_page_worker.wait()  # 종료를 기다림
                    self.instance.search_page_worker = None  # 참조를 해제

                camera_name = self.video_info[0]
                video_date = self.video_info[1]
                video_time = self.video_info[2]

                
                video_file_name = f"{camera_name}/{video_date}/{video_time}/output_video.mp4"

                data = {"msg" : video_file_name}
                url = f'http://{self.instance._parent.HOST}:{self.instance._parent.PORT}/get-par-video'

                response = requests.get(url, json=data, stream=True)

                if response.status_code == 200:
                    play_fps = 30 * float(self.instance.search_ui.par_time_video_time_speed_input.text())

                    viewer = self.instance.search_ui.search_viewer
                    self.instance.search_page_worker = Connect_Playback(response, viewers_widget = viewer, play_fps = play_fps, roi_thickness=2)

                    self.instance.search_page_worker.ImageUpdated.connect(lambda image, viewer=viewer: self.instance._parent.ShowCamera(viewer, image))
                    self.instance.search_page_worker.start()
        
                    self.instance.search_ui.stackedWidget.setCurrentIndex(1)


                else:
                    print("Failed to retrieve video stream.")
        except Exception as e:
                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                tb = traceback.format_exc()
                print(f"Error occurred at {current_time}: {e}\n{tb}", file=sys.stderr)

        super().mouseDoubleClickEvent(event)

    def _update_style(self):
        """Update widget border based on selection state"""
        self.setStyleSheet(self._selected_style if self._is_selected else self._default_style)

class SearchPageViewer(QLabel):
    Checked = Signal(QLabel)
    def __init__(self, base_viewer, camera_num, camera_name, name_label, main_instance, search_instance):
        super().__init__(base_viewer)

        parent_layout = base_viewer.layout()

        # self.setGeometry(QRect(1, 1, 187, 125))
        # print(base_viewer.width(), base_viewer.height())

        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy2)

        # self.setGeometry(QRect(1, 1, self.width(), self.height()))
        self.setScaledContents(True)

        self.checked = False
        self.camera_num = camera_num
        self.camera_name = camera_name
        self.name_label = name_label

        self.main_instance = main_instance
        self.search_instance = search_instance

        self.frame_flag = False

    def setChecked(self, checked):
        # for camera_name, camera_viewer in self.search_instance.search_page_camera_view_list.items():
            # if camera_viewer.checked:
            #     camera_viewer.checked = False
            #     camera_viewer.updateStyle()
                
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

class SearchDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : open search window")
        self.search_page_worker = None
        # self.search_window = QDialog()  # QDialog 인스턴스 생성
        self.search_ui = Ui_Search_window()
        self.search_ui.setupUi(self)
        self._parent = parent

        # 메인 윈도우의 중앙에 팝업 윈도우 위치 계산
        mainWindowGeometry = self._parent.frameGeometry()
        centerPoint = mainWindowGeometry.center() - self.rect().center()
        self.move(centerPoint.x(), centerPoint.y())

        self.switch_event_search_page()
        self.search_ui.stackedWidget.setCurrentIndex(0)

        self.search_ui.time_day_start_input.setDate(QDate.currentDate())
        self.search_ui.time_day_end_input.setDate(QDate.currentDate())
        self.search_ui.time_hour_end_box.setCurrentText("23:59")

        self.search_ui.par_time_day_start_input.setDate(QDate.currentDate())
        self.search_ui.par_time_day_end_input.setDate(QDate.currentDate())
        self.search_ui.par_time_hour_end_box.setCurrentText("23:59")

        self.search_page_camera_view_list = {}
        self.par_page_flag = False

        for camera_name, camera_info in self._parent.camera_info_dict_temp.items():
            num = str(camera_info["Num"])
            layout = getattr(self.search_ui, f"search_camera_view_layout_{num}")
            self.search_page_camera_view_list[camera_name] = SearchPageViewer(getattr(self.search_ui, f"camera_view_{num}"), 
                                                                                camera_name = camera_name, 
                                                                                camera_num = str(num), 
                                                                                name_label = getattr(self.search_ui, f"camera_view_name_{num}"),
                                                                                main_instance = self._parent,
                                                                                search_instance = self,
                                                                                )
            
            getattr(self.search_ui, f"camera_view_name_{num}").setText(camera_name)
            getattr(self.search_ui, f"camera_view_{num}").hide()
            layout.addWidget(self.search_page_camera_view_list[camera_name])

            if camera_name in self._parent.camera_info_dict_temp.keys():
                frame = self._parent.camera_img_dict[camera_name]
                # frame = cv2.resize(frame, (camera_viewer.width(), camera_viewer.height()))
                frame = cv2.resize(frame, (self.search_page_camera_view_list[camera_name].width(), self.search_page_camera_view_list[camera_name].height()))
                self.search_page_camera_view_list[camera_name].set_img(frame, 0.5)

            else:
                self.search_page_camera_view_list[camera_name].setPixmap(QPixmap(u":/ui/ui/images/ico_video_off.svg"))
                self.search_page_camera_view_list[camera_name].setAlignment(Qt.AlignCenter)


        self.search_ui.event_table.setColumnWidth(0, 40)
        self.search_ui.event_table.setColumnWidth(1, 120)
        self.search_ui.event_table.setColumnWidth(2, 40)

        # self.search_ui.event_search_bnt.clicked.connect(lambda click, instance = self : get_alarm_info(click, instance))
        self.search_ui.search_bnt.clicked.connect(self.get_alarm_info)

        # self.search_ui.event_table.itemDoubleClicked.connect(lambda click, instance = self : search_viewer_playback(click, instance))
        self.search_ui.event_table.itemDoubleClicked.connect(self.search_viewer_playback)

        self.search_ui.time_day_start_input.installEventFilter(self._parent)
        self.search_ui.time_day_end_input.installEventFilter(self._parent)

        # self.search_ui.close_bnt.clicked.connect(lambda click, instance = self : search_close_window(click, instance))
        self.search_ui.close_bnt.clicked.connect(self.search_close_window)
        self.search_ui.camera_select_all_bnt.clicked.connect(self.select_all_camera)

        self.search_ui.event_search_bnt.clicked.connect(self.switch_event_search_page)
        self.search_ui.par_search_bnt.clicked.connect(self.switch_par_page)

        self.search_ui.hat_all_select_bnt.clicked.connect(self.select_all_hat)
        self.search_ui.top_type_all_select_bnt.clicked.connect(self.select_all_top)
        self.search_ui.top_color_all_select_bnt.clicked.connect(self.select_all_top_color)
        self.search_ui.bot_type_all_select_bnt.clicked.connect(self.select_all_bot)
        self.search_ui.bot_color_all_select_bnt.clicked.connect(self.select_all_bot_color)

        self.search_ui.par_get_search_bnt.clicked.connect(self.get_par_search_info)

        self.search_ui.page_undo_bnt.clicked.connect(self.switch_camera_select_page)

        self.search_ui.camera_select_undo_bnt.clicked.connect(lambda checked: self.search_ui.stackedWidget.setCurrentIndex(0))

    def get_par_search_info(self):
        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : get par search info")

        day_start = self.search_ui.par_time_day_start_input.text()
        date_time = datetime.strptime(day_start, "%Y. %m. %d")
        before_day = date_time.strftime("%y.%m.%d")

        day_end = self.search_ui.par_time_day_end_input.text()
        date_time = datetime.strptime(day_end, "%Y. %m. %d")
        after_day = date_time.strftime("%y.%m.%d")

        time_start = self.search_ui.par_time_hour_start_box.currentText()
        time_end = self.search_ui.par_time_hour_end_box.currentText()

        time_start += ":00"
        time_end += ":00"

        time_start = datetime.strptime(time_start, "%H:%M:%S")
        time_start = time_start.strftime("%H.%M.%S")

        time_end = datetime.strptime(time_end, "%H:%M:%S")
        time_end = time_end.strftime("%H.%M.%S")

        order = True if self.search_ui.par_sort_box.currentText() == "최신순" else False

        camera_name_list = []
        for camera_name, camera_viewer in self.search_page_camera_view_list.items():
            if camera_viewer.checked == True:
                camera_name_list.append(camera_name)




        hat = [self.search_ui.hat_on_bnt.isChecked(), self.search_ui.hat_off_bnt.isChecked()]
        top_type = [self.search_ui.top_long_bnt.isChecked(), self.search_ui.top_short_bnt.isChecked()]
        top_color = [self.search_ui.top_black_bnt.isChecked(), self.search_ui.top_white_bnt.isChecked(), self.search_ui.top_blue_bnt.isChecked(), 
                    self.search_ui.top_brown_bnt.isChecked(), self.search_ui.top_green_bnt.isChecked(), self.search_ui.top_grey_bnt.isChecked(),
                    self.search_ui.top_orange_bnt.isChecked(), self.search_ui.top_pink_bnt.isChecked(), self.search_ui.top_red_bnt.isChecked(), 
                    self.search_ui.top_yellow_bnt.isChecked()]


        bot_type = [self.search_ui.bot_long_bnt.isChecked(), self.search_ui.bot_short_bnt.isChecked()]
        bot_color = [self.search_ui.bot_black_bnt.isChecked(), self.search_ui.bot_white_bnt.isChecked(), self.search_ui.bot_blue_bnt.isChecked(), 
                    self.search_ui.bot_brown_bnt.isChecked(), self.search_ui.bot_green_bnt.isChecked(), self.search_ui.bot_grey_bnt.isChecked(),
                    self.search_ui.bot_orange_bnt.isChecked(), self.search_ui.bot_pink_bnt.isChecked(), self.search_ui.bot_red_bnt.isChecked(), 
                    self.search_ui.bot_yellow_bnt.isChecked()]

        data = {"msg":{
            "before_day" : before_day,
            "after_day" : after_day,

            "time_start" : time_start,
            "time_end" : time_end,

            "camera_name" : camera_name_list,

            "hat" : hat, #[착용, 미착용]
            "top_type" : top_type, #[긴팔, 반팔]
            "top_color" : top_color, #[빨,주,노,초,파,갈,핑,흰,회,검]
            "bot_type" : bot_type, #[긴바지, 반바지]
            "bot_color" : bot_color, #[빨,주,노,초,파,갈,핑,흰,회,검]

        }}

        url = f'http://{self._parent.HOST}:{self._parent.PORT}/get-par-search-info'
        receive_data = requests.get(url, json=data).json()

        alarm_list = receive_data["data"]

        self.search_ui.stackedWidget.setCurrentIndex(2)

        while self.search_ui.verticalLayout_44.count():
            item = self.search_ui.verticalLayout_44.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

        self.par_label_list = []

        if len(alarm_list):
            font = QFont()
            font.setFamilies([u"Sans"])
            sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)

            sorted_alarm_list = sorted(alarm_list, key=get_datetime_from_list, reverse=order)

            for index, data in enumerate(sorted_alarm_list):
                img_base64, camera_name, date, video_time, label_info = data
                
                img_data = base64.b64decode(img_base64)
                np_array = np.frombuffer(img_data, np.uint8)
                img = cv2.imdecode(np_array, cv2.IMREAD_COLOR)

                img = cv2.resize(img, dsize=(317, 208))
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                height, width, channel = img.shape
                bytes_per_line = 3 * width
                q_img = QImage(img.data, width, height, bytes_per_line, QImage.Format_RGB888)
                pixmap = QPixmap.fromImage(q_img)

                search_widget = ClickableSearchWidget(pixmap, 
                                                      label_info, 
                                                      video_info = [camera_name, date, video_time],
                                                      parent = self.search_ui.scrollAreaWidgetContents, 
                                                      instance = self,)
                
                self.search_ui.verticalLayout_44.addWidget(search_widget)
                
                self.par_label_list.append(search_widget)

        else:

            pixmap = QPixmap(u":/ui/ui/images/logo_viewer.png")
            # for i in range(3):
            search_widget = ClickableSearchWidget(pixmap, 
                                                    parent = self.search_ui.scrollAreaWidgetContents, 
                                                    instance = self,)
            self.search_ui.verticalLayout_44.addWidget(search_widget)
            self.search_ui.verticalLayout_44.addStretch()

        self.search_ui.par_total_result_count_label.setText(f"총 검색 결과  {len(self.par_label_list)} 건")

        print("search done")

    def select_all_hat(self):
        all_check_flag = False

        if self.search_ui.hat_on_bnt.isChecked() == False:
            self.search_ui.hat_on_bnt.setChecked(True)
            all_check_flag = True

        if self.search_ui.hat_off_bnt.isChecked() == False:
            self.search_ui.hat_off_bnt.setChecked(True)
            all_check_flag = True


        if all_check_flag == False:
            self.search_ui.hat_on_bnt.setChecked(False)
            self.search_ui.hat_off_bnt.setChecked(False)

    def select_all_top(self):
        all_check_flag = False

        if self.search_ui.top_long_bnt.isChecked() == False:
            self.search_ui.top_long_bnt.setChecked(True)
            all_check_flag = True

        if self.search_ui.top_short_bnt.isChecked() == False:
            self.search_ui.top_short_bnt.setChecked(True)
            all_check_flag = True


        if all_check_flag == False:
            self.search_ui.top_long_bnt.setChecked(False)
            self.search_ui.top_short_bnt.setChecked(False)

    def select_all_bot(self):
        all_check_flag = False

        if self.search_ui.bot_long_bnt.isChecked() == False:
            self.search_ui.bot_long_bnt.setChecked(True)
            all_check_flag = True

        if self.search_ui.bot_short_bnt.isChecked() == False:
            self.search_ui.bot_short_bnt.setChecked(True)
            all_check_flag = True


        if all_check_flag == False:
            self.search_ui.bot_long_bnt.setChecked(False)
            self.search_ui.bot_short_bnt.setChecked(False)

    def select_all_top_color(self):
        all_check_flag = False

        if self.search_ui.top_red_bnt.isChecked() == False:
            self.search_ui.top_red_bnt.setChecked(True)
            all_check_flag = True

        if self.search_ui.top_orange_bnt.isChecked() == False:
            self.search_ui.top_orange_bnt.setChecked(True)
            all_check_flag = True

        if self.search_ui.top_yellow_bnt.isChecked() == False:
            self.search_ui.top_yellow_bnt.setChecked(True)
            all_check_flag = True

        if self.search_ui.top_green_bnt.isChecked() == False:
            self.search_ui.top_green_bnt.setChecked(True)
            all_check_flag = True

        if self.search_ui.top_blue_bnt.isChecked() == False:
            self.search_ui.top_blue_bnt.setChecked(True)
            all_check_flag = True

        if self.search_ui.top_brown_bnt.isChecked() == False:
            self.search_ui.top_brown_bnt.setChecked(True)
            all_check_flag = True

        if self.search_ui.top_pink_bnt.isChecked() == False:
            self.search_ui.top_pink_bnt.setChecked(True)
            all_check_flag = True

        if self.search_ui.top_white_bnt.isChecked() == False:
            self.search_ui.top_white_bnt.setChecked(True)
            all_check_flag = True

        if self.search_ui.top_grey_bnt.isChecked() == False:
            self.search_ui.top_grey_bnt.setChecked(True)
            all_check_flag = True

        if self.search_ui.top_black_bnt.isChecked() == False:
            self.search_ui.top_black_bnt.setChecked(True)
            all_check_flag = True

        if all_check_flag == False:
            self.search_ui.top_red_bnt.setChecked(False)
            self.search_ui.top_orange_bnt.setChecked(False)
            self.search_ui.top_yellow_bnt.setChecked(False)
            self.search_ui.top_green_bnt.setChecked(False)
            self.search_ui.top_blue_bnt.setChecked(False)
            self.search_ui.top_brown_bnt.setChecked(False)
            self.search_ui.top_pink_bnt.setChecked(False)
            self.search_ui.top_white_bnt.setChecked(False)
            self.search_ui.top_grey_bnt.setChecked(False)
            self.search_ui.top_black_bnt.setChecked(False)


    def select_all_bot_color(self):
        all_check_flag = False

        if self.search_ui.bot_red_bnt.isChecked() == False:
            self.search_ui.bot_red_bnt.setChecked(True)
            all_check_flag = True

        if self.search_ui.bot_orange_bnt.isChecked() == False:
            self.search_ui.bot_orange_bnt.setChecked(True)
            all_check_flag = True

        if self.search_ui.bot_yellow_bnt.isChecked() == False:
            self.search_ui.bot_yellow_bnt.setChecked(True)
            all_check_flag = True

        if self.search_ui.bot_green_bnt.isChecked() == False:
            self.search_ui.bot_green_bnt.setChecked(True)
            all_check_flag = True

        if self.search_ui.bot_blue_bnt.isChecked() == False:
            self.search_ui.bot_blue_bnt.setChecked(True)
            all_check_flag = True

        if self.search_ui.bot_brown_bnt.isChecked() == False:
            self.search_ui.bot_brown_bnt.setChecked(True)
            all_check_flag = True

        if self.search_ui.bot_pink_bnt.isChecked() == False:
            self.search_ui.bot_pink_bnt.setChecked(True)
            all_check_flag = True

        if self.search_ui.bot_white_bnt.isChecked() == False:
            self.search_ui.bot_white_bnt.setChecked(True)
            all_check_flag = True

        if self.search_ui.bot_grey_bnt.isChecked() == False:
            self.search_ui.bot_grey_bnt.setChecked(True)
            all_check_flag = True

        if self.search_ui.bot_black_bnt.isChecked() == False:
            self.search_ui.bot_black_bnt.setChecked(True)
            all_check_flag = True

        if all_check_flag == False:
            self.search_ui.bot_red_bnt.setChecked(False)
            self.search_ui.bot_orange_bnt.setChecked(False)
            self.search_ui.bot_yellow_bnt.setChecked(False)
            self.search_ui.bot_green_bnt.setChecked(False)
            self.search_ui.bot_blue_bnt.setChecked(False)
            self.search_ui.bot_brown_bnt.setChecked(False)
            self.search_ui.bot_pink_bnt.setChecked(False)
            self.search_ui.bot_white_bnt.setChecked(False)
            self.search_ui.bot_grey_bnt.setChecked(False)
            self.search_ui.bot_black_bnt.setChecked(False)

    def switch_camera_select_page(self):
        print("undo")

        if self.par_page_flag:
            self.search_ui.stackedWidget.setCurrentIndex(2)
        else:
            self.search_ui.stackedWidget.setCurrentIndex(0)

        if self.search_page_worker is not None:
            self.search_page_worker.stop()  # 기존 쓰레드를 종료
            self.search_page_worker.wait()  # 종료를 기다림
            self.search_page_worker = None  # 참조를 해제


    def switch_par_page(self):
        self.search_ui.stackedWidget_2.setCurrentIndex(1)
        self.search_ui.event_search_bnt.setStyleSheet("""
                                                        background-color: rgb(36, 39, 44);
                                                        color: rgb(255, 255, 255);
                                                        border-radius: 10px;
                                                        """)
        
        self.search_ui.par_search_bnt.setStyleSheet("""
                                                    background-color: rgb(30, 195, 55);
                                                    color: rgb(255, 255, 255);
                                                    border-radius: 10px;
                                                    """)
        self.par_page_flag = True

    def switch_event_search_page(self):
        self.search_ui.stackedWidget_2.setCurrentIndex(0)
        self.search_ui.par_search_bnt.setStyleSheet("""
                                                        background-color: rgb(36, 39, 44);
                                                        color: rgb(255, 255, 255);
                                                        border-radius: 10px;
                                                    """)
                    
        self.search_ui.event_search_bnt.setStyleSheet("""
                                                    background-color: rgb(30, 195, 55);
                                                    color: rgb(255, 255, 255);
                                                    border-radius: 10px;
                                                    """)
        
        self.par_page_flag = False

        if self.search_page_worker is not None:
            self.search_page_worker.stop()  # 기존 쓰레드를 종료
            self.search_page_worker.wait()  # 종료를 기다림
            self.search_page_worker = None  # 참조를 해제

    def select_all_camera(self):
        all_check_flag = False
        for camera_name, camera_viewer in self.search_page_camera_view_list.items():
            if camera_viewer.checked == False:
                camera_viewer.setChecked(True)
                all_check_flag = True

        if all_check_flag == False:
            for camera_name, camera_viewer in self.search_page_camera_view_list.items():
                camera_viewer.setChecked(False)


    def get_alarm_info(self, click):
        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : get alarm info")

        day_start = self.search_ui.time_day_start_input.text()
        date_time = datetime.strptime(day_start, "%Y. %m. %d")
        before_day = date_time.strftime("%y.%m.%d")

        day_end = self.search_ui.time_day_end_input.text()
        date_time = datetime.strptime(day_end, "%Y. %m. %d")
        after_day = date_time.strftime("%y.%m.%d")

        time_start = self.search_ui.time_hour_start_box.currentText()
        time_end = self.search_ui.time_hour_end_box.currentText()

        time_start += ":00"
        time_end += ":00"

        time_start = datetime.strptime(time_start, "%H:%M:%S")
        time_start = time_start.strftime("%H.%M.%S")

        time_end = datetime.strptime(time_end, "%H:%M:%S")
        time_end = time_end.strftime("%H.%M.%S")

        order = True if self.search_ui.sort_box.currentText() == "최신순" else False

        camera_name_list = []
        for camera_name, camera_viewer in self.search_page_camera_view_list.items():
            if camera_viewer.checked == True:
                camera_name_list.append(camera_name)

        search_detect_type = ["침입", "배회", "방화", "쓰러짐", "싸움"] if self.search_ui.event_box.currentText() == "전체" else [self.search_ui.event_box.currentText()]


        data = {"msg":{
            "before_day" : before_day,
            "after_day" : after_day,

            "time_start" : time_start,
            "time_end" : time_end,

            "camera_name" : camera_name_list,
            "search_detect_type" : search_detect_type,

        }}
        url = f'http://{self._parent.HOST}:{self._parent.PORT}/get-search-info'
        receive_data = requests.get(url, json=data).json()

        alarm_list = receive_data["data"]

        # 파일 경로를 날짜와 시간 기준으로 정렬
        sorted_alarm_list = sorted(alarm_list, key=get_datetime_from_path, reverse=order)
        
        self.search_ui.event_table.setRowCount(0)

        for alarm_info in sorted_alarm_list:
            # alarm_info = camera_8/24.04.25/17:07:50_침입.avi
            # alarm_info = camera_8/videos/24.04.25/17.07.50_침입.avi

            alarm = alarm_info.split("/")
            detect_time = datetime.strptime(alarm[-1].split("_")[0], "%H.%M.%S")
            detect_time = detect_time.strftime("%H:%M:%S")

            detect_type = alarm[-1].split("_")[1][:-4]

            row_position = self.search_ui.event_table.rowCount()
            self.search_ui.event_table.insertRow(row_position)

            text = QTableWidgetItem(str(row_position + 1))
            text.setTextAlignment(Qt.AlignCenter)
            text.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled)
            self.search_ui.event_table.setItem(row_position, 0, text)

            text = QTableWidgetItem(str(alarm[0]))
            text.setTextAlignment(Qt.AlignCenter)
            text.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled)
            self.search_ui.event_table.setItem(row_position, 1, text)

            text = QTableWidgetItem(str(detect_type))
            text.setTextAlignment(Qt.AlignCenter)
            text.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled)
            self.search_ui.event_table.setItem(row_position, 2, text)

            text = QTableWidgetItem(str(alarm[1] + " " + detect_time))
            text.setTextAlignment(Qt.AlignCenter)
            text.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled)
            self.search_ui.event_table.setItem(row_position, 3, text)


    # def search_viewer_playback(click, self):
    def search_viewer_playback(self, click):
        try:
            print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : play alarm video")

            if self.search_page_worker is not None:
                self.search_page_worker.stop()  # 기존 쓰레드를 종료
                self.search_page_worker.wait()  # 종료를 기다림
                self.search_page_worker = None  # 참조를 해제

            selected_indexes = self.search_ui.event_table.selectedIndexes()

            if selected_indexes:
                selected_row = selected_indexes[0].row()

                camera_name = self.search_ui.event_table.item(selected_row, 1).text()
                detect_type = self.search_ui.event_table.item(selected_row, 2).text()

                video_time = self.search_ui.event_table.item(selected_row, 3).text()
                video_time = datetime.strptime(video_time, "%y.%m.%d %H:%M:%S")

                
                date = str(video_time.strftime("%y.%m.%d/%H.%M.%S")).split("/")[0]
                detect_time = str(video_time.strftime("%y.%m.%d/%H.%M.%S")).split("/")[1]

                # video_file_name = f"{camera_name}/{date}/videos/{detect_time}_{detect_type}.mp4"
                video_file_name = f"{camera_name}/{date}/videos/{detect_time}_{detect_type}.avi"

                data = {"msg" : video_file_name}
                url = f'http://{self._parent.HOST}:{self._parent.PORT}/get-search-video'

                response = requests.get(url, json=data, stream=True)
                print(response)

                if response.status_code == 200:
                    play_fps = 30 * float(self.search_ui.time_video_time_speed_input.text())

                    viewer = self.search_ui.search_viewer
                    self.search_page_worker = Connect_Playback(response, viewers_widget = viewer, play_fps = play_fps, roi_thickness=2)

                    self.search_page_worker.ImageUpdated.connect(lambda image, viewer=viewer: self._parent.ShowCamera(viewer, image))
                    self.search_page_worker.start()
        
                    self.search_ui.stackedWidget.setCurrentIndex(1)


                else:
                    print("Failed to retrieve video stream.")
        except Exception as e:
                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                tb = traceback.format_exc()
                print(f"Error occurred at {current_time}: {e}\n{tb}", file=sys.stderr)

    # def search_close_window(click, self):
    def search_close_window(self, click):
        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : close search window")

        self.close()

        if self.search_page_worker is not None:
            self.search_page_worker.stop()  # 기존 쓰레드를 종료
            self.search_page_worker.wait()  # 종료를 기다림
            self.search_page_worker = None  # 참조를 해제


def get_datetime_from_list(list):
    img_base64, camera_name, date, video_time, label_info = list

    return datetime.strptime(date + " " + video_time, "%y-%m-%d %H:%M:%S")

def get_datetime_from_path(path):
    parts = path.split('/')  # 경로를 '/'로 분할
    date_time_str = parts[-1].split('_')[0]  # 파일 이름에서 시간 부분 추출 ('08.54.48')
    date_str = parts[-3]  # 날짜 부분 추출 ('24.04.29')
    # 날짜와 시간 문자열 결합
    full_datetime_str = f"{date_str} {date_time_str}"
    # datetime 객체로 변환
    return datetime.strptime(full_datetime_str, "%y.%m.%d %H.%M.%S")

def open_search_window(click, self):
    self.search_window = SearchDialog(self)
    self.search_window.show()


