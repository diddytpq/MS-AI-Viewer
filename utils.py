import sys
import os
from pathlib import Path

import gi

gi.require_version('Gst', '1.0')
from gi.repository import Gst
Gst.init(None)

from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QComboBox,
    QFrame, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QStackedWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
from PySide6.QtGui import QImage, QPainter, QPen, QColor, QPolygon, QBrush, QMouseEvent, QPixmap
from PySide6.QtCore import Qt, QThread, Signal, QPoint, QObject, QEvent, QTimer, QPropertyAnimation, QEasingCurve, QRect, QSize
import cv2
import numpy as np
import requests
import random
from datetime import datetime, timezone, timedelta
import json

import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.header import Header
import base64

import time

from cryptography.fernet import Fernet
import traceback

KEY = "FBRBdZIbc_ULGN_qOlZjdMLDLPPzdRJ2Nb63kX3wuDI="

ROOT = Path(__file__).resolve().parents[1]

    # def mousePressEvent(self, event):
    #     # 오른쪽 마우스 클릭 감지
    #     if event.button() == Qt.RightButton:
    #         self.deleteLater()  # 버튼 삭제
    #     else:
    #         super().mousePressEvent(event)

class Colors:
    # Ultralytics color palette https://ultralytics.com/
    def __init__(self):
        # hex = matplotlib.colors.TABLEAU_COLORS.values()
        hexs = ('FF3838', 'FF9D97', 'FF701F', 'FFB21D', 'CFD231', '48F90A', '92CC17', '3DDB86', '1A9334', '00D4BB',
                '2C99A8', '00C2FF', '344593', '6473FF', '0018EC', '8438FF', '520085', 'CB38FF', 'FF95C8', 'FF37C7')
        self.palette = [self.hex2rgb(f'#{c}') for c in hexs]
        self.n = len(self.palette)

    def __call__(self, i, bgr=False):
        c = self.palette[int(i) % self.n]
        return (c[2], c[1], c[0]) if bgr else c

    @staticmethod
    def hex2rgb(h):  # rgb order (PIL)
        return tuple(int(h[1 + i:1 + i + 2], 16) for i in (0, 2, 4))    

