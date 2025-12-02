# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'object_setting.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSlider, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)
import resourece_rc

class Ui_object_setting(object):
    def setupUi(self, object_setting):
        if not object_setting.objectName():
            object_setting.setObjectName(u"object_setting")
        object_setting.setWindowModality(Qt.WindowModality.ApplicationModal)
        object_setting.resize(508, 237)
        object_setting.setMaximumSize(QSize(1260, 16777215))
        object_setting.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        object_setting.setWindowTitle(u"object_setting")
        object_setting.setStyleSheet(u"background-color: rgb(3, 3, 13);")
        self.horizontalLayout_5 = QHBoxLayout(object_setting)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.top_logo = QLabel(object_setting)
        self.top_logo.setObjectName(u"top_logo")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.top_logo.sizePolicy().hasHeightForWidth())
        self.top_logo.setSizePolicy(sizePolicy)
        self.top_logo.setMinimumSize(QSize(202, 32))
        self.top_logo.setMaximumSize(QSize(202, 32))
        font = QFont()
        font.setFamilies([u"Sans"])
        self.top_logo.setFont(font)
        self.top_logo.setPixmap(QPixmap(u":/ui/ui/images/logo.png"))
        self.top_logo.setScaledContents(True)

        self.horizontalLayout_9.addWidget(self.top_logo)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.shutdown_bnt = QPushButton(object_setting)
        self.shutdown_bnt.setObjectName(u"shutdown_bnt")
        self.shutdown_bnt.setMinimumSize(QSize(61, 31))
        self.shutdown_bnt.setMaximumSize(QSize(61, 31))
        font1 = QFont()
        font1.setFamilies([u"NanumSquareRound"])
        font1.setPointSize(10)
        font1.setBold(False)
        self.shutdown_bnt.setFont(font1)
        self.shutdown_bnt.setCursor(QCursor(Qt.PointingHandCursor))
        self.shutdown_bnt.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.shutdown_bnt.setStyleSheet(u"background-color: rgb(237, 51, 59);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"")

        self.horizontalLayout_6.addWidget(self.shutdown_bnt)


        self.horizontalLayout_9.addLayout(self.horizontalLayout_6)


        self.verticalLayout_2.addLayout(self.horizontalLayout_9)

        self.widget = QWidget(object_setting)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_4 = QHBoxLayout(self.widget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.person_label = QLabel(self.widget)
        self.person_label.setObjectName(u"person_label")
        self.person_label.setMinimumSize(QSize(203, 28))
        self.person_label.setMaximumSize(QSize(203, 28))
        font2 = QFont()
        font2.setFamilies([u"Sans"])
        font2.setPointSize(11)
        self.person_label.setFont(font2)
        self.person_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.person_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.person_label)

        self.person_active_bnt = QPushButton(self.widget)
        self.person_active_bnt.setObjectName(u"person_active_bnt")
        self.person_active_bnt.setMinimumSize(QSize(61, 25))
        self.person_active_bnt.setMaximumSize(QSize(61, 25))
        icon = QIcon()
        icon.addFile(u":/ui/ui/images/icon-switch-off.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/ui/ui/images/icon-switch-on.png", QSize(), QIcon.Normal, QIcon.On)
        self.person_active_bnt.setIcon(icon)
        self.person_active_bnt.setIconSize(QSize(55, 103))
        self.person_active_bnt.setCheckable(True)

        self.horizontalLayout.addWidget(self.person_active_bnt)

        self.person_conf_slider = QSlider(self.widget)
        self.person_conf_slider.setObjectName(u"person_conf_slider")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.person_conf_slider.sizePolicy().hasHeightForWidth())
        self.person_conf_slider.setSizePolicy(sizePolicy1)
        self.person_conf_slider.setMinimumSize(QSize(114, 31))
        self.person_conf_slider.setMaximumSize(QSize(16777215, 31))
        font3 = QFont()
        font3.setPointSize(11)
        self.person_conf_slider.setFont(font3)
        self.person_conf_slider.setStyleSheet(u"QSlider::handle:horizontal {\n"
"    background-color: rgb(192, 191, 188);\n"
"    border: 1px solid #5c5c5c; /* \ud578\ub4e4\uc758 \ud14c\ub450\ub9ac */\n"
"    width: 20px; /* \ud578\ub4e4\uc758 \ub108\ube44 */\n"
"    height: 5px; /* \ud578\ub4e4\uc758 \ub108\ube44 */\n"
"     margin: -4px 0px; /* \ud578\ub4e4\uc758 \uc704, \uc544\ub798 \uc5ec\ubc31 */\n"
"    border-radius: 4px; /* \ud578\ub4e4\uc758 \ubaa8\uc11c\ub9ac \ub465\uae00\uac8c */\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"    border: 1px solid #999999;\n"
"    height: 5px; /* \uc2ac\ub77c\uc774\ub354\uc758 \ud2b8\ub799 \ub192\uc774 */\n"
"    background: rgb(100, 100, 100); /* \uc2ac\ub77c\uc774\ub354 \ud2b8\ub799\uc758 \uae30\ubcf8 \uc0c9\uc0c1 */\n"
"    border-radius: 4px;\n"
"    margin: 0px; /* \ud2b8\ub799\uc758 \uc5ec\ubc31\uc744 \uc5c6\uc570 */\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: rgb(30, 195, 55); /* \uac8c\uc774\uc9c0 \uc0c9\uc0c1 */\n"
"    border: 1px solid #777;\n"
"    height: 5px; /* \ud2b8\ub799\uacfc"
                        " \ub3d9\uc77c\ud55c \ub192\uc774\ub85c \uc124\uc815 */\n"
"    border-radius: 4px;\n"
"    margin: 0px; /* \uac8c\uc774\uc9c0 \uc5ec\ubc31\uc744 \uc5c6\uc570 */\n"
"}\n"
"")
        self.person_conf_slider.setMinimum(0)
        self.person_conf_slider.setMaximum(100)
        self.person_conf_slider.setSingleStep(2)
        self.person_conf_slider.setValue(33)
        self.person_conf_slider.setTracking(False)
        self.person_conf_slider.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout.addWidget(self.person_conf_slider)

        self.person_conf_value = QSpinBox(self.widget)
        self.person_conf_value.setObjectName(u"person_conf_value")
        sizePolicy.setHeightForWidth(self.person_conf_value.sizePolicy().hasHeightForWidth())
        self.person_conf_value.setSizePolicy(sizePolicy)
        self.person_conf_value.setMinimumSize(QSize(70, 31))
        self.person_conf_value.setMaximumSize(QSize(16777215, 31))
        font4 = QFont()
        font4.setPointSize(10)
        self.person_conf_value.setFont(font4)
        self.person_conf_value.setStyleSheet(u"\n"
"    QSpinBox {\n"
"        subcontrol-origin: padding;\n"
"        subcontrol-position: top right;\n"
"        background: rgb(13, 16, 23);\n"
"        color: rgb(255, 255, 255);\n"
"\n"
"    }")
        self.person_conf_value.setMinimum(1)
        self.person_conf_value.setMaximum(100)
        self.person_conf_value.setValue(33)

        self.horizontalLayout.addWidget(self.person_conf_value)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.car_label = QLabel(self.widget)
        self.car_label.setObjectName(u"car_label")
        self.car_label.setMinimumSize(QSize(203, 28))
        self.car_label.setMaximumSize(QSize(203, 28))
        self.car_label.setFont(font2)
        self.car_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.car_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.car_label)

        self.car_active_bnt = QPushButton(self.widget)
        self.car_active_bnt.setObjectName(u"car_active_bnt")
        self.car_active_bnt.setMinimumSize(QSize(61, 25))
        self.car_active_bnt.setMaximumSize(QSize(61, 25))
        self.car_active_bnt.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.car_active_bnt.setIcon(icon)
        self.car_active_bnt.setIconSize(QSize(55, 103))
        self.car_active_bnt.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.car_active_bnt)

        self.car_conf_slider = QSlider(self.widget)
        self.car_conf_slider.setObjectName(u"car_conf_slider")
        sizePolicy1.setHeightForWidth(self.car_conf_slider.sizePolicy().hasHeightForWidth())
        self.car_conf_slider.setSizePolicy(sizePolicy1)
        self.car_conf_slider.setMinimumSize(QSize(114, 31))
        self.car_conf_slider.setMaximumSize(QSize(16777215, 31))
        self.car_conf_slider.setFont(font3)
        self.car_conf_slider.setStyleSheet(u"QSlider::handle:horizontal {\n"
"    background-color: rgb(192, 191, 188);\n"
"    border: 1px solid #5c5c5c; /* \ud578\ub4e4\uc758 \ud14c\ub450\ub9ac */\n"
"    width: 20px; /* \ud578\ub4e4\uc758 \ub108\ube44 */\n"
"    height: 5px; /* \ud578\ub4e4\uc758 \ub108\ube44 */\n"
"     margin: -4px 0px; /* \ud578\ub4e4\uc758 \uc704, \uc544\ub798 \uc5ec\ubc31 */\n"
"    border-radius: 4px; /* \ud578\ub4e4\uc758 \ubaa8\uc11c\ub9ac \ub465\uae00\uac8c */\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"    border: 1px solid #999999;\n"
"    height: 5px; /* \uc2ac\ub77c\uc774\ub354\uc758 \ud2b8\ub799 \ub192\uc774 */\n"
"    background: rgb(100, 100, 100); /* \uc2ac\ub77c\uc774\ub354 \ud2b8\ub799\uc758 \uae30\ubcf8 \uc0c9\uc0c1 */\n"
"    border-radius: 4px;\n"
"    margin: 0px; /* \ud2b8\ub799\uc758 \uc5ec\ubc31\uc744 \uc5c6\uc570 */\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: rgb(30, 195, 55); /* \uac8c\uc774\uc9c0 \uc0c9\uc0c1 */\n"
"    border: 1px solid #777;\n"
"    height: 5px; /* \ud2b8\ub799\uacfc"
                        " \ub3d9\uc77c\ud55c \ub192\uc774\ub85c \uc124\uc815 */\n"
"    border-radius: 4px;\n"
"    margin: 0px; /* \uac8c\uc774\uc9c0 \uc5ec\ubc31\uc744 \uc5c6\uc570 */\n"
"}\n"
"")
        self.car_conf_slider.setMinimum(0)
        self.car_conf_slider.setMaximum(100)
        self.car_conf_slider.setSingleStep(2)
        self.car_conf_slider.setValue(33)
        self.car_conf_slider.setTracking(False)
        self.car_conf_slider.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_2.addWidget(self.car_conf_slider)

        self.car_conf_value = QSpinBox(self.widget)
        self.car_conf_value.setObjectName(u"car_conf_value")
        sizePolicy.setHeightForWidth(self.car_conf_value.sizePolicy().hasHeightForWidth())
        self.car_conf_value.setSizePolicy(sizePolicy)
        self.car_conf_value.setMinimumSize(QSize(70, 31))
        self.car_conf_value.setMaximumSize(QSize(16777215, 31))
        self.car_conf_value.setFont(font4)
        self.car_conf_value.setStyleSheet(u"\n"
"    QSpinBox {\n"
"        subcontrol-origin: padding;\n"
"        subcontrol-position: top right;\n"
"        background: rgb(13, 16, 23);\n"
"        color: rgb(255, 255, 255);\n"
"\n"
"    }")
        self.car_conf_value.setMinimum(1)
        self.car_conf_value.setMaximum(100)
        self.car_conf_value.setValue(33)

        self.horizontalLayout_2.addWidget(self.car_conf_value)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.fire_label = QLabel(self.widget)
        self.fire_label.setObjectName(u"fire_label")
        self.fire_label.setMinimumSize(QSize(203, 28))
        self.fire_label.setMaximumSize(QSize(203, 28))
        self.fire_label.setFont(font2)
        self.fire_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.fire_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.fire_label)

        self.fire_active_bnt = QPushButton(self.widget)
        self.fire_active_bnt.setObjectName(u"fire_active_bnt")
        self.fire_active_bnt.setMinimumSize(QSize(61, 25))
        self.fire_active_bnt.setMaximumSize(QSize(61, 25))
        self.fire_active_bnt.setIcon(icon)
        self.fire_active_bnt.setIconSize(QSize(55, 103))
        self.fire_active_bnt.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.fire_active_bnt)

        self.fire_conf_slider = QSlider(self.widget)
        self.fire_conf_slider.setObjectName(u"fire_conf_slider")
        sizePolicy1.setHeightForWidth(self.fire_conf_slider.sizePolicy().hasHeightForWidth())
        self.fire_conf_slider.setSizePolicy(sizePolicy1)
        self.fire_conf_slider.setMinimumSize(QSize(114, 31))
        self.fire_conf_slider.setMaximumSize(QSize(16777215, 31))
        self.fire_conf_slider.setFont(font3)
        self.fire_conf_slider.setStyleSheet(u"QSlider::handle:horizontal {\n"
"    background-color: rgb(192, 191, 188);\n"
"    border: 1px solid #5c5c5c; /* \ud578\ub4e4\uc758 \ud14c\ub450\ub9ac */\n"
"    width: 20px; /* \ud578\ub4e4\uc758 \ub108\ube44 */\n"
"    height: 5px; /* \ud578\ub4e4\uc758 \ub108\ube44 */\n"
"     margin: -4px 0px; /* \ud578\ub4e4\uc758 \uc704, \uc544\ub798 \uc5ec\ubc31 */\n"
"    border-radius: 4px; /* \ud578\ub4e4\uc758 \ubaa8\uc11c\ub9ac \ub465\uae00\uac8c */\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"    border: 1px solid #999999;\n"
"    height: 5px; /* \uc2ac\ub77c\uc774\ub354\uc758 \ud2b8\ub799 \ub192\uc774 */\n"
"    background: rgb(100, 100, 100); /* \uc2ac\ub77c\uc774\ub354 \ud2b8\ub799\uc758 \uae30\ubcf8 \uc0c9\uc0c1 */\n"
"    border-radius: 4px;\n"
"    margin: 0px; /* \ud2b8\ub799\uc758 \uc5ec\ubc31\uc744 \uc5c6\uc570 */\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: rgb(30, 195, 55); /* \uac8c\uc774\uc9c0 \uc0c9\uc0c1 */\n"
"    border: 1px solid #777;\n"
"    height: 5px; /* \ud2b8\ub799\uacfc"
                        " \ub3d9\uc77c\ud55c \ub192\uc774\ub85c \uc124\uc815 */\n"
"    border-radius: 4px;\n"
"    margin: 0px; /* \uac8c\uc774\uc9c0 \uc5ec\ubc31\uc744 \uc5c6\uc570 */\n"
"}\n"
"")
        self.fire_conf_slider.setMinimum(0)
        self.fire_conf_slider.setMaximum(100)
        self.fire_conf_slider.setSingleStep(2)
        self.fire_conf_slider.setValue(33)
        self.fire_conf_slider.setTracking(False)
        self.fire_conf_slider.setOrientation(Qt.Orientation.Horizontal)

        self.horizontalLayout_3.addWidget(self.fire_conf_slider)

        self.fire_conf_value = QSpinBox(self.widget)
        self.fire_conf_value.setObjectName(u"fire_conf_value")
        sizePolicy.setHeightForWidth(self.fire_conf_value.sizePolicy().hasHeightForWidth())
        self.fire_conf_value.setSizePolicy(sizePolicy)
        self.fire_conf_value.setMinimumSize(QSize(70, 31))
        self.fire_conf_value.setMaximumSize(QSize(16777215, 31))
        self.fire_conf_value.setFont(font4)
        self.fire_conf_value.setStyleSheet(u"\n"
"    QSpinBox {\n"
"        subcontrol-origin: padding;\n"
"        subcontrol-position: top right;\n"
"        background: rgb(13, 16, 23);\n"
"        color: rgb(255, 255, 255);\n"
"\n"
"    }")
        self.fire_conf_value.setMinimum(1)
        self.fire_conf_value.setMaximum(100)
        self.fire_conf_value.setValue(33)

        self.horizontalLayout_3.addWidget(self.fire_conf_value)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.par_label = QLabel(self.widget)
        self.par_label.setObjectName(u"par_label")
        self.par_label.setMinimumSize(QSize(203, 28))
        self.par_label.setMaximumSize(QSize(203, 28))
        self.par_label.setFont(font2)
        self.par_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.par_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_8.addWidget(self.par_label)

        self.par_active_bnt = QPushButton(self.widget)
        self.par_active_bnt.setObjectName(u"par_active_bnt")
        self.par_active_bnt.setMinimumSize(QSize(61, 25))
        self.par_active_bnt.setMaximumSize(QSize(61, 25))
        self.par_active_bnt.setIcon(icon)
        self.par_active_bnt.setIconSize(QSize(55, 103))
        self.par_active_bnt.setCheckable(True)

        self.horizontalLayout_8.addWidget(self.par_active_bnt)

        self.par_time_label = QLabel(self.widget)
        self.par_time_label.setObjectName(u"par_time_label")
        self.par_time_label.setMinimumSize(QSize(23, 28))
        self.par_time_label.setMaximumSize(QSize(100, 28))
        self.par_time_label.setFont(font2)
        self.par_time_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.par_time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_8.addWidget(self.par_time_label)

        self.par_start_time = QComboBox(self.widget)
        self.par_start_time.addItem("")
        self.par_start_time.addItem("")
        self.par_start_time.addItem("")
        self.par_start_time.addItem("")
        self.par_start_time.addItem("")
        self.par_start_time.addItem("")
        self.par_start_time.addItem("")
        self.par_start_time.addItem("")
        self.par_start_time.addItem("")
        self.par_start_time.addItem("")
        self.par_start_time.addItem("")
        self.par_start_time.addItem("")
        self.par_start_time.addItem("")
        self.par_start_time.addItem("")
        self.par_start_time.addItem("")
        self.par_start_time.addItem("")
        self.par_start_time.addItem("")
        self.par_start_time.addItem("")
        self.par_start_time.addItem("")
        self.par_start_time.addItem("")
        self.par_start_time.addItem("")
        self.par_start_time.addItem("")
        self.par_start_time.addItem("")
        self.par_start_time.addItem("")
        self.par_start_time.addItem("")
        self.par_start_time.setObjectName(u"par_start_time")
        sizePolicy.setHeightForWidth(self.par_start_time.sizePolicy().hasHeightForWidth())
        self.par_start_time.setSizePolicy(sizePolicy)
        self.par_start_time.setMinimumSize(QSize(50, 31))
        self.par_start_time.setMaximumSize(QSize(50, 31))
        font5 = QFont()
        font5.setFamilies([u"Sans"])
        font5.setPointSize(10)
        font5.setBold(False)
        self.par_start_time.setFont(font5)
        self.par_start_time.setFocusPolicy(Qt.FocusPolicy.WheelFocus)
        self.par_start_time.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(13, 16, 23);\n"
