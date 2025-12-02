from PySide6.QtWidgets import QDialog
from ui.ui_ai_setting import Ui_Ai_Setting_Window
from datetime import datetime
from PySide6.QtCore import QTimer
import requests

from PySide6.QtGui import QImage, QPixmap, QPainter, QPen, QColor, QPolygon, QBrush, QFont, QStandardItem, QStandardItemModel, QIcon
from PySide6.QtCore import Qt, QThread, Signal, QPoint, QObject, QEvent, QTimer, QPropertyAnimation, QEasingCurve, QRect, QSize
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QComboBox,
    QFrame, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QStackedWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget, QGridLayout)

from utils import save_info, load_info
import resourece_rc


import cv2
import numpy as np
import math 

class Ai_setting_page_view(QLabel):
    Checked = Signal(QLabel)
    def __init__(self, base_viewer, camera_num, camera_name, name_label, parent):
        super().__init__(base_viewer)
        
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy2)

        self.setScaledContents(True)
        
        # 부모 위젯의 전체 크기를 채우도록 설정
        self.setGeometry(0, 0, base_viewer.width(), base_viewer.height())

        self.checked = False
        self.camera_num = camera_num
        self.camera_name = camera_name
        self.name_label = name_label

        self.parent = parent

        self.frame_flag = False
        
        # 부모 위젯 크기 변경 시 자동으로 리사이즈되도록 이벤트 필터 설치
        base_viewer.installEventFilter(self)

    def setChecked(self, checked):
        self.checked = checked
        self.updateStyle()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            if self.checked == False and self.parent.ai_active_camera_count >= self.parent.admin_info_temp["LICENSE"]["allow_camera_num"]:
                self.parent.create_fade_out_msg(std_window=self.parent.popup_window, msg="최대 허용 카메라 개수를 초과했습니다")
                return

            if self.checked == False:
                self.parent.ai_active_camera_count += 1
            else:
                self.parent.ai_active_camera_count -= 1

            self.setChecked(not self.checked)

    def enterEvent(self, event):
        if event.buttons() & Qt.LeftButton:
            self.setChecked(True)
    
    def eventFilter(self, obj, event):
        # 부모 위젯의 리사이즈 이벤트를 감지하여 자신도 리사이즈
        if event.type() == QEvent.Resize:
            self.setGeometry(0, 0, obj.width(), obj.height())
        return super().eventFilter(obj, event)
            
    def updateStyle(self):
            if self.checked:
                if self.frame_flag:
                    self.setStyleSheet("""
                        QLabel {
                            border: 2px solid rgb(56, 188, 56);
                            color: rgb(255, 255, 255);
                        }
                    """)



                    self.set_img(self.frame, 1)
                    # self.ai_check_box.setPixmap(self.ai_on_img)

                    self.name_label.setStyleSheet(
                                "color: rgb(56, 188, 56);\n"
                                "background-color: rgba(0, 0, 0, 170);\n"
                                "border: 1px solid rgb(119, 118, 123);"
                            )
                    self.parent.camera_info_dict_temp[self.camera_name]["AI"] = True
            else:
                if self.frame_flag:
                    self.setStyleSheet("""
                        QLabel {
                            "border: 1px solid rgb(119, 118, 123);\n"
                        }
                    """)
                    self.set_img(self.frame, 0.5)
                    # self.ai_check_box.setPixmap(self.ai_off_img)

                    self.name_label.setStyleSheet(
                                "color: rgb(255, 255, 255);\n"
                                "background-color: rgba(0, 0, 0, 170);\n"
                                "border: 1px solid rgb(119, 118, 123);"
                            )
                    self.parent.camera_info_dict_temp[self.camera_name]["AI"] = False

    def set_img(self, img, brightness = 1):
        self.frame_flag = True
        self.frame = img.copy()
        
        cv_image = self.frame.copy()
        
        # 밝기 조정
        cv_image = cv_image.astype('float32')
        cv_image = cv_image * brightness
        cv_image = np.clip(cv_image, 0, 255)
        cv_image = cv_image.astype('uint8')

        height, width, channels = cv_image.shape
        # Calculate the number of bytes per line.
        bytes_per_line = width * channels
        # Convert image from BGR (cv2 default color format) to RGB (Qt default color format).
        cv_rgb_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)
        # Convert the image to Qt format.
        qt_rgb_image = QImage(cv_rgb_image.data, width, height, bytes_per_line, QImage.Format_RGB888)

        self.setPixmap(QPixmap.fromImage(qt_rgb_image))

