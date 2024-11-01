# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'search.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractSpinBox, QApplication, QComboBox,
    QDateEdit, QDateTimeEdit, QDoubleSpinBox, QHBoxLayout,
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
import ms_ai_img_rc
import ms_ai_img_rc
import ms_ai_img_rc
import ms_ai_img_rc

class Ui_Search_window(object):
    def setupUi(self, Search_window):
        if not Search_window.objectName():
            Search_window.setObjectName(u"Search_window")
        Search_window.setWindowModality(Qt.WindowModality.ApplicationModal)
        Search_window.resize(1180, 614)
        Search_window.setWindowTitle(u"Search")
        Search_window.setStyleSheet(u"background-color: rgb(3, 3, 13);")
        self.verticalLayout_4 = QVBoxLayout(Search_window)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget = QWidget(Search_window)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(16777215, 54))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.top_logo = QLabel(self.widget)
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
        self.top_logo.setPixmap(QPixmap(u":/newPrefix/ui/images/logo.png"))
        self.top_logo.setScaledContents(True)

        self.horizontalLayout.addWidget(self.top_logo)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addWidget(self.widget)

        self.search_viewer = QLabel(Search_window)
        self.search_viewer.setObjectName(u"search_viewer")
        self.search_viewer.setMinimumSize(QSize(640, 480))
        self.search_viewer.setFont(font)
        self.search_viewer.setStyleSheet(u"border: 1px solid rgb(119, 118, 123);\n"
"border-radius: 10px ;")
        self.search_viewer.setPixmap(QPixmap(u":/newPrefix/ui/images/logo.png"))
        self.search_viewer.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.search_viewer)


        self.horizontalLayout_14.addLayout(self.verticalLayout_2)

        self.widget_2 = QWidget(Search_window)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy1)
        self.widget_2.setMaximumSize(QSize(500, 16777215))
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.time_label = QLabel(self.widget_2)
        self.time_label.setObjectName(u"time_label")
        font1 = QFont()
        font1.setFamilies([u"Sans"])
        font1.setPointSize(11)
        self.time_label.setFont(font1)
        self.time_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(191, 64, 64, 0);")
        self.time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.time_label)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.time_day_start_input = QDateEdit(self.widget_2)
        self.time_day_start_input.setObjectName(u"time_day_start_input")
        self.time_day_start_input.setMinimumSize(QSize(115, 0))
        self.time_day_start_input.setMaximumSize(QSize(105, 16777215))
        font2 = QFont()
        font2.setFamilies([u"Sans"])
        font2.setPointSize(10)
        self.time_day_start_input.setFont(font2)
        self.time_day_start_input.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.time_day_start_input.setStyleSheet(u"QDateEdit {\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(13, 16, 23);\n"
"\n"
"}\n"
"QCalendarWidget {\n"
"    font-size: 11pt; /* \ud3f0\ud2b8 \ud06c\uae30\ub97c \ud06c\uac8c \uc124\uc815\ud558\uc5ec \uc804\uccb4 \ud06c\uae30 \uc99d\uac00 */\n"
"    background-color: rgb(87, 227, 137);\n"
"    alternate-background-color: rgb(87, 227, 137);\n"
"}\n"
"QCalendarWidget QWidget { /* All child widgets of QCalendarWidget */\n"
"color: rgb(255, 255, 255);\n"
"background-color: #323232;  \n"
"alternate-background-color: rgb(28, 113, 216);\n"
"border-radius: 15px;\n"
"}\n"
"QCalendarWidget QAbstractItemView {\n"
"selection-background-color: rgb(100, 100, 100);;\n"
"selection-color: white;\n"
"}\n"
"\n"
"\n"
"")
        self.time_day_start_input.setFrame(False)
        self.time_day_start_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time_day_start_input.setReadOnly(False)
        self.time_day_start_input.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.time_day_start_input.setCorrectionMode(QAbstractSpinBox.CorrectionMode.CorrectToNearestValue)
        self.time_day_start_input.setKeyboardTracking(True)
        self.time_day_start_input.setProperty("showGroupSeparator", False)
        self.time_day_start_input.setCurrentSection(QDateTimeEdit.Section.YearSection)
        self.time_day_start_input.setCalendarPopup(True)

        self.horizontalLayout_3.addWidget(self.time_day_start_input)

        self.time_hour_start_box = QComboBox(self.widget_2)
        self.time_hour_start_box.addItem("")
        self.time_hour_start_box.addItem("")
        self.time_hour_start_box.addItem("")
        self.time_hour_start_box.addItem("")
        self.time_hour_start_box.addItem("")
        self.time_hour_start_box.addItem("")
        self.time_hour_start_box.addItem("")
        self.time_hour_start_box.addItem("")
        self.time_hour_start_box.addItem("")
        self.time_hour_start_box.addItem("")
        self.time_hour_start_box.addItem("")
        self.time_hour_start_box.addItem("")
        self.time_hour_start_box.addItem("")
        self.time_hour_start_box.addItem("")
        self.time_hour_start_box.addItem("")
        self.time_hour_start_box.addItem("")
        self.time_hour_start_box.addItem("")
        self.time_hour_start_box.addItem("")
        self.time_hour_start_box.addItem("")
        self.time_hour_start_box.addItem("")
        self.time_hour_start_box.addItem("")
        self.time_hour_start_box.addItem("")
        self.time_hour_start_box.addItem("")
        self.time_hour_start_box.addItem("")
        self.time_hour_start_box.setObjectName(u"time_hour_start_box")
        self.time_hour_start_box.setMinimumSize(QSize(80, 24))
        self.time_hour_start_box.setMaximumSize(QSize(68, 16777215))
        font3 = QFont()
        font3.setFamilies([u"Sans"])
        font3.setPointSize(10)
        font3.setBold(False)
        self.time_hour_start_box.setFont(font3)
        self.time_hour_start_box.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(53, 132, 228);\n"
