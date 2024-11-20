from PySide6.QtWidgets import QDialog, QListWidgetItem, QPushButton
from PySide6.QtGui import  QIcon
from PySide6.QtCore import Qt, QTimer
from PySide6 import QtCore
from ui.schedule_ui import Ui_schedule_window

from utils import Connect_Camera, Plot_Camera_Viewer, FadeOutWindow, Livepage_view, FadeOutInWindow,\
                  Eng2kor, Kor2eng, send_email_alarm, load_info, save_info

from datetime import datetime, timedelta
import requests
import resourece_rc


class Time_table_bar(QPushButton):
    def __init__(self, cls_name, widget_name, schedule_info, day_index):
        super().__init__(widget_name)
        # Initial base style
        base_style = """
            QPushButton {{
                background-color: {bg_color};
                border: 1px solid rgba(255, 255, 255, 125);
            }}
            QPushButton:hover {{
                border: 3px solid white;
            }}
        """

        if cls_name == "Intrusion":
            bg_color = "qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.233831 rgba(237, 87, 4, 255), stop:1 rgba(253, 207, 137, 255))"
            self.y_pos_gain = 27
        
        elif cls_name == "Fire":
            bg_color = "qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.298507 rgba(30, 92, 184, 255), stop:0.905473 rgba(3, 254, 254, 255))"
            self.y_pos_gain = 42
            
        elif cls_name == "Loitering":
            bg_color = "qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.134328 rgba(66, 110, 23, 255), stop:0.905473 rgba(202, 224, 59, 255))"
            self.y_pos_gain = 57
            
        elif cls_name == "Falldown":
            bg_color = "qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.134328 rgba(52, 65, 88, 255), stop:0.905473 rgba(91, 106, 128, 255))"
            self.y_pos_gain = 72

        elif cls_name == "Fight":
            bg_color = "qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(230, 230, 231, 255), stop:1 rgba(101, 102, 103, 255))"
            self.y_pos_gain = 87

        # Set the style sheet using formatted string
        self.setStyleSheet(base_style.format(bg_color=bg_color))

        self.schedule_info = schedule_info
        self.day_index = day_index
        self.cls_name = cls_name

