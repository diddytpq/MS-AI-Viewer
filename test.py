# import sys
# from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget
# from PySide6.QtCore import QUrl
# from PySide6.QtGui import QDesktopServices

# # 버튼 클릭 시 구글 웹페이지 열기 함수
# def open_google():
#     url = QUrl("https://www.google.com")
#     QDesktopServices.openUrl(url)

# # 애플리케이션 초기화
# app = QApplication(sys.argv)

# # 메인 윈도우 설정
# window = QWidget()
# window.setWindowTitle("Open Google Example")
# layout = QVBoxLayout()

# # 버튼 생성 및 이벤트 연결
# button = QPushButton("Open Google")
# button.clicked.connect(open_google)  # 버튼 클릭 시 함수 연결

# # 레이아웃에 버튼 추가
# layout.addWidget(button)
# window.setLayout(layout)

# # 윈도우 표시
# window.show()

# # 애플리케이션 실행
# sys.exit(app.exec())

# import sys
# from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget, QMenu
# from PySide6.QtCore import Qt, QPoint
# from PySide6.QtGui import QAction  # QAction을 QtGui에서 임포트

# # 커스텀 QLabel 클래스 정의 (오른쪽 클릭 이벤트 처리)
# class ClickableLabel(QLabel):
#     def __init__(self, text, parent=None):
#         super().__init__(text, parent)

#     # 마우스 클릭 이벤트 처리
#     def mousePressEvent(self, event):
#         # 오른쪽 클릭 감지
#         if event.button() == Qt.RightButton:
#             self.show_context_menu(event.pos())  # 오른쪽 클릭 시 컨텍스트 메뉴 띄우기
#         else:
#             super().mousePressEvent(event)  # 다른 버튼은 기본 동작 유지

#     # 컨텍스트 메뉴 생성 및 표시
#     def show_context_menu(self, pos):
#         # QMenu 생성
#         context_menu = QMenu(self)

#         # 메뉴 항목 추가
#         open_action = QAction("열기", self)
#         copy_action = QAction("복사", self)
#         paste_action = QAction("붙여넣기", self)
#         rename_action = QAction("이름 바꾸기", self)

#         # 메뉴에 항목 추가
#         context_menu.addAction(open_action)
#         context_menu.addAction(copy_action)
#         context_menu.addAction(paste_action)
#         context_menu.addAction(rename_action)

#         # 메뉴 항목에 기능 연결 (예시로 출력)
#         open_action.triggered.connect(lambda: print("열기 선택됨"))
#         copy_action.triggered.connect(lambda: print("복사 선택됨"))
#         paste_action.triggered.connect(lambda: print("붙여넣기 선택됨"))
#         rename_action.triggered.connect(lambda: print("이름 바꾸기 선택됨"))

#         # 마우스 오른쪽 클릭 위치에서 컨텍스트 메뉴 띄우기
#         context_menu.exec(self.mapToGlobal(pos))

# # 메인 윈도우 설정
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("오른쪽 클릭 컨텍스트 메뉴 예제")

#         # 라벨 설정
#         label = ClickableLabel("오른쪽 클릭 시 컨텍스트 메뉴가 표시됩니다.")
#         label.setAlignment(Qt.AlignCenter)

#         # 레이아웃 설정
#         layout = QVBoxLayout()
#         layout.addWidget(label)

#         # 중앙 위젯 설정
#         central_widget = QWidget()
#         central_widget.setLayout(layout)
#         self.setCentralWidget(central_widget)

# # 애플리케이션 실행
# if __name__ == "__main__":
#     app = QApplication(sys.argv)

#     window = MainWindow()
#     window.resize(400, 200)
#     window.show()

#     sys.exit(app.exec())


# from onvif import ONVIFCamera

# def get_camera_info(camera_ip, camera_port, username, password):
#     # ONVIF 카메라 연결
#     mycam = ONVIFCamera(camera_ip, camera_port, username, password)

#     # 장치 서비스 가져오기
#     device_service = mycam.create_devicemgmt_service()

#     # 카메라 정보 가져오기
#     camera_info = device_service.GetDeviceInformation()

#     # 카메라 정보 출력
#     print(f"Manufacturer: {camera_info.Manufacturer}")
#     print(f"Model: {camera_info.Model}")
#     print(f"Firmware Version: {camera_info.FirmwareVersion}")
#     print(f"Serial Number: {camera_info.SerialNumber}")
#     print(f"Hardware ID: {camera_info.HardwareId}")

#     # 네트워크 인터페이스 정보 가져오기
#     network_interfaces = device_service.GetNetworkInterfaces()

#     # 네트워크 인터페이스 정보 출력
#     for interface in network_interfaces:
#         print(f"Interface: {interface.Info.Name}")
#         print(f"Enabled: {interface.Enabled}")
#         print(f"IPv4 Address: {interface.IPv4.Config.Manual[0].Address}")