"")
        self.time_hour_start_box.setEditable(True)
        self.time_hour_start_box.setMinimumContentsLength(0)

        self.horizontalLayout_3.addWidget(self.time_hour_start_box)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)

        self.time_tilde = QLabel(self.widget_2)
        self.time_tilde.setObjectName(u"time_tilde")
        sizePolicy.setHeightForWidth(self.time_tilde.sizePolicy().hasHeightForWidth())
        self.time_tilde.setSizePolicy(sizePolicy)
        font4 = QFont()
        font4.setFamilies([u"Sans"])
        font4.setPointSize(12)
        self.time_tilde.setFont(font4)
        self.time_tilde.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(191, 64, 64, 0);")
        self.time_tilde.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.time_tilde)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.time_day_end_input = QDateEdit(self.widget_2)
        self.time_day_end_input.setObjectName(u"time_day_end_input")
        self.time_day_end_input.setMinimumSize(QSize(115, 0))
        self.time_day_end_input.setMaximumSize(QSize(105, 16777215))
        self.time_day_end_input.setFont(font2)
        self.time_day_end_input.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.time_day_end_input.setStyleSheet(u"QDateEdit {\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(13, 16, 23);\n"
"\n"
"}\n"
"QCalendarWidget {\n"
"    font-size: 11pt; /* \ud3f0\ud2b8 \ud06c\uae30\ub97c \ud06c\uac8c \uc124\uc815\ud558\uc5ec \uc804\uccb4 \ud06c\uae30 \uc99d\uac00 */\n"
"    background-color: rgb(87, 227, 137);\n"
"    alternate-background-color: rgb(87, 227, 137);\n"
"}\n"
"QCalendarWidget QWidget { /* All child widgets of QCalendarWidget */\n"
"color: rgb(255, 255, 255);\n"
"background-color: #323232;  \n"
"alternate-background-color: rgb(28, 113, 216);\n"
"border-radius: 15px;\n"
"}\n"
"QCalendarWidget QAbstractItemView {\n"
"selection-background-color: rgb(100, 100, 100);;\n"
"selection-color: white;\n"
"}\n"
"\n"
"\n"
"")
        self.time_day_end_input.setWrapping(False)
        self.time_day_end_input.setFrame(False)
        self.time_day_end_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time_day_end_input.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
        self.time_day_end_input.setCurrentSection(QDateTimeEdit.Section.YearSection)
        self.time_day_end_input.setCalendarPopup(True)

        self.horizontalLayout_6.addWidget(self.time_day_end_input)

        self.time_hour_end_box = QComboBox(self.widget_2)
        self.time_hour_end_box.addItem("")
        self.time_hour_end_box.addItem("")
        self.time_hour_end_box.addItem("")
        self.time_hour_end_box.addItem("")
        self.time_hour_end_box.addItem("")
        self.time_hour_end_box.addItem("")
        self.time_hour_end_box.addItem("")
        self.time_hour_end_box.addItem("")
        self.time_hour_end_box.addItem("")
        self.time_hour_end_box.addItem("")
        self.time_hour_end_box.addItem("")
        self.time_hour_end_box.addItem("")
        self.time_hour_end_box.addItem("")
        self.time_hour_end_box.addItem("")
        self.time_hour_end_box.addItem("")
        self.time_hour_end_box.addItem("")
        self.time_hour_end_box.addItem("")
        self.time_hour_end_box.addItem("")
        self.time_hour_end_box.addItem("")
        self.time_hour_end_box.addItem("")
        self.time_hour_end_box.addItem("")
        self.time_hour_end_box.addItem("")
        self.time_hour_end_box.addItem("")
        self.time_hour_end_box.addItem("")
        self.time_hour_end_box.setObjectName(u"time_hour_end_box")
        self.time_hour_end_box.setMinimumSize(QSize(80, 24))
        self.time_hour_end_box.setMaximumSize(QSize(68, 16777215))
        self.time_hour_end_box.setFont(font3)
        self.time_hour_end_box.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(53, 132, 228);\n"
