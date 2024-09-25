import sys
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

sys.path.append(os.path.join(ROOT, "front", "ui"))

from PySide6.QtWidgets import QDialog, QTableWidgetItem
from ui.ai_setting_ui import Ui_Ai_Setting_Window
from datetime import datetime
from PySide6.QtCore import QTimer, QDate, Qt


import requests
from utils import Connect_Playback, save_info, get_datetime_from_path

from ui.search_ui import Ui_Search_window
import cv2
import numpy as np 
import base64
from io import BytesIO
import traceback


def open_search_window(click, self):
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : open search window")

    self.search_window = QDialog()  # QDialog 인스턴스 생성
    self.search_ui = Ui_Search_window()
    self.search_ui.setupUi(self.search_window)

    # 메인 윈도우의 중앙에 팝업 윈도우 위치 계산
    mainWindowGeometry = self.frameGeometry()
    centerPoint = mainWindowGeometry.center() - self.search_window.rect().center()
    self.search_window.move(centerPoint.x(), centerPoint.y())

    self.search_ui.time_day_start_input.setDate(QDate.currentDate())
    self.search_ui.time_day_end_input.setDate(QDate.currentDate())
    self.search_ui.time_hour_end_box.setCurrentText("23:59")

    self.search_ui.camera_name_box.addItems(["전체"])

    for camera_name in self.camera_info_dict_temp.keys():
        self.search_ui.camera_name_box.addItems([str(camera_name)])

    self.search_ui.event_table.setColumnWidth(0, 40)
    self.search_ui.event_table.setColumnWidth(1, 100)
    self.search_ui.event_table.setColumnWidth(2, 120)

    self.search_ui.time_search_bnt.clicked.connect(lambda click, instance = self : get_alarm_info(click, instance))
    self.search_ui.event_table.itemDoubleClicked.connect(lambda click, instance = self : search_viewer_playback(click, instance))

    self.search_ui.time_day_start_input.installEventFilter(self)
    self.search_ui.time_day_end_input.installEventFilter(self)



    self.search_ui.search_close_bnt.clicked.connect(lambda click, instance = self : search_close_window(click, instance))

    # 팝업 윈도우 표시
    self.search_window.show()


def get_alarm_info(click, self):
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

    camera_num = '*' if self.search_ui.camera_name_box.currentText() == "전체" else self.search_ui.camera_name_box.currentText()
    search_detect_type = ["침입", "배회", "방화", "쓰러짐", "싸움"] if self.search_ui.event_box.currentText() == "전체" else [self.search_ui.event_box.currentText()]


    data = {"msg":{
        "before_day" : before_day,
        "after_day" : after_day,

        "time_start" : time_start,
        "time_end" : time_end,

        "camera_num" : camera_num,
        "search_detect_type" : search_detect_type,

    }}
    url = f'http://{self.HOST}:{self.PORT}/get-search-info'
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


def search_viewer_playback(click, self):
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
            url = f'http://{self.HOST}:{self.PORT}/get-search-video'

            response = requests.get(url, json=data, stream=True)
            print(response)

            if response.status_code == 200:
                play_fps = 30 * float(self.search_ui.time_video_time_speed_input.text())

                viewer = self.search_ui.search_viewer
                self.search_page_worker = Connect_Playback(response, viewers_widget = viewer, play_fps = play_fps, roi_thickness=2)

                self.search_page_worker.ImageUpdated.connect(lambda image, viewer=viewer: self.ShowCamera(viewer, image))
                self.search_page_worker.start()

            else:
                print("Failed to retrieve video stream.")
    except Exception as e:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            tb = traceback.format_exc()
            print(f"Error occurred at {current_time}: {e}\n{tb}", file=sys.stderr)

def search_close_window(click, self):
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : close search window")

    self.search_window.close()

    if self.search_page_worker is not None:
        self.search_page_worker.stop()  # 기존 쓰레드를 종료
        self.search_page_worker.wait()  # 종료를 기다림
        self.search_page_worker = None  # 참조를 해제

