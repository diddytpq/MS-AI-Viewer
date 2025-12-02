# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ai_settingquGyob.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import resourece_rc
import resourece_rc

class Ui_Ai_Setting_Window(object):
    def setupUi(self, Ai_Setting_Window):
        if not Ai_Setting_Window.objectName():
            Ai_Setting_Window.setObjectName(u"Ai_Setting_Window")
        Ai_Setting_Window.setWindowModality(Qt.WindowModality.ApplicationModal)
        Ai_Setting_Window.resize(1048, 752)
        Ai_Setting_Window.setMaximumSize(QSize(1048, 752))
        Ai_Setting_Window.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        Ai_Setting_Window.setWindowTitle(u"\uc9c0\ub2a5\ud615 \ubd84\uc11d \uc124\uc815")
        icon = QIcon()
        icon.addFile(u":/newPrefix/images/icon2.png", QSize(), QIcon.Normal, QIcon.Off)
        Ai_Setting_Window.setWindowIcon(icon)
        Ai_Setting_Window.setStyleSheet(u"background-color: rgb(3, 3, 13);")
        self.verticalLayout_3 = QVBoxLayout(Ai_Setting_Window)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_3 = QWidget(Ai_Setting_Window)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMaximumSize(QSize(9999, 55))
        self.horizontalLayout_5 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.ai_setting_info_label = QLabel(self.widget_3)
        self.ai_setting_info_label.setObjectName(u"ai_setting_info_label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ai_setting_info_label.sizePolicy().hasHeightForWidth())
        self.ai_setting_info_label.setSizePolicy(sizePolicy)
        self.ai_setting_info_label.setMaximumSize(QSize(9999, 37))
        font = QFont()
        font.setFamilies([u"NanumBarunGothic"])
        font.setPointSize(14)
        font.setBold(False)
        self.ai_setting_info_label.setFont(font)
        self.ai_setting_info_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.ai_setting_info_label.setIndent(0)
        self.ai_setting_info_label.setOpenExternalLinks(False)

        self.horizontalLayout_3.addWidget(self.ai_setting_info_label)

        self.all_select_bnt = QPushButton(self.widget_3)
        self.all_select_bnt.setObjectName(u"all_select_bnt")
        self.all_select_bnt.setMinimumSize(QSize(71, 33))
        self.all_select_bnt.setMaximumSize(QSize(71, 33))
        font1 = QFont()
        font1.setFamilies([u"NanumBarunGothic"])
        font1.setPointSize(10)
        self.all_select_bnt.setFont(font1)
        self.all_select_bnt.setCursor(QCursor(Qt.PointingHandCursor))
        self.all_select_bnt.setStyleSheet(u"background-color: rgb(36, 39, 44);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 13px;\n"
"\n"
"\n"
"")

        self.horizontalLayout_3.addWidget(self.all_select_bnt)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)


        self.verticalLayout_2.addWidget(self.widget_3)

        self.widget_2 = QWidget(Ai_Setting_Window)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout = QGridLayout(self.widget_2)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, 0, 0, 0)
        self.search_camera_view_layout_11 = QVBoxLayout()
        self.search_camera_view_layout_11.setSpacing(0)
        self.search_camera_view_layout_11.setObjectName(u"search_camera_view_layout_11")
        self.camera_view_name_11 = QLabel(self.widget_2)
        self.camera_view_name_11.setObjectName(u"camera_view_name_11")
        sizePolicy.setHeightForWidth(self.camera_view_name_11.sizePolicy().hasHeightForWidth())
        self.camera_view_name_11.setSizePolicy(sizePolicy)
        self.camera_view_name_11.setMaximumSize(QSize(722, 20))
        font2 = QFont()
        font2.setFamilies([u"NanumSquareRound"])
        font2.setPointSize(11)
        font2.setBold(False)
        self.camera_view_name_11.setFont(font2)
        self.camera_view_name_11.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 170);\n"
