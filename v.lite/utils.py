import sys
import os
import gi

gi.require_version('Gst', '1.0')
from gi.repository import Gst
Gst.init(None)

from PySide6.QtWidgets import (QLabel, QSizePolicy, QVBoxLayout, QWidget, QApplication, QMainWindow, QMenu)
from PySide6.QtGui import QImage, QPainter, QPen, QColor, QPolygon, QBrush, QMouseEvent, QPixmap, QAction, QDesktopServices
from PySide6.QtCore import Qt, QThread, Signal, QPoint, QObject, QEvent, QTimer, QPropertyAnimation, QEasingCurve, QRect, QSize, QUrl
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

import webbrowser
from cryptography.fernet import Fernet
import traceback
import subprocess

COLOR = {
    0: (60, 20, 220),   # Crimson - person
    1: (113, 179, 60),  # Medium Sea Green - bicycle
    2: (180, 130, 70),  # Steel Blue - car
    3: (0, 140, 255),   # Dark Orange - motorcycle
    4: (219, 112, 147), # Medium Purple - bus
    5: (204, 209, 72),  # Medium Turquoise - truck
    6: (147, 20, 255)   # Deep Pink - fire
}

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

        self.info_label.setStyleSheet("background-color: rgb(30, 195, 55); border-radius: 10px; color: white; font-size: 14px;")
        self.info_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.info_label)
        self.setLayout(layout)

        # self.setWindowFlags(Qt.FramelessWindowHint | Qt.Window | Qt.WindowStaysOnTopHint)
        # self.setWindowFlags(Qt.FramelessWindowHint | Qt.Window)
        # self.fadeout_window.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)


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


class Video_Buffer:
    def __init__(self, pipe, appsink_name="video_sink123", resolution=(640,480), chg_fps_mode = False, fps = 30):
        self._frame = None
        self.connection_status = True  # RTSP 연결 상태를 추적하는 변수
        print(pipe)
        # self.video_source = f'rtspsrc location={pipe} latency=1000 buffer-mode=0 protocols=tcp'
        # self.video_source = f'rtspsrc location={pipe} latency=200 drop-on-latency=true'

        
        # self.video_codec = '! rtph264depay ! h264parse '
        # self.video_decode = f'! decodebin ! videoconvert ! video/x-raw,format=(string)BGR ! appsink name={appsink_name} emit-signals=true sync=false max-buffers=1 drop=true'

        self.video_pipe = None
        self.video_sink = None
        self.appsink_name = appsink_name

        self.video_source = f'rtspsrc location={pipe} latency=200 drop-on-latency=true ! rtph264depay ! h264parse ! avdec_h264 ! queue leaky=downstream max-size-buffers=1 ! videoconvert ! video/x-raw,format=BGR ! appsink name={appsink_name} emit-signals=true sync=false max-buffers=1 drop=true'

        self.run()


    def start_gst(self, config=None):
        """ Start gstreamer pipeline and sink
        Pipeline description list e.g:
            [
                'videotestsrc ! decodebin', \
                '! videoconvert ! video/x-raw,format=(string)BGR ! videoconvert',
                '! appsink'
            ]
        Args:
            config (list, optional): Gstreamer pileline description list
        """

        if not config:
            config = \
                [
                    'videotestsrc ! decodebin',
                    '! videoconvert ! video/x-raw,format=(string)BGR ! videoconvert',
                    '! appsink'
                ]

        command = ' '.join(config)
        self.video_pipe = Gst.parse_launch(command)
        self.video_pipe.set_state(Gst.State.PLAYING)
        self.video_sink = self.video_pipe.get_by_name(self.appsink_name)

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

    def read(self):
        if self.frame_available():
            return self._frame
        else:
            return np.zeros((640, 480, 3), dtype=np.uint8)
        
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
                    # self.video_codec,
                    # ' ! queue leaky=downstream max-size-buffers=100 ',
                    # self.video_decode,
                ])

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

    def release(self):
        if self.video_pipe:
            self.video_pipe.set_state(Gst.State.NULL)  # 파이프라인을 중지 상태로 설정
            self.connection_status = False  # 연결 상태를 False로 설정
            self.video_pipe = None
            # print("RTSP stream stopped.")