# # 예시 사용법
# camera_ip = "117.17.159.196"  # 카메라 IP 주소
# camera_port = 80             # ONVIF 기본 포트 (대부분 80)
# username = "admin"           # ONVIF 카메라의 사용자 이름
# password = "admin13579"           # ONVIF 카메라의 비밀번호

# get_camera_info(camera_ip, camera_port, username, password)



# from PySide6.QtWidgets import QApplication, QCalendarWidget, QToolButton
# from PySide6.QtCore import QDate

# # QApplication 생성
# app = QApplication([])

# # QCalendarWidget 생성
# calendar = QCalendarWidget()
# calendar.setMinimumDate(QDate(2023, 1, 1))
# calendar.setMaximumDate(QDate(2024, 12, 31))

# # 스타일시트 설정
# calendar.setStyleSheet("""
#     /* 이전/다음 달로 이동하는 버튼 숨기기 */
#     QCalendarWidget QToolButton {
#         visibility: hidden;
#     }

#     /* 날짜 셀 하이라이트 - 동그라미 모양 */
#     QCalendarWidget QAbstractItemView::item:hover {
#         background-color: rgba(255, 100, 100, 50); /* 빨간색 반투명 */
#         border: 1px solid rgba(255, 100, 100, 100); /* 경계선 */
#         border-radius: 15px; /* 동그라미 크기 설정 */
#         margin: 3px; /* 동그라미와 셀 경계 간격 */
#     }

#     /* 날짜 셀 기본 스타일 */
#     QCalendarWidget QAbstractItemView::item {
#         padding: 5px;
#         margin: 5px;
#     }
# """)

# # QCalendarWidget 표시
# calendar.show()

# # QApplication 실행
# app.exec_()

# import sys
# import os
# from PySide6.QtWidgets import (
#     QApplication, QWidget, QLabel, QGridLayout, QFileDialog, QPushButton, QVBoxLayout,
#     QScrollArea, QDialog, QHBoxLayout, QSpinBox, QMessageBox
# )
# from PySide6.QtGui import QPixmap
# from PySide6.QtCore import Qt, Signal


# class ImageViewer(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("동적 그리드 이미지 뷰어")
#         self.resize(800, 600)

#         # 메인 레이아웃 설정
#         main_layout = QVBoxLayout()
#         self.setLayout(main_layout)

#         # 상단에 폴더 선택 버튼과 열 수 선택 스핀박스 추가
#         top_layout = QHBoxLayout()
#         main_layout.addLayout(top_layout)

#         self.button = QPushButton("이미지 폴더 선택")
#         self.button.clicked.connect(self.open_folder)
#         top_layout.addWidget(self.button)

#         self.columns_spinbox = QSpinBox()
#         self.columns_spinbox.setRange(1, 10)
#         self.columns_spinbox.setValue(4)
#         self.columns_spinbox.setPrefix("열 수: ")
#         self.columns_spinbox.valueChanged.connect(self.update_grid)
#         top_layout.addWidget(self.columns_spinbox)

#         # 스크롤 영역 추가 (이미지가 많을 경우 스크롤 가능하도록)
#         scroll_area = QScrollArea()
#         scroll_area.setWidgetResizable(True)
#         main_layout.addWidget(scroll_area)

#         # 스크롤 영역에 담을 위젯과 그리드 레이아웃 설정
#         self.grid_widget = QWidget()
#         self.grid_layout = QGridLayout()
#         self.grid_layout.setSpacing(10)  # 이미지 간 간격 설정
#         self.grid_widget.setLayout(self.grid_layout)
#         scroll_area.setWidget(self.grid_widget)

#         # 이미지 레이블 리스트
#         self.image_labels = []
#         self.current_folder = ""
#         self.images = []

#     def open_folder(self):
#         # 폴더 선택 다이얼로그 열기
#         folder_path = QFileDialog.getExistingDirectory(self, "이미지 폴더 선택", os.getcwd())
#         if folder_path:
#             self.current_folder = folder_path
#             self.load_images(folder_path)

#     def load_images(self, folder_path):
#         # 지원되는 이미지 파일 확장자
#         supported_formats = ('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')

#         # 폴더 내 이미지 파일 리스트
#         images = [f for f in os.listdir(folder_path) if f.lower().endswith(supported_formats)]
#         images.sort()  # 정렬 (선택 사항)

#         # 이미지가 없을 경우 알림
#         if not images:
#             self.show_message("선택한 폴더에 이미지 파일이 없습니다.")
#             return

#         self.images = images
#         self.update_grid()

#     def update_grid(self):
#         # 기존 그리드 초기화
#         self.init_grid()