class Video_Buffer:
    def __init__(self, pipe="video1", appsink_name="video_sink", resolution=(640,480)):
        self._frame = None
        self.connection_status = True  # RTSP 연결 상태를 추적하는 변수
        self.video_source = f'rtspsrc location=rtsp://{pipe} latency=10 buffer-mode=0 protocols=tcp'
        # self.video_codec = '! application/x-rtp, encoding-name=(string)H264, payload=96 ! rtph264depay ! h264parse '
        self.video_codec = '! rtph264depay ! h264parse '  # 'application/x-rtp' 생략
        # self.video_decode = f'! decodebin ! videorate ! capsfilter name=capsfilter0 caps=video/x-raw,framerate=30/1 ! videoscale ! video/x-raw,width={resolution[0]},height={resolution[1]} ! videoconvert ! video/x-raw,format=(string)BGR ! appsink name={appsink_name} emit-signals=true sync=false max-buffers=3 drop=true'
        # self.video_decode = f'! decodebin ! videorate ! capsfilter name=capsfilter0 caps=video/x-raw,framerate=1/1 ! videoscale ! video/x-raw,width={resolution[0]},height={resolution[1]} ! videoconvert ! video/x-raw,format=(string)BGR ! appsink name={appsink_name} emit-signals=true sync=false max-buffers=3 drop=true'
        # self.video_decode = f'! decodebin ! videorate ! videoscale ! capsfilter name=capsfilter0 caps=video/x-raw,width={resolution[0]},height={resolution[1]},framerate=5/1 ! videoconvert ! video/x-raw,format=(string)BGR ! appsink name={appsink_name} emit-signals=true sync=false max-buffers=3 drop=true'
        # self.video_decode = f'! decodebin ! videorate ! videoscale ! video/x-raw,format=(string)BGR,width={resolution[0]},height={resolution[1]},framerate=5/1 ! videoconvert ! video/x-raw,format=(string)BGR ! appsink name={appsink_name} emit-signals=true sync=false max-buffers=3 drop=true'
        
        self.video_decode = f'! decodebin ! videorate ! video/x-raw,framerate=30/1 ! videoscale ! video/x-raw,width={resolution[0]},height={resolution[1]} ! videoconvert ! video/x-raw,format=(string)BGR ! appsink name={appsink_name} emit-signals=true sync=false max-buffers=3 drop=true'
        # self.video_decode = f'! decodebin ! videorate ! video/x-raw,framerate=30/1,format=(string)BGR ! videoconvert ! appsink name={appsink_name} emit-signals=true sync=false max-buffers=3 drop=true'
        self.video_pipe = None
        self.video_sink = None
        self.appsink_name = appsink_name
        self.run()

    def start_gst(self, config=None):
        if not config:
            config = [
                'videotestsrc ! decodebin',
                f'! videoconvert ! video/x-raw,format=(string)BGR ! appsink name={self.appsink_name}'
            ]

        command = ' '.join(config)
        try:
            self.video_pipe = Gst.parse_launch(command)
        except:
            self.video_pipe = Gst.parse_launch(command)

        self.video_pipe.set_state(Gst.State.PLAYING)
        self.video_sink = self.video_pipe.get_by_name(self.appsink_name)
        
        if not self.video_sink:
            print(f"Failed to get appsink named {self.appsink_name}")
            return
        
        self.video_sink.set_property("emit-signals", True)
        self.video_sink.set_property("sync", False)

    @staticmethod
    def gst_to_opencv(sample):
        buf = sample.get_buffer()
        caps = sample.get_caps()
        array = np.ndarray(
            (
                caps.get_structure(0).get_value('height'),
                caps.get_structure(0).get_value('width'),
                3
            ),
            buffer=buf.extract_dup(0, buf.get_size()), dtype=np.uint8)
        return array

    def get_frame(self):
        return self._frame

    # def frame_available(self):
    #     return self._frame is not None

    def frame_available(self):
        # 연결 상태를 먼저 확인하고, 끊겨있으면 False를 리턴
        if not self.connection_status:
            return False
        return self._frame is not None

    def run(self):
        try:
            self.start_gst(
                [
                    self.video_source,
                    self.video_codec,
                    ' ! queue leaky=downstream max-size-buffers=20 ',
                    self.video_decode
                ]
            )

            if self.video_sink:
                self.video_sink.connect('new-sample', self.callback)

            bus = self.video_pipe.get_bus()
            bus.add_signal_watch()
            bus.connect("message", self.on_message)
        except Exception as e:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            tb = traceback.format_exc()
            print(f"Error occurred at {current_time}: {e}\n{tb}", file=sys.stderr)

    def on_message(self, bus, message):
        t = message.type
        if t == Gst.MessageType.ERROR or t == Gst.MessageType.EOS:
            self.connection_status = False  # 연결 상태를 False로 설정
            print(f"Error or EOS detected. Reconnecting...")

            if self.video_pipe:
                self.video_pipe.set_state(Gst.State.NULL)

            # self.run()  # 파이프라인이 NULL 상태가 된 후에 재시작

    def callback(self, sink):
        try:
            sample = sink.emit('pull-sample')
            if sample is None:
                print("No sample received, returning...")
                return Gst.FlowReturn.ERROR  # 적절한 예외 처리가 이루어져야 함
            
            new_frame = self.gst_to_opencv(sample)
            self._frame = new_frame

        except Exception as e:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            tb = traceback.format_exc()
            print(f"Error in callback at {current_time}: {e}\n{tb}", file=sys.stderr)
            return Gst.FlowReturn.ERROR

        return Gst.FlowReturn.OK

    def change_framerate(self, fps):
        """Change the framerate dynamically using capsfilter."""
        if self.video_pipe:
            # Get the capsfilter element from the pipeline
            capsfilter = self.video_pipe.get_by_name("capsfilter0")
            if capsfilter:
                # Create new caps with the updated framerate
                new_caps = Gst.Caps.from_string(f"video/x-raw,framerate={fps}/1")
                capsfilter.set_property("caps", new_caps)
                # print(f"Framerate changed to {fps} FPS")
            else:
                print("Could not find capsfilter element.")

    def stop(self):
        if self.video_pipe:
            self.video_pipe.set_state(Gst.State.NULL)  # 파이프라인을 중지 상태로 설정
            self.connection_status = False  # 연결 상태를 False로 설정
            self.video_pipe = None
            # print("RTSP stream stopped.")


