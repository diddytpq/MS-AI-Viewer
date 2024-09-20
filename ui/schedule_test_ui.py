# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'schedule_test.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QHBoxLayout,
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import ms_ai_img_rc
import ms_ai_img_rc
import ms_ai_img_rc
import ms_ai_img_rc
import ms_ai_img_rc

class Ui_schedule_window(object):
    def setupUi(self, schedule_window):
        if not schedule_window.objectName():
            schedule_window.setObjectName(u"schedule_window")
        schedule_window.setWindowModality(Qt.WindowModality.WindowModal)
        schedule_window.resize(1252, 703)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(schedule_window.sizePolicy().hasHeightForWidth())
        schedule_window.setSizePolicy(sizePolicy)
        schedule_window.setMinimumSize(QSize(1252, 703))
        schedule_window.setMaximumSize(QSize(1252, 703))
        schedule_window.setStyleSheet(u"background-color: rgb(20, 20, 20);\n"
"\n"
"")
        self.verticalLayout_23 = QVBoxLayout(schedule_window)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(1)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.top_logo_2 = QLabel(schedule_window)
        self.top_logo_2.setObjectName(u"top_logo_2")
        self.top_logo_2.setMinimumSize(QSize(1, 1))
        self.top_logo_2.setMaximumSize(QSize(177, 33))
        font = QFont()
        font.setFamilies([u"Sans"])
        self.top_logo_2.setFont(font)
        self.top_logo_2.setPixmap(QPixmap(u":/newPrefix/ui/images/logo.png"))
        self.top_logo_2.setScaledContents(True)

        self.horizontalLayout.addWidget(self.top_logo_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.schedule_move_oneshot_bnt = QPushButton(schedule_window)
        self.schedule_move_oneshot_bnt.setObjectName(u"schedule_move_oneshot_bnt")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.schedule_move_oneshot_bnt.sizePolicy().hasHeightForWidth())
        self.schedule_move_oneshot_bnt.setSizePolicy(sizePolicy1)
        self.schedule_move_oneshot_bnt.setMinimumSize(QSize(79, 22))
        self.schedule_move_oneshot_bnt.setMaximumSize(QSize(120, 30))
        font1 = QFont()
        font1.setFamilies([u"Sans"])
        font1.setPointSize(10)
        self.schedule_move_oneshot_bnt.setFont(font1)
        self.schedule_move_oneshot_bnt.setCursor(QCursor(Qt.PointingHandCursor))
        self.schedule_move_oneshot_bnt.setStyleSheet(u"background-color: rgb(36, 39, 44);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"\n"
"")

        self.horizontalLayout.addWidget(self.schedule_move_oneshot_bnt)


        self.verticalLayout_20.addLayout(self.horizontalLayout)

        self.stackedWidget = QStackedWidget(schedule_window)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_18 = QVBoxLayout(self.page_3)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.camera_view_name_1 = QLabel(self.page_3)
        self.camera_view_name_1.setObjectName(u"camera_view_name_1")
        sizePolicy.setHeightForWidth(self.camera_view_name_1.sizePolicy().hasHeightForWidth())
        self.camera_view_name_1.setSizePolicy(sizePolicy)
        self.camera_view_name_1.setMaximumSize(QSize(722, 20))
        font2 = QFont()
        font2.setFamilies([u"NanumSquareRound"])
        font2.setPointSize(11)
        font2.setBold(False)
        self.camera_view_name_1.setFont(font2)
        self.camera_view_name_1.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 170);\n"
"border: 1px solid rgb(119, 118, 123);")
        self.camera_view_name_1.setMargin(0)
        self.camera_view_name_1.setIndent(15)

        self.verticalLayout_2.addWidget(self.camera_view_name_1)

        self.camera_view_1 = QLabel(self.page_3)
        self.camera_view_1.setObjectName(u"camera_view_1")
        sizePolicy1.setHeightForWidth(self.camera_view_1.sizePolicy().hasHeightForWidth())
        self.camera_view_1.setSizePolicy(sizePolicy1)
        font3 = QFont()
        font3.setFamilies([u"NanumBarunGothic"])
        font3.setPointSize(16)
        self.camera_view_1.setFont(font3)
        self.camera_view_1.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.camera_view_1.setStyleSheet(u"border: 1px solid rgb(119, 118, 123);\n"
"color: rgb(255, 255, 255);")
        self.camera_view_1.setPixmap(QPixmap(u":/newPrefix/images/ico_video_off.svg"))
        self.camera_view_1.setScaledContents(False)
        self.camera_view_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.camera_view_1)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.camera_view_name_2 = QLabel(self.page_3)
        self.camera_view_name_2.setObjectName(u"camera_view_name_2")
        sizePolicy.setHeightForWidth(self.camera_view_name_2.sizePolicy().hasHeightForWidth())
        self.camera_view_name_2.setSizePolicy(sizePolicy)
        self.camera_view_name_2.setMaximumSize(QSize(722, 20))
        self.camera_view_name_2.setFont(font2)
        self.camera_view_name_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 170);\n"