def open_schedule_window(click, self):
    self.schedule_window = QDialog()  # QDialog 인스턴스 생성
    self.schedule_ui = Ui_schedule_window()
    self.schedule_ui.setupUi(self.schedule_window)

    # self.icon_check_off = QIcon(u":/newPrefix/ui/images/checkm.svg")
    # self.icon_check_on = QIcon(u":/newPrefix/ui/images/check.svg")
    self.icon_check_off = QIcon(u":/newPrefix/ui/images/checkm.jpg")
    self.icon_check_on = QIcon(u":/newPrefix/ui/images/check.jpg")

    # 메인 윈도우의 중앙에 팝업 윈도우 위치 계산
    mainWindowGeometry = self.frameGeometry()
    centerPoint = mainWindowGeometry.center() - self.schedule_window.rect().center()
    self.schedule_window.move(centerPoint.x(), centerPoint.y())

    self.schedule_ui.schedule_camera_list.clear()
    self.bar_list = []

    for camera_name, camera_info in self.camera_info_dict_temp.items():
        item = QListWidgetItem(camera_name)
        # 텍스트를 가운데 정렬
        item.setTextAlignment(Qt.AlignCenter)
        self.schedule_ui.schedule_camera_list.addItem(item)

    self.week_days_check_box = {"0": self.schedule_ui.check_box_sun,
                                "1": self.schedule_ui.check_box_mon,
                                "2": self.schedule_ui.check_box_tue,
                                "3": self.schedule_ui.check_box_wed,
                                "4": self.schedule_ui.check_box_thu,
                                "5": self.schedule_ui.check_box_fri,
                                "6": self.schedule_ui.check_box_sat,
                                }
    
    self.detect_cls_bnt = {"Intrusion" : self.schedule_ui.intr_bnt,
                                "Loitering" : self.schedule_ui.loit_bnt,
                                "Fire" : self.schedule_ui.fire_bnt,
                                "Falldown" : self.schedule_ui.fall_bnt,
                                "Fight" : self.schedule_ui.fight_bnt}
    
    self.schedule_ui.check_box_sun.toggled.connect(lambda checked, instance = self: update_day_icon_sun(instance, self.schedule_ui.check_box_sun, checked))
    self.schedule_ui.check_box_mon.toggled.connect(lambda checked, instance = self: update_day_icon_mon(instance, self.schedule_ui.check_box_mon, checked))
    self.schedule_ui.check_box_tue.toggled.connect(lambda checked, instance = self: update_day_icon_tue(instance, self.schedule_ui.check_box_tue, checked))
    self.schedule_ui.check_box_wed.toggled.connect(lambda checked, instance = self: update_day_icon_wed(instance, self.schedule_ui.check_box_wed, checked))
    self.schedule_ui.check_box_thu.toggled.connect(lambda checked, instance = self: update_day_icon_thu(instance, self.schedule_ui.check_box_thu, checked))
    self.schedule_ui.check_box_fri.toggled.connect(lambda checked, instance = self: update_day_icon_fri(instance, self.schedule_ui.check_box_fri, checked))
    self.schedule_ui.check_box_sat.toggled.connect(lambda checked, instance = self: update_day_icon_sat(instance, self.schedule_ui.check_box_sat, checked))

    self.schedule_ui.schedule_remove_bnt.clicked.connect(lambda click, instance = self: remove_all_schedule_bar(click, instance))

    self.schedule_ui.schedule_time_table.itemSelectionChanged.connect(lambda instance = self: set_schedule(click, instance))
    self.schedule_ui.schedule_camera_list.itemSelectionChanged.connect(lambda instance = self: refrush_time_table(click, instance))

    first_item = self.schedule_ui.schedule_camera_list.item(0)
    if first_item:
        self.schedule_ui.schedule_camera_list.setCurrentItem(first_item)

    self.schedule_ui.schedule_close_bnt.clicked.connect(lambda click, instance = self: schedule_close_window(click, instance))

    # 팝업 윈도우 표시
    self.schedule_window.show()    


def schedule_close_window(click, self):
    save_info(host=self.HOST, port=self.PORT, file_name="camera_info", info=self.camera_info_dict_temp)

    run_ms_ai(self)
    camera_name = self.ui_main.camera_page_name_box.currentText()

    if self.camera_info_dict_temp[camera_name]["AI"] == True:
        self.ui_main.camera_page_viewer.reset()
        self.ui_main.camera_page_ai_active_label.show()
        self.ui_main.camera_page_ai_active_icon.show()

    # 현재 시간을 계산하고 다음 정각까지 남은 시간을 초 단위로 계산합니다.
    now = datetime.now()
    seconds_till_next_hour = (60 - now.minute) * 60 - now.second

    # 타이머 설정
    self.ai_timer = QTimer(self)
    # 첫 번째 실행을 위해 남은 시간 설정
    self.ai_timer.setSingleShot(True)
    self.ai_timer.timeout.connect(lambda : setup_hourly_timer(self))
    self.ai_timer.start(seconds_till_next_hour * 1000)  # 밀리초 단위로 변환

    self.schedule_window.close()

def setup_hourly_timer(self):
    run_ms_ai(self)
    # 이제 매시간 함수를 실행하기 위한 타이머 설정
    self.hourly_timer = QTimer(self)
    self.hourly_timer.timeout.connect(run_ms_ai(self))
    self.hourly_timer.start(3600 * 1000)  # 매시간 반복

def run_ms_ai(self):
    save_info(host=self.HOST, port=self.PORT, file_name="camera_info", info=self.camera_info_dict_temp)

    data = {"msg" : "ms_ai"}
    url = f'http://{self.HOST}:{self.PORT}/run_ms_ai'
    receive_data = requests.post(url, json=data).json()


