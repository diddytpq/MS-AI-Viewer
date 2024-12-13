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

from ui.ai_labeling_ui import Ui_labeling_window
import base64

COLOR = {
    0: (220, 20, 60),   # Crimson - person
    1: (60, 179, 113),  # Medium Sea Green - bicycle
    2: (70, 130, 180),  # Steel Blue - car
    3: (255, 140, 0),   # Dark Orange - motorcycle
    4: (147, 112, 219), # Medium Purple - bus
    5: (72, 209, 204),  # Medium Turquoise - truck
    6: (255, 20, 147)   # Deep Pink - fire
}


class Labeling_Viewer(QLabel):
    clicked = Signal(QPoint)  # 사용자가 클릭한 위치를 전달하는 시그널

    def __init__(self, parent):
        super().__init__(parent)
        
        self.point_list = []
        self.non_active_point_list = []
        self.setPixmap(QPixmap(u":/ui/ui/images/logo.png"))
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setStyleSheet(f"border: 1px solid rgb(119, 118, 123);\n"
                            "border-radius: 10px;\n"
                            )
        self.parent = parent
        self.label_list = []
        self.selected_box = None
        self.dragging = False
        self.resizing = False
        self.drawing_new_box = False
        self.drag_start_pos = None
        self.resize_corner = None
        self.mouse_pos = None
        self.box_resize_mode = False
        self.labeling_flag = False

        self.cls_bnt_list = []
        self.class_name_dict = { 0 : "person", 1 : "bicycle", 2 : "car", 3 : "motorcycle", 4 : "bus", 5 : "truck", 6 : "fire"}

        for num, cls_name in self.class_name_dict.items():
            # self.label_ui.label_image_viewer.make_cls_bnt(num, num, self.color(num))
            self.make_cls_bnt(num, num, COLOR[num])

    # 새로운 메서드 추가
    def handle_button_toggled(self, checked, button):
        if checked:
            # 현재 체크된 버튼을 제외한 나머지 버튼들은 체크 해제
            for btn in self.cls_bnt_list:
                if btn != button:
                    btn.setChecked(False)

    def make_cls_bnt(self, bnt_num, cls, color):
        cls_bnt = QPushButton(self.parent.label_ui.label_class_widget)
        bnt_name = f"{self.class_name_dict[cls]}"
        cls_bnt.setObjectName(bnt_name)
        cls_bnt.setMinimumSize(QSize(55, 25))

        if cls == 3:
            cls_bnt.setMinimumSize(QSize(75, 25))

        # cls_bnt.setMaximumSize(QSize(550, 25))

        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(cls_bnt.sizePolicy().hasHeightForWidth())
        cls_bnt.setSizePolicy(sizePolicy2)

        font = QFont()
        font.setFamilies([u"Sans"])
        font.setPointSize(10)
        cls_bnt.setFont(font)
        cls_bnt.setCursor(QCursor(Qt.PointingHandCursor))
        cls_bnt.setStyleSheet(
                                "QPushButton{\n"
                                f"background-color: rgb({color[0]}, {color[1]}, {color[2]});\n"
                                "color: rgb(255, 255, 255);\n"
                                "border-radius: 9px;\n"
                                "border: 1px solid rgba(255, 255, 255, 100);\n"
                                "}\n"
                                                
                                "QPushButton:checked {\n"
                                "color: white;\n"
                                "border-radius: 9px;\n"
                                "border: 2px solid rgb(255, 255, 255);\n"
                                "}"
                                )
        cls_bnt.setText(str(self.class_name_dict[cls]))
        cls_bnt.setCheckable(True)

        # 버튼이 체크될 때, 나머지 버튼의 체크를 해제하는 메서드 연결
        cls_bnt.toggled.connect(lambda checked, btn=cls_bnt: self.handle_button_toggled(checked, btn))

        self.parent.label_ui.horizontalLayout_7.insertWidget(bnt_num, cls_bnt)

        self.cls_bnt_list.append(cls_bnt)

    def display_label_image(self):
        self.label_list = []
        if 0 <= self.parent.cnt < len(self.parent.img_buffer):
            img = self.parent.img_buffer[self.parent.cnt]

            # for bnt in self.cls_bnt_list:
            #     try:
            #         bnt.deleteLater()
                    
            #     except:
            #         pass
            
            # self.cls_bnt_list = []

            if len(self.parent.label_buffer[self.parent.cnt]):
                for cls, xc, yc, w, h in self.parent.label_buffer[self.parent.cnt]:
                    self.label_list.append([int(cls), float(xc), float(yc), float(w), float(h), COLOR[cls]])
                    # self.cls_bnt_list.append(self.make_cls_bnt(len(self.cls_bnt_list), cls, color))
                    
            else: self.label_list = []
            
            img = cv2.resize(img, dsize=(self.width(), self.height()))
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            height, width, channel = img.shape
            bytes_per_line = 3 * width
            q_img = QImage(img.data, width, height, bytes_per_line, QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(q_img)
            self.setPixmap(pixmap)
            self.update()

    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        for label in self.label_list:
            cls, xc, yc, w, h, color = label
            x1 = int((xc - w / 2) * self.width())
            y1 = int((yc - h / 2) * self.height())
            x2 = int((xc + w / 2) * self.width())
            y2 = int((yc + h / 2) * self.height())
            rect = QRect(x1, y1, x2 - x1, y2 - y1)

            pen = QPen(QColor(color[0], color[1], color[2]), 3)
            painter.setPen(pen)
            brush = QBrush(QColor(color[0], color[1], color[2], 100))  # 100 is the alpha value for transparency
            painter.setBrush(brush)

            painter.drawRect(rect)

        if self.drawing_new_box and self.drag_start_pos and self.mouse_pos:
            pen = QPen(QColor(0, 255, 0), 2, Qt.DashLine)
            painter.setPen(pen)
            brush = QBrush(QColor(0, 0, 0, 0))
            painter.setBrush(brush)

            painter.drawRect(QRect(self.drag_start_pos, self.mouse_pos))

        if self.mouse_pos:
            pen = QPen(QColor(81, 174, 50), 2)
            painter.setPen(pen)
            painter.drawLine(0, self.mouse_pos.y(), self.width(), self.mouse_pos.y())
            painter.drawLine(self.mouse_pos.x(), 0, self.mouse_pos.x(), self.height())

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and self.labeling_flag:
            self.drag_start_pos = event.pos()
            self.drawing_new_box = True
            for index, label in enumerate(self.label_list):
                cls, xc, yc, w, h, color = label
                x1 = int((xc - w / 2) * self.width())
                y1 = int((yc - h / 2) * self.height())
                x2 = int((xc + w / 2) * self.width())
                y2 = int((yc + h / 2) * self.height())
                rect = QRect(x1, y1, x2 - x1, y2 - y1)

                if rect.contains(event.pos()):
                    self.drawing_new_box = False
                    self.selected_box = index
                    corner = self.get_resize_corner(event.pos(), rect)
                    if corner and self.box_resize_mode:
                        self.resizing = True
                        self.resize_corner = corner
                    else:
                        self.dragging = True
                    break

        if event.button() == Qt.RightButton:
            check_index = []
            check_distance = []

            for index, label in enumerate(self.label_list):
                cls, xc, yc, w, h, color = label
                x1 = int((xc - w / 2) * self.width())
                y1 = int((yc - h / 2) * self.height())
                x2 = int((xc + w / 2) * self.width())
                y2 = int((yc + h / 2) * self.height())
                rect = QRect(x1, y1, x2 - x1, y2 - y1)

                if rect.contains(event.pos()):
                    check_index.append(index)
                    check_distance.append(abs(event.pos().x() - xc*self.width()) + abs(event.pos().y() - yc*self.height()))

            if check_index:
                del_index = check_index[np.argmin(np.array(check_distance))]
                del self.label_list[del_index]
                del self.parent.label_buffer[self.parent.cnt][del_index]

                # self.cls_bnt_list[del_index].deleteLater()
                # del self.cls_bnt_list[del_index]
                self.update()

    def mouseMoveEvent(self, event):
        self.mouse_pos = event.pos()
        if self.drawing_new_box:
            self.update()
        elif self.dragging and self.selected_box is not None:
            dx = event.pos().x() - self.drag_start_pos.x()
            dy = event.pos().y() - self.drag_start_pos.y()
            cls, xc, yc, w, h, color = self.label_list[self.selected_box]

            new_xc = (int(xc * self.width()) + dx) / self.width()
            new_yc = (int(yc * self.height()) + dy) / self.height()

            # xc = (int(xc * self.width()) + dx) / self.width()
            # yc = (int(yc * self.height()) + dy) / self.height()

            if (new_xc - w/2) <= 0 or (new_xc + w/2) >= 1 : xc = xc
            else: xc = new_xc
            if (new_yc - h/2) <= 0 or (new_yc + h/2) >= 1 : yc = yc
            else: yc = new_yc

            self.label_list[self.selected_box] = [cls, xc, yc, w, h, color]
            self.parent.label_buffer[self.parent.cnt][self.selected_box] = [cls, xc, yc, w, h]
            self.drag_start_pos = event.pos()
            self.update()
        elif self.resizing and self.selected_box is not None:
            self.resize_box(event.pos())
            self.update()
        else:
            self.update()

    def mouseReleaseEvent(self, event):
        if self.drawing_new_box:
            self.create_new_box(event.pos())
        self.dragging = False
        self.resizing = False
        self.drawing_new_box = False

    def enterEvent(self, event):
        self.setMouseTracking(True)
        self.mouse_pos = None
        self.update()

    def leaveEvent(self, event):
        self.setMouseTracking(False)
        self.mouse_pos = None
        self.update()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.display_label_image()

    def get_resize_corner(self, pos, rect):
        margin = 50
        corners = {
            "top_left": rect.topLeft(),
            "top_right": rect.topRight(),
            "bottom_left": rect.bottomLeft(),
            "bottom_right": rect.bottomRight()
        }
        edges = {
            "top": (rect.left(), rect.top(), rect.right(), rect.top()),
            "bottom": (rect.left(), rect.bottom(), rect.right(), rect.bottom()),
            "left": (rect.left(), rect.top(), rect.left(), rect.bottom()),
            "right": (rect.right(), rect.top(), rect.right(), rect.bottom())
        }
        for corner, corner_pos in corners.items():
            if (corner_pos - pos).manhattanLength() < margin:
                return corner
        for edge, (x1, y1, x2, y2) in edges.items():
            if x1 == x2:  # Vertical edge
                if abs(pos.x() - x1) < margin and y1 <= pos.y() <= y2:
                    return edge
            elif y1 == y2:  # Horizontal edge
                if abs(pos.y() - y1) < margin and x1 <= pos.x() <= x2:
                    return edge
        return None

    def resize_box(self, pos):
        cls, xc, yc, w, h, color = self.label_list[self.selected_box]
        x1 = (xc - w / 2) * self.width()
        y1 = (yc - h / 2) * self.height()
        x2 = (xc + w / 2) * self.width()
        y2 = (yc + h / 2) * self.height()

        if self.resize_corner == "top_left":
            x1 = pos.x()
            y1 = pos.y()
            if x1 >= x2:
                self.resize_corner = "top_right"
                x1, x2 = x2, x1
            elif y1 > y2:
                self.resize_corner = "bottom_left"
                y1, y2 = y2, y1

        elif self.resize_corner == "top_right":
            x2 = pos.x()
            y1 = pos.y()
            if x2 < x1:
                self.resize_corner = "top_left"
                x1, x2 = x2, x1
            if y1 > y2:
                self.resize_corner = "bottom_right"
                y1, y2 = y2, y1
        elif self.resize_corner == "bottom_left":
            x1 = pos.x()
            y2 = pos.y()
            if x1 > x2:
                self.resize_corner = "bottom_right"
                x1, x2 = x2, x1
            if y2 < y1:
                self.resize_corner = "top_left"
                y1, y2 = y2, y1
        elif self.resize_corner == "bottom_right":
            x2 = pos.x()
            y2 = pos.y()
            if x2 < x1:
                self.resize_corner = "bottom_left"
                x1, x2 = x2, x1
            if y2 < y1:
                self.resize_corner = "top_right"
                y1, y2 = y2, y1

        elif self.resize_corner == "top":
            y1 = pos.y()
            if y1 > y2:
                self.resize_corner = "bottom"
                y1, y2 = y2, y1
        elif self.resize_corner == "bottom":
            y2 = pos.y()
            if y2 < y1:
                self.resize_corner = "top"
                y1, y2 = y2, y1
        elif self.resize_corner == "left":
            x1 = pos.x()
            if x1 > x2:
                self.resize_corner = "right"
                x1, x2 = x2, x1
        elif self.resize_corner == "right":
            x2 = pos.x()
            if x2 < x1:
                self.resize_corner = "left"
                x1, x2 = x2, x1

        if x1 <= 0: x1 = 1
        if x2 >= self.width() : x2 = self.width() -1
        if y1 <= 0: y1 = 1
        if y2 >= self.height(): y2 = self.height() - 1

        new_xc = ((x1 + x2) / 2) / self.width()
        new_yc = ((y1 + y2) / 2) / self.height()
        new_w = abs(x2 - x1) / self.width()
        new_h = abs(y2 - y1) / self.height()
        
        self.label_list[self.selected_box] = [cls, new_xc, new_yc, new_w, new_h, color]
        self.parent.label_buffer[self.parent.cnt][self.selected_box] = [cls, new_xc, new_yc, new_w, new_h]

    def create_new_box(self, end_pos):
        start_x = self.drag_start_pos.x()
        start_y = self.drag_start_pos.y()
        end_x = end_pos.x()
        end_y = end_pos.y()

        new_xc = (start_x + end_x) / 2 / self.width()
        new_yc = (start_y + end_y) / 2 / self.height()
        new_w = abs(end_x - start_x) / self.width()
        new_h = abs(end_y - start_y) / self.height()

        # 체크된 버튼의 인덱스를 찾습니다.
        cls_num = None
        for index, button in enumerate(self.cls_bnt_list):
            if button.isChecked():
                cls_num = index
                break
        # 만약 체크된 버튼이 없다면, 경고 메시지를 출력하고 종료
        if cls_num is None:
            print("아무 버튼도 체크되지 않았습니다. 클래스 번호를 지정하려면 하나의 버튼을 체크하세요.")
            return
        
        if new_w * new_h * self.width() * self.height() > 100:
            color = COLOR[cls_num]

            self.label_list.append([cls_num, new_xc, new_yc, new_w, new_h, color])
            self.parent.label_buffer[self.parent.cnt].append([cls_num, new_xc, new_yc, new_w, new_h])


            # 필요한 경우 버튼을 추가하는 로직이 있는지 확인
            # self.cls_bnt_list.append(self.make_cls_bnt(len(self.cls_bnt_list), 0, color))

            self.update()

class LabelingDialog(QDialog):
    def __init__(self, parent=None):
        print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} : open labeling window")

        super().__init__(parent)
        self.label_ui = Ui_labeling_window()
        self.label_ui.setupUi(self)
        self.parent = parent

        self.label_ui.cls_1.hide()

        self.event_data_exist = False
        self.cnt = 0
        self.img_buffer = []
        self.label_buffer = []

        # 메인 윈도우의 중앙에 팝업 윈도우 위치 계산
        mainWindowGeometry = parent.frameGeometry()
        centerPoint = mainWindowGeometry.center() - self.rect().center()
        self.move(centerPoint.x(), centerPoint.y())

        # 카메라 페이지 영상 뷰어
        self.label_ui.label_image_viewer.hide()
        self.label_ui.label_image_viewer = Labeling_Viewer(self)
        self.label_ui.label_image_viewer.setObjectName(u"camera_page_viewer")
        self.label_ui.label_image_viewer.setMinimumSize(QSize(343, 581))
        self.label_ui.label_image_viewer.setStyleSheet(u"border: 1px solid rgb(119, 118, 123);\n"
                                                         "background-color: rgba(255, 255, 255, 0);")
        self.label_ui.label_image_viewer.setScaledContents(False)
        self.label_ui.verticalLayout_3.addWidget(self.label_ui.label_image_viewer)

        self.label_data_refresh()

        self.label_ui.camera_name_box.currentTextChanged.connect(self.set_date_list)
        self.label_ui.event_date_box.currentTextChanged.connect(self.set_event_list)
        # self.label_ui.label_list_table.itemSelectionChanged.connect(self.load_event_data)
        self.label_ui.label_list_table.itemDoubleClicked.connect(self.load_event_data)

        self.label_ui.shutdown_bnt.clicked.connect(self.close_window)
        self.label_ui.label_save_bnt.clicked.connect(self.save_label_buffer)
        self.label_ui.label_del_bnt.clicked.connect(self.del_all_label)
        self.label_ui.self_labeling_bnt.clicked.connect(self.start_self_labeling)
        self.label_ui.train_bnt.clicked.connect(self.start_train)
        self.label_ui.label_refresh_bnt.clicked.connect(self.label_data_refresh)
        self.label_ui.label_data_del_bnt.clicked.connect(self.del_label_data)

        self.label_ui.camera_name_box.setCurrentIndex(0)

        self.setFocusPolicy(Qt.StrongFocus)
        self.installEventFilter(self)

    def label_data_refresh(self):
        data = {"msg" : {"cmd" : "get_label_info"}} 
        url = f'http://{self.parent.HOST}:{self.parent.PORT}/get-autolabel-info'
        receive_data = requests.get(url, json=data).json()
        self.label_data_info = receive_data["label_data_info"]

        self.label_flag = receive_data["label_flag"]
        self.train_flag = receive_data["train_flag"]

        current_name_box_text = self.label_ui.camera_name_box.currentText()

        self.label_ui.camera_name_box.clear()
        for camera_name, camera_info in receive_data["label_data_info"].items():
            self.label_ui.camera_name_box.addItems([camera_name])

        index = self.label_ui.camera_name_box.findText(current_name_box_text)

        self.label_ui.camera_name_box.setCurrentIndex(index)

        if self.label_flag == True:
            #자동 라벨링 진행중
            self.label_ui.self_labeling_bnt.setStyleSheet("""
                                                        background-color: rgb(30, 195, 55);
                                                        color: rgb(255, 255, 255);
                                                        border-radius: 15px;
                                                        """)
            self.label_ui.self_labeling_bnt.setText("자동 라벨링 진행중")
            
        else:
            self.label_ui.self_labeling_bnt.setStyleSheet("""
                                            background-color: rgb(36, 39, 44);
                                            color: rgb(255, 255, 255);
                                            border-radius: 15px;
                                            """)
            
            self.label_ui.self_labeling_bnt.setText("자동 라벨링 시작")

        if self.train_flag == True:
            #자동 라벨링 진행중
            self.label_ui.train_bnt.setStyleSheet("""
                                                        background-color: rgb(30, 195, 55);
                                                        color: rgb(255, 255, 255);
                                                        border-radius: 15px;
                                                        """)
            self.label_ui.train_bnt.setText("학습 진행중")
            
        else:
            self.label_ui.train_bnt.setStyleSheet("""
                                            background-color: rgb(36, 39, 44);
                                            color: rgb(255, 255, 255);
                                            border-radius: 15px;
                                            """)
            
            self.label_ui.train_bnt.setText("학습 시작")

        self.set_date_list()
        self.set_event_list()

    def start_train(self):
        if self.train_flag == False:
            data = {"msg" : ""} 
            url = f'http://{self.parent.HOST}:{self.parent.PORT}/start_trainer'
            receive_data = requests.post(url, json=data).json()

        else:
            data = {"msg" : "ms_train"} 
            url = f'http://{self.parent.HOST}:{self.parent.PORT}/pause_ms_labeler'
            receive_data = requests.put(url, json=data).json()

        self.label_data_refresh()

    def eventFilter(self, source, event):
        if event.type() == QEvent.KeyPress:
            self.keyPressEvent(event)
            return True
        return super(LabelingDialog, self).eventFilter(source, event)

    def start_self_labeling(self):
        if self.label_flag == False:
            data = {"msg" : "self_labeling"} 
            url = f'http://{self.parent.HOST}:{self.parent.PORT}/start_ms_labeler'
            receive_data = requests.put(url, json=data).json()

            if receive_data["success"] == True:
                self.label_flag = True
                #자동 라벨링 진행중

        else:
            data = {"msg" : "ms_labeling"} 
            url = f'http://{self.parent.HOST}:{self.parent.PORT}/pause_ms_labeler'
            receive_data = requests.put(url, json=data).json()

        self.label_data_refresh()

    def del_all_label(self):
        self.label_buffer[self.cnt] = []
        self.label_ui.label_image_viewer.display_label_image()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_D:
            self.cnt += 1
            if self.cnt >= len(self.img_buffer):
                self.cnt = 0  # 다시 처음 이미지로 돌아가도록

            self.label_ui.img_cur_num.setText(str(self.cnt + 1))
            self.label_ui.label_image_viewer.display_label_image()
        elif event.key() == Qt.Key_A:
            self.cnt -= 1
            if self.cnt < 0:
                self.cnt = len(self.img_buffer) - 1  # 마지막 이미지로 돌아가도록
 
            self.label_ui.label_image_viewer.display_label_image()
            self.label_ui.img_cur_num.setText(str(self.cnt + 1))

        if event.key() == Qt.Key_W:
            self.label_ui.label_image_viewer.box_resize_mode = True

        if event.key() == Qt.Key_F:
            self.del_label_data()
            self.parent.create_fade_out_msg(std_window = self, msg="삭제 완료")

        if (event.key() == Qt.Key_S and event.modifiers() == Qt.ControlModifier) or event.key() == Qt.Key_Space:
            self.save_label_buffer()
            self.parent.create_fade_out_msg(std_window = self, msg="저장 완료")

        if event.key() == Qt.Key_Q:
            self.del_all_label()

    def keyReleaseEvent(self, event):
        if event.key() == Qt.Key_W:
            self.label_ui.label_image_viewer.box_resize_mode = False

    def close_window(self):
        self.close()

    def set_date_list(self):
        camera_name = self.label_ui.camera_name_box.currentText()
        self.label_ui.event_date_box.clear()
        
        if camera_name in self.label_data_info.keys():
            date_list = self.label_data_info[camera_name].keys()
            date_list = sorted(date_list, key=lambda date: datetime.strptime(date, "%y.%m.%d"))

            self.label_ui.event_date_box.clear()

            for date in date_list:
                self.label_ui.event_date_box.addItems([date])

    def set_event_list(self):
        self.label_ui.label_list_table.setRowCount(0)
        camera_name = self.label_ui.camera_name_box.currentText()
        date = self.label_ui.event_date_box.currentText()

        if camera_name in self.label_data_info.keys() and date in self.label_data_info[camera_name].keys():
            event_data_list = self.label_data_info[camera_name][date]
            event_data_list = sorted(event_data_list)

            for event_data in event_data_list:
                row_position = self.label_ui.label_list_table.rowCount()
                self.label_ui.label_list_table.insertRow(row_position)
                text = QTableWidgetItem(str(event_data))
                text.setTextAlignment(Qt.AlignCenter)
                text.setFlags(Qt.ItemIsSelectable | Qt.ItemIsDragEnabled | Qt.ItemIsDropEnabled | Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
                self.label_ui.label_list_table.setItem(row_position, 0, text)

            if self.label_ui.label_list_table.rowCount() > 0:
                self.label_ui.label_list_table.setCurrentCell(0, 0)

    def load_event_data(self):
        # self.parent.create_fade_out_msg(std_window = self, msg="라벨 데이터 로딩중")

        self.img_buffer = []
        selected_indexes = self.label_ui.label_list_table.selectedIndexes()

        if selected_indexes:
            selected_row = selected_indexes[0].row()
            data = {"msg" : {"cmd" : "get_label_data", 
                            "camera_name" : self.label_ui.camera_name_box.currentText(),
                            "date" : self.label_ui.event_date_box.currentText(),
                            "event_name" : self.label_ui.label_list_table.item(selected_row, 0).text()}} 
            url = f'http://{self.parent.HOST}:{self.parent.PORT}/get-autolabel-info'
            self.receive_data = requests.get(url, json=data).json()

            for img_base64 in self.receive_data["image"]:
                img_data = base64.b64decode(img_base64)
                np_array = np.frombuffer(img_data, np.uint8)
                img = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
                self.img_buffer.append(img)


            self.label_buffer = self.receive_data["label"]
            self.cnt = 0

            if len(self.img_buffer):
                self.label_ui.label_image_viewer.display_label_image()
                self.label_ui.label_image_viewer.labeling_flag = True
                self.label_ui.img_cur_num.setText(str(1))
                self.label_ui.img_total_num.setText(str(len(self.img_buffer)))

    def del_label_data(self):
        camera_name = self.label_ui.camera_name_box.currentText()
        date = self.label_ui.event_date_box.currentText()
        selected_indexes = self.label_ui.label_list_table.selectedIndexes()

        # if selected_indexes:
        #     selected_row = selected_indexes[0].row()
        #     event_name = self.label_ui.label_list_table.item(selected_row, 0).text()

        #     data = {"msg" : {"cmd" : "del_label", 
        #                     "camera_name" : camera_name,
        #                     "date" : date,
        #                     "event_name" : event_name},
        #                     } 
            
        #     url = f'http://{self.parent.HOST}:{self.parent.PORT}/get-autolabel-info'
        #     self.receive_data = requests.get(url, json=data).json()

        #     if self.receive_data["msg"] == True:
        #         data = {"msg" : {"cmd" : "get_label_info"}} 
        #         url = f'http://{self.parent.HOST}:{self.parent.PORT}/get-autolabel-info'
        #         receive_data = requests.get(url, json=data).json()
        #         self.label_data_info = receive_data["label_data_info"]

        #         self.label_flag = receive_data["label_flag"]
        #         self.set_event_list()
        #         self.label_ui.label_list_table.selectRow(selected_row)

        event_name_list = []
        if selected_indexes:
            for i in range(len(selected_indexes)):
                selected_row = selected_indexes[i].row()
                event_name = self.label_ui.label_list_table.item(selected_row, 0).text()
                # print(event_name)
                event_name_list.append(event_name)

            data = {"msg" : {"cmd" : "del_label", 
                            "camera_name" : camera_name,
                            "date" : date,
                            "event_name" : event_name_list},
                            } 
            
            url = f'http://{self.parent.HOST}:{self.parent.PORT}/get-autolabel-info'
            self.receive_data = requests.get(url, json=data).json()

            if self.receive_data["msg"] == True:
                data = {"msg" : {"cmd" : "get_label_info"}} 
                url = f'http://{self.parent.HOST}:{self.parent.PORT}/get-autolabel-info'
                receive_data = requests.get(url, json=data).json()
                self.label_data_info = receive_data["label_data_info"]

                self.label_flag = receive_data["label_flag"]
                self.set_event_list()
                self.label_ui.label_list_table.selectRow(selected_row)
                self.load_event_data()



    def save_label_buffer(self):
        camera_name = self.label_ui.camera_name_box.currentText()
        date = self.label_ui.event_date_box.currentText()
        selected_indexes = self.label_ui.label_list_table.selectedIndexes()
        if selected_indexes:
            selected_row = selected_indexes[0].row()
            event_name = self.label_ui.label_list_table.item(selected_row, 0).text()

            data = {"msg" : {"cmd" : "save_label", 
                            "camera_name" : camera_name,
                            "date" : date,
                            "event_name" : event_name,
                            "label_buffer" : self.label_buffer},
                            } 
            
            url = f'http://{self.parent.HOST}:{self.parent.PORT}/get-autolabel-info'
            self.receive_data = requests.get(url, json=data).json()

            if self.receive_data["msg"] == True:
                data = {"msg" : {"cmd" : "get_label_info"}} 
                url = f'http://{self.parent.HOST}:{self.parent.PORT}/get-autolabel-info'
                receive_data = requests.get(url, json=data).json()
                self.label_data_info = receive_data["label_data_info"]

                self.label_flag = receive_data["label_flag"]
                self.set_event_list()
                self.label_ui.label_list_table.selectRow(selected_row+1)
                self.load_event_data()
            # self.parent.create_fade_out_msg("Save Label")

def open_labeling_window(click, self):
    self.labeling_window = LabelingDialog(self)
    self.labeling_window.show()

def event_key(file_name):
    date_time_str = file_name.split('_')[0]
    # date_time = datetime.strptime(date_time_str, "%H.%M.%S")
    date_time = datetime.strptime("%H.%M.%S")

    return date_time