"border: 1px solid rgb(119, 118, 123);")
        self.camera_view_name_2.setMargin(0)
        self.camera_view_name_2.setIndent(15)

        self.verticalLayout_3.addWidget(self.camera_view_name_2)

        self.camera_view_2 = QLabel(self.page_3)
        self.camera_view_2.setObjectName(u"camera_view_2")
        sizePolicy1.setHeightForWidth(self.camera_view_2.sizePolicy().hasHeightForWidth())
        self.camera_view_2.setSizePolicy(sizePolicy1)
        self.camera_view_2.setFont(font3)
        self.camera_view_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.camera_view_2.setStyleSheet(u"border: 1px solid rgb(119, 118, 123);\n"
"color: rgb(255, 255, 255);")
        self.camera_view_2.setPixmap(QPixmap(u":/newPrefix/images/ico_video_off.svg"))
        self.camera_view_2.setScaledContents(False)
        self.camera_view_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.camera_view_2)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.camera_view_name_3 = QLabel(self.page_3)
        self.camera_view_name_3.setObjectName(u"camera_view_name_3")
        sizePolicy.setHeightForWidth(self.camera_view_name_3.sizePolicy().hasHeightForWidth())
        self.camera_view_name_3.setSizePolicy(sizePolicy)
        self.camera_view_name_3.setMaximumSize(QSize(722, 20))
        self.camera_view_name_3.setFont(font2)
        self.camera_view_name_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 170);\n"
"border: 1px solid rgb(119, 118, 123);")
        self.camera_view_name_3.setMargin(0)
        self.camera_view_name_3.setIndent(15)

        self.verticalLayout_4.addWidget(self.camera_view_name_3)

        self.camera_view_3 = QLabel(self.page_3)
        self.camera_view_3.setObjectName(u"camera_view_3")
        sizePolicy1.setHeightForWidth(self.camera_view_3.sizePolicy().hasHeightForWidth())
        self.camera_view_3.setSizePolicy(sizePolicy1)
        self.camera_view_3.setFont(font3)
        self.camera_view_3.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.camera_view_3.setStyleSheet(u"border: 1px solid rgb(119, 118, 123);\n"
"color: rgb(255, 255, 255);")
        self.camera_view_3.setPixmap(QPixmap(u":/newPrefix/images/ico_video_off.svg"))
        self.camera_view_3.setScaledContents(False)
        self.camera_view_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.camera_view_3)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.camera_view_name_4 = QLabel(self.page_3)
        self.camera_view_name_4.setObjectName(u"camera_view_name_4")
        sizePolicy.setHeightForWidth(self.camera_view_name_4.sizePolicy().hasHeightForWidth())
        self.camera_view_name_4.setSizePolicy(sizePolicy)
        self.camera_view_name_4.setMaximumSize(QSize(722, 20))
        self.camera_view_name_4.setFont(font2)
        self.camera_view_name_4.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 170);\n"
"border: 1px solid rgb(119, 118, 123);")
        self.camera_view_name_4.setMargin(0)
        self.camera_view_name_4.setIndent(15)

        self.verticalLayout_5.addWidget(self.camera_view_name_4)

        self.camera_view_4 = QLabel(self.page_3)
        self.camera_view_4.setObjectName(u"camera_view_4")
        sizePolicy1.setHeightForWidth(self.camera_view_4.sizePolicy().hasHeightForWidth())
        self.camera_view_4.setSizePolicy(sizePolicy1)
        self.camera_view_4.setFont(font3)
        self.camera_view_4.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.camera_view_4.setStyleSheet(u"border: 1px solid rgb(119, 118, 123);\n"
"color: rgb(255, 255, 255);")
        self.camera_view_4.setPixmap(QPixmap(u":/newPrefix/images/ico_video_off.svg"))
        self.camera_view_4.setScaledContents(False)
        self.camera_view_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.camera_view_4)


        self.horizontalLayout_2.addLayout(self.verticalLayout_5)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.camera_view_name_5 = QLabel(self.page_3)
        self.camera_view_name_5.setObjectName(u"camera_view_name_5")
        sizePolicy.setHeightForWidth(self.camera_view_name_5.sizePolicy().hasHeightForWidth())
        self.camera_view_name_5.setSizePolicy(sizePolicy)
        self.camera_view_name_5.setMaximumSize(QSize(722, 20))
        self.camera_view_name_5.setFont(font2)
        self.camera_view_name_5.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 170);\n"
"border: 1px solid rgb(119, 118, 123);")
        self.camera_view_name_5.setMargin(0)
        self.camera_view_name_5.setIndent(15)

        self.verticalLayout_6.addWidget(self.camera_view_name_5)

        self.camera_view_5 = QLabel(self.page_3)
        self.camera_view_5.setObjectName(u"camera_view_5")
        sizePolicy1.setHeightForWidth(self.camera_view_5.sizePolicy().hasHeightForWidth())
        self.camera_view_5.setSizePolicy(sizePolicy1)
        self.camera_view_5.setFont(font3)
        self.camera_view_5.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.camera_view_5.setStyleSheet(u"border: 1px solid rgb(119, 118, 123);\n"
"color: rgb(255, 255, 255);")
        self.camera_view_5.setPixmap(QPixmap(u":/newPrefix/images/ico_video_off.svg"))
        self.camera_view_5.setScaledContents(False)
        self.camera_view_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.camera_view_5)


        self.horizontalLayout_3.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.camera_view_name_6 = QLabel(self.page_3)
        self.camera_view_name_6.setObjectName(u"camera_view_name_6")
        sizePolicy.setHeightForWidth(self.camera_view_name_6.sizePolicy().hasHeightForWidth())
        self.camera_view_name_6.setSizePolicy(sizePolicy)
        self.camera_view_name_6.setMaximumSize(QSize(722, 20))
        self.camera_view_name_6.setFont(font2)
        self.camera_view_name_6.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 170);\n"