#         columns = self.columns_spinbox.value()  # 현재 설정된 열 수
#         rows = (len(self.images) + columns - 1) // columns  # 필요한 행 수 계산

#         for index, image_name in enumerate(self.images):
#             row = index // columns
#             col = index % columns
#             image_path = os.path.join(self.current_folder, image_name)

#             pixmap = QPixmap(image_path)
#             if pixmap.isNull():
#                 # 이미지 로드 실패 시 텍스트 표시
#                 label = QLabel("이미지 로드 실패")
#                 label.setAlignment(Qt.AlignCenter)
#                 label.setStyleSheet("border: 1px solid black;")
#             else:
#                 label = ClickableLabel(image_path)
#                 label.setPixmap(pixmap.scaled(180, 180, Qt.KeepAspectRatio, Qt.SmoothTransformation))
#                 label.setAlignment(Qt.AlignCenter)
#                 label.setStyleSheet("border: 1px solid black;")
#                 label.clicked.connect(self.show_full_image)

#             self.grid_layout.addWidget(label, row, col)
#             self.image_labels.append(label)

#     def init_grid(self):
#         # 기존 레이블 제거
#         for label in self.image_labels:
#             self.grid_layout.removeWidget(label)
#             label.deleteLater()
#         self.image_labels.clear()

#     def show_full_image(self, image_path):
#         # 이미지 확대 창 열기
#         dialog = QDialog(self)
#         dialog.setWindowTitle("확대된 이미지")
#         dialog_layout = QVBoxLayout()
#         dialog.setLayout(dialog_layout)

#         pixmap = QPixmap(image_path)
#         if pixmap.isNull():
#             label = QLabel("이미지 로드 실패")
#         else:
#             label = QLabel()
#             label.setPixmap(pixmap.scaled(800, 800, Qt.KeepAspectRatio, Qt.SmoothTransformation))
#             label.setAlignment(Qt.AlignCenter)

#         dialog_layout.addWidget(label)
#         dialog.exec()

#     def show_message(self, message):
#         # QMessageBox를 사용한 메시지 박스
#         msg_box = QMessageBox(self)
#         msg_box.setWindowTitle("알림")
#         msg_box.setText(message)
#         msg_box.setIcon(QMessageBox.Information)
#         msg_box.setStandardButtons(QMessageBox.Ok)
#         msg_box.exec()


# class ClickableLabel(QLabel):
#     # PySide6에서는 pyqtSignal 대신 Signal을 사용합니다.
#     clicked = Signal(str)

#     def __init__(self, image_path, parent=None):
#         super().__init__(parent)
#         self.image_path = image_path

#     def mouseReleaseEvent(self, event):
#         if self.pixmap():
#             # 클릭 시 시그널에 이미지 경로 전달
#             self.clicked.emit(self.image_path)
#         super().mouseReleaseEvent(event)


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     viewer = ImageViewer()
#     viewer.show()
#     sys.exit(app.exec())



# import sys
# from PySide6.QtWidgets import (
#     QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout,
#     QScrollArea, QMainWindow
# )
# from PySide6.QtGui import QPixmap
# from PySide6.QtCore import Qt

# class ListItem(QWidget):
#     def __init__(self, image_path, text, parent=None):
#         super().__init__(parent)

#         # Create layout for the list item
#         layout = QHBoxLayout()
#         layout.setContentsMargins(10, 10, 10, 10)
#         layout.setSpacing(15)

#         # Image label
#         self.image_label = QLabel()
#         pixmap = QPixmap(image_path)
#         if pixmap.isNull():
#             # If image fails to load, use a placeholder
#             pixmap = QPixmap(50, 50)
#             pixmap.fill(Qt.gray)
#         else:
#             # Scale the pixmap to a desired size while keeping aspect ratio
#             pixmap = pixmap.scaled(50, 50, Qt.KeepAspectRatio, Qt.SmoothTransformation)
#         self.image_label.setPixmap(pixmap)
#         self.image_label.setFixedSize(50, 50)

#         # Text label
#         self.text_label = QLabel(text)
#         self.text_label.setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
#         self.text_label.setStyleSheet("font-size: 14px;")

#         # Add widgets to the layout
#         layout.addWidget(self.image_label)
#         layout.addWidget(self.text_label)

#         self.setLayout(layout)

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("Scroll Area with Image and Text List")
#         self.resize(400, 600)

#         # Create the scroll area
#         scroll = QScrollArea()
#         scroll.setWidgetResizable(True)

#         # Create a widget to hold the list items
#         list_widget = QWidget()
#         list_layout = QVBoxLayout()
#         list_layout.setContentsMargins(0, 0, 0, 0)
#         list_layout.setSpacing(0)

#         # Example list of images and names
#         items = [
#             {"image": "path/to/image1.png", "name": "Photo 1"},
#             {"image": "path/to/image2.png", "name": "Photo 2"},
#             {"image": "path/to/image3.png", "name": "Photo 3"},
#             {"image": "path/to/image3.png", "name": "Photo 3"},