class Connect_Camera(QThread):
    # Signal emitted when a new image or a new frame is ready.
    ImageUpdated = Signal(QImage)
    doubleClicked = Signal()

    def __init__(self, pipe, host, port, camera_name, viewer, plot_bbox = True, plot_label = True,  roi_thickness = 1, ai_active = False) -> None:
        super(Connect_Camera, self).__init__()
        # Declare and initialize instance variables.
        self.pipe = pipe
        self.__thread_active = True
        self.disconnect_cnt = 0
        self.__thread_pause = False
        self.camera_connect_flag = False
        # self.camera_num = camera_num
        self.camera_name = camera_name

        self.ai_active = ai_active

        self.viewer = viewer

        self.host = host
        self.port = port

        self.color = Colors()

        self.back_url = f"http://{self.host}:{self.port}/get-camera-info"

        self.roi_thickness = roi_thickness

        self.plot_bbox = plot_bbox
        self.plot_label = plot_label

    def mouseDoubleClickEvent(self, event):
        self.doubleClicked.emit()  # 더블 클릭 시 시그널 발생

    def run(self) -> None:
            self.cap = Video_Buffer(pipe=self.pipe, resolution=(640,480))
            session = requests.Session()

            # While the thread is active.
            while self.__thread_active:
                if self.cap.frame_available() and not self.__thread_pause:
                    self.camera_connect_flag = True
                    self.frame_ori = self.cap.get_frame()
                    # If frame is read correctly.
                    self.frame = cv2.resize(self.frame_ori, dsize=(self.viewer.width(), self.viewer.height()))

                    if self.ai_active and  (self.plot_bbox or self.plot_label):
                        try:
                            receive_data = session.get(self.back_url, json={"msg" : self.camera_name}).json()

                            if receive_data[self.camera_name]:
                                self.frame = plot_detect_info(img = self.frame, detect_info = receive_data[self.camera_name], roi_thickness = self.roi_thickness, plot_bbox = self.plot_bbox, plot_label = self.plot_label)
                        except:
                            pass                
                    self.disconnect_cnt = 0
                    height, width, channels = self.frame.shape
                    bytes_per_line = width * channels
                    cv_rgb_image = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)

                    qt_rgb_image = QImage(cv_rgb_image.data, width, height, bytes_per_line, QImage.Format_RGB888)

                    self.ImageUpdated.emit(qt_rgb_image)

                    time.sleep(0.01)

                else:
                    self.camera_connect_flag = False


            self.cap.stop()
            self.quit()

    def stop(self) -> None:
        self.__thread_active = False
        self.wait()

    def pause(self) -> None:
        self.__thread_pause = True

    def unpause(self) -> None:
        self.__thread_pause = False