"border: 1px solid rgb(119, 118, 123);")
        self.camera_view_name_6.setMargin(0)
        self.camera_view_name_6.setIndent(15)

        self.verticalLayout_7.addWidget(self.camera_view_name_6)

        self.camera_view_6 = QLabel(self.page_3)
        self.camera_view_6.setObjectName(u"camera_view_6")
        sizePolicy1.setHeightForWidth(self.camera_view_6.sizePolicy().hasHeightForWidth())
        self.camera_view_6.setSizePolicy(sizePolicy1)
        self.camera_view_6.setFont(font3)
        self.camera_view_6.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.camera_view_6.setStyleSheet(u"border: 1px solid rgb(119, 118, 123);\n"
"color: rgb(255, 255, 255);")
        self.camera_view_6.setPixmap(QPixmap(u":/newPrefix/images/ico_video_off.svg"))
        self.camera_view_6.setScaledContents(False)
        self.camera_view_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.camera_view_6)


        self.horizontalLayout_3.addLayout(self.verticalLayout_7)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.camera_view_name_7 = QLabel(self.page_3)
        self.camera_view_name_7.setObjectName(u"camera_view_name_7")
        sizePolicy.setHeightForWidth(self.camera_view_name_7.sizePolicy().hasHeightForWidth())
        self.camera_view_name_7.setSizePolicy(sizePolicy)
        self.camera_view_name_7.setMaximumSize(QSize(722, 20))
        self.camera_view_name_7.setFont(font2)
        self.camera_view_name_7.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 170);\n"
"border: 1px solid rgb(119, 118, 123);")
        self.camera_view_name_7.setMargin(0)
        self.camera_view_name_7.setIndent(15)

        self.verticalLayout_8.addWidget(self.camera_view_name_7)

        self.camera_view_7 = QLabel(self.page_3)
        self.camera_view_7.setObjectName(u"camera_view_7")
        sizePolicy1.setHeightForWidth(self.camera_view_7.sizePolicy().hasHeightForWidth())
        self.camera_view_7.setSizePolicy(sizePolicy1)
        self.camera_view_7.setFont(font3)
        self.camera_view_7.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.camera_view_7.setStyleSheet(u"border: 1px solid rgb(119, 118, 123);\n"
"color: rgb(255, 255, 255);")
        self.camera_view_7.setPixmap(QPixmap(u":/newPrefix/images/ico_video_off.svg"))
        self.camera_view_7.setScaledContents(False)
        self.camera_view_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.camera_view_7)


        self.horizontalLayout_3.addLayout(self.verticalLayout_8)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.camera_view_name_8 = QLabel(self.page_3)
        self.camera_view_name_8.setObjectName(u"camera_view_name_8")
        sizePolicy.setHeightForWidth(self.camera_view_name_8.sizePolicy().hasHeightForWidth())
        self.camera_view_name_8.setSizePolicy(sizePolicy)
        self.camera_view_name_8.setMaximumSize(QSize(722, 20))
        self.camera_view_name_8.setFont(font2)
        self.camera_view_name_8.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 170);\n"
"border: 1px solid rgb(119, 118, 123);")
        self.camera_view_name_8.setMargin(0)
        self.camera_view_name_8.setIndent(15)

        self.verticalLayout_9.addWidget(self.camera_view_name_8)

        self.camera_view_8 = QLabel(self.page_3)
        self.camera_view_8.setObjectName(u"camera_view_8")
        sizePolicy1.setHeightForWidth(self.camera_view_8.sizePolicy().hasHeightForWidth())
        self.camera_view_8.setSizePolicy(sizePolicy1)
        self.camera_view_8.setFont(font3)
        self.camera_view_8.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.camera_view_8.setStyleSheet(u"border: 1px solid rgb(119, 118, 123);\n"
"color: rgb(255, 255, 255);")
        self.camera_view_8.setPixmap(QPixmap(u":/newPrefix/images/ico_video_off.svg"))
        self.camera_view_8.setScaledContents(False)
        self.camera_view_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.camera_view_8)


        self.horizontalLayout_3.addLayout(self.verticalLayout_9)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.camera_view_name_9 = QLabel(self.page_3)
        self.camera_view_name_9.setObjectName(u"camera_view_name_9")
        sizePolicy.setHeightForWidth(self.camera_view_name_9.sizePolicy().hasHeightForWidth())
        self.camera_view_name_9.setSizePolicy(sizePolicy)
        self.camera_view_name_9.setMaximumSize(QSize(722, 20))
        self.camera_view_name_9.setFont(font2)
        self.camera_view_name_9.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 170);\n"
"border: 1px solid rgb(119, 118, 123);")
        self.camera_view_name_9.setMargin(0)
        self.camera_view_name_9.setIndent(15)

        self.verticalLayout_10.addWidget(self.camera_view_name_9)

        self.camera_view_9 = QLabel(self.page_3)
        self.camera_view_9.setObjectName(u"camera_view_9")
        sizePolicy1.setHeightForWidth(self.camera_view_9.sizePolicy().hasHeightForWidth())
        self.camera_view_9.setSizePolicy(sizePolicy1)
        self.camera_view_9.setFont(font3)
        self.camera_view_9.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.camera_view_9.setStyleSheet(u"border: 1px solid rgb(119, 118, 123);\n"
"color: rgb(255, 255, 255);")
        self.camera_view_9.setPixmap(QPixmap(u":/newPrefix/images/ico_video_off.svg"))
        self.camera_view_9.setScaledContents(False)
        self.camera_view_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_10.addWidget(self.camera_view_9)


        self.horizontalLayout_4.addLayout(self.verticalLayout_10)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.camera_view_name_10 = QLabel(self.page_3)
        self.camera_view_name_10.setObjectName(u"camera_view_name_10")
        sizePolicy.setHeightForWidth(self.camera_view_name_10.sizePolicy().hasHeightForWidth())
        self.camera_view_name_10.setSizePolicy(sizePolicy)
        self.camera_view_name_10.setMaximumSize(QSize(722, 20))
        self.camera_view_name_10.setFont(font2)
        self.camera_view_name_10.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 170);\n"