"")
        self.time_hour_end_box.setEditable(True)
        self.time_hour_end_box.setMinimumContentsLength(0)

        self.horizontalLayout_6.addWidget(self.time_hour_end_box)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_6)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.camera_num_label = QLabel(self.widget_2)
        self.camera_num_label.setObjectName(u"camera_num_label")
        self.camera_num_label.setMaximumSize(QSize(81, 25))
        self.camera_num_label.setFont(font1)
        self.camera_num_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(191, 64, 64, 0);")
        self.camera_num_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_7.addWidget(self.camera_num_label)

        self.camera_name_box = QComboBox(self.widget_2)
        self.camera_name_box.setObjectName(u"camera_name_box")
        self.camera_name_box.setMinimumSize(QSize(128, 0))
        self.camera_name_box.setMaximumSize(QSize(16777215, 24))
        font5 = QFont()
        font5.setFamilies([u"Sans"])
        font5.setPointSize(11)
        font5.setBold(False)
        self.camera_name_box.setFont(font5)
        self.camera_name_box.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(13, 16, 23);\n"
"selection-background-color: rgb(53, 132, 228);\n"
"")
        self.camera_name_box.setMaxVisibleItems(16)
        self.camera_name_box.setMinimumContentsLength(0)

        self.horizontalLayout_7.addWidget(self.camera_name_box)


        self.horizontalLayout_8.addLayout(self.horizontalLayout_7)

        self.horizontalSpacer_3 = QSpacerItem(26, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.sort_label = QLabel(self.widget_2)
        self.sort_label.setObjectName(u"sort_label")
        self.sort_label.setMaximumSize(QSize(70, 57))
        self.sort_label.setFont(font4)
        self.sort_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(191, 64, 64, 0);")
        self.sort_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_9.addWidget(self.sort_label)

        self.sort_box = QComboBox(self.widget_2)
        self.sort_box.addItem("")
        self.sort_box.addItem("")
        self.sort_box.setObjectName(u"sort_box")
        self.sort_box.setMaximumSize(QSize(71, 16777215))
        self.sort_box.setFont(font5)
        self.sort_box.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(13, 16, 23);\n"
"selection-background-color: rgb(53, 132, 228);\n"
"")
        self.sort_box.setMinimumContentsLength(0)

        self.horizontalLayout_9.addWidget(self.sort_box)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_2)


        self.horizontalLayout_8.addLayout(self.horizontalLayout_9)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.event_label = QLabel(self.widget_2)
        self.event_label.setObjectName(u"event_label")
        self.event_label.setMaximumSize(QSize(52, 16777215))
        self.event_label.setFont(font4)
        self.event_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(191, 64, 64, 0);")
        self.event_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_10.addWidget(self.event_label)

        self.event_box = QComboBox(self.widget_2)
        self.event_box.addItem("")
        self.event_box.addItem("")
        self.event_box.addItem("")
        self.event_box.addItem("")
        self.event_box.addItem("")
        self.event_box.addItem("")
        self.event_box.setObjectName(u"event_box")
        self.event_box.setFont(font3)
        self.event_box.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(13, 16, 23);\n"
