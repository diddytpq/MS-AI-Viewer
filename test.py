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


from onvif import ONVIFCamera

def get_camera_info(camera_ip, camera_port, username, password):
    # ONVIF 카메라 연결
    mycam = ONVIFCamera(camera_ip, camera_port, username, password)

    # 장치 서비스 가져오기
    device_service = mycam.create_devicemgmt_service()

    # 카메라 정보 가져오기
    camera_info = device_service.GetDeviceInformation()

    # 카메라 정보 출력
    print(f"Manufacturer: {camera_info.Manufacturer}")
    print(f"Model: {camera_info.Model}")
    print(f"Firmware Version: {camera_info.FirmwareVersion}")
    print(f"Serial Number: {camera_info.SerialNumber}")
    print(f"Hardware ID: {camera_info.HardwareId}")

    # 네트워크 인터페이스 정보 가져오기
    network_interfaces = device_service.GetNetworkInterfaces()

    # 네트워크 인터페이스 정보 출력
    for interface in network_interfaces:
        print(f"Interface: {interface.Info.Name}")
        print(f"Enabled: {interface.Enabled}")
        print(f"IPv4 Address: {interface.IPv4.Config.Manual[0].Address}")


# 예시 사용법
camera_ip = "117.17.159.196"  # 카메라 IP 주소
camera_port = 80             # ONVIF 기본 포트 (대부분 80)
username = "admin"           # ONVIF 카메라의 사용자 이름
password = "admin13579"           # ONVIF 카메라의 비밀번호

get_camera_info(camera_ip, camera_port, username, password)