"border: 1px solid rgb(119, 118, 123);")
        self.camera_view_name_10.setMargin(0)
        self.camera_view_name_10.setIndent(15)

        self.verticalLayout_11.addWidget(self.camera_view_name_10)

        self.camera_view_10 = QLabel(self.page_3)
        self.camera_view_10.setObjectName(u"camera_view_10")
        sizePolicy1.setHeightForWidth(self.camera_view_10.sizePolicy().hasHeightForWidth())
        self.camera_view_10.setSizePolicy(sizePolicy1)
        self.camera_view_10.setFont(font3)
        self.camera_view_10.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.camera_view_10.setStyleSheet(u"border: 1px solid rgb(119, 118, 123);\n"
"color: rgb(255, 255, 255);")
        self.camera_view_10.setPixmap(QPixmap(u":/newPrefix/images/ico_video_off.svg"))
        self.camera_view_10.setScaledContents(False)
        self.camera_view_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_11.addWidget(self.camera_view_10)


        self.horizontalLayout_4.addLayout(self.verticalLayout_11)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.camera_view_name_11 = QLabel(self.page_3)
        self.camera_view_name_11.setObjectName(u"camera_view_name_11")
        sizePolicy.setHeightForWidth(self.camera_view_name_11.sizePolicy().hasHeightForWidth())
        self.camera_view_name_11.setSizePolicy(sizePolicy)
        self.camera_view_name_11.setMaximumSize(QSize(722, 20))
        self.camera_view_name_11.setFont(font2)
        self.camera_view_name_11.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 170);\n"
"border: 1px solid rgb(119, 118, 123);")
        self.camera_view_name_11.setMargin(0)
        self.camera_view_name_11.setIndent(15)

        self.verticalLayout_12.addWidget(self.camera_view_name_11)

        self.camera_view_11 = QLabel(self.page_3)
        self.camera_view_11.setObjectName(u"camera_view_11")
        sizePolicy1.setHeightForWidth(self.camera_view_11.sizePolicy().hasHeightForWidth())
        self.camera_view_11.setSizePolicy(sizePolicy1)
        self.camera_view_11.setFont(font3)
        self.camera_view_11.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.camera_view_11.setStyleSheet(u"border: 1px solid rgb(119, 118, 123);\n"
"color: rgb(255, 255, 255);")
        self.camera_view_11.setPixmap(QPixmap(u":/newPrefix/images/ico_video_off.svg"))
        self.camera_view_11.setScaledContents(False)
        self.camera_view_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_12.addWidget(self.camera_view_11)


        self.horizontalLayout_4.addLayout(self.verticalLayout_12)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.camera_view_name_12 = QLabel(self.page_3)
        self.camera_view_name_12.setObjectName(u"camera_view_name_12")
        sizePolicy.setHeightForWidth(self.camera_view_name_12.sizePolicy().hasHeightForWidth())
        self.camera_view_name_12.setSizePolicy(sizePolicy)
        self.camera_view_name_12.setMaximumSize(QSize(722, 20))
        self.camera_view_name_12.setFont(font2)
        self.camera_view_name_12.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 170);\n"
"border: 1px solid rgb(119, 118, 123);")
        self.camera_view_name_12.setMargin(0)
        self.camera_view_name_12.setIndent(15)

        self.verticalLayout_13.addWidget(self.camera_view_name_12)

        self.camera_view_12 = QLabel(self.page_3)
        self.camera_view_12.setObjectName(u"camera_view_12")
        sizePolicy1.setHeightForWidth(self.camera_view_12.sizePolicy().hasHeightForWidth())
        self.camera_view_12.setSizePolicy(sizePolicy1)
        self.camera_view_12.setFont(font3)
        self.camera_view_12.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.camera_view_12.setStyleSheet(u"border: 1px solid rgb(119, 118, 123);\n"
"color: rgb(255, 255, 255);")
        self.camera_view_12.setPixmap(QPixmap(u":/newPrefix/images/ico_video_off.svg"))
        self.camera_view_12.setScaledContents(False)
        self.camera_view_12.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_13.addWidget(self.camera_view_12)


        self.horizontalLayout_4.addLayout(self.verticalLayout_13)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.camera_view_name_13 = QLabel(self.page_3)
        self.camera_view_name_13.setObjectName(u"camera_view_name_13")
        sizePolicy.setHeightForWidth(self.camera_view_name_13.sizePolicy().hasHeightForWidth())
        self.camera_view_name_13.setSizePolicy(sizePolicy)
        self.camera_view_name_13.setMaximumSize(QSize(722, 20))
        self.camera_view_name_13.setFont(font2)
        self.camera_view_name_13.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 170);\n"
"border: 1px solid rgb(119, 118, 123);")
        self.camera_view_name_13.setMargin(0)
        self.camera_view_name_13.setIndent(15)

        self.verticalLayout_14.addWidget(self.camera_view_name_13)

        self.camera_view_13 = QLabel(self.page_3)
        self.camera_view_13.setObjectName(u"camera_view_13")
        sizePolicy1.setHeightForWidth(self.camera_view_13.sizePolicy().hasHeightForWidth())
        self.camera_view_13.setSizePolicy(sizePolicy1)
        self.camera_view_13.setFont(font3)
        self.camera_view_13.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.camera_view_13.setStyleSheet(u"border: 1px solid rgb(119, 118, 123);\n"
"color: rgb(255, 255, 255);")
        self.camera_view_13.setPixmap(QPixmap(u":/newPrefix/images/ico_video_off.svg"))
        self.camera_view_13.setScaledContents(False)
        self.camera_view_13.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_14.addWidget(self.camera_view_13)


        self.horizontalLayout_5.addLayout(self.verticalLayout_14)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.camera_view_name_14 = QLabel(self.page_3)
        self.camera_view_name_14.setObjectName(u"camera_view_name_14")
        sizePolicy.setHeightForWidth(self.camera_view_name_14.sizePolicy().hasHeightForWidth())
        self.camera_view_name_14.setSizePolicy(sizePolicy)
        self.camera_view_name_14.setMaximumSize(QSize(722, 20))
        self.camera_view_name_14.setFont(font2)
        self.camera_view_name_14.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 170);\n"