def create_camera_grid_page(popup_ui, page_index, camera_list, parent):
    """
    4x4 그리드 레이아웃으로 카메라 뷰를 생성하는 함수
    
    Args:
        popup_ui: UI 인스턴스
        page_index: 페이지 인덱스 (0부터 시작)
        camera_list: 이 페이지에 표시할 카메라 정보 리스트 [(camera_name, camera_info), ...]
        parent: 메인 인스턴스
    
    Returns:
        page_widget: 생성된 페이지 위젯
        camera_views: 생성된 카메라 뷰 딕셔너리 {camera_name: Ai_setting_page_view}
    """
    # 페이지 위젯 생성
    page_widget = QWidget()
    page_widget.setObjectName(f"ai_setting_page_{page_index}")
    
    # 메인 레이아웃
    main_layout = QHBoxLayout(page_widget)
    main_layout.setSpacing(0)
    main_layout.setContentsMargins(0, 0, 0, 0)
    
    # 그리드 레이아웃을 담을 위젯
    grid_widget = QWidget(page_widget)
    grid_widget.setObjectName(f"ai_setting_grid_widget_{page_index}")
    
    grid_layout = QGridLayout(grid_widget)
    grid_layout.setSpacing(0)
    grid_layout.setContentsMargins(-1, 0, 0, 0)
    
    camera_views = {}
    
    # 4x4 그리드로 카메라 뷰 생성
    for idx, (camera_name, camera_info) in enumerate(camera_list):
        row = idx // 4
        col = idx % 4
        
        # VBoxLayout 생성
        camera_layout = QVBoxLayout()
        camera_layout.setSpacing(0)
        camera_layout.setObjectName(f"camera_view_layout_{page_index}_{idx}")
        
        # 카메라 이름 라벨 생성
        name_label = QLabel(grid_widget)
        name_label.setObjectName(f"camera_view_name_{page_index}_{idx}")
        
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHeightForWidth(name_label.sizePolicy().hasHeightForWidth())
        name_label.setSizePolicy(sizePolicy)
        name_label.setMaximumSize(QSize(720, 20))
        
        font = QFont()
        font.setFamilies(["NanumSquareRound"])
        font.setPointSize(11)
        font.setBold(False)
        name_label.setFont(font)
        name_label.setStyleSheet(
            "color: rgb(255, 255, 255);\n"
            "background-color: rgba(0, 0, 0, 170);\n"
            "border: 1px solid rgb(119, 118, 123);"
        )
        name_label.setMargin(0)
        name_label.setIndent(15)
        name_label.setText(camera_name)
        
        camera_layout.addWidget(name_label)
        
        # 카메라 뷰 라벨 생성 (실제 영상이 표시될 부분)
        view_label = QLabel(grid_widget)
        view_label.setObjectName(f"camera_view_{page_index}_{idx}")
        
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHeightForWidth(view_label.sizePolicy().hasHeightForWidth())
        view_label.setSizePolicy(sizePolicy1)
        
        font2 = QFont()
        font2.setFamilies(["NanumBarunGothic"])
        font2.setPointSize(16)
        view_label.setFont(font2)
        view_label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        view_label.setStyleSheet(
            "border: 1px solid rgb(119, 118, 123);\n"
            "color: rgb(255, 255, 255);"
        )
        view_label.setPixmap(QPixmap(u":/ui/ui/images/ico_video_off.svg"))
        view_label.setScaledContents(False)
        view_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        camera_layout.addWidget(view_label)
        
        # AI 체크 아이콘 라벨 생성
        ai_check_label = QLabel(grid_widget)
        ai_check_label.setObjectName(f"camera_view_ai_check_{page_index}_{idx}")
        ai_check_label.setPixmap(QPixmap(u":/newPrefix/images/ai_on.png"))
        ai_check_label.setParent(view_label)
        ai_check_label.setGeometry(QRect(5, 5, 30, 30))
        ai_check_label.hide()
        
        # Ai_setting_page_view 인스턴스 생성
        camera_view = Ai_setting_page_view(
            base_viewer=view_label,
            camera_name=camera_name,
            camera_num=str(camera_info["Num"]),
            name_label=name_label,
            parent=parent
        )
        
        camera_views[camera_name] = camera_view
        
        # 그리드 레이아웃에 추가
        grid_layout.addLayout(camera_layout, row, col, 1, 1)
    
    main_layout.addWidget(grid_widget)
    
    return page_widget, camera_views

