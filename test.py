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


import cv2

def main():
    # RTSP 스트림 URL에 사용자 인증 정보 포함
    rtsp_url = "rtsp://microsystems:admin123@117.17.159.118:8554/test"

    # OpenCV에서 RTSP 스트림을 읽기 위한 VideoCapture 객체 생성
    cap = cv2.VideoCapture(rtsp_url)

    if not cap.isOpened():
        print("RTSP 스트림을 열 수 없습니다.")
        return

    while True:
        ret, frame = cap.read()

        if not ret:
            print("프레임을 읽을 수 없습니다.")
            break

        # 받은 프레임을 화면에 표시
        cv2.imshow('RTSP Stream', frame)

        # 'q'를 눌러서 스트리밍 종료
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()