class Connect_Camera_Group(QThread):
    ImageUpdated = Signal(str, QImage)  # 카메라 이름과 함께 이미지를 보냄
    doubleClicked = Signal()

    def __init__(self, cameras, host, port, viewers, viewers_widget, settings) -> None:
        super(Connect_Camera_Group, self).__init__()
        self.cameras = cameras
        self.__thread_active = True
        self.__thread_pause = False
        self.host = host
        self.port = port
        self.viewers = viewers
        self.viewers_widget = viewers_widget
        self.settings = settings
        self.camera_connect_flag = {}

    def run(self) -> None:
        sessions = {camera_name: requests.Session() for camera_name in self.cameras}
        self.caps = {camera_name: Video_Buffer(pipe=camera_info['pipe'], resolution=(640,480)) for camera_name, camera_info in self.cameras.items()}

        while self.__thread_active:
            for camera_name, camera_info in self.cameras.items():
                if self.caps[camera_name].frame_available() and not self.__thread_pause:
                    self.camera_connect_flag[camera_name] = True

                    frame_ori = self.caps[camera_name].get_frame()
                    # frame = cv2.resize(frame_ori, dsize=(self.viewers[camera_name].width(), self.viewers[camera_name].height()))
                    frame = cv2.resize(frame_ori, dsize=(self.viewers_widget.width()//4 - 5, self.viewers_widget.height()//4 - 5))

                    if camera_info["ai_active"] and (self.settings["plot_bbox"] or self.settings["plot_label"]):
                        try:
                            receive_data = sessions[camera_name].get(camera_info['back_url'], json={"msg": camera_name}).json()
                            if receive_data[camera_name]:
                                frame = plot_detect_info(img=frame, detect_info=receive_data[camera_name],
                                                        roi_thickness=camera_info["roi_thickness"],
                                                        plot_bbox=self.settings["plot_bbox"],
                                                        plot_label=self.settings["plot_label"])
                        except requests.RequestException as e:
                            print(f"Network error occurred while fetching data for {camera_name}: {e}")
                            
 
                    height, width, channels = frame.shape
                    bytes_per_line = width * channels
                    cv_rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    qt_rgb_image = QImage(cv_rgb_image.data, width, height, bytes_per_line, QImage.Format_RGB888)

                    self.ImageUpdated.emit(camera_name, qt_rgb_image)
                
                else:
                    self.camera_connect_flag["camera_name"] = False

            time.sleep(0.01)
            # time.sleep(1)
                

        for cap in self.caps.values():
            cap.stop()
            del cap
        for session in sessions.values():
            session.close()
    
        self.quit()

    def stop(self) -> None:
        self.__thread_active = False
        for cap in self.caps.values():
            cap.stop()
            del cap

        self.wait()
        self.quit()

class Connect_Playback(QThread):
    # Signal emitted when a new image or a new frame is ready.
    ImageUpdated = Signal(QImage)

    def __init__(self, url, output_size = (360, 216), play_fps = 30, roi_thickness = 1) -> None:
        super(Connect_Playback, self).__init__()
        # Declare and initialize instance variables.
        self.url = url
        self.__thread_active = True
        self.fps = 0
        self.disconnect_cnt = 0

        self.output_size = output_size
        self.play_fps = int(play_fps)

        self.roi_thickness = roi_thickness

    def run(self) -> None:
        frame_num = 0

        while self.__thread_active:
            bytes_data = b''  # 스트리밍 데이터 저장할 바이트 버퍼

            for chunk in self.url.iter_content(chunk_size=1024):
                bytes_data += chunk

                # JPEG 이미지의 시작과 끝을 찾습니다.
                a = bytes_data.find(b'\xff\xd8')
                b = bytes_data.find(b'\xff\xd9')

                if a != -1 and b != -1:
                    jpg = bytes_data[a:b+2]
                    bytes_data = bytes_data[b+2:]

                    frame = cv2.resize(cv2.imdecode(np.frombuffer(jpg, dtype=np.uint8), cv2.IMREAD_COLOR), dsize=self.output_size)
                    # frame = cv2.resize(self.jpeg.decode(np.frombuffer(jpg, dtype=np.uint8), cv2.IMREAD_COLOR), dsize=self.output_size)

                    height, width, channels = frame.shape
                    # Calculate the number of bytes per line.
                    bytes_per_line = width * channels
                    self.ImageUpdated.emit(QImage(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB).data, width, height, bytes_per_line, QImage.Format_RGB888))
                    frame_num += 1

                    if not self.__thread_active:
                        break
                        
                    time.sleep(1/self.play_fps)
                    
            else:
                self.stop()
                break

    def stop(self) -> None:
        self.__thread_active = False
        self.wait()

class Plot_Camera_Viewer(QLabel):
    clicked = Signal(QPoint)  # 사용자가 클릭한 위치를 전달하는 시그널

    def __init__(self, parent=None):
        super().__init__(parent)
        self.point_list = []
        self.non_active_point_list = []
        # self.setMinimumSize(1, 1)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.clicked.emit(event.pos())  # 클릭 위치를 emit

        if event.button() == Qt.RightButton:
            self.clicked.emit(QPoint(-1, -1))  # 클릭 위치를 emit

    def set_point(self, point_list, img_size = None):
        # self.point_list = [QPoint(int(img_size[0] * point[0]), int(img_size[1] * point[1])) for point in point_list]  # QPoint 객체로 변환
        self.point_list = []
        for point in point_list:
            self.point_list.append([point[0], point[1]])
        
        self.update()

    def set_gray_point(self, non_active_point_list, img_size = None):
        self.non_active_point_list = []
        for point_list in non_active_point_list:
            non_point_list = []

            for point in point_list:
                non_point_list.append([point[0], point[1]])

            self.non_active_point_list.append(non_point_list)

            # self.non_active_point_list.append([QPoint(int(img_size[0] * point[0]), int(img_size[1] * point[1])) for point in point_list]  )
            # self.non_active_point_list.append([[point[0], point[1]] for point in point_list])
                                  
        self.update()

    def paintEvent(self, event):
        super().paintEvent(event)

        gray_painter = QPainter(self)
        gray_pen = QPen(QColor(QColor(84,84,84)))
        
        gray_pen.setWidth(5)  # 펜의 두께 설정
        gray_painter.setPen(gray_pen)

        fillColor = QColor(84,84,84,127)
        brush = QBrush(fillColor)
        gray_painter.setBrush(brush)

        for gray_point_list in self.non_active_point_list:
            if len(gray_point_list) > 2:
                gray_point_list = [QPoint(int(self.width() * point[0]), int(self.height() * point[1])) for point in gray_point_list]  # QPoint 객체로 변환
                gray_polygon = QPolygon(gray_point_list)
                gray_painter.drawPolygon(gray_polygon)
                # gray_painter.drawPolygon([x * self.width(), y * self.height()])  # 제공된 좌표에 점을 그림


        painter = QPainter(self)
        pen = QPen(QColor(QColor(83,195,2)))
        
        pen.setWidth(5)  # 펜의 두께 설정
        painter.setPen(pen)

        fillColor = QColor(129,215,66,127)
        brush = QBrush(fillColor)
        painter.setBrush(brush)

        for point in self.point_list:
            painter.drawPoint(int(point[0] * self.width()), int(point[1] * self.height()))  # 제공된 좌표에 점을 그림
        if len(self.point_list) > 2:
            point_list = [QPoint(int(self.width() * point[0]), int(self.height() * point[1])) for point in self.point_list]  # QPoint 객체로 변환
            polygon = QPolygon(point_list)
            painter.drawPolygon(polygon)

    def reset(self):
        self.point_list = []
        self.non_active_point_list = []

        self.update()

    def reset_green_area(self):
        self.point_list = []

        self.update()

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.update()


class FadeOutWindow(QWidget):
    def __init__(self, parent=None, msg="None"):
        super().__init__(parent=parent)
        self.msg = msg
        self.initUI()
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.startFadeOut()

    def initUI(self):
        self.setWindowTitle('Information')
        self.setFixedSize(381, 61)  # 고정 크기
        self.setStyleSheet("background-color: rgba(255, 255, 255, 255); border-radius: 10px;")
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        self.info_label = QLabel(self.msg, self)
        self.info_label.setObjectName(u"info_label")
        # self.info_label.setGeometry(QRect(0, 0, 381, 61))

        self.info_label.setStyleSheet("background-color: rgb(53, 132, 228); border-radius: 10px; color: white; font-size: 14px;")
        self.info_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.info_label)
        self.setLayout(layout)

        # self.setWindowFlags(Qt.FramelessWindowHint | Qt.Window | Qt.WindowStaysOnTopHint)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Window)

    def startFadeOut(self):
        QTimer.singleShot(1000, self.fadeOut)

    def fadeOut(self):
        self.anim = QPropertyAnimation(self, b'windowOpacity')
        self.anim.setDuration(1500)
        self.anim.setStartValue(1)
        self.anim.setEndValue(0)
        self.anim.setEasingCurve(QEasingCurve.InOutQuad)
        self.anim.finished.connect(self.close)
        self.anim.start()