def open_ai_setting_window(click, self):
    self.dark_layer.show()
    self.popup_window = QDialog()  # QDialog 인스턴스 생성
    self.popup_window.setWindowFlag(Qt.FramelessWindowHint)

    self.popup_ui = Ui_Ai_Setting_Window()
    self.popup_ui.setupUi(self.popup_window)

    self.ai_setting_camera_view_list = {}
    self.ai_setting_current_page = 0
    self.ai_active_camera_count = 0
    
    save_info(host=self.HOST, port=self.PORT, file_name="camera_info", info=self.camera_info_dict_temp)

    # 카메라 리스트를 정렬 (Num 기준)
    camera_items = sorted(self.camera_info_dict_temp.items(), key=lambda x: x[1]["Num"])
    
    # 카메라 개수에 따라 페이지 수 계산 (16개씩)
    total_cameras = len(camera_items)
    cameras_per_page = 16
    total_pages = math.ceil(total_cameras / cameras_per_page)
    
    # stackedWidget_5의 기존 페이지 모두 제거 (첫 페이지 제외하고 동적으로 생성)
    while self.popup_ui.stackedWidget_5.count() > 0:
        widget = self.popup_ui.stackedWidget_5.widget(0)
        self.popup_ui.stackedWidget_5.removeWidget(widget)
        if widget:
            widget.deleteLater()
    
    # 각 페이지 생성
    for page_idx in range(total_pages):
        start_idx = page_idx * cameras_per_page
        end_idx = min(start_idx + cameras_per_page, total_cameras)
        page_cameras = camera_items[start_idx:end_idx]
        
        # 4x4 그리드 페이지 생성
        page_widget, camera_views = create_camera_grid_page(
            self.popup_ui, 
            page_idx, 
            page_cameras, 
            self
        )
        
        # stackedWidget에 페이지 추가
        self.popup_ui.stackedWidget_5.addWidget(page_widget)
        
        # 카메라 뷰 리스트에 추가
        self.ai_setting_camera_view_list.update(camera_views)
    
    # 카메라 이미지 설정
    for camera_name, camera_viewer in self.ai_setting_camera_view_list.items():
        if camera_name in self.camera_img_temp.keys():
            img = self.camera_img_temp[camera_name]
            # set_img 메서드에서 자동으로 리사이즈됨
            camera_viewer.set_img(img, 0.5)
        else:
            camera_viewer.setPixmap(QPixmap(u":/newPrefix/ui/images/ico_video_off.svg"))
            camera_viewer.setAlignment(Qt.AlignCenter)

    # AI 체크 상태 확인
    check_camera_viewer(self)

    # 버튼 이벤트 연결
    self.popup_ui.camera_save_bnt.clicked.connect(lambda click, instance = self : send_camera_info_and_close(click, instance))
    self.popup_ui.close_bnt.clicked.connect(lambda click, instance = self : cancel_ai_setting(click, instance))
    self.popup_ui.all_select_bnt.clicked.connect(lambda click, instance = self : select_camera(click, instance))
    self.popup_ui.all_release_bnt.clicked.connect(lambda click, instance = self : release_camera(click, instance))

    
    # 페이지 네비게이션 버튼 연결
    self.popup_ui.ai_setting_camera_next_page_bnt.clicked.connect(lambda: change_ai_setting_page(self, 1))
    self.popup_ui.ai_setting_camera_undo_page_bnt.clicked.connect(lambda: change_ai_setting_page(self, -1))
    
    # 페이지 네비게이션 버튼 표시/숨김 처리
    update_page_navigation_buttons(self, total_pages)

    self.popup_window.finished.connect(self.dark_layer.hide)

    # 메인 윈도우의 중앙에 팝업 윈도우 위치 계산
    mainWindowGeometry = self.frameGeometry()
    centerPoint = mainWindowGeometry.center()

    popupWindowGeometry = self.popup_window.frameGeometry()
    popupCenterPoint = popupWindowGeometry.center()

    # 중앙점에서 팝업 윈도우의 절반 크기를 빼서 팝업 윈도우의 좌상단 좌표를 계산
    topLeftPoint = centerPoint - (popupCenterPoint - popupWindowGeometry.topLeft())
    self.popup_window.move(topLeftPoint)

    # 팝업 윈도우 표시
    self.popup_window.show()

def change_ai_setting_page(self, direction):
    """
    AI 설정 페이지를 변경하는 함수
    
    Args:
        self: 인스턴스
        direction: 1 (다음 페이지) 또는 -1 (이전 페이지)
    """
    total_pages = self.popup_ui.stackedWidget_5.count()
    new_page = self.ai_setting_current_page + direction
    
    # 페이지 범위 체크
    if 0 <= new_page < total_pages:
        self.ai_setting_current_page = new_page
        self.popup_ui.stackedWidget_5.setCurrentIndex(new_page)
        update_page_navigation_buttons(self, total_pages)