"border: 1px solid rgb(119, 118, 123);")
        self.camera_view_name_11.setMargin(0)
        self.camera_view_name_11.setIndent(15)

        self.search_camera_view_layout_11.addWidget(self.camera_view_name_11)

        self.camera_view_11 = QLabel(self.widget_2)
        self.camera_view_11.setObjectName(u"camera_view_11")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.camera_view_11.sizePolicy().hasHeightForWidth())
        self.camera_view_11.setSizePolicy(sizePolicy1)
        font3 = QFont()
        font3.setFamilies([u"NanumBarunGothic"])
        font3.setPointSize(16)
        self.camera_view_11.setFont(font3)
        self.camera_view_11.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.camera_view_11.setStyleSheet(u"border: 1px solid rgb(119, 118, 123);\n"
"color: rgb(255, 255, 255);")
        self.camera_view_11.setPixmap(QPixmap(u":/ui/ui/images/ico_video_off.svg"))
        self.camera_view_11.setScaledContents(False)
        self.camera_view_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.search_camera_view_layout_11.addWidget(self.camera_view_11)


        self.gridLayout.addLayout(self.search_camera_view_layout_11, 3, 2, 1, 1)

        self.search_camera_view_layout_4 = QVBoxLayout()
        self.search_camera_view_layout_4.setSpacing(0)
        self.search_camera_view_layout_4.setObjectName(u"search_camera_view_layout_4")
        self.camera_view_name_4 = QLabel(self.widget_2)
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

        self.search_camera_view_layout_4.addWidget(self.camera_view_name_4)

        self.camera_view_4 = QLabel(self.widget_2)
        self.camera_view_4.setObjectName(u"camera_view_4")
        sizePolicy1.setHeightForWidth(self.camera_view_4.sizePolicy().hasHeightForWidth())
        self.camera_view_4.setSizePolicy(sizePolicy1)
        self.camera_view_4.setFont(font3)
        self.camera_view_4.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.camera_view_4.setStyleSheet(u"border: 1px solid rgb(119, 118, 123);\n"
"color: rgb(255, 255, 255);")
        self.camera_view_4.setPixmap(QPixmap(u":/ui/ui/images/ico_video_off.svg"))
        self.camera_view_4.setScaledContents(False)
        self.camera_view_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.search_camera_view_layout_4.addWidget(self.camera_view_4)


        self.gridLayout.addLayout(self.search_camera_view_layout_4, 1, 3, 1, 1)

        self.search_camera_view_layout_8 = QVBoxLayout()
        self.search_camera_view_layout_8.setSpacing(0)
        self.search_camera_view_layout_8.setObjectName(u"search_camera_view_layout_8")
        self.camera_view_name_8 = QLabel(self.widget_2)
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

        self.search_camera_view_layout_8.addWidget(self.camera_view_name_8)

        self.camera_view_8 = QLabel(self.widget_2)
        self.camera_view_8.setObjectName(u"camera_view_8")
        sizePolicy1.setHeightForWidth(self.camera_view_8.sizePolicy().hasHeightForWidth())
        self.camera_view_8.setSizePolicy(sizePolicy1)
        self.camera_view_8.setFont(font3)
        self.camera_view_8.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.camera_view_8.setStyleSheet(u"border: 1px solid rgb(119, 118, 123);\n"
"color: rgb(255, 255, 255);")
        self.camera_view_8.setPixmap(QPixmap(u":/ui/ui/images/ico_video_off.svg"))
        self.camera_view_8.setScaledContents(False)
        self.camera_view_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.search_camera_view_layout_8.addWidget(self.camera_view_8)


        self.gridLayout.addLayout(self.search_camera_view_layout_8, 2, 3, 1, 1)

        self.search_camera_view_layout_5 = QVBoxLayout()
        self.search_camera_view_layout_5.setSpacing(0)
        self.search_camera_view_layout_5.setObjectName(u"search_camera_view_layout_5")
        self.camera_view_name_5 = QLabel(self.widget_2)
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

        self.search_camera_view_layout_5.addWidget(self.camera_view_name_5)

        self.camera_view_5 = QLabel(self.widget_2)
        self.camera_view_5.setObjectName(u"camera_view_5")
        sizePolicy1.setHeightForWidth(self.camera_view_5.sizePolicy().hasHeightForWidth())
        self.camera_view_5.setSizePolicy(sizePolicy1)
        self.camera_view_5.setFont(font3)
        self.camera_view_5.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.camera_view_5.setStyleSheet(u"border: 1px solid rgb(119, 118, 123);\n"
"color: rgb(255, 255, 255);")
        self.camera_view_5.setPixmap(QPixmap(u":/ui/ui/images/ico_video_off.svg"))
        self.camera_view_5.setScaledContents(False)
        self.camera_view_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.search_camera_view_layout_5.addWidget(self.camera_view_5)


        self.gridLayout.addLayout(self.search_camera_view_layout_5, 2, 0, 1, 1)

        self.search_camera_view_layout_9 = QVBoxLayout()
        self.search_camera_view_layout_9.setSpacing(0)
        self.search_camera_view_layout_9.setObjectName(u"search_camera_view_layout_9")
        self.camera_view_name_9 = QLabel(self.widget_2)
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

        self.search_camera_view_layout_9.addWidget(self.camera_view_name_9)

        self.camera_view_9 = QLabel(self.widget_2)
        self.camera_view_9.setObjectName(u"camera_view_9")
        sizePolicy1.setHeightForWidth(self.camera_view_9.sizePolicy().hasHeightForWidth())
        self.camera_view_9.setSizePolicy(sizePolicy1)
        self.camera_view_9.setFont(font3)
        self.camera_view_9.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.camera_view_9.setStyleSheet(u"border: 1px solid rgb(119, 118, 123);\n"
"color: rgb(255, 255, 255);")
        self.camera_view_9.setPixmap(QPixmap(u":/ui/ui/images/ico_video_off.svg"))
        self.camera_view_9.setScaledContents(False)
        self.camera_view_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.search_camera_view_layout_9.addWidget(self.camera_view_9)


        self.gridLayout.addLayout(self.search_camera_view_layout_9, 3, 0, 1, 1)

        self.search_camera_view_layout_10 = QVBoxLayout()
        self.search_camera_view_layout_10.setSpacing(0)
        self.search_camera_view_layout_10.setObjectName(u"search_camera_view_layout_10")
        self.camera_view_name_10 = QLabel(self.widget_2)
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

        self.search_camera_view_layout_10.addWidget(self.camera_view_name_10)

        self.camera_view_10 = QLabel(self.widget_2)
        self.camera_view_10.setObjectName(u"camera_view_10")
        sizePolicy1.setHeightForWidth(self.camera_view_10.sizePolicy().hasHeightForWidth())
        self.camera_view_10.setSizePolicy(sizePolicy1)
        self.camera_view_10.setFont(font3)
        self.camera_view_10.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.camera_view_10.setStyleSheet(u"border: 1px solid rgb(119, 118, 123);\n"
"color: rgb(255, 255, 255);")
        self.camera_view_10.setPixmap(QPixmap(u":/ui/ui/images/ico_video_off.svg"))
        self.camera_view_10.setScaledContents(False)
        self.camera_view_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.search_camera_view_layout_10.addWidget(self.camera_view_10)


        self.gridLayout.addLayout(self.search_camera_view_layout_10, 3, 1, 1, 1)

        self.search_camera_view_layout_2 = QVBoxLayout()
        self.search_camera_view_layout_2.setSpacing(0)
        self.search_camera_view_layout_2.setObjectName(u"search_camera_view_layout_2")
        self.camera_view_name_2 = QLabel(self.widget_2)
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

        self.search_camera_view_layout_2.addWidget(self.camera_view_name_2)

        self.camera_view_2 = QLabel(self.widget_2)
        self.camera_view_2.setObjectName(u"camera_view_2")
        sizePolicy1.setHeightForWidth(self.camera_view_2.sizePolicy().hasHeightForWidth())
        self.camera_view_2.setSizePolicy(sizePolicy1)
        self.camera_view_2.setFont(font3)
        self.camera_view_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.camera_view_2.setStyleSheet(u"border: 1px solid rgb(119, 118, 123);\n"
"color: rgb(255, 255, 255);")
        self.camera_view_2.setPixmap(QPixmap(u":/ui/ui/images/ico_video_off.svg"))
        self.camera_view_2.setScaledContents(False)
        self.camera_view_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.search_camera_view_layout_2.addWidget(self.camera_view_2)


        self.gridLayout.addLayout(self.search_camera_view_layout_2, 1, 1, 1, 1)

        self.search_camera_view_layout_3 = QVBoxLayout()
        self.search_camera_view_layout_3.setSpacing(0)
        self.search_camera_view_layout_3.setObjectName(u"search_camera_view_layout_3")
        self.camera_view_name_3 = QLabel(self.widget_2)
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

        self.search_camera_view_layout_3.addWidget(self.camera_view_name_3)

        self.camera_view_3 = QLabel(self.widget_2)
        self.camera_view_3.setObjectName(u"camera_view_3")
        sizePolicy1.setHeightForWidth(self.camera_view_3.sizePolicy().hasHeightForWidth())
        self.camera_view_3.setSizePolicy(sizePolicy1)
        self.camera_view_3.setFont(font3)
        self.camera_view_3.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.camera_view_3.setStyleSheet(u"border: 1px solid rgb(119, 118, 123);\n"
"color: rgb(255, 255, 255);")
        self.camera_view_3.setPixmap(QPixmap(u":/ui/ui/images/ico_video_off.svg"))
        self.camera_view_3.setScaledContents(False)
        self.camera_view_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.search_camera_view_layout_3.addWidget(self.camera_view_3)


        self.gridLayout.addLayout(self.search_camera_view_layout_3, 1, 2, 1, 1)

        self.search_camera_view_layout_12 = QVBoxLayout()
        self.search_camera_view_layout_12.setSpacing(0)
        self.search_camera_view_layout_12.setObjectName(u"search_camera_view_layout_12")
        self.camera_view_name_12 = QLabel(self.widget_2)
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

        self.search_camera_view_layout_12.addWidget(self.camera_view_name_12)

        self.camera_view_12 = QLabel(self.widget_2)
        self.camera_view_12.setObjectName(u"camera_view_12")
        sizePolicy1.setHeightForWidth(self.camera_view_12.sizePolicy().hasHeightForWidth())
        self.camera_view_12.setSizePolicy(sizePolicy1)
        self.camera_view_12.setFont(font3)
        self.camera_view_12.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.camera_view_12.setStyleSheet(u"border: 1px solid rgb(119, 118, 123);\n"
"color: rgb(255, 255, 255);")
        self.camera_view_12.setPixmap(QPixmap(u":/ui/ui/images/ico_video_off.svg"))
        self.camera_view_12.setScaledContents(False)
        self.camera_view_12.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.search_camera_view_layout_12.addWidget(self.camera_view_12)


        self.gridLayout.addLayout(self.search_camera_view_layout_12, 3, 3, 1, 1)

        self.search_camera_view_layout_6 = QVBoxLayout()
        self.search_camera_view_layout_6.setSpacing(0)
        self.search_camera_view_layout_6.setObjectName(u"search_camera_view_layout_6")
        self.camera_view_name_6 = QLabel(self.widget_2)
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

        self.search_camera_view_layout_6.addWidget(self.camera_view_name_6)

        self.camera_view_6 = QLabel(self.widget_2)
        self.camera_view_6.setObjectName(u"camera_view_6")
        sizePolicy1.setHeightForWidth(self.camera_view_6.sizePolicy().hasHeightForWidth())
        self.camera_view_6.setSizePolicy(sizePolicy1)
        self.camera_view_6.setFont(font3)
        self.camera_view_6.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.camera_view_6.setStyleSheet(u"border: 1px solid rgb(119, 118, 123);\n"
"color: rgb(255, 255, 255);")
        self.camera_view_6.setPixmap(QPixmap(u":/ui/ui/images/ico_video_off.svg"))
        self.camera_view_6.setScaledContents(False)
        self.camera_view_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.search_camera_view_layout_6.addWidget(self.camera_view_6)


        self.gridLayout.addLayout(self.search_camera_view_layout_6, 2, 1, 1, 1)

        self.search_camera_view_layout_1 = QVBoxLayout()
        self.search_camera_view_layout_1.setSpacing(0)
        self.search_camera_view_layout_1.setObjectName(u"search_camera_view_layout_1")
        self.camera_view_name_1 = QLabel(self.widget_2)
        self.camera_view_name_1.setObjectName(u"camera_view_name_1")
        sizePolicy.setHeightForWidth(self.camera_view_name_1.sizePolicy().hasHeightForWidth())
        self.camera_view_name_1.setSizePolicy(sizePolicy)
        self.camera_view_name_1.setMaximumSize(QSize(722, 20))
        self.camera_view_name_1.setFont(font2)
        self.camera_view_name_1.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(0, 0, 0, 170);\n"