class FadeOutInWindow(QWidget):
    def __init__(self, parent=None, camera_num = 0, data = {}, window_num = 0):
        super().__init__(parent=parent)
        now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        # print(data)
        self.window_title = f"Alarm {window_num}"
        if len(data):
            self.msg = f"{camera_num}번 카메라 : {data[0]} \n {data[2]}"

        self.initUI()
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.toggleFade()

    def initUI(self):
        self.setWindowTitle(self.window_title)
        self.setFixedSize(381, 61)  # 고정 크기
        self.setStyleSheet("background-color: rgba(255, 255, 255, 255); border-radius: 10px;")
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        self.info_label = QLabel(self.msg, self)
        self.info_label.setObjectName(u"info_label")
        self.info_label.setStyleSheet("background-color: rgb(53, 132, 228); border-radius: 10px; color: white; font-size: 14px;")
        # self.info_label.setStyleSheet("background-color: rgb(19, 193, 13); border-radius: 10px; color: white; font-size: 14px;")
        
        self.info_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.info_label)
        self.setLayout(layout)

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Window | Qt.WindowStaysOnTopHint)


    def toggleFade(self):
        self.anim = QPropertyAnimation(self, b'windowOpacity')
        self.anim.setDuration(1500)
        self.anim.setStartValue(1)
        self.anim.setEndValue(0)
        self.anim.setEasingCurve(QEasingCurve.InOutQuad)
        self.anim.finished.connect(self.fadeIn)
        self.anim.start()

    def fadeIn(self):
        self.anim.setStartValue(0)
        self.anim.setEndValue(1)
        self.anim.finished.connect(self.toggleFade)
        self.anim.start()

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.close()  # 창을 닫습니다.

class Livepage_view(QLabel):
    doubleClicked = Signal(QLabel)
    def __init__(self, base_viewer, camera_num, camera_name, stackedWidget):
        super().__init__(base_viewer)
        # self.setGeometry(QRect(0, 0, 292, 188))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(stackedWidget.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)

        self.setMinimumSize(QSize(200, 121))
        self.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.setStyleSheet(u"border: 1px solid rgb(119, 118, 123);\n"
                            "color: rgb(255, 255, 255);")
        self.setPixmap(QPixmap(u":/newPrefix/images/ico_video_off.svg"))
        self.setScaledContents(False)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.click_count = 0
        self.camera_num = camera_num
        self.camera_name = camera_name

        self.aspect_ratio = 1.5
        self.base_viewer = base_viewer

    def mouseDoubleClickEvent(self, event):
        # 더블클릭 이벤트 발생 시, 시그널을 emit
        if event.button() == Qt.LeftButton:
            self.click_count += 1
            self.doubleClicked.emit(self)
            print(self.camera_num)
            print(self.camera_name)

    # def resizeEvent(self, event):
    #     parent = self.base_viewer
    #     if parent:
    #         new_width = parent.width()
    #         new_height = int(new_width / self.aspect_ratio)
    #         if new_height > parent.height():
    #             new_height = parent.height()
    #             new_width = int(new_height * self.aspect_ratio)
    #         self.setFixedSize(new_width, new_height)
    #     super().resizeEvent(event)  # 부모 클래스의 resizeEvent 호출