def update_page_navigation_buttons(self, total_pages):
    """
    페이지 네비게이션 버튼의 표시/숨김을 업데이트하는 함수
    
    Args:
        self: 인스턴스
        total_pages: 전체 페이지 수
    """
    # 페이지가 1개면 네비게이션 버튼 숨김
    if total_pages <= 1:
        self.popup_ui.ai_setting_camera_next_page_bnt.hide()
        self.popup_ui.ai_setting_camera_undo_page_bnt.hide()
    else:
        # 첫 페이지면 이전 버튼 숨김
        if self.ai_setting_current_page == 0:
            self.popup_ui.ai_setting_camera_undo_page_bnt.hide()
        else:
            self.popup_ui.ai_setting_camera_undo_page_bnt.show()
        
        # 마지막 페이지면 다음 버튼 숨김
        if self.ai_setting_current_page == total_pages - 1:
            self.popup_ui.ai_setting_camera_next_page_bnt.hide()
        else:
            self.popup_ui.ai_setting_camera_next_page_bnt.show()

def select_camera(click, self):
    all_check_flag = False
    for camera_name, camera_info in self.camera_info_dict_temp.items():
        if self.ai_active_camera_count < self.admin_info_temp["LICENSE"]["allow_camera_num"]:
            if self.ai_setting_camera_view_list[camera_name].checked == False:
                self.ai_setting_camera_view_list[camera_name].setChecked(True)
                all_check_flag = True
                self.ai_active_camera_count += 1
        else:
            self.create_fade_out_msg(std_window=self.popup_window, msg="최대 허용 카메라 개수를 초과했습니다")
            return

def release_camera(click, self):
    for camera_name, camera_info in self.camera_info_dict_temp.items():
        if self.ai_setting_camera_view_list[camera_name].checked == True:
            self.ai_setting_camera_view_list[camera_name].setChecked(False)
            self.ai_active_camera_count -= 1

def cancel_ai_setting(click, self):

    self.camera_info_dict_temp = load_info(host=self.HOST,
                                    port=self.PORT,
                                    file_name="camera_info")

    self.popup_window.close()

    if self.camera_info_dict_temp[self.ui_main.camera_page_name_box.currentText()]["AI"] == True:
        self.ui_main.camera_page_viewer.reset()
        self.ui_main.camera_page_ai_active_label.show()
        self.ui_main.camera_page_ai_active_icon.show()
        if self.camera_page_worker is not None:
            self.camera_page_worker.ai_active = True

    else:
        self.ui_main.camera_page_viewer.reset()
        self.ui_main.camera_page_ai_active_label.hide()
        self.ui_main.camera_page_ai_active_icon.hide()
        if self.camera_page_worker is not None:
            self.camera_page_worker.ai_active = False

def send_camera_info_and_close(click, self):
    run_ms_ai(self)
    self.popup_window.close()
    # 팝업이 닫힌 후 메인 윈도우에 메시지 표시
    self.create_fade_out_msg(msg="지능형 분석 시작")

def run_ms_ai(self):
    save_info(host=self.HOST, port=self.PORT, file_name="camera_info", info=self.camera_info_dict_temp)

    data = {"msg" : "ms_ai"}
    url = f'http://{self.HOST}:{self.PORT}/run_ms_ai'
    receive_data = requests.post(url, json=data).json()

    if self.camera_info_dict_temp[self.ui_main.camera_page_name_box.currentText()]["AI"] == True:
        self.ui_main.camera_page_viewer.reset()
        self.ui_main.camera_page_ai_active_label.show()
        self.ui_main.camera_page_ai_active_icon.show()
        if self.camera_page_worker is not None:
            self.camera_page_worker.ai_active = True

    else:
        self.ui_main.camera_page_viewer.reset()
        self.ui_main.camera_page_ai_active_label.hide()
        self.ui_main.camera_page_ai_active_icon.hide()
        if self.camera_page_worker is not None:
            self.camera_page_worker.ai_active = False

def check_camera_viewer(self):
    for camera_name, camera_info in self.camera_info_dict_temp.items():
        if len(camera_info["IP"]):
            if camera_info["AI"] == False:
                self.ai_setting_camera_view_list[camera_name].setChecked(False)

            elif camera_info["AI"] == True:
                self.ai_setting_camera_view_list[camera_name].setChecked(True)
                self.ai_active_camera_count += 1