"border: 1px solid rgb(119, 118, 123);")
        self.camera_view_name_1.setMargin(0)
        self.camera_view_name_1.setIndent(15)

        self.search_camera_view_layout_1.addWidget(self.camera_view_name_1)

        self.camera_view_1 = QLabel(self.widget_2)
        self.camera_view_1.setObjectName(u"camera_view_1")
        sizePolicy1.setHeightForWidth(self.camera_view_1.sizePolicy().hasHeightForWidth())
        self.camera_view_1.setSizePolicy(sizePolicy1)
        self.camera_view_1.setFont(font3)
        self.camera_view_1.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.camera_view_1.setStyleSheet(u"border: 1px solid rgb(119, 118, 123);\n"
"color: rgb(255, 255, 255);")
        self.camera_view_1.setPixmap(QPixmap(u":/ui/ui/images/ico_video_off.svg"))
        self.camera_view_1.setScaledContents(False)
        self.camera_view_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.search_camera_view_layout_1.addWidget(self.camera_view_1)


        self.gridLayout.addLayout(self.search_camera_view_layout_1, 1, 0, 1, 1)

        self.search_camera_view_layout_7 = QVBoxLayout()
        self.search_camera_view_layout_7.setSpacing(0)
        self.search_camera_view_layout_7.setObjectName(u"search_camera_view_layout_7")
        self.camera_view_name_7 = QLabel(self.widget_2)
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

        self.search_camera_view_layout_7.addWidget(self.camera_view_name_7)

        self.camera_view_7 = QLabel(self.widget_2)
        self.camera_view_7.setObjectName(u"camera_view_7")
        sizePolicy1.setHeightForWidth(self.camera_view_7.sizePolicy().hasHeightForWidth())
        self.camera_view_7.setSizePolicy(sizePolicy1)
        self.camera_view_7.setFont(font3)
        self.camera_view_7.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.camera_view_7.setStyleSheet(u"border: 1px solid rgb(119, 118, 123);\n"
"color: rgb(255, 255, 255);")
        self.camera_view_7.setPixmap(QPixmap(u":/ui/ui/images/ico_video_off.svg"))
        self.camera_view_7.setScaledContents(False)
        self.camera_view_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.search_camera_view_layout_7.addWidget(self.camera_view_7)


        self.gridLayout.addLayout(self.search_camera_view_layout_7, 2, 2, 1, 1)

        self.search_camera_view_layout_13 = QVBoxLayout()
        self.search_camera_view_layout_13.setSpacing(0)
        self.search_camera_view_layout_13.setObjectName(u"search_camera_view_layout_13")
        self.camera_view_name_13 = QLabel(self.widget_2)
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

        self.search_camera_view_layout_13.addWidget(self.camera_view_name_13)

        self.camera_view_13 = QLabel(self.widget_2)
        self.camera_view_13.setObjectName(u"camera_view_13")
        sizePolicy1.setHeightForWidth(self.camera_view_13.sizePolicy().hasHeightForWidth())
        self.camera_view_13.setSizePolicy(sizePolicy1)
        self.camera_view_13.setFont(font3)
        self.camera_view_13.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.camera_view_13.setStyleSheet(u"border: 1px solid rgb(119, 118, 123);\n"
"color: rgb(255, 255, 255);")
        self.camera_view_13.setPixmap(QPixmap(u":/ui/ui/images/ico_video_off.svg"))
        self.camera_view_13.setScaledContents(False)
        self.camera_view_13.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.search_camera_view_layout_13.addWidget(self.camera_view_13)


        self.gridLayout.addLayout(self.search_camera_view_layout_13, 4, 0, 1, 1)

        self.search_camera_view_layout_14 = QVBoxLayout()
        self.search_camera_view_layout_14.setSpacing(0)
        self.search_camera_view_layout_14.setObjectName(u"search_camera_view_layout_14")
        self.camera_view_name_14 = QLabel(self.widget_2)
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

        self.search_camera_view_layout_14.addWidget(self.camera_view_name_14)

        self.camera_view_14 = QLabel(self.widget_2)
        self.camera_view_14.setObjectName(u"camera_view_14")
        sizePolicy1.setHeightForWidth(self.camera_view_14.sizePolicy().hasHeightForWidth())
        self.camera_view_14.setSizePolicy(sizePolicy1)
        self.camera_view_14.setFont(font3)
        self.camera_view_14.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.camera_view_14.setStyleSheet(u"border: 1px solid rgb(119, 118, 123);\n"
"color: rgb(255, 255, 255);")
        self.camera_view_14.setPixmap(QPixmap(u":/ui/ui/images/ico_video_off.svg"))
        self.camera_view_14.setScaledContents(False)
        self.camera_view_14.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.search_camera_view_layout_14.addWidget(self.camera_view_14)


        self.gridLayout.addLayout(self.search_camera_view_layout_14, 4, 1, 1, 1)

        self.search_camera_view_layout_15 = QVBoxLayout()
        self.search_camera_view_layout_15.setSpacing(0)
        self.search_camera_view_layout_15.setObjectName(u"search_camera_view_layout_15")
        self.camera_view_name_15 = QLabel(self.widget_2)
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

        self.search_camera_view_layout_15.addWidget(self.camera_view_name_15)

        self.camera_view_15 = QLabel(self.widget_2)
        self.camera_view_15.setObjectName(u"camera_view_15")
        sizePolicy1.setHeightForWidth(self.camera_view_15.sizePolicy().hasHeightForWidth())
        self.camera_view_15.setSizePolicy(sizePolicy1)
        self.camera_view_15.setFont(font3)
        self.camera_view_15.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.camera_view_15.setStyleSheet(u"border: 1px solid rgb(119, 118, 123);\n"
"color: rgb(255, 255, 255);")
        self.camera_view_15.setPixmap(QPixmap(u":/ui/ui/images/ico_video_off.svg"))
        self.camera_view_15.setScaledContents(False)
        self.camera_view_15.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.search_camera_view_layout_15.addWidget(self.camera_view_15)


        self.gridLayout.addLayout(self.search_camera_view_layout_15, 4, 2, 1, 1)

        self.search_camera_view_layout_16 = QVBoxLayout()
        self.search_camera_view_layout_16.setSpacing(0)
        self.search_camera_view_layout_16.setObjectName(u"search_camera_view_layout_16")
        self.camera_view_name_16 = QLabel(self.widget_2)
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

        self.search_camera_view_layout_16.addWidget(self.camera_view_name_16)

        self.camera_view_16 = QLabel(self.widget_2)
        self.camera_view_16.setObjectName(u"camera_view_16")
        sizePolicy1.setHeightForWidth(self.camera_view_16.sizePolicy().hasHeightForWidth())
        self.camera_view_16.setSizePolicy(sizePolicy1)
        self.camera_view_16.setFont(font3)
        self.camera_view_16.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.camera_view_16.setStyleSheet(u"border: 1px solid rgb(119, 118, 123);\n"
"color: rgb(255, 255, 255);")
        self.camera_view_16.setPixmap(QPixmap(u":/ui/ui/images/ico_video_off.svg"))
        self.camera_view_16.setScaledContents(False)
        self.camera_view_16.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.search_camera_view_layout_16.addWidget(self.camera_view_16)


        self.gridLayout.addLayout(self.search_camera_view_layout_16, 4, 3, 1, 1)


        self.verticalLayout_2.addWidget(self.widget_2)

        self.widget = QWidget(Ai_Setting_Window)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(9999, 63))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.camera_save_bnt = QPushButton(self.widget)
        self.camera_save_bnt.setObjectName(u"camera_save_bnt")
        sizePolicy1.setHeightForWidth(self.camera_save_bnt.sizePolicy().hasHeightForWidth())
        self.camera_save_bnt.setSizePolicy(sizePolicy1)
        self.camera_save_bnt.setMinimumSize(QSize(71, 41))
        self.camera_save_bnt.setMaximumSize(QSize(16777210, 41))
        self.camera_save_bnt.setFont(font1)
        self.camera_save_bnt.setCursor(QCursor(Qt.PointingHandCursor))
        self.camera_save_bnt.setStyleSheet(u"background-color: rgb(30, 195, 55);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"")

        self.horizontalLayout.addWidget(self.camera_save_bnt)

        self.close_bnt = QPushButton(self.widget)
        self.close_bnt.setObjectName(u"close_bnt")
        self.close_bnt.setMinimumSize(QSize(71, 41))
        self.close_bnt.setFont(font1)
        self.close_bnt.setCursor(QCursor(Qt.PointingHandCursor))
        self.close_bnt.setStyleSheet(u"background-color: rgb(255, 49, 38);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")

        self.horizontalLayout.addWidget(self.close_bnt)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addWidget(self.widget)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.retranslateUi(Ai_Setting_Window)

        QMetaObject.connectSlotsByName(Ai_Setting_Window)
    # setupUi

    def retranslateUi(self, Ai_Setting_Window):
        self.ai_setting_info_label.setText(QCoreApplication.translate("Ai_Setting_Window", u"\uc9c0\ub2a5\ud615 \ubd84\uc11d \uc2e4\ud589 \uce74\uba54\ub77c \uc120\ud0dd", None))
        self.all_select_bnt.setText(QCoreApplication.translate("Ai_Setting_Window", u"\ubaa8\ub450 \uc120\ud0dd", None))
        self.camera_view_name_11.setText(QCoreApplication.translate("Ai_Setting_Window", u"\uce74\uba54\ub77c11", None))
        self.camera_view_11.setText("")
        self.camera_view_name_4.setText(QCoreApplication.translate("Ai_Setting_Window", u"\uce74\uba54\ub77c4", None))
        self.camera_view_4.setText("")
        self.camera_view_name_8.setText(QCoreApplication.translate("Ai_Setting_Window", u"\uce74\uba54\ub77c8", None))
        self.camera_view_8.setText("")
        self.camera_view_name_5.setText(QCoreApplication.translate("Ai_Setting_Window", u"\uce74\uba54\ub77c5", None))
        self.camera_view_5.setText("")
        self.camera_view_name_9.setText(QCoreApplication.translate("Ai_Setting_Window", u"\uce74\uba54\ub77c9", None))
        self.camera_view_9.setText("")
        self.camera_view_name_10.setText(QCoreApplication.translate("Ai_Setting_Window", u"\uce74\uba54\ub77c10", None))
        self.camera_view_10.setText("")
        self.camera_view_name_2.setText(QCoreApplication.translate("Ai_Setting_Window", u"\uce74\uba54\ub77c2", None))
        self.camera_view_2.setText("")
        self.camera_view_name_3.setText(QCoreApplication.translate("Ai_Setting_Window", u"\uce74\uba54\ub77c3", None))
        self.camera_view_3.setText("")
        self.camera_view_name_12.setText(QCoreApplication.translate("Ai_Setting_Window", u"\uce74\uba54\ub77c12", None))
        self.camera_view_12.setText("")
        self.camera_view_name_6.setText(QCoreApplication.translate("Ai_Setting_Window", u"\uce74\uba54\ub77c6", None))
        self.camera_view_6.setText("")
        self.camera_view_name_1.setText(QCoreApplication.translate("Ai_Setting_Window", u"\uce74\uba54\ub77c1", None))
        self.camera_view_1.setText("")
        self.camera_view_name_7.setText(QCoreApplication.translate("Ai_Setting_Window", u"\uce74\uba54\ub77c7", None))
        self.camera_view_7.setText("")
        self.camera_view_name_13.setText(QCoreApplication.translate("Ai_Setting_Window", u"\uce74\uba54\ub77c13", None))
        self.camera_view_13.setText("")
        self.camera_view_name_14.setText(QCoreApplication.translate("Ai_Setting_Window", u"\uce74\uba54\ub77c14", None))
        self.camera_view_14.setText("")
        self.camera_view_name_15.setText(QCoreApplication.translate("Ai_Setting_Window", u"\uce74\uba54\ub77c15", None))
        self.camera_view_15.setText("")
        self.camera_view_name_16.setText(QCoreApplication.translate("Ai_Setting_Window", u"\uce74\uba54\ub77c16", None))
        self.camera_view_16.setText("")
        self.camera_save_bnt.setText(QCoreApplication.translate("Ai_Setting_Window", u"\uc2dc\uc791", None))
        self.close_bnt.setText(QCoreApplication.translate("Ai_Setting_Window", u"\ub2eb\uae30", None))
        pass
    # retranslateUi