"border: 1px solid rgb(119, 118, 123);")
        self.camera_view_name_14.setMargin(0)
        self.camera_view_name_14.setIndent(15)

        self.verticalLayout_15.addWidget(self.camera_view_name_14)

        self.camera_view_14 = QLabel(self.page_3)
        self.camera_view_14.setObjectName(u"camera_view_14")
        sizePolicy1.setHeightForWidth(self.camera_view_14.sizePolicy().hasHeightForWidth())
        self.camera_view_14.setSizePolicy(sizePolicy1)
        self.camera_view_14.setFont(font3)
        self.camera_view_14.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.camera_view_14.setStyleSheet(u"border: 1px solid rgb(119, 118, 123);\n"
"color: rgb(255, 255, 255);")
        self.camera_view_14.setPixmap(QPixmap(u":/newPrefix/images/ico_video_off.svg"))
        self.camera_view_14.setScaledContents(False)
        self.camera_view_14.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_15.addWidget(self.camera_view_14)


        self.horizontalLayout_5.addLayout(self.verticalLayout_15)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.camera_view_name_15 = QLabel(self.page_3)
        self.camera_view_name_15.setObjectName(u"camera_view_name_15")
        sizePolicy.setHeightForWidth(self.camera_view_name_15.sizePolicy().hasHeightForWidth())
        self.camera_view_name_15.setSizePolicy(sizePolicy)
        self.camera_view_name_15.setMaximumSize(QSize(722, 20))
        self.camera_view_name_15.setFont(font2)
        self.camera_view_name_15.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 170);\n"
"border: 1px solid rgb(119, 118, 123);")
        self.camera_view_name_15.setMargin(0)
        self.camera_view_name_15.setIndent(15)

        self.verticalLayout_16.addWidget(self.camera_view_name_15)

        self.camera_view_15 = QLabel(self.page_3)
        self.camera_view_15.setObjectName(u"camera_view_15")
        sizePolicy1.setHeightForWidth(self.camera_view_15.sizePolicy().hasHeightForWidth())
        self.camera_view_15.setSizePolicy(sizePolicy1)
        self.camera_view_15.setFont(font3)
        self.camera_view_15.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.camera_view_15.setStyleSheet(u"border: 1px solid rgb(119, 118, 123);\n"
"color: rgb(255, 255, 255);")
        self.camera_view_15.setPixmap(QPixmap(u":/newPrefix/images/ico_video_off.svg"))
        self.camera_view_15.setScaledContents(False)
        self.camera_view_15.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_16.addWidget(self.camera_view_15)


        self.horizontalLayout_5.addLayout(self.verticalLayout_16)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.camera_view_name_16 = QLabel(self.page_3)
        self.camera_view_name_16.setObjectName(u"camera_view_name_16")
        sizePolicy.setHeightForWidth(self.camera_view_name_16.sizePolicy().hasHeightForWidth())
        self.camera_view_name_16.setSizePolicy(sizePolicy)
        self.camera_view_name_16.setMaximumSize(QSize(722, 20))
        self.camera_view_name_16.setFont(font2)
        self.camera_view_name_16.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 170);\n"
"border: 1px solid rgb(119, 118, 123);")
        self.camera_view_name_16.setMargin(0)
        self.camera_view_name_16.setIndent(15)

        self.verticalLayout_17.addWidget(self.camera_view_name_16)

        self.camera_view_16 = QLabel(self.page_3)
        self.camera_view_16.setObjectName(u"camera_view_16")
        sizePolicy1.setHeightForWidth(self.camera_view_16.sizePolicy().hasHeightForWidth())
        self.camera_view_16.setSizePolicy(sizePolicy1)
        self.camera_view_16.setFont(font3)
        self.camera_view_16.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.camera_view_16.setStyleSheet(u"border: 1px solid rgb(119, 118, 123);\n"
"color: rgb(255, 255, 255);")
        self.camera_view_16.setPixmap(QPixmap(u":/newPrefix/images/ico_video_off.svg"))
        self.camera_view_16.setScaledContents(False)
        self.camera_view_16.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_17.addWidget(self.camera_view_16)


        self.horizontalLayout_5.addLayout(self.verticalLayout_17)


        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.verticalLayout_18.addLayout(self.verticalLayout)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_19 = QVBoxLayout(self.page_4)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.search_viewer = QLabel(self.page_4)
        self.search_viewer.setObjectName(u"search_viewer")
        self.search_viewer.setMinimumSize(QSize(640, 480))
        self.search_viewer.setFont(font)
        self.search_viewer.setStyleSheet(u"border: 1px solid rgb(119, 118, 123);\n"
"border-radius: 10px ;")
        self.search_viewer.setPixmap(QPixmap(u":/newPrefix/ui/images/logo.png"))
        self.search_viewer.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_19.addWidget(self.search_viewer)

        self.stackedWidget.addWidget(self.page_4)

        self.verticalLayout_20.addWidget(self.stackedWidget)


        self.horizontalLayout_10.addLayout(self.verticalLayout_20)

        self.widget = QWidget(schedule_window)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(383, 709))
        self.verticalLayout_21 = QVBoxLayout(self.widget)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.event_label = QLabel(self.widget)
        self.event_label.setObjectName(u"event_label")
        self.event_label.setMaximumSize(QSize(52, 16777215))
        font4 = QFont()
        font4.setFamilies([u"Sans"])
        font4.setPointSize(12)
        self.event_label.setFont(font4)
        self.event_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(191, 64, 64, 0);")
        self.event_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_6.addWidget(self.event_label)

        self.event_box = QComboBox(self.widget)
        self.event_box.addItem("")
        self.event_box.addItem("")
        self.event_box.addItem("")
        self.event_box.addItem("")
        self.event_box.addItem("")
        self.event_box.setObjectName(u"event_box")
        font5 = QFont()
        font5.setFamilies([u"Sans"])
        font5.setPointSize(10)
        font5.setBold(False)
        self.event_box.setFont(font5)
        self.event_box.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(13, 16, 23);\n"