def plot_one_box(x, img, color=None, label=None, bbox=None, line_thickness=3):
    # Plots one bounding box on image img
    tl = line_thickness or round(0.002 * (img.shape[0] + img.shape[1]) / 2) + 1  # line/font thickness
    color = color or [random.randint(0, 255) for _ in range(3)]
    c1, c2 = (int(x[0]), int(x[1])), (int(x[2]), int(x[3]))
    if bbox:
        cv2.rectangle(img, c1, c2, color, thickness=tl, lineType=cv2.LINE_AA)
    if label:
        tf = max(tl - 1, 1)  # font thickness
        t_size = cv2.getTextSize(label, 0, fontScale=tl / 3, thickness=tf)[0]
        c2 = c1[0] + t_size[0], c1[1] - t_size[1] - 3
        cv2.rectangle(img, c1, c2, color, -1, cv2.LINE_AA)  # filled
        cv2.putText(img, label, (c1[0], c1[1] - 2), 0, tl / 3, [225, 255, 255], thickness=tf, lineType=cv2.LINE_AA)

def draw_roi(points, image, color, thickness=1, is_closed=True):
    """ 이미지에 관심 영역(ROI)를 그립니다. """
    cv2.polylines(image, [np.int32(points)], is_closed, color, thickness)

def TF_detect_area(detect_info, img_size):
    TF_detect_area_list = []
    if len(detect_info):
        if isinstance(detect_info[0], list): 
            for item in detect_info:
                # 새로운 리스트의 첫 번째 요소는 기존 문자열 그대로 유지
                label = item[0]
                coordinates = item[1:]

                # 좌표에 대한 변환 수행
                transformed_coordinates = [[int(x[0] * img_size[0]), int(x[1] * img_size[1])] for x in coordinates]
                
                # 변환된 좌표를 포함하는 새로운 리스트 생성
                TF_detect_area_list.append([label] + transformed_coordinates)

        elif isinstance(detect_info[0], str): 
            label = detect_info[0]
            coordinates = detect_info[1:]

            # 좌표에 대한 변환 수행
            transformed_coordinates = [[int(x[0] * img_size[0]), int(x[1] * img_size[1])] for x in coordinates]
            
            # 변환된 좌표를 포함하는 새로운 리스트 생성
            TF_detect_area_list.append([label] + transformed_coordinates)

    return TF_detect_area_list

def TF_bbox(bbox, ori_imsz=(640, 360), target_imsz=(1920, 1080)):
    # 원본 이미지와 목표 이미지의 크기 비율 계산
    width_ratio = target_imsz[0] / ori_imsz[0]
    height_ratio = target_imsz[1] / ori_imsz[1]
    
    # 변환된 바운딩 박스를 저장할 리스트 초기화
    TF_boxes = []
    
    # 각 바운딩 박스에 대해 좌표 변환 수행
    for box in bbox:
        if len(box) == 8:
            x1, y1, x2, y2, id, conf, cls, ind  = box  # 좌표 추출
            # 좌표를 int(새로운 이미지 크기에 맞게 조정
            new_x1 = int(x1 * width_ratio)
            new_y1 = int(y1 * height_ratio)
            new_x2 = int(x2 * width_ratio)
            new_y2 = int(y2 * height_ratio)
        
            # 변환된 좌표와 기존 정보를 합쳐 새로운 리스트 생성
            TF_boxes.append([new_x1, new_y1, new_x2, new_y2, id, conf, cls, ind])
        
        elif len(box) == 6:
            x1, y1, x2, y2, conf, cls, = box  # 좌표 추출

            # 좌표를 int(새로운 이미지 크기에 맞게 조정
            new_x1 = int(x1 * width_ratio)
            new_y1 = int(y1 * height_ratio)
            new_x2 = int(x2 * width_ratio)
            new_y2 = int(y2 * height_ratio)
            
            # 변환된 좌표와 기존 정보를 합쳐 새로운 리스트 생성
            TF_boxes.append([new_x1, new_y1, new_x2, new_y2, conf, cls])

        if len(box) == 9:
                x1, y1, x2, y2, id, conf, cls, ind, status = box  # 좌표 추출
                # 좌표를 int(새로운 이미지 크기에 맞게 조정
                new_x1 = int(x1 * width_ratio)
                new_y1 = int(y1 * height_ratio)
                new_x2 = int(x2 * width_ratio)
                new_y2 = int(y2 * height_ratio)
            
                # 변환된 좌표와 기존 정보를 합쳐 새로운 리스트 생성
                TF_boxes.append([new_x1, new_y1, new_x2, new_y2, id, conf, cls, ind, status])
        
    return TF_boxes