"selection-background-color: rgb(53, 132, 228);\n"
"")
        self.event_box.setMinimumContentsLength(0)

        self.horizontalLayout_10.addWidget(self.event_box)


        self.horizontalLayout_12.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.time_video_time_speed_label = QLabel(self.widget_2)
        self.time_video_time_speed_label.setObjectName(u"time_video_time_speed_label")
        self.time_video_time_speed_label.setMaximumSize(QSize(49, 16777215))
        self.time_video_time_speed_label.setFont(font1)
        self.time_video_time_speed_label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.time_video_time_speed_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.time_video_time_speed_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_11.addWidget(self.time_video_time_speed_label)

        self.time_video_time_speed_input = QDoubleSpinBox(self.widget_2)
        self.time_video_time_speed_input.setObjectName(u"time_video_time_speed_input")
        self.time_video_time_speed_input.setMinimumSize(QSize(88, 24))
        self.time_video_time_speed_input.setMaximumSize(QSize(65, 24))
        self.time_video_time_speed_input.setStyleSheet(u"\n"
"    QDoubleSpinBox {\n"
"        subcontrol-origin: padding;\n"
"        subcontrol-position: top right;\n"
"        background: rgb(13, 16, 23);\n"
"        color: rgb(255, 255, 255);\n"
"\n"
"    }")
        self.time_video_time_speed_input.setMinimum(1.000000000000000)
        self.time_video_time_speed_input.setMaximum(10.000000000000000)
        self.time_video_time_speed_input.setSingleStep(0.200000000000000)

        self.horizontalLayout_11.addWidget(self.time_video_time_speed_input)

        self.horizontalSpacer_4 = QSpacerItem(19, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_4)


        self.horizontalLayout_12.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.time_search_bnt = QPushButton(self.widget_2)
        self.time_search_bnt.setObjectName(u"time_search_bnt")
        self.time_search_bnt.setMinimumSize(QSize(61, 31))
        self.time_search_bnt.setMaximumSize(QSize(61, 31))
        self.time_search_bnt.setFont(font2)
        self.time_search_bnt.setCursor(QCursor(Qt.PointingHandCursor))
        self.time_search_bnt.setStyleSheet(u"background-color: rgb(30, 195, 55);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"")

        self.horizontalLayout_13.addWidget(self.time_search_bnt)

        self.search_close_bnt = QPushButton(self.widget_2)
        self.search_close_bnt.setObjectName(u"search_close_bnt")
        self.search_close_bnt.setMinimumSize(QSize(61, 31))
        self.search_close_bnt.setMaximumSize(QSize(61, 31))
        self.search_close_bnt.setFont(font2)
        self.search_close_bnt.setCursor(QCursor(Qt.PointingHandCursor))
        self.search_close_bnt.setStyleSheet(u"background-color: rgb(255, 49, 38);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"")

        self.horizontalLayout_13.addWidget(self.search_close_bnt)


        self.horizontalLayout_12.addLayout(self.horizontalLayout_13)


        self.verticalLayout_3.addLayout(self.horizontalLayout_12)

        self.event_table = QTableWidget(self.widget_2)
        if (self.event_table.columnCount() < 4):
            self.event_table.setColumnCount(4)
        font6 = QFont()
        font6.setPointSize(11)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font6);
        self.event_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font6);
        self.event_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font6);
        self.event_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font6);
        self.event_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.event_table.setObjectName(u"event_table")
        self.event_table.setMinimumSize(QSize(477, 5))
        self.event_table.setMaximumSize(QSize(477, 16777215))
        self.event_table.setFont(font5)
        self.event_table.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.event_table.setStyleSheet(u"QTableWidget {\n"
"    background-color: rgb(13, 16, 23); /* \ud14c\uc774\ube14 \uc804\uccb4 \ubc30\uacbd\uc0c9 */\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    color: rgb(209, 209, 209); /* \ud5e4\ub354 \ud14d\uc2a4\ud2b8 \uc0c9\uc0c1 - \ud68c\uc0c9 */\n"
"background-color: rgb(7, 7, 16); /* \ud14c\uc774\ube14 \uc804\uccb4 \ubc30\uacbd\uc0c9 */\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    color: rgb(255, 255, 255); /* \uae30\ubcf8 \uc0c1\ud0dc\uc5d0\uc11c\uc758 \ud14d\uc2a4\ud2b8 \uc0c9\uc0c1 - \ud770\uc0c9 */\n"
"\n"
"}\n"
"\n"
"QTableWidget::item:selected {\n"
"    background-color: rgb(32,39,49); /* \uc120\ud0dd\ub41c \uc140\uc758 \ubc30\uacbd\uc0c9 */\n"
"    color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    border: 1px solid #999999;\n"
"    background: #b3b3b3c6;\n"
"    width: 8px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"background: #2f2f2f; \n"
"min-height: 10px;\n"
"width: 8px;\n"
"\n"
"}\n"
"")
        self.event_table.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.event_table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.event_table.setTextElideMode(Qt.TextElideMode.ElideRight)
        self.event_table.setShowGrid(False)
        self.event_table.setGridStyle(Qt.PenStyle.DashDotLine)
        self.event_table.setSortingEnabled(False)
        self.event_table.setWordWrap(False)
        self.event_table.horizontalHeader().setVisible(True)
        self.event_table.horizontalHeader().setCascadingSectionResizes(False)
        self.event_table.horizontalHeader().setMinimumSectionSize(56)
        self.event_table.horizontalHeader().setHighlightSections(False)
        self.event_table.horizontalHeader().setStretchLastSection(True)
        self.event_table.verticalHeader().setVisible(False)
        self.event_table.verticalHeader().setMinimumSectionSize(21)
        self.event_table.verticalHeader().setDefaultSectionSize(30)
        self.event_table.verticalHeader().setHighlightSections(False)
        self.event_table.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_3.addWidget(self.event_table)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)


        self.horizontalLayout_14.addWidget(self.widget_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_14)


        self.retranslateUi(Search_window)

        QMetaObject.connectSlotsByName(Search_window)
    # setupUi

    def retranslateUi(self, Search_window):
        self.top_logo.setText("")
        self.search_viewer.setText("")
        self.time_label.setText(QCoreApplication.translate("Search_window", u"\uae30\uac04", None))
        self.time_day_start_input.setDisplayFormat(QCoreApplication.translate("Search_window", u"yyyy. M. d", None))
        self.time_hour_start_box.setItemText(0, QCoreApplication.translate("Search_window", u"00:00", None))
        self.time_hour_start_box.setItemText(1, QCoreApplication.translate("Search_window", u"01:00", None))
        self.time_hour_start_box.setItemText(2, QCoreApplication.translate("Search_window", u"02:00", None))
        self.time_hour_start_box.setItemText(3, QCoreApplication.translate("Search_window", u"03:00", None))
        self.time_hour_start_box.setItemText(4, QCoreApplication.translate("Search_window", u"04:00", None))
        self.time_hour_start_box.setItemText(5, QCoreApplication.translate("Search_window", u"05:00", None))
        self.time_hour_start_box.setItemText(6, QCoreApplication.translate("Search_window", u"06:00", None))
        self.time_hour_start_box.setItemText(7, QCoreApplication.translate("Search_window", u"07:00", None))
        self.time_hour_start_box.setItemText(8, QCoreApplication.translate("Search_window", u"08:00", None))
        self.time_hour_start_box.setItemText(9, QCoreApplication.translate("Search_window", u"09:00", None))
        self.time_hour_start_box.setItemText(10, QCoreApplication.translate("Search_window", u"10:00", None))
        self.time_hour_start_box.setItemText(11, QCoreApplication.translate("Search_window", u"11:00", None))
        self.time_hour_start_box.setItemText(12, QCoreApplication.translate("Search_window", u"12:00", None))
        self.time_hour_start_box.setItemText(13, QCoreApplication.translate("Search_window", u"13:00", None))
        self.time_hour_start_box.setItemText(14, QCoreApplication.translate("Search_window", u"14:00", None))
        self.time_hour_start_box.setItemText(15, QCoreApplication.translate("Search_window", u"15:00", None))
        self.time_hour_start_box.setItemText(16, QCoreApplication.translate("Search_window", u"16:00", None))
        self.time_hour_start_box.setItemText(17, QCoreApplication.translate("Search_window", u"17:00", None))
        self.time_hour_start_box.setItemText(18, QCoreApplication.translate("Search_window", u"18:00", None))
        self.time_hour_start_box.setItemText(19, QCoreApplication.translate("Search_window", u"19:00", None))
        self.time_hour_start_box.setItemText(20, QCoreApplication.translate("Search_window", u"20:00", None))
        self.time_hour_start_box.setItemText(21, QCoreApplication.translate("Search_window", u"21:00", None))
        self.time_hour_start_box.setItemText(22, QCoreApplication.translate("Search_window", u"22:00", None))
        self.time_hour_start_box.setItemText(23, QCoreApplication.translate("Search_window", u"23:00", None))

        self.time_tilde.setText(QCoreApplication.translate("Search_window", u"~", None))
        self.time_day_end_input.setDisplayFormat(QCoreApplication.translate("Search_window", u"yyyy. M. d", None))
        self.time_hour_end_box.setItemText(0, QCoreApplication.translate("Search_window", u"00:00", None))
        self.time_hour_end_box.setItemText(1, QCoreApplication.translate("Search_window", u"01:00", None))
        self.time_hour_end_box.setItemText(2, QCoreApplication.translate("Search_window", u"02:00", None))
        self.time_hour_end_box.setItemText(3, QCoreApplication.translate("Search_window", u"03:00", None))
        self.time_hour_end_box.setItemText(4, QCoreApplication.translate("Search_window", u"04:00", None))
        self.time_hour_end_box.setItemText(5, QCoreApplication.translate("Search_window", u"05:00", None))
        self.time_hour_end_box.setItemText(6, QCoreApplication.translate("Search_window", u"06:00", None))
        self.time_hour_end_box.setItemText(7, QCoreApplication.translate("Search_window", u"07:00", None))
        self.time_hour_end_box.setItemText(8, QCoreApplication.translate("Search_window", u"08:00", None))
        self.time_hour_end_box.setItemText(9, QCoreApplication.translate("Search_window", u"09:00", None))
        self.time_hour_end_box.setItemText(10, QCoreApplication.translate("Search_window", u"10:00", None))
        self.time_hour_end_box.setItemText(11, QCoreApplication.translate("Search_window", u"11:00", None))
        self.time_hour_end_box.setItemText(12, QCoreApplication.translate("Search_window", u"12:00", None))
        self.time_hour_end_box.setItemText(13, QCoreApplication.translate("Search_window", u"13:00", None))
        self.time_hour_end_box.setItemText(14, QCoreApplication.translate("Search_window", u"14:00", None))
        self.time_hour_end_box.setItemText(15, QCoreApplication.translate("Search_window", u"15:00", None))
        self.time_hour_end_box.setItemText(16, QCoreApplication.translate("Search_window", u"16:00", None))
        self.time_hour_end_box.setItemText(17, QCoreApplication.translate("Search_window", u"17:00", None))
        self.time_hour_end_box.setItemText(18, QCoreApplication.translate("Search_window", u"18:00", None))
        self.time_hour_end_box.setItemText(19, QCoreApplication.translate("Search_window", u"19:00", None))
        self.time_hour_end_box.setItemText(20, QCoreApplication.translate("Search_window", u"20:00", None))
        self.time_hour_end_box.setItemText(21, QCoreApplication.translate("Search_window", u"21:00", None))
        self.time_hour_end_box.setItemText(22, QCoreApplication.translate("Search_window", u"22:00", None))
        self.time_hour_end_box.setItemText(23, QCoreApplication.translate("Search_window", u"23:00", None))

        self.camera_num_label.setText(QCoreApplication.translate("Search_window", u"\uce74\uba54\ub77c \uc774\ub984", None))
        self.sort_label.setText(QCoreApplication.translate("Search_window", u"\uc815\ub82c", None))
        self.sort_box.setItemText(0, QCoreApplication.translate("Search_window", u"\ucd5c\uc2e0\uc21c", None))
        self.sort_box.setItemText(1, QCoreApplication.translate("Search_window", u"\uc2dc\uac04\uc21c", None))

        self.event_label.setText(QCoreApplication.translate("Search_window", u"\uc774\ubca4\ud2b8", None))
        self.event_box.setItemText(0, QCoreApplication.translate("Search_window", u"\uc804\uccb4", None))
        self.event_box.setItemText(1, QCoreApplication.translate("Search_window", u"\uce68\uc785", None))
        self.event_box.setItemText(2, QCoreApplication.translate("Search_window", u"\ubc30\ud68c", None))
        self.event_box.setItemText(3, QCoreApplication.translate("Search_window", u"\uc4f0\ub7ec\uc9d0", None))
        self.event_box.setItemText(4, QCoreApplication.translate("Search_window", u"\uc2f8\uc6c0", None))
        self.event_box.setItemText(5, QCoreApplication.translate("Search_window", u"\ubc29\ud654", None))

        self.time_video_time_speed_label.setText(QCoreApplication.translate("Search_window", u"\ubc30\uc18d", None))
        self.time_search_bnt.setText(QCoreApplication.translate("Search_window", u"\uac80\uc0c9", None))
        self.search_close_bnt.setText(QCoreApplication.translate("Search_window", u"\ub2eb\uae30", None))
        ___qtablewidgetitem = self.event_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Search_window", u"\ubc88\ud638", None));
        ___qtablewidgetitem1 = self.event_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Search_window", u"\uce74\uba54\ub77c", None));
        ___qtablewidgetitem2 = self.event_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Search_window", u"\uc885\ub958", None));
        ___qtablewidgetitem3 = self.event_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Search_window", u"\uc2dc\uac04", None));
        pass
    # retranslateUi