"selection-background-color: rgb(53, 132, 228);\n"
"")
        self.event_box.setMinimumContentsLength(0)

        self.horizontalLayout_6.addWidget(self.event_box)


        self.horizontalLayout_8.addLayout(self.horizontalLayout_6)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.schedule_all_remove_bnt = QPushButton(self.widget)
        self.schedule_all_remove_bnt.setObjectName(u"schedule_all_remove_bnt")
        self.schedule_all_remove_bnt.setMinimumSize(QSize(61, 31))
        self.schedule_all_remove_bnt.setMaximumSize(QSize(61, 31))
        self.schedule_all_remove_bnt.setFont(font1)
        self.schedule_all_remove_bnt.setCursor(QCursor(Qt.PointingHandCursor))
        self.schedule_all_remove_bnt.setStyleSheet(u"background-color: rgb(36, 39, 44);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"\n"
"")

        self.horizontalLayout_7.addWidget(self.schedule_all_remove_bnt)

        self.schedule_apply_bnt = QPushButton(self.widget)
        self.schedule_apply_bnt.setObjectName(u"schedule_apply_bnt")
        self.schedule_apply_bnt.setMinimumSize(QSize(61, 31))
        self.schedule_apply_bnt.setMaximumSize(QSize(61, 31))
        self.schedule_apply_bnt.setFont(font1)
        self.schedule_apply_bnt.setCursor(QCursor(Qt.PointingHandCursor))
        self.schedule_apply_bnt.setStyleSheet(u"background-color: rgb(30, 195, 55);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"\n"
"")

        self.horizontalLayout_7.addWidget(self.schedule_apply_bnt)

        self.schedule_close_bnt = QPushButton(self.widget)
        self.schedule_close_bnt.setObjectName(u"schedule_close_bnt")
        self.schedule_close_bnt.setMinimumSize(QSize(61, 31))
        self.schedule_close_bnt.setMaximumSize(QSize(61, 31))
        self.schedule_close_bnt.setFont(font1)
        self.schedule_close_bnt.setCursor(QCursor(Qt.PointingHandCursor))
        self.schedule_close_bnt.setStyleSheet(u"background-color: rgb(237, 51, 59);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"\n"
"")

        self.horizontalLayout_7.addWidget(self.schedule_close_bnt)


        self.horizontalLayout_8.addLayout(self.horizontalLayout_7)


        self.verticalLayout_22.addLayout(self.horizontalLayout_8)

        self.detect_time_table_widget = QWidget(self.widget)
        self.detect_time_table_widget.setObjectName(u"detect_time_table_widget")
        sizePolicy1.setHeightForWidth(self.detect_time_table_widget.sizePolicy().hasHeightForWidth())
        self.detect_time_table_widget.setSizePolicy(sizePolicy1)
        self.detect_time_table_widget.setMinimumSize(QSize(365, 622))
        self.detect_time_table_widget.setMaximumSize(QSize(365, 622))
        self.detect_time_table_widget.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(32,39,49);\n"