def plot_detect_info(img, detect_info, line_thickness = 1 , roi_thickness = 1, plot_bbox = True, plot_label = True):
    color = Colors()
    ROI_color_dict = {"Loitering": [53, 225, 225], "Intrusion": [35, 28, 255], "Fire": [33, 145, 237],
                                "Fight": [255, 0, 127], "Falldown": [230, 255, 121]}

    names = { 0 : "person", 1 : "fire"}

    person_bbox = TF_bbox(detect_info["person_bbox"], ori_imsz=(640, 480), target_imsz=(img.shape[1], img.shape[0]))
    non_person_bbox = TF_bbox(detect_info["non_person_bbox"], ori_imsz=(640, 480), target_imsz=(img.shape[1], img.shape[0]))
    for person_box in person_bbox:
        if len(person_box) == 9:
            x1, y1, x2, y2, id, conf, cls, ind, status = person_box
            xyxy = np.array([x1, y1, x2, y2],dtype="int") # float64 to int
            conf = conf
            id = int(id)
            cls = int(cls)

            if plot_label:
                label = f'{id} {names[cls]} {conf:.2f}'
            else:
                label = False

            if status == 1 :
                bbox_color = (0,75,150)

            elif status == 2 :
                bbox_color = (60,20,220)

            elif status == 0 :
                bbox_color = (0,150,95)

            else:
                bbox_color = color(int(cls))

            plot_one_box(xyxy, img, label=label, bbox = plot_bbox, color=bbox_color, line_thickness=line_thickness) # 박스 그리기

        elif len(person_box) == 8:
            x1, y1, x2, y2, id, conf, cls, ind = person_box
            xyxy = np.array([x1, y1, x2, y2],dtype="int") # float64 to int
            conf = conf
            id = int(id)
            cls = int(cls)

            if plot_label:
                label = f'{id} {names[cls]} {conf:.2f}'
            else:
                label = False

            bbox_color = color(int(cls))

            plot_one_box(xyxy, img, label=label, bbox = plot_bbox, color=bbox_color, line_thickness=line_thickness) # 박스 그리기

    for (x1, y1, x2, y2, conf, cls) in non_person_bbox: #fire bbox
        xyxy = np.array([x1, y1, x2, y2],dtype="int") # float64 to int
        conf = conf
        cls = int(cls)

        bbox_color = (4,19,190)
        if plot_label:
            label = f'{names[cls]} {conf:.2f}'
        else:
            label = False

        plot_one_box(xyxy, img, label=label, bbox = plot_bbox, color=bbox_color, line_thickness=line_thickness) # 박스 그리기

    TF_roi_info = TF_detect_area(detect_info["ROI_ori"], img_size=(img.shape[1], img.shape[0]))
    for roi_info in TF_roi_info:
        draw_roi(points = roi_info[1:], 
                    image = img,
                    color = ROI_color_dict[roi_info[0]], 
                    thickness = roi_thickness, 
                    is_closed = True)

    return img

def load_info(host, port, file_name):
    data = {"msg" : {"file_name" : file_name}}

    # receive_data = socket_communication(self.HOST, self.PORT, cmd, on_data_received)
    url = f'http://{host}:{port}/load_info'
    # receive_data = requests.post(url, json=data).json()
    try:
        receive_data = requests.post(url, json=data).json()
    except Exception as e:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        tb = traceback.format_exc()
        print(f"Error occurred at {current_time}: {e}\n{tb}", file=sys.stderr)
        print(requests.post(url, json=data))
    if receive_data["success"] == True:
        return receive_data["data"]

    else: raise(f"{file_name} 파일을 찾을 수 없습니다.")

def save_info(host, port, file_name, info):
    data = {"msg" : {"file_name" : file_name, "info" : info}}

    # receive_data = socket_communication(self.HOST, self.PORT, cmd, on_data_received)
    url = f'http://{host}:{port}/save_info'
    # receive_data = requests.post(url, json=data).json()

    receive_data = requests.post(url, json=data).json()

def Eng2kor(eng):
    if eng == "Intrusion": return "침입"
    elif eng == "Loitering": return "배회"
    elif eng == "Falldown": return "쓰러짐"
    elif eng == "Fire": return "방화"
    elif eng == "Fight": return "싸움"


def Kor2eng(kor):
    if kor == "침입" : return "Intrusion"
    elif kor == "배회": return "Loitering"
    elif kor == "쓰러짐": return "Falldown"
    elif kor == "방화": return "Fire"
    elif kor == "싸움": return "Fight"


    # gmail_sender = 'diddytpq5@gmail.com'
    # gmail_passwd = 'zqpx escp ebme yjyf'
    # TO = 'ysyang@microsystems.co.kr'