class Plot_Camera_Viewer(QLabel):
    clicked = Signal(QPoint)  # 사용자가 클릭한 위치를 전달하는 시그널

    def __init__(self, parent=None):
        super().__init__(parent)
        self.point_list = []
        self.non_active_point_list = []
        self.zoom_factor = 1.0  # 초기 확대 배율
        self.offset = QPoint(0, 0)  # 확대/축소의 오프셋을 저장
        self.setScaledContents(True)  # QLabel이 이미지 크기에 맞게 조정됨

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


class Connect_Camera(QThread):
    # Signal emitted when a new image or a new frame is ready.
    ImageUpdated = Signal(QImage)
    doubleClicked = Signal()

    def __init__(self, pipe) -> None:
        super(Connect_Camera, self).__init__()
        # Declare and initialize instance variables.
        self.pipe = pipe
        self.fps = 30
        self.camera_name = "main"

        self.host = "127.0.0.1"
        self.port = "65432"

        self.back_url = f"http://{self.host}:{self.port}/get-camera-info"

        self.plot_bbox = True
        self.plot_label = True
        self.plot_roi = False

        self.__thread_active = True

        self.roi_thickness = 3

        # self.cap = cv2.VideoCapture(self.pipe)
        self.cap = Video_Buffer(pipe=self.pipe, resolution=(1920,1080))

    def mouseDoubleClickEvent(self, event):
        self.doubleClicked.emit()  # 더블 클릭 시 시그널 발생

    def run(self) -> None:

        session = requests.Session()

        while self.__thread_active:
            t0 = time.time()

            # _, frame = self.cap.read()
            # _, frame = self.cap.read()
            # _, frame = self.cap.read()
            
            frame = self.cap.read()
            self.frame = np.array(frame)

            # if self.ai_active and  (self.plot_bbox or self.plot_label or self.plot_roi):
            if True:
                try:
                    receive_data = session.get(self.back_url, json={"msg" : self.camera_name}).json()

                    if receive_data[self.camera_name]:
                        line_thickness = 3 if self.frame.shape[1] == 1920 else 1
                        self.frame = plot_detect_info(img = self.frame, detect_info = receive_data[self.camera_name], line_thickness = line_thickness, roi_thickness = self.roi_thickness, plot_bbox = self.plot_bbox, plot_label = self.plot_label, plot_roi = self.plot_roi)
                except:
                    pass         

            self.disconnect_cnt = 0
            height, width, channels = self.frame.shape
            bytes_per_line = width * channels
            cv_rgb_image = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)

            qt_rgb_image = QImage(cv_rgb_image.data, width, height, bytes_per_line, QImage.Format_RGB888)

            self.ImageUpdated.emit(qt_rgb_image)

            # time.sleep(0.033)
            sleep_time = max(0, (1 / self.fps) - (time.time() - t0))
            time.sleep(sleep_time)

        # self.cap.stop()
        self.cap.release()

        self.quit()

    def stop(self) -> None:
        self.__thread_active = False
        self.wait()

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