"selection-background-color: rgb(53, 132, 228);\n"
"")
        self.par_start_time.setCurrentText(u"0")
        self.par_start_time.setMaxVisibleItems(10)
        self.par_start_time.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)

        self.horizontalLayout_8.addWidget(self.par_start_time)

        self.time_text_label = QLabel(self.widget)
        self.time_text_label.setObjectName(u"time_text_label")
        sizePolicy.setHeightForWidth(self.time_text_label.sizePolicy().hasHeightForWidth())
        self.time_text_label.setSizePolicy(sizePolicy)
        self.time_text_label.setMinimumSize(QSize(9, 28))
        self.time_text_label.setMaximumSize(QSize(21, 28))
        self.time_text_label.setFont(font2)
        self.time_text_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.time_text_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_8.addWidget(self.time_text_label)

        self.par_end_time = QComboBox(self.widget)
        self.par_end_time.addItem("")
        self.par_end_time.addItem("")
        self.par_end_time.addItem("")
        self.par_end_time.addItem("")
        self.par_end_time.addItem("")
        self.par_end_time.addItem("")
        self.par_end_time.addItem("")
        self.par_end_time.addItem("")
        self.par_end_time.addItem("")
        self.par_end_time.addItem("")
        self.par_end_time.addItem("")
        self.par_end_time.addItem("")
        self.par_end_time.addItem("")
        self.par_end_time.addItem("")
        self.par_end_time.addItem("")
        self.par_end_time.addItem("")
        self.par_end_time.addItem("")
        self.par_end_time.addItem("")
        self.par_end_time.addItem("")
        self.par_end_time.addItem("")
        self.par_end_time.addItem("")
        self.par_end_time.addItem("")
        self.par_end_time.addItem("")
        self.par_end_time.addItem("")
        self.par_end_time.addItem("")
        self.par_end_time.setObjectName(u"par_end_time")
        sizePolicy.setHeightForWidth(self.par_end_time.sizePolicy().hasHeightForWidth())
        self.par_end_time.setSizePolicy(sizePolicy)
        self.par_end_time.setMinimumSize(QSize(50, 31))
        self.par_end_time.setMaximumSize(QSize(50, 31))
        self.par_end_time.setFont(font5)
        self.par_end_time.setFocusPolicy(Qt.FocusPolicy.WheelFocus)
        self.par_end_time.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(13, 16, 23);\n"