def send_email_alarm(camera_worker_list, alarm, mail_sender, mail_passwd, mail_receive, camera_num):
    camera_num = str(camera_num)

    for worker in camera_worker_list:
        if camera_num == worker.camera_num:
            img = worker.img_buffer[-1]
            detect_info = worker.event_buffer[-1]

            img = plot_detect_info(img, detect_info, line_thickness = 1 , roi_thickness = 1)

    # datetime 모듈로 기존 날짜 문자열 파싱 (현재 양식에 따라)
    parsed_date = datetime.strptime(alarm[2], "%d/%m/%Y %H:%M:%S")

    # 원하는 형식으로 날짜 출력 (년도/월/일 형식)
    new_date_str = parsed_date.strftime("%Y/%m/%d %H:%M:%S")

    # SMTP 서버 설정
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(mail_sender, mail_passwd)

    # 이메일 메시지 구성
    msg = MIMEMultipart()
    msg['From'] = mail_sender
    msg['To'] = mail_receive
    msg['Subject'] = Header(f'[MS-AI]{camera_num} 번 카메라 {Eng2kor(alarm[0])} 알람', 'utf-8').encode()

    image_path = os.path.join(ROOT, "front", "ui", "images", "logo_bck.png")

    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')

    encoded_image = encoded_string


    html = f"""\
    <html>
    <head>
    </head>
    <body>
        <img src="data:image/jpeg;base64,{encoded_image}" alt="microsystems" style="width: 200px; height: auto;">
        <table role="presentation" width="400" style="border-collapse: collapse; margin: 10px 0;">
            <tr>
                <td style="border-bottom: 2px solid #BDBDBD; padding: 0; line-height: 0;">
                    &nbsp; <!-- Non-breaking space to ensure the line is visible -->
                </td>
            </tr>
        </table>
        <h1 style="font-size: 32px; font-weight: bold; padding-left: 100px;">{Eng2kor(alarm[0])}알람 발생</h1>
        <table role="presentation" width="400" style="border-collapse: collapse; margin: 10px 0;">
            <tr>
                <td style="border-bottom: 2px solid #BDBDBD; padding: 0; line-height: 0;">
                    &nbsp; <!-- Non-breaking space to ensure the line is visible -->
                </td>
            </tr>
        </table>
        <p><strong style="color: #008299; padding-left: 10px;">알람 카메라:</strong> 카메라 {camera_num} 번</p>
        <p><strong style="color: #008299; padding-left: 10px;">알람 시간:</strong> {new_date_str}</p>
        <p><strong style="color: #008299; padding-left: 10px;">알람 종류:</strong> {Eng2kor(alarm[0])}</p>
    </body>
    </html>
    """


    part = MIMEText(html, 'html', 'utf-8')
    msg.attach(part)

    # 이미지 첨부
    if img is not None:
        _, img_encoded = cv2.imencode('.jpg', img)  # OpenCV 이미지를 JPEG 형식으로 인코딩
        img_attachment = MIMEImage(img_encoded.tobytes(), name=f'camera_{camera_num}.jpg')
        msg.attach(img_attachment)

    # 이메일 전송 시도
    try:
        server.sendmail(mail_sender, [mail_receive], msg.as_string())
        # print('email sent')
    except Exception as e:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        tb = traceback.format_exc()
        print(f"Error occurred at {current_time}: {e}\n{tb}", file=sys.stderr)
        print('error sending mail:', e)

    server.quit()



# def get_datetime_from_path(path):
#     parts = path.split('/')  # 경로를 '/'로 분할
#     date_time_str = parts[-1].split('_')[0]  # 파일 이름에서 날짜와 시간 부분 추출 ('17:07:24')
#     date_str = parts[1]  # 날짜 부분 추출 ('24.04.25')
#     # 날짜와 시간 문자열 결합
#     full_datetime_str = f"{date_str} {date_time_str}"
#     # datetime 객체로 변환
#     return datetime.strptime(full_datetime_str, "%d.%m.%y %H.%M.%S")


def get_datetime_from_path(path):
    parts = path.split('/')  # 경로를 '/'로 분할
    date_time_str = parts[-1].split('_')[0]  # 파일 이름에서 시간 부분 추출 ('08.54.48')
    date_str = parts[-3]  # 날짜 부분 추출 ('24.04.29')
    # 날짜와 시간 문자열 결합
    full_datetime_str = f"{date_str} {date_time_str}"
    # datetime 객체로 변환
    return datetime.strptime(full_datetime_str, "%y.%m.%d %H.%M.%S")