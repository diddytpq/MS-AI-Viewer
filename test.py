# from PySide6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QTableWidgetSelectionRange

# class MainWindow(QTableWidget):
#     def __init__(self):
#         super().__init__(5, 5)  # 5x5 table

#         # Populate the table with some items
#         # for row in range(5):
#         #     for col in range(5):
#         #         item = QTableWidgetItem(f"R{row+1}C{col+1}")
#         #         self.setItem(row, col, item)

#         # Enable drag selection and highlight of rows/columns
#         self.setSelectionMode(QTableWidget.ExtendedSelection)  # Allow multiple item selection
#         self.setSelectionBehavior(QTableWidget.SelectItems)    # Select individual cells

#         # Set up the size of the table
#         self.resize(500, 300)

#         # Select a specific range (from row 3, column 3 to row 3, column 5)
#         selection_range = QTableWidgetSelectionRange(0, 2, 4, 2)  # QTableWidgetSelectionRange(startRow, startColumn, endRow, endColumn)
#         self.setRangeSelected(selection_range, True)

#         selection_range = QTableWidgetSelectionRange(0, 1, 4, 1)  # QTableWidgetSelectionRange(startRow, startColumn, endRow, endColumn)
#         self.setRangeSelected(selection_range, True)


# if __name__ == "__main__":
#     app = QApplication([])
#     window = MainWindow()
#     window.show()
#     app.exec()
# import ffmpeg
# import cv2
# import numpy as np
# import time
# import select

# # FFmpeg를 사용하여 RTSP 스트림을 가져오는 명령어
# process = (
    # ffmpeg
    # .input(
    #     'rtsp://admin:1234@117.17.159.143/video1',  # 카메라 URL
    #     rtsp_transport='tcp',  # 네트워크에 맞게 'udp' 또는 'tcp' 사용
    #     fflags='nobuffer',
    #     flags='low_delay',
    #     max_delay='0',
    #     probesize='32',
    #     analyzeduration='0',
    #     use_wallclock_as_timestamps='1'
    # )
    # .output(
    #     '-', 
    #     format='rawvideo', 
    #     pix_fmt='bgr24',
    #     vsync='vfr'  # 프레임 드롭을 허용하는 비동기 프레임 처리
    # )
#     .run_async(pipe_stdout=True)
# )

# # 프레임 크기 정의
# width = 1920
# height = 1080

# # 타임아웃 설정 (5초)
# timeout = 2
# start_time = time.time()

# # 데이터를 수신했는지 확인하는 플래그
# data_received = False

# # 초기 프레임 수신을 위한 타임아웃 처리
# while process.poll() is None and time.time() - start_time < timeout:
#     # select를 사용하여 비동기적으로 stdout에서 데이터를 읽음
#     ready_to_read, _, _ = select.select([process.stdout], [], [], 1)
    
#     if ready_to_read:
#         in_bytes = process.stdout.read(width * height * 3)
#         if in_bytes:
#             data_received = True  # 데이터를 성공적으로 받았을 경우
#             break

# if not data_received:
#     print("카메라로부터 데이터를 받지 못했습니다. 프로그램을 종료합니다...")
#     exit()
# else:
#     print("카메라 연결 성공.")

#     # 연결 후 스트림을 표시
#     while process.poll() is None:
#         ready_to_read, _, _ = select.select([process.stdout], [], [], 1)
        
#         if ready_to_read:
#             in_bytes = process.stdout.read(width * height * 3)
#             if not in_bytes:
#                 break

#             # 받은 데이터를 numpy 배열로 변환하고 이미지로 디코딩
#             frame = np.frombuffer(in_bytes, np.uint8).reshape([height, width, 3])

#             # 프레임을 OpenCV로 화면에 표시
#             cv2.imshow('RTSP Stream', frame)

#             # 'q' 키를 누르면 종료
#             if cv2.waitKey(1) & 0xFF == ord('q'):
#                 break

#     # 종료 후 리소스 해제
#     process.stdout.close()
#     process.wait()
#     cv2.destroyAllWindows()

import os
import cv2

os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = (
    "rtsp_transport;tcp|fflags;nobuffer|flags;low_delay|"
    "max_delay;0|probesize;32|analyzeduration;0|use_wallclock_as_timestamps;1"
)

cap = cv2.VideoCapture("rtsp://admin:1234@117.17.159.143/video1", cv2.CAP_FFMPEG)

while True:
    _, img = cap.read()

    cv2.imshow("123", img)
    key = cv2.waitKey(1)

    if key == 27:
        break


cap.release()
cv2.destroyAllWindows()