def plot_detect_info(img, detect_info, line_thickness = 1 , roi_thickness = 1, plot_bbox = True, plot_label = True, plot_roi = True):
    ROI_color_dict = {"Loitering": [53, 225, 225], "Intrusion": [35, 28, 255], "Fire": [33, 145, 237],
                                "Fight": [255, 0, 127], "Falldown": [230, 255, 121]}

    # names = { 0 : "person", 1 : "fire"}
    names = { 0 : "person", 1 : "bicycle", 2 : "car", 3 : "motorcycle", 4 : "bus", 5 : "truck", 6 : "fire"}


    # person_bbox = TF_bbox(detect_info["person_bbox"], ori_imsz=(1280, 720), target_imsz=(img.shape[1], img.shape[0]))
    # non_person_bbox = TF_bbox(detect_info["non_person_bbox"], ori_imsz=(1280, 720), target_imsz=(img.shape[1], img.shape[0]))

    person_bbox = TF_bbox(detect_info["person_bbox"], ori_imsz=(1920, 1080), target_imsz=(img.shape[1], img.shape[0]))
    non_person_bbox = TF_bbox(detect_info["non_person_bbox"], ori_imsz=(1920, 1080), target_imsz=(img.shape[1], img.shape[0]))
    for person_box in person_bbox:
        if len(person_box) == 9:
            x1, y1, x2, y2, id, conf, cls, ind, status = person_box
            xyxy = np.array([x1, y1, x2, y2],dtype="int") # float64 to int
            conf = conf
            id = int(id)
            cls = int(cls)

            if plot_label:
                # label = f'{id} {names[cls]} {conf:.2f}'
                label = f'{names[cls]} {100 * conf:.1f}%'

            else:
                label = False

            if status == 1 :
                bbox_color = (0,75,150)

            elif status == 2 :
                bbox_color = (60,20,220)

            elif status == 0 :
                bbox_color = (0,150,95)

            else:
                bbox_color = COLOR[int(cls)]
                # bbox_color = COLOR(int(cls))

            plot_one_box(xyxy, img, label=label, bbox = plot_bbox, color=bbox_color, line_thickness=line_thickness) # 박스 그리기

        elif len(person_box) == 8:
            x1, y1, x2, y2, id, conf, cls, ind = person_box
            xyxy = np.array([x1, y1, x2, y2],dtype="int") # float64 to int
            conf = conf
            id = int(id)
            cls = int(cls)

            if plot_label:
                # label = f'{id} {names[cls]} {conf:.2f}'
                label = f'{names[cls]} {conf:.2f}'

            else:
                label = False

            # bbox_color = COLOR(int(cls))
            bbox_color = COLOR[int(cls)]

            plot_one_box(xyxy, img, label=label, bbox = plot_bbox, color=bbox_color, line_thickness=line_thickness) # 박스 그리기

    for (x1, y1, x2, y2, conf, cls) in non_person_bbox: #fire bbox
        xyxy = np.array([x1, y1, x2, y2],dtype="int") # float64 to int
        conf = conf
        cls = int(cls)

        # bbox_color = (4,19,190)
        bbox_color = COLOR[int(cls)]
        if plot_label:
            label = f'{names[cls]} {conf:.2f}'
        else:
            label = False

        plot_one_box(xyxy, img, label=label, bbox = plot_bbox, color=bbox_color, line_thickness=line_thickness) # 박스 그리기

    if plot_roi:
        TF_roi_info = TF_detect_area(detect_info["ROI_ori"], img_size=(img.shape[1], img.shape[0]))
        for roi_info in TF_roi_info:
            draw_roi(points = roi_info[1:], 
                        image = img,
                        color = ROI_color_dict[roi_info[0]], 
                        thickness = roi_thickness, 
                        is_closed = True)

    return img

def save_info(host, port, file_name, info):
    data = {"msg" : {"file_name" : file_name, "info" : info}}

    # receive_data = socket_communication(self.HOST, self.PORT, cmd, on_data_received)
    url = f'http://{host}:{port}/save_info'
    # receive_data = requests.post(url, json=data).json()

    receive_data = requests.post(url, json=data).json()

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


def find_in_first_column(parent, text):
    # 첫 번째 열에서 특정 문자를 포함한 행의 인덱스를 반환
    for row in range(parent.ui_main.camera_list_table.rowCount()):
        item = parent.ui_main.camera_list_table.item(row, 2)  # 첫 번째 열의 항목 가져오기
        if item is not None and text in item.text():
            return row
    return None

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

def set_button_style(parent, active_button):
    # 모든 버튼을 기본 스타일로 설정
    default_style = "color: white; border: 1px solid rgba(191, 64, 64, 0); background-color: rgba(191, 64, 64, 0);"
    active_style = "color: green; border: 1px solid rgba(191, 64, 64, 0); background-color: rgba(191, 64, 64, 0);"
    
    buttons = {
        'camera': parent.ui_main.camera_bnt,
        'setting': parent.ui_main.setting_bnt,
        'admin': parent.ui_main.admin_bnt,
        'search': parent.ui_main.search_bnt

    }
    
    for key, button in buttons.items():
        button.setStyleSheet(active_style if key == active_button else default_style)