"selection-background-color: rgb(53, 132, 228);\n"
"")
        self.par_end_time.setCurrentText(u"0")
        self.par_end_time.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)

        self.horizontalLayout_8.addWidget(self.par_end_time)


        self.verticalLayout.addLayout(self.horizontalLayout_8)


        self.horizontalLayout_4.addLayout(self.verticalLayout)


        self.verticalLayout_2.addWidget(self.widget)

        self.verticalSpacer = QSpacerItem(26, 317, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout_5.addLayout(self.verticalLayout_2)


        self.retranslateUi(object_setting)

        self.par_start_time.setCurrentIndex(0)
        self.par_end_time.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(object_setting)
    # setupUi

    def retranslateUi(self, object_setting):
        self.top_logo.setText("")
        self.shutdown_bnt.setText(QCoreApplication.translate("object_setting", u"\ub2eb\uae30", None))
        self.person_label.setText(QCoreApplication.translate("object_setting", u"\uc0ac\ub78c", None))
        self.person_active_bnt.setText("")
        self.car_label.setText(QCoreApplication.translate("object_setting", u"\ud0c8\uac83(\uc790\ub3d9\ucc28, \uc790\uc804\uac70, \uc624\ud1a0\ubc14\uc774)", None))
        self.car_active_bnt.setText("")
        self.fire_label.setText(QCoreApplication.translate("object_setting", u"\ubd88", None))
        self.fire_active_bnt.setText("")
        self.par_label.setText(QCoreApplication.translate("object_setting", u"\ubcf4\ud589\uc790 \uc18d\uc131 \ucd94\ucd9c", None))
        self.par_active_bnt.setText("")
        self.par_time_label.setText(QCoreApplication.translate("object_setting", u"\uc2dc\uac04   :", None))
        self.par_start_time.setItemText(0, QCoreApplication.translate("object_setting", u"0", None))
        self.par_start_time.setItemText(1, QCoreApplication.translate("object_setting", u"1", None))
        self.par_start_time.setItemText(2, QCoreApplication.translate("object_setting", u"2", None))
        self.par_start_time.setItemText(3, QCoreApplication.translate("object_setting", u"3", None))
        self.par_start_time.setItemText(4, QCoreApplication.translate("object_setting", u"4", None))
        self.par_start_time.setItemText(5, QCoreApplication.translate("object_setting", u"5", None))
        self.par_start_time.setItemText(6, QCoreApplication.translate("object_setting", u"6", None))
        self.par_start_time.setItemText(7, QCoreApplication.translate("object_setting", u"7", None))
        self.par_start_time.setItemText(8, QCoreApplication.translate("object_setting", u"8", None))
        self.par_start_time.setItemText(9, QCoreApplication.translate("object_setting", u"9", None))
        self.par_start_time.setItemText(10, QCoreApplication.translate("object_setting", u"10", None))
        self.par_start_time.setItemText(11, QCoreApplication.translate("object_setting", u"11", None))
        self.par_start_time.setItemText(12, QCoreApplication.translate("object_setting", u"12", None))
        self.par_start_time.setItemText(13, QCoreApplication.translate("object_setting", u"13", None))
        self.par_start_time.setItemText(14, QCoreApplication.translate("object_setting", u"14", None))
        self.par_start_time.setItemText(15, QCoreApplication.translate("object_setting", u"15", None))
        self.par_start_time.setItemText(16, QCoreApplication.translate("object_setting", u"16", None))
        self.par_start_time.setItemText(17, QCoreApplication.translate("object_setting", u"17", None))
        self.par_start_time.setItemText(18, QCoreApplication.translate("object_setting", u"18", None))
        self.par_start_time.setItemText(19, QCoreApplication.translate("object_setting", u"19", None))
        self.par_start_time.setItemText(20, QCoreApplication.translate("object_setting", u"20", None))
        self.par_start_time.setItemText(21, QCoreApplication.translate("object_setting", u"21", None))
        self.par_start_time.setItemText(22, QCoreApplication.translate("object_setting", u"22", None))
        self.par_start_time.setItemText(23, QCoreApplication.translate("object_setting", u"21", None))
        self.par_start_time.setItemText(24, QCoreApplication.translate("object_setting", u"23", None))

        self.par_start_time.setPlaceholderText("")
        self.time_text_label.setText(QCoreApplication.translate("object_setting", u"~", None))
        self.par_end_time.setItemText(0, QCoreApplication.translate("object_setting", u"0", None))
        self.par_end_time.setItemText(1, QCoreApplication.translate("object_setting", u"1", None))
        self.par_end_time.setItemText(2, QCoreApplication.translate("object_setting", u"2", None))
        self.par_end_time.setItemText(3, QCoreApplication.translate("object_setting", u"3", None))
        self.par_end_time.setItemText(4, QCoreApplication.translate("object_setting", u"4", None))
        self.par_end_time.setItemText(5, QCoreApplication.translate("object_setting", u"5", None))
        self.par_end_time.setItemText(6, QCoreApplication.translate("object_setting", u"6", None))
        self.par_end_time.setItemText(7, QCoreApplication.translate("object_setting", u"7", None))
        self.par_end_time.setItemText(8, QCoreApplication.translate("object_setting", u"8", None))
        self.par_end_time.setItemText(9, QCoreApplication.translate("object_setting", u"9", None))
        self.par_end_time.setItemText(10, QCoreApplication.translate("object_setting", u"10", None))
        self.par_end_time.setItemText(11, QCoreApplication.translate("object_setting", u"11", None))
        self.par_end_time.setItemText(12, QCoreApplication.translate("object_setting", u"12", None))
        self.par_end_time.setItemText(13, QCoreApplication.translate("object_setting", u"13", None))
        self.par_end_time.setItemText(14, QCoreApplication.translate("object_setting", u"14", None))
        self.par_end_time.setItemText(15, QCoreApplication.translate("object_setting", u"15", None))
        self.par_end_time.setItemText(16, QCoreApplication.translate("object_setting", u"16", None))
        self.par_end_time.setItemText(17, QCoreApplication.translate("object_setting", u"17", None))
        self.par_end_time.setItemText(18, QCoreApplication.translate("object_setting", u"18", None))
        self.par_end_time.setItemText(19, QCoreApplication.translate("object_setting", u"19", None))
        self.par_end_time.setItemText(20, QCoreApplication.translate("object_setting", u"20", None))
        self.par_end_time.setItemText(21, QCoreApplication.translate("object_setting", u"21", None))
        self.par_end_time.setItemText(22, QCoreApplication.translate("object_setting", u"22", None))
        self.par_end_time.setItemText(23, QCoreApplication.translate("object_setting", u"21", None))
        self.par_end_time.setItemText(24, QCoreApplication.translate("object_setting", u"23", None))

        self.par_end_time.setPlaceholderText("")
        pass
    # retranslateUi

