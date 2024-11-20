import sys
import os
from pathlib import Path
import cv2
import numpy as np
import shutil

ROOT = Path(__file__).resolve().parents[1]

sys.path.append(os.path.join(ROOT, "front", "ui"))

from PySide6.QtWidgets import QDialog, QTableWidgetItem, QLabel, QApplication, QMainWindow, QPushButton
from datetime import datetime
from PySide6.QtCore import QTimer, QDate, Qt, QSize, Signal, QPoint, QRect, QEvent
from PySide6.QtGui import QImage, QPainter, QPen, QColor, QPolygon, QBrush, QMouseEvent, QPixmap, QCursor, QFont
from PySide6.QtWidgets import QSizePolicy
import requests

from ui.object_setting_ui import Ui_object_setting
import base64

class Object_settint_Dialog(QDialog):
    def __init__(self, parent=None):
        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : open object_setting window")

        super().__init__(parent)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.object_setting_ui = Ui_object_setting()
        self.object_setting_ui.setupUi(self)
        self.parent = parent

        cls_list = self.parent.camera_info_dict_temp[self.parent.ui_main.camera_page_name_box.currentText()]["Cls"]
        conf_list = self.parent.camera_info_dict_temp[self.parent.ui_main.camera_page_name_box.currentText()]["Conf"]

        self.object_setting_ui.person_active_bnt.setChecked(cls_list[0])
        self.object_setting_ui.car_active_bnt.setChecked(cls_list[1])
        self.object_setting_ui.fire_active_bnt.setChecked(cls_list[2])

        self.object_setting_ui.person_conf_slider.valueChanged.connect(
            lambda value, 
                    intance = self,
                    std = self.object_setting_ui.person_conf_slider, 
                    target = self.object_setting_ui.person_conf_value, 
                    index = 0
                    : set_conf(intance, std, target, index))
        
        self.object_setting_ui.person_conf_value.valueChanged.connect(
            lambda value, 
                    intance = self,
                    std = self.object_setting_ui.person_conf_value, 
                    target = self.object_setting_ui.person_conf_slider, 
                    index = 0 : 
                    set_conf(intance, std, target, index))

        self.object_setting_ui.car_conf_slider.valueChanged.connect(
            lambda value, 
                    intance = self,
                    std = self.object_setting_ui.car_conf_slider, 
                    target = self.object_setting_ui.car_conf_value, 
                    index = 1 
                    : set_conf(intance, std, target, index))
        
        self.object_setting_ui.car_conf_value.valueChanged.connect(
            lambda value, 
                    intance = self,
                    std = self.object_setting_ui.car_conf_value, 
                    target = self.object_setting_ui.car_conf_slider, 
                    index = 1
                    : set_conf(intance, std, target, index))

        self.object_setting_ui.fire_conf_slider.valueChanged.connect(
            lambda value, 
                    intance = self,
                    std = self.object_setting_ui.fire_conf_slider, 
                    target = self.object_setting_ui.fire_conf_value, 
                    index = 2
                    : set_conf(intance, std, target, index))
        
        self.object_setting_ui.fire_conf_value.valueChanged.connect(
            lambda value,
                    intance = self,
                    std = self.object_setting_ui.fire_conf_value, 
                    target = self.object_setting_ui.fire_conf_slider, 
                    index = 2
                    : set_conf(intance, std, target, index))
        

        self.object_setting_ui.person_conf_slider.setValue(conf_list[0])
        self.object_setting_ui.car_conf_slider.setValue(conf_list[1])
        self.object_setting_ui.fire_conf_slider.setValue(conf_list[2])


        self.object_setting_ui.shutdown_bnt.clicked.connect(self.close_window)

    def close_window(self):
        self.parent.camera_info_dict_temp[self.parent.ui_main.camera_page_name_box.currentText()]["Cls"][0] = self.object_setting_ui.person_active_bnt.isChecked()
        self.parent.camera_info_dict_temp[self.parent.ui_main.camera_page_name_box.currentText()]["Cls"][1] = self.object_setting_ui.car_active_bnt.isChecked()
        self.parent.camera_info_dict_temp[self.parent.ui_main.camera_page_name_box.currentText()]["Cls"][2] = self.object_setting_ui.fire_active_bnt.isChecked()
        self.close()


def set_conf(intance, std, target, index):
    target.setValue(std.value())
    intance.parent.camera_info_dict_temp[intance.parent.ui_main.camera_page_name_box.currentText()]["Conf"][index] = std.value()

def open_object_setting_window(click, self):
    if self.camera_edit_permission:
        self.labeling_window = Object_settint_Dialog(self)
        self.labeling_window.show()

    else:
        self.create_fade_out_msg(msg="수정 권한이 없습니다.")