def update_day_icon_sun(self, checkbox, checked):
    # checkbox.setIcon(self.icon_check_on if checked else self.icon_check_off)
    camera_name = self.schedule_ui.schedule_camera_list.currentItem().text()

    self.camera_info_dict_temp[camera_name]["active_week_days"][0] = 1 if checked else 0
    
def update_day_icon_mon(self, checkbox, checked):
    # checkbox.setIcon(self.icon_check_on if checked else self.icon_check_off)
    camera_name = self.schedule_ui.schedule_camera_list.currentItem().text()

    self.camera_info_dict_temp[camera_name]["active_week_days"][1] = 1 if checked else 0

def update_day_icon_tue(self, checkbox, checked):
    # checkbox.setIcon(self.icon_check_on if checked else self.icon_check_off)
    camera_name = self.schedule_ui.schedule_camera_list.currentItem().text()

    self.camera_info_dict_temp[camera_name]["active_week_days"][2] = 1 if checked else 0

def update_day_icon_wed(self, checkbox, checked):
    # checkbox.setIcon(self.icon_check_on if checked else self.icon_check_off)
    camera_name = self.schedule_ui.schedule_camera_list.currentItem().text()

    self.camera_info_dict_temp[camera_name]["active_week_days"][3] = 1 if checked else 0

def update_day_icon_thu(self, checkbox, checked):
    # checkbox.setIcon(self.icon_check_on if checked else self.icon_check_off)
    camera_name = self.schedule_ui.schedule_camera_list.currentItem().text()

    self.camera_info_dict_temp[camera_name]["active_week_days"][4] = 1 if checked else 0

def update_day_icon_fri(self, checkbox, checked):
    # checkbox.setIcon(self.icon_check_on if checked else self.icon_check_off)
    camera_name = self.schedule_ui.schedule_camera_list.currentItem().text()

    self.camera_info_dict_temp[camera_name]["active_week_days"][5] = 1 if checked else 0

def update_day_icon_sat(self, checkbox, checked):
    # checkbox.setIcon(self.icon_check_on if checked else self.icon_check_off)
    camera_name = self.schedule_ui.schedule_camera_list.currentItem().text()

    self.camera_info_dict_temp[camera_name]["active_week_days"][6] = 1 if checked else 0

def remove_all_schedule_bar(click, self):
    camera_name = self.schedule_ui.schedule_camera_list.currentItem().text()

    self.camera_info_dict_temp[camera_name]["detect_schedule"] = {"0" : {"Intrusion" : [],
                                                                    "Fire" : [],
                                                                    "Loitering" : [],
                                                                    "Falldown" : [],
                                                                    "Fight" : []},
                                                            "1" : {"Intrusion" : [],
                                                                    "Fire" : [],
                                                                    "Loitering" : [],
                                                                    "Falldown" : [],
                                                                    "Fight" : []},

                                                            "2" : {"Intrusion" : [],
                                                                    "Fire" : [],
                                                                    "Loitering" : [],
                                                                    "Falldown" : [],
                                                                    "Fight" : []},

                                                            "3" : {"Intrusion" : [],
                                                                    "Fire" : [],
                                                                    "Loitering" : [],
                                                                    "Falldown" : [],
                                                                    "Fight" : []},

                                                            "4" : {"Intrusion" : [],
                                                                    "Fire" : [],
                                                                    "Loitering" : [],
                                                                    "Falldown" : [],
                                                                    "Fight" : []},

                                                            "5" : {"Intrusion" : [],
                                                                    "Fire" : [],
                                                                    "Loitering" : [],
                                                                    "Falldown" : [],
                                                                    "Fight" : []},

                                                            "6" : {"Intrusion" : [],
                                                                    "Fire" : [],
                                                                    "Loitering" : [],
                                                                    "Falldown" : [],
                                                                    "Fight" : []}
                                                                    }

    drew_schedule_time_table(self, self.camera_info_dict_temp[camera_name]["detect_schedule"])

