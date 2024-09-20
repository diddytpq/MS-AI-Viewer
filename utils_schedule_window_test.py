from PySide6.QtWidgets import QDialog, QListWidgetItem, QPushButton, QLabel, QTableWidgetSelectionRange, QTableWidget, QTableWidgetItem
from PySide6.QtGui import  QIcon, QImage, QPixmap
from PySide6.QtCore import Qt, QTimer, Signal, QRect
from PySide6 import QtCore
from ui.schedule_test_ui import Ui_schedule_window

from utils import Connect_Camera, Plot_Camera_Viewer, FadeOutWindow, Livepage_view, FadeOutInWindow,\
                  Eng2kor, Kor2eng, send_email_alarm, load_info, save_info

from datetime import datetime, timedelta
import numpy as np
import cv2
import requests
import ms_ai_img_rc

class schedule_page_view(QLabel):
    Checked = Signal(QLabel)
    def __init__(self, base_viewer, camera_num, camera_name, name_label, instance, time_table):
        super().__init__(base_viewer)
        # self.setGeometry(QRect(1, 1, base_viewer.width(), base_viewer.height()))
        self.setGeometry(QRect(1, 1, 203, 131))

        self.checked = False
        self.camera_num = camera_num
        self.camera_name = camera_name
        self.name_label = name_label

        self.instance = instance
        self.time_table = time_table

        self.frame_flag = False

    def setChecked(self, checked):
        for camera_name, camera_viewer in self.instance.schedule_page_camera_view_list.items():
            if camera_viewer.checked:
                camera_viewer.checked = False
                camera_viewer.updateStyle()
                
        self.checked = checked
        self.instance.schedule_ui.event_box.clear()
        for detect_info in self.instance.camera_info_dict_temp[self.camera_name]["detect_info"]:
            self.instance.schedule_ui.event_box.addItem(Eng2kor(detect_info[0]))

        self.updateStyle()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.setChecked(not self.checked)

    def enterEvent(self, event):
        if event.buttons() & Qt.LeftButton:
            self.setChecked(True)
            
    def updateStyle(self):
            if self.checked:
                self.time_table.clearSelection()
                for week_num, schedule_info in self.instance.camera_info_dict_temp[self.camera_name]["detect_schedule"].items():
                    for detect_type, time_table_info in schedule_info.items():
                        if Eng2kor(detect_type) == self.instance.schedule_ui.event_box.currentText():
                            for start, end in time_table_info:
                                for i in range(start, end):
                                    item_1 = self.time_table.item(i, int(week_num))
                                
                                    if item_1 is not None:  # 셀이 존재하는 경우에만 선택 처리
                                        item_1.setSelected(True)
                                    else:
                                        print(f"Cell at row {i} and column {week_num} does not exist.")

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


def open_schedule_window(click, self):
    self.schedule_window = QDialog()  # QDialog 인스턴스 생성
    self.schedule_window.setWindowFlags(self.schedule_window.windowFlags() | Qt.WindowStaysOnTopHint)

    self.schedule_ui = Ui_schedule_window()
    self.schedule_ui.setupUi(self.schedule_window)
    self.schedule_ui.schedule_move_oneshot_bnt.hide()

    self.schedule_ui.schedule_time_table.setSelectionMode(QTableWidget.MultiSelection)

    self.schedule_ui.event_box.clear()

    for row in range(24):
        for column in range(7):
            item = QTableWidgetItem(f" ")
            self.schedule_ui.schedule_time_table.setItem(row, column, item)

    if self.live_page_worker_dict != None :
        for worker in self.live_page_worker_dict.values():
            for camera_name in worker.caps.keys():
                self.camera_img_temp[camera_name] = worker.caps[camera_name].get_frame()

    # 메인 윈도우의 중앙에 팝업 윈도우 위치 계산
    mainWindowGeometry = self.frameGeometry()
    centerPoint = mainWindowGeometry.center() - self.schedule_window.rect().center()
    self.schedule_window.move(centerPoint.x(), centerPoint.y())

    self.schedule_page_camera_view_list = {}

    for camera_name, camera_info in self.camera_info_dict_temp.items():
        num = str(camera_info["Num"])
        self.schedule_page_camera_view_list[camera_name] = schedule_page_view(getattr(self.schedule_ui, f"camera_view_{num}"), 
                                                                            camera_name = camera_name, 
                                                                            camera_num = str(num), 
                                                                            name_label = getattr(self.schedule_ui, f"camera_view_name_{num}"),
                                                                            instance = self,
                                                                            time_table=self.schedule_ui.schedule_time_table)
        
        getattr(self.schedule_ui, f"camera_view_name_{num}").setText(camera_name)

    for camera_name, camera_viewer in self.schedule_page_camera_view_list.items():
        find_worker_flag = False
        if camera_name in self.camera_view_list.keys():
            img = self.camera_img_temp[camera_name]
            frame = cv2.resize(img, (camera_viewer.width(), camera_viewer.height()))
            camera_viewer.set_img(frame, 0.5)
            find_worker_flag = True

        if find_worker_flag == False:
            camera_viewer.setPixmap(QPixmap(u":/newPrefix/ui/images/ico_video_off.svg"))
            camera_viewer.setAlignment(Qt.AlignCenter)

    self.schedule_ui.event_box.currentIndexChanged.connect(lambda index: change_time_table(index, self))

    self.schedule_ui.schedule_apply_bnt.clicked.connect(lambda click, instance = self: apply_schedule(click, instance))
    self.schedule_ui.schedule_close_bnt.clicked.connect(lambda click, instance = self: schedule_close_window(click, instance))

    # 팝업 윈도우 표시
    self.schedule_window.show()    


def change_time_table(index, self):
    for camera_name, camera_viewer in self.schedule_page_camera_view_list.items():
        if camera_viewer.checked:
            camera_viewer.updateStyle()
            break

def apply_schedule(click, instance):
    selected_indexes_dict = {0 : [], 1 : [], 2 : [], 3 : [], 4 : [], 5 : [], 6 : []}
    selected_indexes = instance.schedule_ui.schedule_time_table.selectedIndexes()

    for index in selected_indexes:
        time = index.row()
        day = index.column()
        selected_indexes_dict[day].append(time)

    for day, info in selected_indexes_dict.items():
        for camera_name, camera_viewer in instance.schedule_page_camera_view_list.items():
            if camera_viewer.checked:
                instance.camera_info_dict_temp[camera_name]["detect_schedule"][str(day)][Kor2eng(instance.schedule_ui.event_box.currentText())] = group_ranges(info)
                break

    instance.create_fade_out_msg(std_window = instance.schedule_window, msg="저장 완료")

def group_ranges(lst):
    if not lst:
        return []

    lst = sorted(lst) 
    result = []
    start = lst[0]
    end = lst[0]

    for num in lst[1:]:
        if num == end + 1:
            end = num
        else:
            result.append([start, end + 1]) 
            start = num
            end = num

    result.append([start, end + 1])
    return result

def schedule_close_window(click, self):
    save_info(host=self.HOST, port=self.PORT, file_name="camera_info", info=self.camera_info_dict_temp)
    data = {"msg" : "ms_ai"}
    url = f'http://{self.HOST}:{self.PORT}/run_ms_ai'
    receive_data = requests.post(url, json=data).json()

    self.schedule_window.close()


    
