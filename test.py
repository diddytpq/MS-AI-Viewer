# from onvif import ONVIFCamera

# # ONVIF 카메라에 연결 (IP 주소, 포트, 사용자 이름, 비밀번호)
# # mycam = ONVIFCamera('117.17.159.195', 80, 'admin', 'admin13579')
# mycam = ONVIFCamera('117.17.159.221', 80, 'admin', 'Admin13579')


# # 카메라의 장치 정보 가져오기
# device_info = mycam.devicemgmt.GetDeviceInformation()
# print(f"Manufacturer: {device_info.Manufacturer}")
# print(f"Model: {device_info.Model}")
# print(f"Firmware Version: {device_info.FirmwareVersion}")
# print(f"Serial Number: {device_info.SerialNumber}")
# print(f"Hardware ID: {device_info.HardwareId}")

# # 카메라의 PTZ(Pan-Tilt-Zoom) 기능 확인 (가능한 경우)
# # ptz_service = mycam.create_ptz_service()
# # status = ptz_service.GetStatus({'ProfileToken': '000'})
# # print(f"Pan-Tilt-Zoom 상태: {status}")


# # 카메라의 Media 서비스 사용
# media_service = mycam.create_media_service()

# # 지원되는 프로파일 목록 가져오기
# profiles = media_service.GetProfiles()

# for i in range(len(profiles)):
#     profile_token = profiles[i].token  # 첫 번째 프로파일 선택

#     # RTSP 스트림 URI 가져오기
#     stream_uri = media_service.GetStreamUri({
#         'StreamSetup': {'Stream': 'RTP-Unicast', 'Transport': {'Protocol': 'RTSP'}},
#         'ProfileToken': profile_token
#     })

#     print(f"RTSP Stream URI: {stream_uri.Uri}")


import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QDateEdit
from PySide6.QtCore import QEvent
from PySide6.QtGui import QWheelEvent

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Modify Existing DateEdit Event")

        # 기존에 생성된 QDateEdit 위젯
        self.date_edit = QDateEdit(self)
        self.date_edit.setGeometry(100, 100, 200, 30)
        self.date_edit.setCalendarPopup(True)

        # 이벤트 필터를 통해 마우스 휠을 억제
        self.date_edit.installEventFilter(self)

    def eventFilter(self, obj, event):
        # QDateEdit 위젯에서 발생하는 휠 이벤트를 억제
        if obj == self.date_edit and isinstance(event, QWheelEvent):
            return True  # 이벤트를 무시하여 휠로 변경되지 않게 만듦
        return super().eventFilter(obj, event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())