def set_schedule(click, self):
        camera_name = self.schedule_ui.schedule_camera_list.currentItem().text()

        selected_indexes = self.schedule_ui.schedule_time_table.selectedIndexes()

        check_detect_cls = []
        select_index_dict = {}
        time_range_info = {}

    
        for cls_name, bnt in self.detect_cls_bnt.items():
            if bnt.isChecked() == True:
                check_detect_cls.append(cls_name)

        if selected_indexes and len(check_detect_cls):
            for index in selected_indexes:
                x_position = self.schedule_ui.schedule_time_table.columnViewportPosition(index.column())
                y_position = self.schedule_ui.schedule_time_table.rowViewportPosition(index.row())

                day_num = int(y_position / 82)
                end_time = int(x_position / 40)

                if day_num in select_index_dict.keys():
                    select_index_dict[day_num].append(end_time)
                else:
                    select_index_dict[day_num] = [end_time]
        
        for day_num, time_list in select_index_dict.items():
            time_range_info[day_num] = (time_list[0], time_list[-1])

        for day_num, time_range in time_range_info.items():
            # 추가할 스케줄 정보
            add_detect_schedule_info = time_range

            for detect_class in check_detect_cls:
                # 기존 스케줄 정보
                detect_schedule_info = self.camera_info_dict_temp[camera_name]["detect_schedule"][str(day_num)][detect_class]
                new_schedule_info = []
                add_detect_schedule = [add_detect_schedule_info[0], add_detect_schedule_info[1]]

                if len(detect_schedule_info) > 0:
                    new_schedule_info = self.merge_intervals(detect_schedule_info + [add_detect_schedule])
                else:
                    new_schedule_info.append(add_detect_schedule)


                self.camera_info_dict_temp[camera_name]["detect_schedule"][str(day_num)][detect_class] = new_schedule_info
            
        drew_schedule_time_table(self, self.camera_info_dict_temp[camera_name]["detect_schedule"])
    
def refrush_time_table(click, self):
    self.schedule_ui.schedule_time_table.clearSelection()
    for bar in self.bar_list:
        bar.deleteLater()

    self.bar_list.clear()

    camera_name = self.schedule_ui.schedule_camera_list.currentItem().text()

    for day_num, activte in enumerate(self.camera_info_dict_temp[camera_name]["active_week_days"]):
        self.week_days_check_box[str(day_num)].setChecked(activte)
        
    drew_schedule_time_table(self, self.camera_info_dict_temp[camera_name]["detect_schedule"])


def drew_schedule_time_table(self, detect_schedule_info):
    for bar in self.bar_list:
        bar.deleteLater()

    self.bar_list.clear()

    for day_index, schedule_info_list in detect_schedule_info.items():
        for cls_name, schedule_info in schedule_info_list.items():
            for schedule in schedule_info:
                x_length = (schedule[1] - schedule[0] + 1) * 40

                bar = Time_table_bar(cls_name=cls_name, widget_name = self.schedule_ui.schedule_time_table, schedule_info = schedule, day_index = day_index)
                bar.setGeometry(schedule[0] * 40 + 18, int(day_index) * 82 + bar.y_pos_gain, x_length, 10)

                bar.show()

                self.bar_list.append(bar)

                bar.clicked.connect(lambda click, instance = self, bar=self.bar_list[-1] : remove_schedule_bar(click, instance, bar))


def remove_schedule_bar(click, self, bar):
    camera_name = self.schedule_ui.schedule_camera_list.currentItem().text()

    for index, time_info in enumerate(self.camera_info_dict_temp[camera_name]["detect_schedule"][bar.day_index][bar.cls_name]):
        if time_info == bar.schedule_info:
            del self.camera_info_dict_temp[camera_name]["detect_schedule"][bar.day_index][bar.cls_name][index]
            bar.deleteLater()

            break

    drew_schedule_time_table(self, self.camera_info_dict_temp[camera_name]["detect_schedule"])


    
    