"border-radius: 10px;\n"
"\n"
"\n"
"")
        self.horizontalLayout_9 = QHBoxLayout(self.detect_time_table_widget)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.schedule_time_table = QTableWidget(self.detect_time_table_widget)
        if (self.schedule_time_table.columnCount() < 7):
            self.schedule_time_table.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.schedule_time_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.schedule_time_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.schedule_time_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.schedule_time_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.schedule_time_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.schedule_time_table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.schedule_time_table.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        if (self.schedule_time_table.rowCount() < 24):
            self.schedule_time_table.setRowCount(24)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.schedule_time_table.setVerticalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.schedule_time_table.setVerticalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.schedule_time_table.setVerticalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.schedule_time_table.setVerticalHeaderItem(3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.schedule_time_table.setVerticalHeaderItem(4, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.schedule_time_table.setVerticalHeaderItem(5, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.schedule_time_table.setVerticalHeaderItem(6, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.schedule_time_table.setVerticalHeaderItem(7, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.schedule_time_table.setVerticalHeaderItem(8, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.schedule_time_table.setVerticalHeaderItem(9, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.schedule_time_table.setVerticalHeaderItem(10, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.schedule_time_table.setVerticalHeaderItem(11, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.schedule_time_table.setVerticalHeaderItem(12, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.schedule_time_table.setVerticalHeaderItem(13, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.schedule_time_table.setVerticalHeaderItem(14, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.schedule_time_table.setVerticalHeaderItem(15, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.schedule_time_table.setVerticalHeaderItem(16, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.schedule_time_table.setVerticalHeaderItem(17, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.schedule_time_table.setVerticalHeaderItem(18, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.schedule_time_table.setVerticalHeaderItem(19, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.schedule_time_table.setVerticalHeaderItem(20, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.schedule_time_table.setVerticalHeaderItem(21, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.schedule_time_table.setVerticalHeaderItem(22, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.schedule_time_table.setVerticalHeaderItem(23, __qtablewidgetitem30)
        self.schedule_time_table.setObjectName(u"schedule_time_table")
        self.schedule_time_table.setMinimumSize(QSize(0, 575))
        self.schedule_time_table.setMaximumSize(QSize(9999, 9999))
        self.schedule_time_table.setFont(font)
        self.schedule_time_table.setStyleSheet(u"QTableView {\n"
"\n"
"gridline-color: rgb(119, 118, 123);\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"        background-color:  rgba(30, 195, 55, 130); /* \ub4dc\ub798\uadf8 \uc2dc \uc120\ud0dd\ub41c \uc140\uc758 \ubc30\uacbd\uc0c9 */\n"
"		border: 1px solid rgba(30, 195, 55, 130);\n"
"        color: white; /* \uc120\ud0dd\ub41c \uc140\uc758 \uae00\uc790 \uc0c9 */\n"
"    }\n"
"    QTableWidget::item:hover {\n"
"        background-color: rgba(209, 209, 209, 30);; /* \ub4dc\ub798\uadf8\ud560 \ub54c \ub9c8\uc6b0\uc2a4\uac00 \uc704\uce58\ud55c \uc140\uc758 \ubc30\uacbd\uc0c9 */\n"
"    }")
        self.schedule_time_table.setProperty("showDropIndicator", True)
        self.schedule_time_table.setDragEnabled(False)
        self.schedule_time_table.setDragDropOverwriteMode(True)
        self.schedule_time_table.setDragDropMode(QAbstractItemView.DragDropMode.NoDragDrop)
        self.schedule_time_table.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)
        self.schedule_time_table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectItems)
        self.schedule_time_table.setGridStyle(Qt.PenStyle.SolidLine)
        self.schedule_time_table.setSortingEnabled(False)
        self.schedule_time_table.setRowCount(24)
        self.schedule_time_table.horizontalHeader().setCascadingSectionResizes(False)
        self.schedule_time_table.horizontalHeader().setMinimumSectionSize(3)
        self.schedule_time_table.horizontalHeader().setDefaultSectionSize(46)
        self.schedule_time_table.horizontalHeader().setProperty("showSortIndicator", False)
        self.schedule_time_table.horizontalHeader().setStretchLastSection(False)
        self.schedule_time_table.verticalHeader().setVisible(True)
        self.schedule_time_table.verticalHeader().setCascadingSectionResizes(False)
        self.schedule_time_table.verticalHeader().setMinimumSectionSize(18)
        self.schedule_time_table.verticalHeader().setDefaultSectionSize(24)
        self.schedule_time_table.verticalHeader().setProperty("showSortIndicator", False)
        self.schedule_time_table.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout_9.addWidget(self.schedule_time_table)


        self.verticalLayout_22.addWidget(self.detect_time_table_widget)


        self.verticalLayout_21.addLayout(self.verticalLayout_22)


        self.horizontalLayout_10.addWidget(self.widget)


        self.verticalLayout_23.addLayout(self.horizontalLayout_10)


        self.retranslateUi(schedule_window)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(schedule_window)
    # setupUi

    def retranslateUi(self, schedule_window):
        schedule_window.setWindowTitle(QCoreApplication.translate("schedule_window", u"camera schedule", None))
        self.top_logo_2.setText("")
        self.schedule_move_oneshot_bnt.setText(QCoreApplication.translate("schedule_window", u"\uc0c1\uc138 \ubcf4\uae30", None))
        self.camera_view_name_1.setText(QCoreApplication.translate("schedule_window", u"\uce74\uba54\ub77c1", None))
        self.camera_view_1.setText("")
        self.camera_view_name_2.setText(QCoreApplication.translate("schedule_window", u"\uce74\uba54\ub77c2", None))
        self.camera_view_2.setText("")
        self.camera_view_name_3.setText(QCoreApplication.translate("schedule_window", u"\uce74\uba54\ub77c3", None))
        self.camera_view_3.setText("")
        self.camera_view_name_4.setText(QCoreApplication.translate("schedule_window", u"\uce74\uba54\ub77c4", None))
        self.camera_view_4.setText("")
        self.camera_view_name_5.setText(QCoreApplication.translate("schedule_window", u"\uce74\uba54\ub77c5", None))
        self.camera_view_5.setText("")
        self.camera_view_name_6.setText(QCoreApplication.translate("schedule_window", u"\uce74\uba54\ub77c6", None))
        self.camera_view_6.setText("")
        self.camera_view_name_7.setText(QCoreApplication.translate("schedule_window", u"\uce74\uba54\ub77c7", None))
        self.camera_view_7.setText("")
        self.camera_view_name_8.setText(QCoreApplication.translate("schedule_window", u"\uce74\uba54\ub77c8", None))
        self.camera_view_8.setText("")
        self.camera_view_name_9.setText(QCoreApplication.translate("schedule_window", u"\uce74\uba54\ub77c9", None))
        self.camera_view_9.setText("")
        self.camera_view_name_10.setText(QCoreApplication.translate("schedule_window", u"\uce74\uba54\ub77c10", None))
        self.camera_view_10.setText("")
        self.camera_view_name_11.setText(QCoreApplication.translate("schedule_window", u"\uce74\uba54\ub77c11", None))
        self.camera_view_11.setText("")
        self.camera_view_name_12.setText(QCoreApplication.translate("schedule_window", u"\uce74\uba54\ub77c12", None))
        self.camera_view_12.setText("")
        self.camera_view_name_13.setText(QCoreApplication.translate("schedule_window", u"\uce74\uba54\ub77c13", None))
        self.camera_view_13.setText("")
        self.camera_view_name_14.setText(QCoreApplication.translate("schedule_window", u"\uce74\uba54\ub77c14", None))
        self.camera_view_14.setText("")
        self.camera_view_name_15.setText(QCoreApplication.translate("schedule_window", u"\uce74\uba54\ub77c15", None))
        self.camera_view_15.setText("")
        self.camera_view_name_16.setText(QCoreApplication.translate("schedule_window", u"\uce74\uba54\ub77c16", None))
        self.camera_view_16.setText("")
        self.search_viewer.setText("")
        self.event_label.setText(QCoreApplication.translate("schedule_window", u"\uc774\ubca4\ud2b8", None))
        self.event_box.setItemText(0, QCoreApplication.translate("schedule_window", u"\uce68\uc785", None))
        self.event_box.setItemText(1, QCoreApplication.translate("schedule_window", u"\ubc30\ud68c", None))
        self.event_box.setItemText(2, QCoreApplication.translate("schedule_window", u"\uc4f0\ub7ec\uc9d0", None))
        self.event_box.setItemText(3, QCoreApplication.translate("schedule_window", u"\uc2f8\uc6c0", None))
        self.event_box.setItemText(4, QCoreApplication.translate("schedule_window", u"\ubc29\ud654", None))

        self.schedule_all_remove_bnt.setText(QCoreApplication.translate("schedule_window", u"\uc804\uccb4 \uc0ad\uc81c", None))
        self.schedule_apply_bnt.setText(QCoreApplication.translate("schedule_window", u"\uc800\uc7a5", None))
        self.schedule_close_bnt.setText(QCoreApplication.translate("schedule_window", u"\ub2eb\uae30", None))
        ___qtablewidgetitem = self.schedule_time_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("schedule_window", u"\uc77c", None));
        ___qtablewidgetitem1 = self.schedule_time_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("schedule_window", u"\uc6d4", None));
        ___qtablewidgetitem2 = self.schedule_time_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("schedule_window", u"\ud654", None));
        ___qtablewidgetitem3 = self.schedule_time_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("schedule_window", u"\uc218", None));
        ___qtablewidgetitem4 = self.schedule_time_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("schedule_window", u"\ubaa9", None));
        ___qtablewidgetitem5 = self.schedule_time_table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("schedule_window", u"\uae08", None));
        ___qtablewidgetitem6 = self.schedule_time_table.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("schedule_window", u"\ud1a0", None));
        ___qtablewidgetitem7 = self.schedule_time_table.verticalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("schedule_window", u"0", None));
        ___qtablewidgetitem8 = self.schedule_time_table.verticalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("schedule_window", u"1", None));
        ___qtablewidgetitem9 = self.schedule_time_table.verticalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("schedule_window", u"2", None));
        ___qtablewidgetitem10 = self.schedule_time_table.verticalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("schedule_window", u"3", None));
        ___qtablewidgetitem11 = self.schedule_time_table.verticalHeaderItem(4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("schedule_window", u"4", None));
        ___qtablewidgetitem12 = self.schedule_time_table.verticalHeaderItem(5)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("schedule_window", u"5", None));
        ___qtablewidgetitem13 = self.schedule_time_table.verticalHeaderItem(6)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("schedule_window", u"6", None));
        ___qtablewidgetitem14 = self.schedule_time_table.verticalHeaderItem(7)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("schedule_window", u"7", None));
        ___qtablewidgetitem15 = self.schedule_time_table.verticalHeaderItem(8)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("schedule_window", u"8", None));
        ___qtablewidgetitem16 = self.schedule_time_table.verticalHeaderItem(9)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("schedule_window", u"9", None));
        ___qtablewidgetitem17 = self.schedule_time_table.verticalHeaderItem(10)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("schedule_window", u"10", None));
        ___qtablewidgetitem18 = self.schedule_time_table.verticalHeaderItem(11)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("schedule_window", u"11", None));
        ___qtablewidgetitem19 = self.schedule_time_table.verticalHeaderItem(12)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("schedule_window", u"12", None));
        ___qtablewidgetitem20 = self.schedule_time_table.verticalHeaderItem(13)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("schedule_window", u"13", None));
        ___qtablewidgetitem21 = self.schedule_time_table.verticalHeaderItem(14)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("schedule_window", u"14", None));
        ___qtablewidgetitem22 = self.schedule_time_table.verticalHeaderItem(15)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("schedule_window", u"15", None));
        ___qtablewidgetitem23 = self.schedule_time_table.verticalHeaderItem(16)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("schedule_window", u"16", None));
        ___qtablewidgetitem24 = self.schedule_time_table.verticalHeaderItem(17)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("schedule_window", u"17", None));
        ___qtablewidgetitem25 = self.schedule_time_table.verticalHeaderItem(18)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("schedule_window", u"18", None));
        ___qtablewidgetitem26 = self.schedule_time_table.verticalHeaderItem(19)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("schedule_window", u"19", None));
        ___qtablewidgetitem27 = self.schedule_time_table.verticalHeaderItem(20)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("schedule_window", u"20", None));
        ___qtablewidgetitem28 = self.schedule_time_table.verticalHeaderItem(21)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("schedule_window", u"21", None));
        ___qtablewidgetitem29 = self.schedule_time_table.verticalHeaderItem(22)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("schedule_window", u"22", None));
        ___qtablewidgetitem30 = self.schedule_time_table.verticalHeaderItem(23)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("schedule_window", u"23", None));
    # retranslateUi