#             {"image": "path/to/image3.png", "name": "Photo 3"},

#             {"image": "path/to/image3.png", "name": "Photo 3"},

#             {"image": "path/to/image3.png", "name": "Photo 3"},

#             {"image": "path/to/image3.png", "name": "Photo 3"},

#             {"image": "path/to/image3.png", "name": "Photo 3"},

#             # Add more items as needed
#         ]

#         # Add list items to the layout
#         for item in items:
#             list_item = ListItem(item["image"], item["name"])
#             list_layout.addWidget(list_item)

#         # Add stretch to push items to the top
#         list_layout.addStretch()

#         list_widget.setLayout(list_layout)

#         scroll.setWidget(list_widget)

#         self.setCentralWidget(scroll)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)

#     window = MainWindow()
#     window.show()

#     sys.exit(app.exec())


import sys
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QPainter, QBrush, QColor, QPen, QCursor
from PySide6.QtCore import Qt, QRectF, QPointF

class ResizableRectangle(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Resizable Rectangle with Corners")
        self.setGeometry(100, 100, 400, 300)
        self.rect = QRectF(100, 100, 200, 150)  # 초기 네모의 위치와 크기

        # 동그라미의 반지름
        self.circle_radius = 5

        # 드래그 상태 변수
        self.dragging = False
        self.drag_corner = None

        # 마우스 트래킹 설정
        self.setMouseTracking(True)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # 네모 그리기
        pen = QPen(QColor(0, 0, 0), 2)
        painter.setPen(pen)
        painter.drawRect(self.rect)

        # 각 모서리에 동그라미 그리기
        brush = QBrush(QColor(255, 0, 0))
        painter.setBrush(brush)
        corners = self.get_corners()
        for point in corners.values():
            painter.drawEllipse(point, self.circle_radius, self.circle_radius)

    def get_corners(self):
        """네모의 각 모서리 위치를 반환"""
        return {
            'top_left': self.rect.topLeft(),
            'top_right': self.rect.topRight(),
            'bottom_left': self.rect.bottomLeft(),
            'bottom_right': self.rect.bottomRight(),
        }

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            clicked_corner = self.get_clicked_corner(event.position())
            if clicked_corner:
                self.dragging = True
                self.drag_corner = clicked_corner
                self.drag_start_pos = event.position()
                self.rect_start = QRectF(self.rect)  # 드래그 시작 시 네모의 상태 저장

    def mouseMoveEvent(self, event):
        if self.dragging and self.drag_corner:
            delta = event.position() - self.drag_start_pos
            new_rect = QRectF(self.rect_start)

            if self.drag_corner == 'top_left':
                new_rect.setTopLeft(new_rect.topLeft() + delta)
            elif self.drag_corner == 'top_right':
                new_rect.setTopRight(new_rect.topRight() + delta)
            elif self.drag_corner == 'bottom_left':
                new_rect.setBottomLeft(new_rect.bottomLeft() + delta)
            elif self.drag_corner == 'bottom_right':
                new_rect.setBottomRight(new_rect.bottomRight() + delta)

            # 최소 크기 설정 (예: 너비와 높이가 50 이상)
            min_width = 50
            min_height = 50
            if new_rect.width() < min_width:
                new_rect.setWidth(min_width)
                if self.drag_corner in ['top_left', 'bottom_left']:
                    new_rect.setLeft(self.rect_start.right() - min_width)
            if new_rect.height() < min_height:
                new_rect.setHeight(min_height)
                if self.drag_corner in ['top_left', 'top_right']:
                    new_rect.setTop(self.rect_start.bottom() - min_height)

            self.rect = new_rect
            self.update()

        else:
            # 커서 모양 변경
            hovered_corner = self.get_clicked_corner(event.position())
            if hovered_corner:
                if hovered_corner in ['top_left', 'bottom_right']:
                    self.setCursor(QCursor(Qt.SizeFDiagCursor))
                elif hovered_corner in ['top_right', 'bottom_left']:
                    self.setCursor(QCursor(Qt.SizeBDiagCursor))
            else:
                self.setCursor(QCursor(Qt.ArrowCursor))

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragging = False
            self.drag_corner = None

    def get_clicked_corner(self, pos: QPointF):
        """마우스 클릭 위치가 동그라미와 일치하는지 확인"""
        corners = self.get_corners()
        for name, point in corners.items():
            distance = (pos - point).manhattanLength()
            if distance <= self.circle_radius + 2:  # 약간의 여유를 두어 클릭 인식
                return name
        return None

    def sizeHint(self):
        return self.size()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ResizableRectangle()
    window.show()
    sys.exit(app.exec())

