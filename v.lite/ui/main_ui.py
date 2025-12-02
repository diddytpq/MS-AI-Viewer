# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QComboBox,
    QFrame, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QLineEdit, QListView, QListWidget,
    QListWidgetItem, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import resourece_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModality.NonModal)
        MainWindow.resize(1505, 804)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1270, 655))
        MainWindow.setMaximumSize(QSize(3840, 2160))
        MainWindow.setContextMenuPolicy(Qt.ContextMenuPolicy.PreventContextMenu)
        icon = QIcon()
        icon.addFile(u":/ui/ui/images/icon2.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: rgb(3, 3, 13);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_58 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetMinimumSize)
        self.top_logo = QLabel(self.centralwidget)
        self.top_logo.setObjectName(u"top_logo")
        self.top_logo.setMinimumSize(QSize(240, 38))
        self.top_logo.setMaximumSize(QSize(240, 38))
        font = QFont()
        font.setFamilies([u"Sans"])
        self.top_logo.setFont(font)
        self.top_logo.setPixmap(QPixmap(u":/ui/ui/images/logo.png"))
        self.top_logo.setScaledContents(True)

        self.horizontalLayout.addWidget(self.top_logo)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.verson_label = QLabel(self.centralwidget)
        self.verson_label.setObjectName(u"verson_label")
        self.verson_label.setMaximumSize(QSize(16777215, 21))
        font1 = QFont()
        font1.setFamilies([u"Sans"])
        font1.setPointSize(10)
        self.verson_label.setFont(font1)
        self.verson_label.setStyleSheet(u"color: rgb(255, 255, 255)")

        self.verticalLayout.addWidget(self.verson_label)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.server_icon = QLabel(self.centralwidget)
        self.server_icon.setObjectName(u"server_icon")
        self.server_icon.setMaximumSize(QSize(23, 23))
        self.server_icon.setFont(font)
        self.server_icon.setPixmap(QPixmap(u":/newPrefix/images/ico_server.svg"))
        self.server_icon.setScaledContents(True)

        self.horizontalLayout.addWidget(self.server_icon)

        self.server_info_label = QLabel(self.centralwidget)
        self.server_info_label.setObjectName(u"server_info_label")
        self.server_info_label.setMaximumSize(QSize(91, 41))
        font2 = QFont()
        font2.setFamilies([u"Sans"])
        font2.setPointSize(10)
        font2.setBold(True)
        self.server_info_label.setFont(font2)
        self.server_info_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.server_info_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.server_info_label)

        self.horizontalSpacer = QSpacerItem(20, 18, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.server_ip_label = QLabel(self.centralwidget)
        self.server_ip_label.setObjectName(u"server_ip_label")
        self.server_ip_label.setMaximumSize(QSize(72, 41))
        self.server_ip_label.setFont(font2)
        self.server_ip_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.server_ip_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.server_ip_label)

        self.server_ip_input = QLineEdit(self.centralwidget)
        self.server_ip_input.setObjectName(u"server_ip_input")
        self.server_ip_input.setMinimumSize(QSize(0, 31))
        self.server_ip_input.setMaximumSize(QSize(121, 31))
        self.server_ip_input.setFont(font1)
        self.server_ip_input.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.server_ip_input.setStyleSheet(u"qproperty-frame: false;\n"
"font-size:10pt;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);\n"
"lineedit-password-character: 9679; /* Unicode for '\u2022' */")
        self.server_ip_input.setEchoMode(QLineEdit.EchoMode.Normal)

        self.horizontalLayout.addWidget(self.server_ip_input)

        self.server_id_label = QLabel(self.centralwidget)
        self.server_id_label.setObjectName(u"server_id_label")
        self.server_id_label.setMaximumSize(QSize(61, 41))
        self.server_id_label.setFont(font2)
        self.server_id_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.server_id_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.server_id_label)

        self.server_id_input = QLineEdit(self.centralwidget)
        self.server_id_input.setObjectName(u"server_id_input")
        self.server_id_input.setMaximumSize(QSize(121, 41))
        self.server_id_input.setFont(font1)
        self.server_id_input.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.server_id_input.setStyleSheet(u"qproperty-frame: false;\n"
"font-size:10pt;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")

        self.horizontalLayout.addWidget(self.server_id_input)

        self.server_pw_label = QLabel(self.centralwidget)
        self.server_pw_label.setObjectName(u"server_pw_label")
        self.server_pw_label.setMaximumSize(QSize(61, 41))
        self.server_pw_label.setFont(font2)
        self.server_pw_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.server_pw_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout.addWidget(self.server_pw_label)

        self.server_pw_input = QLineEdit(self.centralwidget)
        self.server_pw_input.setObjectName(u"server_pw_input")
        self.server_pw_input.setMaximumSize(QSize(121, 41))
        self.server_pw_input.setFont(font1)
        self.server_pw_input.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.server_pw_input.setStyleSheet(u"qproperty-frame: false;\n"
"font-size:10pt;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.server_pw_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.horizontalLayout.addWidget(self.server_pw_input)

        self.server_login_bnt = QPushButton(self.centralwidget)
        self.server_login_bnt.setObjectName(u"server_login_bnt")
        self.server_login_bnt.setMinimumSize(QSize(51, 21))
        self.server_login_bnt.setMaximumSize(QSize(51, 21))
        font3 = QFont()
        font3.setFamilies([u"\ub9d1\uc740 \uace0\ub515"])
        font3.setPointSize(10)
        font3.setBold(False)
        self.server_login_bnt.setFont(font3)
        self.server_login_bnt.setCursor(QCursor(Qt.PointingHandCursor))
        self.server_login_bnt.setStyleSheet(u"\n"
"background-color: rgb(30, 195, 55);\n"
"\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"")

        self.horizontalLayout.addWidget(self.server_login_bnt)

        self.horizontalSpacer_2 = QSpacerItem(37, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.widget_6 = QWidget(self.centralwidget)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setStyleSheet(u"border-radius: 19px;\n"
"background-color: rgb(20, 22, 30);")
        self.horizontalLayout_64 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.horizontalLayout_65 = QHBoxLayout()
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.connected_user_icon_2 = QLabel(self.widget_6)
        self.connected_user_icon_2.setObjectName(u"connected_user_icon_2")
        self.connected_user_icon_2.setMaximumSize(QSize(19, 19))
        self.connected_user_icon_2.setFont(font2)
        self.connected_user_icon_2.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.connected_user_icon_2.setPixmap(QPixmap(u":/ui/ui/images/friends.png"))
        self.connected_user_icon_2.setScaledContents(True)
        self.connected_user_icon_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_65.addWidget(self.connected_user_icon_2)

        self.horizontalSpacer_72 = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_65.addItem(self.horizontalSpacer_72)

        self.connected_user_label_2 = QLabel(self.widget_6)
        self.connected_user_label_2.setObjectName(u"connected_user_label_2")
        self.connected_user_label_2.setMaximumSize(QSize(16, 22))
        font4 = QFont()
        font4.setFamilies([u"Sans"])
        font4.setPointSize(11)
        font4.setWeight(QFont.Medium)
        self.connected_user_label_2.setFont(font4)
        self.connected_user_label_2.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.connected_user_label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_65.addWidget(self.connected_user_label_2)


        self.horizontalLayout_64.addLayout(self.horizontalLayout_65)


        self.horizontalLayout.addWidget(self.widget_6)

        self.shutdown_bnt = QPushButton(self.centralwidget)
        self.shutdown_bnt.setObjectName(u"shutdown_bnt")
        self.shutdown_bnt.setMinimumSize(QSize(61, 31))
        self.shutdown_bnt.setMaximumSize(QSize(61, 31))
        font5 = QFont()
        font5.setFamilies([u"NanumSquareRound"])
        font5.setPointSize(10)
        font5.setBold(False)
        self.shutdown_bnt.setFont(font5)
        self.shutdown_bnt.setCursor(QCursor(Qt.PointingHandCursor))
        self.shutdown_bnt.setStyleSheet(u"background-color: rgb(255, 49, 38);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"")

        self.horizontalLayout.addWidget(self.shutdown_bnt)


        self.verticalLayout_11.addLayout(self.horizontalLayout)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tab_layout = QHBoxLayout()
        self.tab_layout.setObjectName(u"tab_layout")
        self.tab_backgournd = QWidget(self.centralwidget)
        self.tab_backgournd.setObjectName(u"tab_backgournd")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tab_backgournd.sizePolicy().hasHeightForWidth())
        self.tab_backgournd.setSizePolicy(sizePolicy1)
        self.tab_backgournd.setMinimumSize(QSize(522, 50))
        self.tab_backgournd.setMaximumSize(QSize(12345, 50))
        self.tab_backgournd.setStyleSheet(u"background-color: rgb(16, 20, 25);\n"
"\n"
"border-right: 1px solid rgb(119, 118, 123);\n"
"border-bottom-right-radius:20px solid rgb(119, 118, 123);\n"
"\n"
"border-bottom:1px solid rgb(119, 118, 123);\n"
"")
        self.horizontalLayout_14 = QHBoxLayout(self.tab_backgournd)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.camera_bnt = QPushButton(self.tab_backgournd)
        self.camera_bnt.setObjectName(u"camera_bnt")
        self.camera_bnt.setMinimumSize(QSize(163, 28))
        self.camera_bnt.setMaximumSize(QSize(163, 28))
        font6 = QFont()
        font6.setFamilies([u"Sans"])
        font6.setPointSize(13)
        self.camera_bnt.setFont(font6)
        self.camera_bnt.setCursor(QCursor(Qt.PointingHandCursor))
        self.camera_bnt.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 1px solid rgba(0, 0, 0, 0);\n"
"background-color: rgba(191, 64, 64, 0);")

        self.horizontalLayout_31.addWidget(self.camera_bnt)

        self.tab_partion_1 = QLabel(self.tab_backgournd)
        self.tab_partion_1.setObjectName(u"tab_partion_1")
        sizePolicy1.setHeightForWidth(self.tab_partion_1.sizePolicy().hasHeightForWidth())
        self.tab_partion_1.setSizePolicy(sizePolicy1)
        self.tab_partion_1.setMinimumSize(QSize(3, 0))
        font7 = QFont()
        font7.setFamilies([u"Sans"])
        font7.setPointSize(14)
        self.tab_partion_1.setFont(font7)
        self.tab_partion_1.setStyleSheet(u"color: rgb(119, 118, 123);\n"
"background-color: rgba(191, 64, 64, 0);\n"
"border: 1px solid rgba(0, 0, 0, 0);\n"
"background-color: rgba(0, 0 0, 0);")
        self.tab_partion_1.setTextFormat(Qt.TextFormat.PlainText)
        self.tab_partion_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_31.addWidget(self.tab_partion_1)

        self.search_bnt = QPushButton(self.tab_backgournd)
        self.search_bnt.setObjectName(u"search_bnt")
        self.search_bnt.setMinimumSize(QSize(163, 28))
        self.search_bnt.setMaximumSize(QSize(163, 28))
        self.search_bnt.setFont(font6)
        self.search_bnt.setCursor(QCursor(Qt.PointingHandCursor))
        self.search_bnt.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 1px solid rgba(0, 0, 0, 0);\n"
"background-color: rgba(191, 64, 64, 0);")

        self.horizontalLayout_31.addWidget(self.search_bnt)

        self.tab_partion_2 = QLabel(self.tab_backgournd)
        self.tab_partion_2.setObjectName(u"tab_partion_2")
        sizePolicy1.setHeightForWidth(self.tab_partion_2.sizePolicy().hasHeightForWidth())
        self.tab_partion_2.setSizePolicy(sizePolicy1)
        self.tab_partion_2.setMinimumSize(QSize(3, 0))
        self.tab_partion_2.setFont(font7)
        self.tab_partion_2.setStyleSheet(u"color: rgb(119, 118, 123);\n"
"background-color: rgba(191, 64, 64, 0);\n"
"border: 1px solid rgba(0, 0, 0, 0);\n"
"background-color: rgba(0, 0 0, 0);")
        self.tab_partion_2.setTextFormat(Qt.TextFormat.PlainText)
        self.tab_partion_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_31.addWidget(self.tab_partion_2)

        self.setting_bnt = QPushButton(self.tab_backgournd)
        self.setting_bnt.setObjectName(u"setting_bnt")
        self.setting_bnt.setMinimumSize(QSize(163, 28))
        self.setting_bnt.setMaximumSize(QSize(163, 28))
        self.setting_bnt.setFont(font6)
        self.setting_bnt.setCursor(QCursor(Qt.PointingHandCursor))
        self.setting_bnt.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(191, 64, 64, 0);\n"
"border: 1px solid rgba(0, 0, 0, 0);")

        self.horizontalLayout_31.addWidget(self.setting_bnt)

        self.tab_partion_3 = QLabel(self.tab_backgournd)
        self.tab_partion_3.setObjectName(u"tab_partion_3")
        sizePolicy1.setHeightForWidth(self.tab_partion_3.sizePolicy().hasHeightForWidth())
        self.tab_partion_3.setSizePolicy(sizePolicy1)
        self.tab_partion_3.setMinimumSize(QSize(3, 0))
        self.tab_partion_3.setFont(font7)
        self.tab_partion_3.setStyleSheet(u"color: rgb(119, 118, 123);\n"
"background-color: rgba(191, 64, 64, 0);\n"
"border: 1px solid rgba(0, 0, 0, 0);\n"
"background-color: rgba(0, 0 0, 0);")
        self.tab_partion_3.setTextFormat(Qt.TextFormat.PlainText)
        self.tab_partion_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_31.addWidget(self.tab_partion_3)

        self.admin_bnt = QPushButton(self.tab_backgournd)
        self.admin_bnt.setObjectName(u"admin_bnt")
        self.admin_bnt.setMinimumSize(QSize(163, 28))
        self.admin_bnt.setMaximumSize(QSize(163, 28))
        self.admin_bnt.setFont(font6)
        self.admin_bnt.setCursor(QCursor(Qt.PointingHandCursor))
        self.admin_bnt.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 1px solid rgba(0, 0, 0, 0);\n"
"background-color: rgba(191, 64, 64, 0);")

        self.horizontalLayout_31.addWidget(self.admin_bnt)


        self.horizontalLayout_14.addLayout(self.horizontalLayout_31)


        self.tab_layout.addWidget(self.tab_backgournd)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.tab_layout.addItem(self.horizontalSpacer_18)

        self.verticalLayout_55 = QVBoxLayout()
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.verticalSpacer_17 = QSpacerItem(20, 11, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_55.addItem(self.verticalSpacer_17)

        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setSpacing(9)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.labeling_bnt = QPushButton(self.centralwidget)
        self.labeling_bnt.setObjectName(u"labeling_bnt")
        self.labeling_bnt.setMinimumSize(QSize(37, 52))
        self.labeling_bnt.setFont(font1)
        self.labeling_bnt.setCursor(QCursor(Qt.PointingHandCursor))
        self.labeling_bnt.setStyleSheet(u"background-color: rgb(3, 3, 13);\n"
"border: 1px solid rgb(3, 3, 13);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/ui/ui/images/ico_ai_setting.png", QSize(), QIcon.Normal, QIcon.Off)
        self.labeling_bnt.setIcon(icon1)
        self.labeling_bnt.setIconSize(QSize(31, 50))

        self.horizontalLayout_36.addWidget(self.labeling_bnt)

        self.camera_schedule_bnt = QPushButton(self.centralwidget)
        self.camera_schedule_bnt.setObjectName(u"camera_schedule_bnt")
        self.camera_schedule_bnt.setMinimumSize(QSize(37, 52))
        self.camera_schedule_bnt.setFont(font1)
        self.camera_schedule_bnt.setCursor(QCursor(Qt.PointingHandCursor))
        self.camera_schedule_bnt.setStyleSheet(u"background-color: rgb(3, 3, 13);\n"
"border: 1px solid rgb(3, 3, 13);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/ui/ui/images/ico_timer.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.camera_schedule_bnt.setIcon(icon2)
        self.camera_schedule_bnt.setIconSize(QSize(31, 50))

        self.horizontalLayout_36.addWidget(self.camera_schedule_bnt)


        self.verticalLayout_55.addLayout(self.horizontalLayout_36)


        self.tab_layout.addLayout(self.verticalLayout_55)


        self.verticalLayout_2.addLayout(self.tab_layout)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy2)
        self.stackedWidget.setMinimumSize(QSize(790, 499))
        self.ai_camera_page = QWidget()
        self.ai_camera_page.setObjectName(u"ai_camera_page")
        self.horizontalLayout_3 = QHBoxLayout(self.ai_camera_page)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.widget_5 = QWidget(self.ai_camera_page)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMinimumSize(QSize(0, 0))
        self.widget_5.setMaximumSize(QSize(16777215, 25))
        self.verticalLayout_30 = QVBoxLayout(self.widget_5)
        self.verticalLayout_30.setSpacing(6)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_54 = QHBoxLayout()
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.horizontalLayout_63 = QHBoxLayout()
        self.horizontalLayout_63.setSpacing(0)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")

        self.horizontalLayout_54.addLayout(self.horizontalLayout_63)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_54.addItem(self.horizontalSpacer_14)


        self.verticalLayout_30.addLayout(self.horizontalLayout_54)


        self.verticalLayout_15.addWidget(self.widget_5)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalSpacer_26 = QSpacerItem(20, 3, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_10.addItem(self.verticalSpacer_26)

        self.camera_page_viewer = QLabel(self.ai_camera_page)
        self.camera_page_viewer.setObjectName(u"camera_page_viewer")
        sizePolicy2.setHeightForWidth(self.camera_page_viewer.sizePolicy().hasHeightForWidth())
        self.camera_page_viewer.setSizePolicy(sizePolicy2)
        self.camera_page_viewer.setMinimumSize(QSize(472, 360))
        self.camera_page_viewer.setMaximumSize(QSize(9999, 9999))
        font8 = QFont()
        font8.setFamilies([u"Sans"])
        font8.setPointSize(11)
        self.camera_page_viewer.setFont(font8)
        self.camera_page_viewer.setStyleSheet(u"border: 1px solid rgb(119, 118, 123);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.camera_page_viewer.setScaledContents(False)

        self.verticalLayout_10.addWidget(self.camera_page_viewer)


        self.verticalLayout_15.addLayout(self.verticalLayout_10)


        self.horizontalLayout_3.addLayout(self.verticalLayout_15)

        self.widget = QWidget(self.ai_camera_page)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(301, 351))
        self.widget.setMaximumSize(QSize(298, 9999))
        self.horizontalLayout_17 = QHBoxLayout(self.widget)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(-1, 0, 0, 0)
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(8)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.camera_page_camera_event_label = QLabel(self.widget)
        self.camera_page_camera_event_label.setObjectName(u"camera_page_camera_event_label")
        sizePolicy1.setHeightForWidth(self.camera_page_camera_event_label.sizePolicy().hasHeightForWidth())
        self.camera_page_camera_event_label.setSizePolicy(sizePolicy1)
        self.camera_page_camera_event_label.setMinimumSize(QSize(93, 31))
        font9 = QFont()
        font9.setFamilies([u"Sans"])
        font9.setPointSize(12)
        font9.setBold(True)
        self.camera_page_camera_event_label.setFont(font9)
        self.camera_page_camera_event_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.camera_page_camera_event_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_11.addWidget(self.camera_page_camera_event_label)

        self.camera_page_camera_event_box = QComboBox(self.widget)
        self.camera_page_camera_event_box.addItem("")
        self.camera_page_camera_event_box.addItem("")
        self.camera_page_camera_event_box.addItem("")
        self.camera_page_camera_event_box.addItem("")
        self.camera_page_camera_event_box.setObjectName(u"camera_page_camera_event_box")
        self.camera_page_camera_event_box.setMinimumSize(QSize(141, 39))
        self.camera_page_camera_event_box.setMaximumSize(QSize(141, 39))
        font10 = QFont()
        font10.setFamilies([u"Sans"])
        font10.setPointSize(11)
        font10.setBold(False)
        self.camera_page_camera_event_box.setFont(font10)
        self.camera_page_camera_event_box.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(13, 16, 23);\n"
"selection-background-color: rgb(53, 132, 228);\n"
"")
        self.camera_page_camera_event_box.setMaxVisibleItems(16)
        self.camera_page_camera_event_box.setMinimumContentsLength(0)

        self.horizontalLayout_11.addWidget(self.camera_page_camera_event_box)

        self.camera_page_detect_add_bnt = QPushButton(self.widget)
        self.camera_page_detect_add_bnt.setObjectName(u"camera_page_detect_add_bnt")
        sizePolicy1.setHeightForWidth(self.camera_page_detect_add_bnt.sizePolicy().hasHeightForWidth())
        self.camera_page_detect_add_bnt.setSizePolicy(sizePolicy1)
        self.camera_page_detect_add_bnt.setMinimumSize(QSize(31, 31))
        self.camera_page_detect_add_bnt.setFont(font1)
        self.camera_page_detect_add_bnt.setCursor(QCursor(Qt.PointingHandCursor))
        self.camera_page_detect_add_bnt.setStyleSheet(u"background-color: rgb(3, 3, 13);\n"
"border: 1px solid rgb(3, 3, 13);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/ui/ui/images/ico_add_circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.camera_page_detect_add_bnt.setIcon(icon3)
        self.camera_page_detect_add_bnt.setIconSize(QSize(31, 50))

        self.horizontalLayout_11.addWidget(self.camera_page_detect_add_bnt)

        self.horizontalSpacer_15 = QSpacerItem(30, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_15)


        self.verticalLayout_9.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.camera_page_detect_area_table = QTableWidget(self.widget)
        if (self.camera_page_detect_area_table.columnCount() < 1):
            self.camera_page_detect_area_table.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.camera_page_detect_area_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        self.camera_page_detect_area_table.setObjectName(u"camera_page_detect_area_table")
        self.camera_page_detect_area_table.setMinimumSize(QSize(120, 400))
        self.camera_page_detect_area_table.setMaximumSize(QSize(231, 9999))
        self.camera_page_detect_area_table.setFont(font)
        self.camera_page_detect_area_table.setStyleSheet(u"QTableWidget {\n"
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
        self.camera_page_detect_area_table.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.camera_page_detect_area_table.setDragDropOverwriteMode(False)
        self.camera_page_detect_area_table.setAlternatingRowColors(False)
        self.camera_page_detect_area_table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.camera_page_detect_area_table.setShowGrid(False)
        self.camera_page_detect_area_table.setGridStyle(Qt.PenStyle.NoPen)
        self.camera_page_detect_area_table.setWordWrap(False)
        self.camera_page_detect_area_table.setCornerButtonEnabled(False)
        self.camera_page_detect_area_table.horizontalHeader().setHighlightSections(False)
        self.camera_page_detect_area_table.horizontalHeader().setStretchLastSection(True)
        self.camera_page_detect_area_table.verticalHeader().setVisible(False)
        self.camera_page_detect_area_table.verticalHeader().setHighlightSections(False)

        self.horizontalLayout_12.addWidget(self.camera_page_detect_area_table)

        self.horizontalSpacer_7 = QSpacerItem(31, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_7)


        self.verticalLayout_9.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_20 = QSpacerItem(166, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_20)

        self.camera_page_object_setting_bnt = QPushButton(self.widget)
        self.camera_page_object_setting_bnt.setObjectName(u"camera_page_object_setting_bnt")
        sizePolicy1.setHeightForWidth(self.camera_page_object_setting_bnt.sizePolicy().hasHeightForWidth())
        self.camera_page_object_setting_bnt.setSizePolicy(sizePolicy1)
        self.camera_page_object_setting_bnt.setMinimumSize(QSize(100, 30))
        self.camera_page_object_setting_bnt.setMaximumSize(QSize(100, 30))
        self.camera_page_object_setting_bnt.setFont(font1)
        self.camera_page_object_setting_bnt.setCursor(QCursor(Qt.PointingHandCursor))
        self.camera_page_object_setting_bnt.setStyleSheet(u"background-color: rgb(36, 39, 44);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 12px;\n"
"\n"
"")

        self.horizontalLayout_13.addWidget(self.camera_page_object_setting_bnt)

        self.camera_page_detect_area_del_bnt = QPushButton(self.widget)
        self.camera_page_detect_area_del_bnt.setObjectName(u"camera_page_detect_area_del_bnt")
        sizePolicy1.setHeightForWidth(self.camera_page_detect_area_del_bnt.sizePolicy().hasHeightForWidth())
        self.camera_page_detect_area_del_bnt.setSizePolicy(sizePolicy1)
        self.camera_page_detect_area_del_bnt.setMinimumSize(QSize(61, 31))
        self.camera_page_detect_area_del_bnt.setMaximumSize(QSize(61, 31))
        self.camera_page_detect_area_del_bnt.setFont(font1)
        self.camera_page_detect_area_del_bnt.setCursor(QCursor(Qt.PointingHandCursor))
        self.camera_page_detect_area_del_bnt.setStyleSheet(u"background-color: rgb(255, 49, 38);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 12px;\n"
"")

        self.horizontalLayout_13.addWidget(self.camera_page_detect_area_del_bnt)

        self.horizontalSpacer_12 = QSpacerItem(70, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_12)


        self.verticalLayout_9.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalSpacer_13 = QSpacerItem(207, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_13)

        self.camera_page_ai_bnt = QPushButton(self.widget)
        self.camera_page_ai_bnt.setObjectName(u"camera_page_ai_bnt")
        sizePolicy1.setHeightForWidth(self.camera_page_ai_bnt.sizePolicy().hasHeightForWidth())
        self.camera_page_ai_bnt.setSizePolicy(sizePolicy1)
        self.camera_page_ai_bnt.setMinimumSize(QSize(122, 33))
        self.camera_page_ai_bnt.setFont(font1)
        self.camera_page_ai_bnt.setCursor(QCursor(Qt.PointingHandCursor))
        self.camera_page_ai_bnt.setStyleSheet(u"background-color: rgb(30, 195, 55);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"\n"
"")

        self.horizontalLayout_15.addWidget(self.camera_page_ai_bnt)

        self.horizontalSpacer_17 = QSpacerItem(63, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_17)


        self.verticalLayout_9.addLayout(self.horizontalLayout_15)

        self.verticalSpacer = QSpacerItem(20, 270, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_9.addItem(self.verticalSpacer)


        self.horizontalLayout_17.addLayout(self.verticalLayout_9)


        self.horizontalLayout_3.addWidget(self.widget)

        self.stackedWidget.addWidget(self.ai_camera_page)
        self.setting_page = QWidget()
        self.setting_page.setObjectName(u"setting_page")
        self.verticalLayout_53 = QVBoxLayout(self.setting_page)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.horizontalLayout_49 = QHBoxLayout()
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.setting_page_tab = QWidget(self.setting_page)
        self.setting_page_tab.setObjectName(u"setting_page_tab")
        self.setting_page_tab.setMinimumSize(QSize(190, 0))
        self.setting_page_tab.setMaximumSize(QSize(190, 16777215))
        self.verticalLayout_31 = QVBoxLayout(self.setting_page_tab)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_32 = QVBoxLayout()
        self.verticalLayout_32.setSpacing(12)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.setting_alarm_bnt = QPushButton(self.setting_page_tab)
        self.setting_alarm_bnt.setObjectName(u"setting_alarm_bnt")
        self.setting_alarm_bnt.setMinimumSize(QSize(171, 41))
        self.setting_alarm_bnt.setMaximumSize(QSize(171, 41))
        self.setting_alarm_bnt.setFont(font8)
        self.setting_alarm_bnt.setCursor(QCursor(Qt.PointingHandCursor))
        self.setting_alarm_bnt.setStyleSheet(u"border-radius: 15px;\n"
"\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 39, 44);")
        self.setting_alarm_bnt.setCheckable(True)
        self.setting_alarm_bnt.setChecked(False)
        self.setting_alarm_bnt.setAutoExclusive(True)

        self.verticalLayout_32.addWidget(self.setting_alarm_bnt)

        self.setting_user_setting_bnt = QPushButton(self.setting_page_tab)
        self.setting_user_setting_bnt.setObjectName(u"setting_user_setting_bnt")
        self.setting_user_setting_bnt.setMinimumSize(QSize(171, 41))
        self.setting_user_setting_bnt.setMaximumSize(QSize(171, 41))
        self.setting_user_setting_bnt.setFont(font8)
        self.setting_user_setting_bnt.setCursor(QCursor(Qt.PointingHandCursor))
        self.setting_user_setting_bnt.setStyleSheet(u"border-radius: 15px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 39, 44);\n"
"")
        self.setting_user_setting_bnt.setCheckable(True)
        self.setting_user_setting_bnt.setChecked(False)
        self.setting_user_setting_bnt.setAutoExclusive(True)

        self.verticalLayout_32.addWidget(self.setting_user_setting_bnt)

        self.setting_ai_bnt = QPushButton(self.setting_page_tab)
        self.setting_ai_bnt.setObjectName(u"setting_ai_bnt")
        self.setting_ai_bnt.setMinimumSize(QSize(171, 41))
        self.setting_ai_bnt.setMaximumSize(QSize(171, 41))
        self.setting_ai_bnt.setFont(font8)
        self.setting_ai_bnt.setCursor(QCursor(Qt.PointingHandCursor))
        self.setting_ai_bnt.setStyleSheet(u"border-radius: 15px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(36, 39, 44);\n"
"")
        self.setting_ai_bnt.setCheckable(True)
        self.setting_ai_bnt.setChecked(False)
        self.setting_ai_bnt.setAutoExclusive(True)

        self.verticalLayout_32.addWidget(self.setting_ai_bnt)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_32.addItem(self.verticalSpacer_8)


        self.verticalLayout_31.addLayout(self.verticalLayout_32)


        self.horizontalLayout_49.addWidget(self.setting_page_tab)

        self.setting_stack_widget = QStackedWidget(self.setting_page)
        self.setting_stack_widget.setObjectName(u"setting_stack_widget")
        self.setting_stack_widget.setStyleSheet(u"border-radius: 20px;\n"
"background-color: rgb(13, 16, 23);")
        self.setting_stack_widget.setFrameShape(QFrame.Shape.Box)
        self.setting_stack_widget.setFrameShadow(QFrame.Shadow.Plain)
        self.setting_notice_tab = QWidget()
        self.setting_notice_tab.setObjectName(u"setting_notice_tab")
        self.verticalLayout_14 = QVBoxLayout(self.setting_notice_tab)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.horizontalLayout_52 = QHBoxLayout()
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.horizontalSpacer_46 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_52.addItem(self.horizontalSpacer_46)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalSpacer_5 = QSpacerItem(20, 13, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_13.addItem(self.verticalSpacer_5)

        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setSpacing(1)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.setting_video_save_alarm_active_label = QLabel(self.setting_notice_tab)
        self.setting_video_save_alarm_active_label.setObjectName(u"setting_video_save_alarm_active_label")
        self.setting_video_save_alarm_active_label.setMinimumSize(QSize(173, 28))
        self.setting_video_save_alarm_active_label.setMaximumSize(QSize(9999, 28))
        self.setting_video_save_alarm_active_label.setFont(font8)
        self.setting_video_save_alarm_active_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.setting_video_save_alarm_active_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_26.addWidget(self.setting_video_save_alarm_active_label)

        self.setting_video_save_alarm_active_bnt = QPushButton(self.setting_notice_tab)
        self.setting_video_save_alarm_active_bnt.setObjectName(u"setting_video_save_alarm_active_bnt")
        self.setting_video_save_alarm_active_bnt.setMinimumSize(QSize(61, 25))
        self.setting_video_save_alarm_active_bnt.setMaximumSize(QSize(61, 25))
        icon4 = QIcon()
        icon4.addFile(u":/ui/ui/images/icon-switch-off.png", QSize(), QIcon.Normal, QIcon.Off)
        icon4.addFile(u":/ui/ui/images/icon-switch-on.png", QSize(), QIcon.Normal, QIcon.On)
        self.setting_video_save_alarm_active_bnt.setIcon(icon4)
        self.setting_video_save_alarm_active_bnt.setIconSize(QSize(55, 103))
        self.setting_video_save_alarm_active_bnt.setCheckable(True)

        self.horizontalLayout_26.addWidget(self.setting_video_save_alarm_active_bnt)

        self.horizontalSpacer_25 = QSpacerItem(40, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_25)


        self.verticalLayout_25.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalSpacer_31 = QSpacerItem(85, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_31)

        self.setting_event_video_storage_period_label = QLabel(self.setting_notice_tab)
        self.setting_event_video_storage_period_label.setObjectName(u"setting_event_video_storage_period_label")
        self.setting_event_video_storage_period_label.setMinimumSize(QSize(159, 28))
        self.setting_event_video_storage_period_label.setMaximumSize(QSize(9999, 28))
        self.setting_event_video_storage_period_label.setFont(font8)
        self.setting_event_video_storage_period_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.setting_event_video_storage_period_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_25.addWidget(self.setting_event_video_storage_period_label)

        self.setting_event_video_storage_period = QComboBox(self.setting_notice_tab)
        self.setting_event_video_storage_period.addItem("")
        self.setting_event_video_storage_period.addItem("")
        self.setting_event_video_storage_period.addItem("")
        self.setting_event_video_storage_period.setObjectName(u"setting_event_video_storage_period")
        self.setting_event_video_storage_period.setMinimumSize(QSize(61, 31))
        self.setting_event_video_storage_period.setMaximumSize(QSize(61, 31))
        self.setting_event_video_storage_period.setFont(font8)
        self.setting_event_video_storage_period.setFocusPolicy(Qt.FocusPolicy.WheelFocus)
        self.setting_event_video_storage_period.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(13, 16, 23);\n"
"selection-background-color: rgb(53, 132, 228);\n"
"")
        self.setting_event_video_storage_period.setCurrentText(u"30\uc77c")

        self.horizontalLayout_25.addWidget(self.setting_event_video_storage_period)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_24)


        self.verticalLayout_25.addLayout(self.horizontalLayout_25)


        self.verticalLayout_13.addLayout(self.verticalLayout_25)

        self.verticalSpacer_6 = QSpacerItem(20, 8, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_13.addItem(self.verticalSpacer_6)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalSpacer_30 = QSpacerItem(3, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_30)

        self.setting_popup_alarm_active_label = QLabel(self.setting_notice_tab)
        self.setting_popup_alarm_active_label.setObjectName(u"setting_popup_alarm_active_label")
        self.setting_popup_alarm_active_label.setMinimumSize(QSize(165, 28))
        self.setting_popup_alarm_active_label.setMaximumSize(QSize(200, 28))
        self.setting_popup_alarm_active_label.setFont(font8)
        self.setting_popup_alarm_active_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.setting_popup_alarm_active_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_24.addWidget(self.setting_popup_alarm_active_label)

        self.setting_popup_alarm_active_bnt = QPushButton(self.setting_notice_tab)
        self.setting_popup_alarm_active_bnt.setObjectName(u"setting_popup_alarm_active_bnt")
        self.setting_popup_alarm_active_bnt.setMinimumSize(QSize(61, 25))
        self.setting_popup_alarm_active_bnt.setMaximumSize(QSize(61, 25))
        self.setting_popup_alarm_active_bnt.setIcon(icon4)
        self.setting_popup_alarm_active_bnt.setIconSize(QSize(55, 103))
        self.setting_popup_alarm_active_bnt.setCheckable(True)

        self.horizontalLayout_24.addWidget(self.setting_popup_alarm_active_bnt)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_23)


        self.verticalLayout_13.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalSpacer_29 = QSpacerItem(85, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_29)

        self.setting_popup_alarm_cnt_label = QLabel(self.setting_notice_tab)
        self.setting_popup_alarm_cnt_label.setObjectName(u"setting_popup_alarm_cnt_label")
        self.setting_popup_alarm_cnt_label.setMinimumSize(QSize(137, 28))
        self.setting_popup_alarm_cnt_label.setMaximumSize(QSize(9999, 28))
        self.setting_popup_alarm_cnt_label.setFont(font8)
        self.setting_popup_alarm_cnt_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.setting_popup_alarm_cnt_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_23.addWidget(self.setting_popup_alarm_cnt_label)

        self.setting_popup_alarm_cnt = QComboBox(self.setting_notice_tab)
        self.setting_popup_alarm_cnt.addItem("")
        self.setting_popup_alarm_cnt.addItem("")
        self.setting_popup_alarm_cnt.addItem("")
        self.setting_popup_alarm_cnt.addItem("")
        self.setting_popup_alarm_cnt.addItem("")
        self.setting_popup_alarm_cnt.addItem("")
        self.setting_popup_alarm_cnt.addItem("")
        self.setting_popup_alarm_cnt.addItem("")
        self.setting_popup_alarm_cnt.addItem("")
        self.setting_popup_alarm_cnt.addItem("")
        self.setting_popup_alarm_cnt.setObjectName(u"setting_popup_alarm_cnt")
        self.setting_popup_alarm_cnt.setMinimumSize(QSize(61, 31))
        self.setting_popup_alarm_cnt.setMaximumSize(QSize(61, 31))
        self.setting_popup_alarm_cnt.setFont(font8)
        self.setting_popup_alarm_cnt.setFocusPolicy(Qt.FocusPolicy.WheelFocus)
        self.setting_popup_alarm_cnt.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(13, 16, 23);\n"
"selection-background-color: rgb(53, 132, 228);\n"
"")
        self.setting_popup_alarm_cnt.setCurrentText(u"3")

        self.horizontalLayout_23.addWidget(self.setting_popup_alarm_cnt)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_22)


        self.verticalLayout_13.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")

        self.verticalLayout_13.addLayout(self.horizontalLayout_20)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_12)


        self.horizontalLayout_52.addLayout(self.verticalLayout_13)

        self.horizontalSpacer_47 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_52.addItem(self.horizontalSpacer_47)


        self.verticalLayout_14.addLayout(self.horizontalLayout_52)

        self.setting_stack_widget.addWidget(self.setting_notice_tab)
        self.setting_user_setting_tab = QWidget()
        self.setting_user_setting_tab.setObjectName(u"setting_user_setting_tab")
        self.verticalLayout_51 = QVBoxLayout(self.setting_user_setting_tab)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_45 = QSpacerItem(15, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_45)

        self.verticalLayout_33 = QVBoxLayout()
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalSpacer_24 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_33.addItem(self.verticalSpacer_24)

        self.verticalLayout_29 = QVBoxLayout()
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.horizontalLayout_40 = QHBoxLayout()
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalSpacer_35 = QSpacerItem(48, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_40.addItem(self.horizontalSpacer_35)

        self.setting_user_id_label = QLabel(self.setting_user_setting_tab)
        self.setting_user_id_label.setObjectName(u"setting_user_id_label")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.setting_user_id_label.sizePolicy().hasHeightForWidth())
        self.setting_user_id_label.setSizePolicy(sizePolicy3)
        self.setting_user_id_label.setMinimumSize(QSize(60, 22))
        self.setting_user_id_label.setMaximumSize(QSize(60, 22))
        self.setting_user_id_label.setFont(font8)
        self.setting_user_id_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.setting_user_id_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_40.addWidget(self.setting_user_id_label)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.setting_user_id_input = QLineEdit(self.setting_user_setting_tab)
        self.setting_user_id_input.setObjectName(u"setting_user_id_input")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.setting_user_id_input.sizePolicy().hasHeightForWidth())
        self.setting_user_id_input.setSizePolicy(sizePolicy4)
        self.setting_user_id_input.setMinimumSize(QSize(246, 19))
        self.setting_user_id_input.setMaximumSize(QSize(9999, 19))
        self.setting_user_id_input.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.setting_user_id_input.setReadOnly(True)

        self.verticalLayout_20.addWidget(self.setting_user_id_input)

        self.setting_user_id_input_line = QFrame(self.setting_user_setting_tab)
        self.setting_user_id_input_line.setObjectName(u"setting_user_id_input_line")
        self.setting_user_id_input_line.setMinimumSize(QSize(246, 3))
        self.setting_user_id_input_line.setMaximumSize(QSize(246, 3))
        font11 = QFont()
        font11.setFamilies([u"Sans"])
        font11.setPointSize(5)
        font11.setStrikeOut(False)
        self.setting_user_id_input_line.setFont(font11)
        self.setting_user_id_input_line.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.setting_user_id_input_line.setAutoFillBackground(False)
        self.setting_user_id_input_line.setStyleSheet(u"background-color: rgb(36, 39, 44)")
        self.setting_user_id_input_line.setFrameShape(QFrame.Shape.HLine)
        self.setting_user_id_input_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_20.addWidget(self.setting_user_id_input_line)


        self.horizontalLayout_40.addLayout(self.verticalLayout_20)


        self.verticalLayout_29.addLayout(self.horizontalLayout_40)

        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setSpacing(6)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalSpacer_60 = QSpacerItem(5, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_39.addItem(self.horizontalSpacer_60)

        self.setting_user_pw_label = QLabel(self.setting_user_setting_tab)
        self.setting_user_pw_label.setObjectName(u"setting_user_pw_label")
        sizePolicy3.setHeightForWidth(self.setting_user_pw_label.sizePolicy().hasHeightForWidth())
        self.setting_user_pw_label.setSizePolicy(sizePolicy3)
        self.setting_user_pw_label.setMinimumSize(QSize(104, 22))
        self.setting_user_pw_label.setMaximumSize(QSize(104, 22))
        self.setting_user_pw_label.setFont(font8)
        self.setting_user_pw_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.setting_user_pw_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_39.addWidget(self.setting_user_pw_label)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setSpacing(5)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.setting_user_pw_input = QLineEdit(self.setting_user_setting_tab)
        self.setting_user_pw_input.setObjectName(u"setting_user_pw_input")
        sizePolicy4.setHeightForWidth(self.setting_user_pw_input.sizePolicy().hasHeightForWidth())
        self.setting_user_pw_input.setSizePolicy(sizePolicy4)
        self.setting_user_pw_input.setMinimumSize(QSize(246, 19))
        self.setting_user_pw_input.setMaximumSize(QSize(9999, 19))
        self.setting_user_pw_input.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.setting_user_pw_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout_19.addWidget(self.setting_user_pw_input)

        self.setting_user_pw_input_line = QFrame(self.setting_user_setting_tab)
        self.setting_user_pw_input_line.setObjectName(u"setting_user_pw_input_line")
        self.setting_user_pw_input_line.setMinimumSize(QSize(246, 3))
        self.setting_user_pw_input_line.setMaximumSize(QSize(246, 3))
        self.setting_user_pw_input_line.setFont(font11)
        self.setting_user_pw_input_line.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.setting_user_pw_input_line.setAutoFillBackground(False)
        self.setting_user_pw_input_line.setStyleSheet(u"background-color: rgb(36, 39, 44)")
        self.setting_user_pw_input_line.setFrameShape(QFrame.Shape.HLine)
        self.setting_user_pw_input_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_19.addWidget(self.setting_user_pw_input_line)


        self.horizontalLayout_39.addLayout(self.verticalLayout_19)


        self.verticalLayout_29.addLayout(self.horizontalLayout_39)

        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalSpacer_61 = QSpacerItem(6, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_37.addItem(self.horizontalSpacer_61)

        self.setting_user_new_pw_label = QLabel(self.setting_user_setting_tab)
        self.setting_user_new_pw_label.setObjectName(u"setting_user_new_pw_label")
        sizePolicy3.setHeightForWidth(self.setting_user_new_pw_label.sizePolicy().hasHeightForWidth())
        self.setting_user_new_pw_label.setSizePolicy(sizePolicy3)
        self.setting_user_new_pw_label.setMinimumSize(QSize(104, 22))
        self.setting_user_new_pw_label.setMaximumSize(QSize(104, 22))
        self.setting_user_new_pw_label.setFont(font8)
        self.setting_user_new_pw_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.setting_user_new_pw_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_37.addWidget(self.setting_user_new_pw_label)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.setting_user_new_pw_input = QLineEdit(self.setting_user_setting_tab)
        self.setting_user_new_pw_input.setObjectName(u"setting_user_new_pw_input")
        sizePolicy4.setHeightForWidth(self.setting_user_new_pw_input.sizePolicy().hasHeightForWidth())
        self.setting_user_new_pw_input.setSizePolicy(sizePolicy4)
        self.setting_user_new_pw_input.setMinimumSize(QSize(246, 19))
        self.setting_user_new_pw_input.setMaximumSize(QSize(9999, 19))
        self.setting_user_new_pw_input.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.setting_user_new_pw_input.setFrame(True)
        self.setting_user_new_pw_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout_17.addWidget(self.setting_user_new_pw_input)

        self.setting_user_new_pw_input_line = QFrame(self.setting_user_setting_tab)
        self.setting_user_new_pw_input_line.setObjectName(u"setting_user_new_pw_input_line")
        self.setting_user_new_pw_input_line.setMinimumSize(QSize(246, 3))
        self.setting_user_new_pw_input_line.setMaximumSize(QSize(246, 3))
        self.setting_user_new_pw_input_line.setFont(font11)
        self.setting_user_new_pw_input_line.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.setting_user_new_pw_input_line.setAutoFillBackground(False)
        self.setting_user_new_pw_input_line.setStyleSheet(u"background-color: rgb(36, 39, 44)")
        self.setting_user_new_pw_input_line.setFrameShape(QFrame.Shape.HLine)
        self.setting_user_new_pw_input_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_17.addWidget(self.setting_user_new_pw_input_line)


        self.horizontalLayout_37.addLayout(self.verticalLayout_17)


        self.verticalLayout_29.addLayout(self.horizontalLayout_37)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalSpacer_62 = QSpacerItem(7, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_33.addItem(self.horizontalSpacer_62)

        self.setting_user_new_pw_label2 = QLabel(self.setting_user_setting_tab)
        self.setting_user_new_pw_label2.setObjectName(u"setting_user_new_pw_label2")
        sizePolicy3.setHeightForWidth(self.setting_user_new_pw_label2.sizePolicy().hasHeightForWidth())
        self.setting_user_new_pw_label2.setSizePolicy(sizePolicy3)
        self.setting_user_new_pw_label2.setMinimumSize(QSize(104, 27))
        self.setting_user_new_pw_label2.setMaximumSize(QSize(104, 27))
        self.setting_user_new_pw_label2.setFont(font8)
        self.setting_user_new_pw_label2.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.setting_user_new_pw_label2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_33.addWidget(self.setting_user_new_pw_label2)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.setting_user_new_pw_input2 = QLineEdit(self.setting_user_setting_tab)
        self.setting_user_new_pw_input2.setObjectName(u"setting_user_new_pw_input2")
        sizePolicy4.setHeightForWidth(self.setting_user_new_pw_input2.sizePolicy().hasHeightForWidth())
        self.setting_user_new_pw_input2.setSizePolicy(sizePolicy4)
        self.setting_user_new_pw_input2.setMinimumSize(QSize(246, 19))
        self.setting_user_new_pw_input2.setMaximumSize(QSize(9999, 19))
        self.setting_user_new_pw_input2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.setting_user_new_pw_input2.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout_18.addWidget(self.setting_user_new_pw_input2)

        self.setting_user_new_pw_input2_line = QFrame(self.setting_user_setting_tab)
        self.setting_user_new_pw_input2_line.setObjectName(u"setting_user_new_pw_input2_line")
        self.setting_user_new_pw_input2_line.setMinimumSize(QSize(246, 3))
        self.setting_user_new_pw_input2_line.setMaximumSize(QSize(246, 3))
        self.setting_user_new_pw_input2_line.setFont(font11)
        self.setting_user_new_pw_input2_line.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.setting_user_new_pw_input2_line.setAutoFillBackground(False)
        self.setting_user_new_pw_input2_line.setStyleSheet(u"background-color: rgb(36, 39, 44)")
        self.setting_user_new_pw_input2_line.setFrameShape(QFrame.Shape.HLine)
        self.setting_user_new_pw_input2_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_18.addWidget(self.setting_user_new_pw_input2_line)


        self.horizontalLayout_33.addLayout(self.verticalLayout_18)


        self.verticalLayout_29.addLayout(self.horizontalLayout_33)

        self.horizontalLayout_41 = QHBoxLayout()
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalSpacer_36 = QSpacerItem(280, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_41.addItem(self.horizontalSpacer_36)

        self.setting_user_save_bnt = QPushButton(self.setting_user_setting_tab)
        self.setting_user_save_bnt.setObjectName(u"setting_user_save_bnt")
        self.setting_user_save_bnt.setMinimumSize(QSize(71, 41))
        self.setting_user_save_bnt.setMaximumSize(QSize(71, 41))
        self.setting_user_save_bnt.setFont(font1)
        self.setting_user_save_bnt.setCursor(QCursor(Qt.PointingHandCursor))
        self.setting_user_save_bnt.setStyleSheet(u"background-color: rgb(30, 195, 55);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"\n"
"")

        self.horizontalLayout_41.addWidget(self.setting_user_save_bnt)


        self.verticalLayout_29.addLayout(self.horizontalLayout_41)


        self.verticalLayout_33.addLayout(self.verticalLayout_29)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_33.addItem(self.verticalSpacer_13)


        self.horizontalLayout_2.addLayout(self.verticalLayout_33)

        self.horizontalSpacer_44 = QSpacerItem(452, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_44)


        self.verticalLayout_51.addLayout(self.horizontalLayout_2)

        self.setting_stack_widget.addWidget(self.setting_user_setting_tab)
        self.setting_ai_tab = QWidget()
        self.setting_ai_tab.setObjectName(u"setting_ai_tab")
        self.verticalLayout_59 = QVBoxLayout(self.setting_ai_tab)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.verticalLayout_52 = QVBoxLayout()
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.horizontalLayout_53 = QHBoxLayout()
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.verticalLayout_54 = QVBoxLayout()
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.verticalLayout_56 = QVBoxLayout()
        self.verticalLayout_56.setSpacing(13)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.horizontalLayout_55 = QHBoxLayout()
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalSpacer_52 = QSpacerItem(36, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_55.addItem(self.horizontalSpacer_52)

        self.setting_ai_weight_label = QLabel(self.setting_ai_tab)
        self.setting_ai_weight_label.setObjectName(u"setting_ai_weight_label")
        sizePolicy1.setHeightForWidth(self.setting_ai_weight_label.sizePolicy().hasHeightForWidth())
        self.setting_ai_weight_label.setSizePolicy(sizePolicy1)
        self.setting_ai_weight_label.setMinimumSize(QSize(176, 28))
        self.setting_ai_weight_label.setMaximumSize(QSize(9999, 28))
        self.setting_ai_weight_label.setFont(font8)
        self.setting_ai_weight_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.setting_ai_weight_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_55.addWidget(self.setting_ai_weight_label)

        self.horizontalSpacer_70 = QSpacerItem(59, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_55.addItem(self.horizontalSpacer_70)

        self.setting_setting_ai_weight_box = QComboBox(self.setting_ai_tab)
        self.setting_setting_ai_weight_box.addItem("")
        self.setting_setting_ai_weight_box.setObjectName(u"setting_setting_ai_weight_box")
        sizePolicy1.setHeightForWidth(self.setting_setting_ai_weight_box.sizePolicy().hasHeightForWidth())
        self.setting_setting_ai_weight_box.setSizePolicy(sizePolicy1)
        self.setting_setting_ai_weight_box.setMinimumSize(QSize(105, 31))
        self.setting_setting_ai_weight_box.setMaximumSize(QSize(105, 31))
        font12 = QFont()
        font12.setFamilies([u"Sans"])
        font12.setPointSize(10)
        font12.setBold(False)
        self.setting_setting_ai_weight_box.setFont(font12)
        self.setting_setting_ai_weight_box.setFocusPolicy(Qt.FocusPolicy.WheelFocus)
        self.setting_setting_ai_weight_box.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(13, 16, 23);\n"
"selection-background-color: rgb(53, 132, 228);\n"
"")
        self.setting_setting_ai_weight_box.setCurrentText(u"2024-07-24")
        self.setting_setting_ai_weight_box.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)

        self.horizontalLayout_55.addWidget(self.setting_setting_ai_weight_box)

        self.horizontalSpacer_53 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_55.addItem(self.horizontalSpacer_53)


        self.verticalLayout_56.addLayout(self.horizontalLayout_55)

        self.horizontalLayout_56 = QHBoxLayout()
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.horizontalSpacer_54 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_56.addItem(self.horizontalSpacer_54)

        self.setting_self_training_auto_labeling_label = QLabel(self.setting_ai_tab)
        self.setting_self_training_auto_labeling_label.setObjectName(u"setting_self_training_auto_labeling_label")
        sizePolicy1.setHeightForWidth(self.setting_self_training_auto_labeling_label.sizePolicy().hasHeightForWidth())
        self.setting_self_training_auto_labeling_label.setSizePolicy(sizePolicy1)
        self.setting_self_training_auto_labeling_label.setMinimumSize(QSize(1, 28))
        self.setting_self_training_auto_labeling_label.setMaximumSize(QSize(194, 28))
        self.setting_self_training_auto_labeling_label.setFont(font8)
        self.setting_self_training_auto_labeling_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.setting_self_training_auto_labeling_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_56.addWidget(self.setting_self_training_auto_labeling_label)

        self.horizontalSpacer_55 = QSpacerItem(92, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_56.addItem(self.horizontalSpacer_55)

        self.setting_self_training_auto_labeling_bnt = QPushButton(self.setting_ai_tab)
        self.setting_self_training_auto_labeling_bnt.setObjectName(u"setting_self_training_auto_labeling_bnt")
        sizePolicy1.setHeightForWidth(self.setting_self_training_auto_labeling_bnt.sizePolicy().hasHeightForWidth())
        self.setting_self_training_auto_labeling_bnt.setSizePolicy(sizePolicy1)
        self.setting_self_training_auto_labeling_bnt.setMinimumSize(QSize(61, 25))
        self.setting_self_training_auto_labeling_bnt.setMaximumSize(QSize(187, 25))
        self.setting_self_training_auto_labeling_bnt.setIcon(icon4)
        self.setting_self_training_auto_labeling_bnt.setIconSize(QSize(55, 103))
        self.setting_self_training_auto_labeling_bnt.setCheckable(True)

        self.horizontalLayout_56.addWidget(self.setting_self_training_auto_labeling_bnt)

        self.horizontalSpacer_56 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_56.addItem(self.horizontalSpacer_56)


        self.verticalLayout_56.addLayout(self.horizontalLayout_56)

        self.verticalLayout_57 = QVBoxLayout()
        self.verticalLayout_57.setSpacing(5)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.horizontalLayout_57 = QHBoxLayout()
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.horizontalSpacer_57 = QSpacerItem(41, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_57.addItem(self.horizontalSpacer_57)

        self.setting_self_training_zeroshot_label = QLabel(self.setting_ai_tab)
        self.setting_self_training_zeroshot_label.setObjectName(u"setting_self_training_zeroshot_label")
        sizePolicy1.setHeightForWidth(self.setting_self_training_zeroshot_label.sizePolicy().hasHeightForWidth())
        self.setting_self_training_zeroshot_label.setSizePolicy(sizePolicy1)
        self.setting_self_training_zeroshot_label.setMinimumSize(QSize(9, 28))
        self.setting_self_training_zeroshot_label.setMaximumSize(QSize(300, 28))
        self.setting_self_training_zeroshot_label.setFont(font8)
        self.setting_self_training_zeroshot_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.setting_self_training_zeroshot_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_57.addWidget(self.setting_self_training_zeroshot_label)

        self.horizontalSpacer_58 = QSpacerItem(68, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_57.addItem(self.horizontalSpacer_58)

        self.setting_self_training_zeroshot_bnt = QPushButton(self.setting_ai_tab)
        self.setting_self_training_zeroshot_bnt.setObjectName(u"setting_self_training_zeroshot_bnt")
        sizePolicy1.setHeightForWidth(self.setting_self_training_zeroshot_bnt.sizePolicy().hasHeightForWidth())
        self.setting_self_training_zeroshot_bnt.setSizePolicy(sizePolicy1)
        self.setting_self_training_zeroshot_bnt.setMinimumSize(QSize(61, 25))
        self.setting_self_training_zeroshot_bnt.setMaximumSize(QSize(151, 25))
        self.setting_self_training_zeroshot_bnt.setIcon(icon4)
        self.setting_self_training_zeroshot_bnt.setIconSize(QSize(55, 103))
        self.setting_self_training_zeroshot_bnt.setCheckable(True)

        self.horizontalLayout_57.addWidget(self.setting_self_training_zeroshot_bnt)

        self.horizontalSpacer_59 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_57.addItem(self.horizontalSpacer_59)


        self.verticalLayout_57.addLayout(self.horizontalLayout_57)

        self.verticalLayout_58 = QVBoxLayout()
        self.verticalLayout_58.setSpacing(0)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.horizontalLayout_59 = QHBoxLayout()
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.horizontalSpacer_63 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_59.addItem(self.horizontalSpacer_63)

        self.setting_page_email_info_label_5 = QLabel(self.setting_ai_tab)
        self.setting_page_email_info_label_5.setObjectName(u"setting_page_email_info_label_5")
        sizePolicy1.setHeightForWidth(self.setting_page_email_info_label_5.sizePolicy().hasHeightForWidth())
        self.setting_page_email_info_label_5.setSizePolicy(sizePolicy1)
        self.setting_page_email_info_label_5.setMinimumSize(QSize(12, 21))
        self.setting_page_email_info_label_5.setMaximumSize(QSize(9999, 21))
        self.setting_page_email_info_label_5.setFont(font1)
        self.setting_page_email_info_label_5.setStyleSheet(u"color: rgb(242, 18, 94);")

        self.horizontalLayout_59.addWidget(self.setting_page_email_info_label_5)

        self.horizontalSpacer_64 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_59.addItem(self.horizontalSpacer_64)


        self.verticalLayout_58.addLayout(self.horizontalLayout_59)

        self.horizontalLayout_60 = QHBoxLayout()
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.horizontalSpacer_65 = QSpacerItem(48, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_60.addItem(self.horizontalSpacer_65)

        self.setting_page_email_info_label_6 = QLabel(self.setting_ai_tab)
        self.setting_page_email_info_label_6.setObjectName(u"setting_page_email_info_label_6")
        sizePolicy1.setHeightForWidth(self.setting_page_email_info_label_6.sizePolicy().hasHeightForWidth())
        self.setting_page_email_info_label_6.setSizePolicy(sizePolicy1)
        self.setting_page_email_info_label_6.setMinimumSize(QSize(1, 21))
        self.setting_page_email_info_label_6.setMaximumSize(QSize(9999, 21))
        self.setting_page_email_info_label_6.setFont(font1)
        self.setting_page_email_info_label_6.setStyleSheet(u"color: rgb(242, 18, 94);")

        self.horizontalLayout_60.addWidget(self.setting_page_email_info_label_6)

        self.horizontalSpacer_66 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_60.addItem(self.horizontalSpacer_66)


        self.verticalLayout_58.addLayout(self.horizontalLayout_60)


        self.verticalLayout_57.addLayout(self.verticalLayout_58)


        self.verticalLayout_56.addLayout(self.verticalLayout_57)


        self.verticalLayout_54.addLayout(self.verticalLayout_56)

        self.horizontalLayout_61 = QHBoxLayout()
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.horizontalSpacer_67 = QSpacerItem(338, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_61.addItem(self.horizontalSpacer_67)

        self.setting_ai_setting_save_bnt = QPushButton(self.setting_ai_tab)
        self.setting_ai_setting_save_bnt.setObjectName(u"setting_ai_setting_save_bnt")
        sizePolicy1.setHeightForWidth(self.setting_ai_setting_save_bnt.sizePolicy().hasHeightForWidth())
        self.setting_ai_setting_save_bnt.setSizePolicy(sizePolicy1)
        self.setting_ai_setting_save_bnt.setMinimumSize(QSize(76, 39))
        self.setting_ai_setting_save_bnt.setMaximumSize(QSize(76, 39))
        self.setting_ai_setting_save_bnt.setFont(font1)
        self.setting_ai_setting_save_bnt.setCursor(QCursor(Qt.PointingHandCursor))
        self.setting_ai_setting_save_bnt.setStyleSheet(u"\n"
"\n"
"background-color: rgb(30, 195, 55);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 19px;\n"
"\n"
"")

        self.horizontalLayout_61.addWidget(self.setting_ai_setting_save_bnt)

        self.horizontalSpacer_69 = QSpacerItem(40, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_61.addItem(self.horizontalSpacer_69)


        self.verticalLayout_54.addLayout(self.horizontalLayout_61)


        self.horizontalLayout_53.addLayout(self.verticalLayout_54)

        self.horizontalSpacer_68 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_53.addItem(self.horizontalSpacer_68)


        self.verticalLayout_52.addLayout(self.horizontalLayout_53)

        self.verticalSpacer_28 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_52.addItem(self.verticalSpacer_28)


        self.verticalLayout_59.addLayout(self.verticalLayout_52)

        self.setting_stack_widget.addWidget(self.setting_ai_tab)

        self.horizontalLayout_49.addWidget(self.setting_stack_widget)


        self.verticalLayout_53.addLayout(self.horizontalLayout_49)

        self.stackedWidget.addWidget(self.setting_page)
        self.admin_page = QWidget()
        self.admin_page.setObjectName(u"admin_page")
        self.verticalLayout_37 = QVBoxLayout(self.admin_page)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_36 = QVBoxLayout()
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalSpacer_14 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_36.addItem(self.verticalSpacer_14)

        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalSpacer_37 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_38.addItem(self.horizontalSpacer_37)

        self.admin_pw_label = QLabel(self.admin_page)
        self.admin_pw_label.setObjectName(u"admin_pw_label")
        self.admin_pw_label.setMinimumSize(QSize(115, 46))
        self.admin_pw_label.setMaximumSize(QSize(115, 46))
        font13 = QFont()
        font13.setFamilies([u"Sans"])
        font13.setPointSize(12)
        self.admin_pw_label.setFont(font13)
        self.admin_pw_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.admin_pw_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_38.addWidget(self.admin_pw_label)

        self.verticalLayout_35 = QVBoxLayout()
        self.verticalLayout_35.setSpacing(0)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.admin_pw_input = QLineEdit(self.admin_page)
        self.admin_pw_input.setObjectName(u"admin_pw_input")
        self.admin_pw_input.setMinimumSize(QSize(221, 21))
        self.admin_pw_input.setMaximumSize(QSize(221, 21))
        self.admin_pw_input.setFont(font1)
        self.admin_pw_input.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.admin_pw_input.setStyleSheet(u"qproperty-frame: false;\n"
"font-size:10pt;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.admin_pw_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout_35.addWidget(self.admin_pw_input)

        self.admin_pw_input_line = QFrame(self.admin_page)
        self.admin_pw_input_line.setObjectName(u"admin_pw_input_line")
        self.admin_pw_input_line.setMinimumSize(QSize(221, 3))
        self.admin_pw_input_line.setMaximumSize(QSize(221, 3))
        self.admin_pw_input_line.setFont(font11)
        self.admin_pw_input_line.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.admin_pw_input_line.setAutoFillBackground(False)
        self.admin_pw_input_line.setStyleSheet(u"background-color: rgb(36, 39, 44)")
        self.admin_pw_input_line.setFrameShape(QFrame.Shape.HLine)
        self.admin_pw_input_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_35.addWidget(self.admin_pw_input_line)


        self.horizontalLayout_38.addLayout(self.verticalLayout_35)

        self.admin_page_bnt = QPushButton(self.admin_page)
        self.admin_page_bnt.setObjectName(u"admin_page_bnt")
        self.admin_page_bnt.setMinimumSize(QSize(71, 41))
        self.admin_page_bnt.setMaximumSize(QSize(71, 41))
        self.admin_page_bnt.setFont(font1)
        self.admin_page_bnt.setCursor(QCursor(Qt.PointingHandCursor))
        self.admin_page_bnt.setStyleSheet(u"\n"
"background-color: rgb(30, 195, 55);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"")

        self.horizontalLayout_38.addWidget(self.admin_page_bnt)

        self.horizontalSpacer_38 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_38.addItem(self.horizontalSpacer_38)


        self.verticalLayout_36.addLayout(self.horizontalLayout_38)

        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_36.addItem(self.verticalSpacer_15)


        self.verticalLayout_37.addLayout(self.verticalLayout_36)

        self.stackedWidget.addWidget(self.admin_page)
        self.admin_page_2 = QWidget()
        self.admin_page_2.setObjectName(u"admin_page_2")
        self.horizontalLayout_47 = QHBoxLayout(self.admin_page_2)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.widget_2 = QWidget(self.admin_page_2)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_50 = QVBoxLayout(self.widget_2)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.verticalLayout_49 = QVBoxLayout()
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.verticalLayout_48 = QVBoxLayout()
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.admin_license_bnt = QPushButton(self.widget_2)
        self.admin_license_bnt.setObjectName(u"admin_license_bnt")
        sizePolicy2.setHeightForWidth(self.admin_license_bnt.sizePolicy().hasHeightForWidth())
        self.admin_license_bnt.setSizePolicy(sizePolicy2)
        self.admin_license_bnt.setMinimumSize(QSize(171, 41))
        self.admin_license_bnt.setMaximumSize(QSize(171, 41))
        self.admin_license_bnt.setFont(font8)
        self.admin_license_bnt.setCursor(QCursor(Qt.PointingHandCursor))
        self.admin_license_bnt.setStyleSheet(u"border-radius: 20px;\n"
"border: 1px solid rgb(179,179,179);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(3, 3, 13);\n"
"")
        self.admin_license_bnt.setCheckable(True)
        self.admin_license_bnt.setChecked(False)
        self.admin_license_bnt.setAutoExclusive(True)

        self.verticalLayout_48.addWidget(self.admin_license_bnt)

        self.admin_fn_permission_bnt = QPushButton(self.widget_2)
        self.admin_fn_permission_bnt.setObjectName(u"admin_fn_permission_bnt")
        sizePolicy2.setHeightForWidth(self.admin_fn_permission_bnt.sizePolicy().hasHeightForWidth())
        self.admin_fn_permission_bnt.setSizePolicy(sizePolicy2)
        self.admin_fn_permission_bnt.setMinimumSize(QSize(171, 41))
        self.admin_fn_permission_bnt.setMaximumSize(QSize(171, 41))
        self.admin_fn_permission_bnt.setFont(font8)
        self.admin_fn_permission_bnt.setCursor(QCursor(Qt.PointingHandCursor))
        self.admin_fn_permission_bnt.setStyleSheet(u"border-radius: 20px;\n"
"border: 1px solid rgb(179,179,179);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(3, 3, 13);\n"
"")
        self.admin_fn_permission_bnt.setCheckable(True)
        self.admin_fn_permission_bnt.setChecked(False)
        self.admin_fn_permission_bnt.setAutoExclusive(True)

        self.verticalLayout_48.addWidget(self.admin_fn_permission_bnt)


        self.verticalLayout_49.addLayout(self.verticalLayout_48)

        self.verticalSpacer_23 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_49.addItem(self.verticalSpacer_23)


        self.verticalLayout_50.addLayout(self.verticalLayout_49)


        self.horizontalLayout_47.addWidget(self.widget_2)

        self.stackedWidget_2 = QStackedWidget(self.admin_page_2)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"background-color: rgb(13, 16, 23);\n"
"")
        self.license_page = QWidget()
        self.license_page.setObjectName(u"license_page")
        self.horizontalLayout_18 = QHBoxLayout(self.license_page)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.verticalLayout_46 = QVBoxLayout()
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalSpacer_21 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_46.addItem(self.verticalSpacer_21)

        self.horizontalLayout_46 = QHBoxLayout()
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalSpacer_42 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_46.addItem(self.horizontalSpacer_42)

        self.verticalLayout_38 = QVBoxLayout()
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.horizontalLayout_42 = QHBoxLayout()
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.verticalLayout_39 = QVBoxLayout()
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.non_active_license_label = QLabel(self.license_page)
        self.non_active_license_label.setObjectName(u"non_active_license_label")
        self.non_active_license_label.setMinimumSize(QSize(171, 31))
        self.non_active_license_label.setMaximumSize(QSize(171, 31))
        font14 = QFont()
        font14.setFamilies([u"Ubuntu Light"])
        font14.setPointSize(11)
        font14.setBold(True)
        self.non_active_license_label.setFont(font14)
        self.non_active_license_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"background-color: rgb(32,39,49);\n"
"\n"
"")
        self.non_active_license_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_39.addWidget(self.non_active_license_label)

        self.widget_3 = QWidget(self.license_page)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(171, 0))
        self.widget_3.setMaximumSize(QSize(171, 16777215))
        self.widget_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"background-color: rgb(32,39,49);\n"
"\n"
"")
        self.verticalLayout_40 = QVBoxLayout(self.widget_3)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.non_active_license_list = QListWidget(self.widget_3)
        QListWidgetItem(self.non_active_license_list)
        QListWidgetItem(self.non_active_license_list)
        QListWidgetItem(self.non_active_license_list)
        QListWidgetItem(self.non_active_license_list)
        QListWidgetItem(self.non_active_license_list)
        self.non_active_license_list.setObjectName(u"non_active_license_list")
        self.non_active_license_list.setMinimumSize(QSize(156, 397))
        self.non_active_license_list.setMaximumSize(QSize(156, 16777215))
        font15 = QFont()
        font15.setPointSize(11)
        font15.setBold(False)
        font15.setItalic(False)
        font15.setUnderline(False)
        font15.setStrikeOut(False)
        font15.setKerning(True)
        self.non_active_license_list.setFont(font15)
        self.non_active_license_list.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.non_active_license_list.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.non_active_license_list.setAcceptDrops(True)
        self.non_active_license_list.setStyleSheet(u"QListWidget::item {\n"
"    padding: 3px;\n"
"}\n"
"QListWidget::item:selected {\n"
"    background-color: rgba(19, 193, 13, 200);\n"
"    border: 2px solid green;\n"
"    border-radius: 5px; /* \ub465\uadfc \ud14c\ub450\ub9ac \ucd94\uac00 */\n"
"}\n"
"")
        self.non_active_license_list.setFrameShape(QFrame.Shape.NoFrame)
        self.non_active_license_list.setLineWidth(1)
        self.non_active_license_list.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.non_active_license_list.setTabKeyNavigation(False)
        self.non_active_license_list.setProperty("showDropIndicator", True)
        self.non_active_license_list.setDragEnabled(True)
        self.non_active_license_list.setDragDropMode(QAbstractItemView.DragDropMode.NoDragDrop)
        self.non_active_license_list.setDefaultDropAction(Qt.DropAction.IgnoreAction)
        self.non_active_license_list.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.non_active_license_list.setTextElideMode(Qt.TextElideMode.ElideLeft)
        self.non_active_license_list.setVerticalScrollMode(QAbstractItemView.ScrollMode.ScrollPerItem)
        self.non_active_license_list.setMovement(QListView.Movement.Static)
        self.non_active_license_list.setFlow(QListView.Flow.TopToBottom)
        self.non_active_license_list.setProperty("isWrapping", False)
        self.non_active_license_list.setResizeMode(QListView.ResizeMode.Fixed)
        self.non_active_license_list.setLayoutMode(QListView.LayoutMode.SinglePass)
        self.non_active_license_list.setSpacing(1)
        self.non_active_license_list.setModelColumn(0)
        self.non_active_license_list.setUniformItemSizes(True)
        self.non_active_license_list.setWordWrap(False)
        self.non_active_license_list.setSelectionRectVisible(True)

        self.verticalLayout_40.addWidget(self.non_active_license_list)


        self.verticalLayout_39.addWidget(self.widget_3)


        self.horizontalLayout_42.addLayout(self.verticalLayout_39)

        self.verticalLayout_41 = QVBoxLayout()
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_41.addItem(self.verticalSpacer_16)

        self.license_add_bnt = QPushButton(self.license_page)
        self.license_add_bnt.setObjectName(u"license_add_bnt")
        self.license_add_bnt.setMinimumSize(QSize(41, 41))
        self.license_add_bnt.setMaximumSize(QSize(41, 41))
        font16 = QFont()
        font16.setPointSize(10)
        self.license_add_bnt.setFont(font16)
        self.license_add_bnt.setCursor(QCursor(Qt.PointingHandCursor))
        self.license_add_bnt.setStyleSheet(u"background-color: rgb(3, 3, 13);\n"
"border: 1px solid rgb(3, 3, 13);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        icon5 = QIcon()
        icon5.addFile(u":/ui/ui/images/ico_arrow_right.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.license_add_bnt.setIcon(icon5)
        self.license_add_bnt.setIconSize(QSize(31, 50))

        self.verticalLayout_41.addWidget(self.license_add_bnt)

        self.license_remove_bnt = QPushButton(self.license_page)
        self.license_remove_bnt.setObjectName(u"license_remove_bnt")
        self.license_remove_bnt.setMinimumSize(QSize(41, 41))
        self.license_remove_bnt.setMaximumSize(QSize(41, 41))
        self.license_remove_bnt.setFont(font16)
        self.license_remove_bnt.setCursor(QCursor(Qt.PointingHandCursor))
        self.license_remove_bnt.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.license_remove_bnt.setStyleSheet(u"background-color: rgb(3, 3, 13);\n"
"border: 1px solid rgb(3, 3, 13);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"Rotation: ( origin.x: 25; origin.y: 25; angle: 45);")
        icon6 = QIcon()
        icon6.addFile(u":/ui/ui/images/ico_arrow_left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.license_remove_bnt.setIcon(icon6)
        self.license_remove_bnt.setIconSize(QSize(31, 50))

        self.verticalLayout_41.addWidget(self.license_remove_bnt)

        self.verticalSpacer_18 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_41.addItem(self.verticalSpacer_18)


        self.horizontalLayout_42.addLayout(self.verticalLayout_41)

        self.verticalLayout_42 = QVBoxLayout()
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.active_license_label = QLabel(self.license_page)
        self.active_license_label.setObjectName(u"active_license_label")
        self.active_license_label.setMinimumSize(QSize(171, 31))
        self.active_license_label.setMaximumSize(QSize(171, 31))
        self.active_license_label.setFont(font14)
        self.active_license_label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"background-color: rgb(32,39,49);\n"
"\n"
"")
        self.active_license_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_42.addWidget(self.active_license_label)

        self.widget_4 = QWidget(self.license_page)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(171, 0))
        self.widget_4.setMaximumSize(QSize(171, 16777215))
        self.widget_4.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"background-color: rgb(32,39,49);\n"
"\n"
"")
        self.verticalLayout_43 = QVBoxLayout(self.widget_4)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.active_license_list = QListWidget(self.widget_4)
        QListWidgetItem(self.active_license_list)
        QListWidgetItem(self.active_license_list)
        QListWidgetItem(self.active_license_list)
        QListWidgetItem(self.active_license_list)
        self.active_license_list.setObjectName(u"active_license_list")
        self.active_license_list.setMinimumSize(QSize(156, 397))
        self.active_license_list.setMaximumSize(QSize(156, 16777215))
        self.active_license_list.setFont(font15)
        self.active_license_list.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.active_license_list.setAcceptDrops(True)
        self.active_license_list.setStyleSheet(u"QListWidget::item {\n"
"    padding: 3px;\n"
"}\n"
"QListWidget::item:selected {\n"
"    background-color: rgba(19, 193, 13, 200);\n"
"    border: 2px solid green;\n"
"    border-radius: 5px; /* \ub465\uadfc \ud14c\ub450\ub9ac \ucd94\uac00 */\n"
"}\n"
"")
        self.active_license_list.setFrameShape(QFrame.Shape.NoFrame)
        self.active_license_list.setLineWidth(1)
        self.active_license_list.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.active_license_list.setTabKeyNavigation(False)
        self.active_license_list.setProperty("showDropIndicator", False)
        self.active_license_list.setDragEnabled(True)
        self.active_license_list.setDragDropMode(QAbstractItemView.DragDropMode.NoDragDrop)
        self.active_license_list.setDefaultDropAction(Qt.DropAction.IgnoreAction)
        self.active_license_list.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.active_license_list.setTextElideMode(Qt.TextElideMode.ElideLeft)
        self.active_license_list.setVerticalScrollMode(QAbstractItemView.ScrollMode.ScrollPerItem)
        self.active_license_list.setMovement(QListView.Movement.Static)
        self.active_license_list.setFlow(QListView.Flow.TopToBottom)
        self.active_license_list.setProperty("isWrapping", False)
        self.active_license_list.setResizeMode(QListView.ResizeMode.Fixed)
        self.active_license_list.setLayoutMode(QListView.LayoutMode.SinglePass)
        self.active_license_list.setSpacing(1)
        self.active_license_list.setModelColumn(0)
        self.active_license_list.setUniformItemSizes(True)
        self.active_license_list.setWordWrap(False)
        self.active_license_list.setSelectionRectVisible(True)

        self.verticalLayout_43.addWidget(self.active_license_list)


        self.verticalLayout_42.addWidget(self.widget_4)


        self.horizontalLayout_42.addLayout(self.verticalLayout_42)


        self.verticalLayout_38.addLayout(self.horizontalLayout_42)

        self.horizontalLayout_43 = QHBoxLayout()
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalSpacer_39 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_43.addItem(self.horizontalSpacer_39)

        self.license_save_bnt = QPushButton(self.license_page)
        self.license_save_bnt.setObjectName(u"license_save_bnt")
        sizePolicy2.setHeightForWidth(self.license_save_bnt.sizePolicy().hasHeightForWidth())
        self.license_save_bnt.setSizePolicy(sizePolicy2)
        self.license_save_bnt.setMinimumSize(QSize(71, 41))
        self.license_save_bnt.setMaximumSize(QSize(71, 41))
        self.license_save_bnt.setFont(font16)
        self.license_save_bnt.setCursor(QCursor(Qt.PointingHandCursor))
        self.license_save_bnt.setStyleSheet(u"\n"
"background-color: rgb(30, 195, 55);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"\n"
"")

        self.horizontalLayout_43.addWidget(self.license_save_bnt)


        self.verticalLayout_38.addLayout(self.horizontalLayout_43)


        self.horizontalLayout_46.addLayout(self.verticalLayout_38)

        self.horizontalSpacer_43 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_46.addItem(self.horizontalSpacer_43)


        self.verticalLayout_46.addLayout(self.horizontalLayout_46)

        self.verticalSpacer_22 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_46.addItem(self.verticalSpacer_22)


        self.horizontalLayout_18.addLayout(self.verticalLayout_46)

        self.stackedWidget_2.addWidget(self.license_page)
        self.fn_permission_page = QWidget()
        self.fn_permission_page.setObjectName(u"fn_permission_page")
        self.verticalLayout_6 = QVBoxLayout(self.fn_permission_page)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(17, 15, -1, -1)
        self.horizontalLayout_44 = QHBoxLayout()
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(0, -1, -1, -1)
        self.admin_fn_active_label = QLabel(self.fn_permission_page)
        self.admin_fn_active_label.setObjectName(u"admin_fn_active_label")
        self.admin_fn_active_label.setMinimumSize(QSize(160, 25))
        self.admin_fn_active_label.setMaximumSize(QSize(167, 25))
        self.admin_fn_active_label.setFont(font8)
        self.admin_fn_active_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.admin_fn_active_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_44.addWidget(self.admin_fn_active_label)

        self.admin_fn_active_bnt = QPushButton(self.fn_permission_page)
        self.admin_fn_active_bnt.setObjectName(u"admin_fn_active_bnt")
        self.admin_fn_active_bnt.setMinimumSize(QSize(61, 25))
        self.admin_fn_active_bnt.setMaximumSize(QSize(61, 25))
        self.admin_fn_active_bnt.setIcon(icon4)
        self.admin_fn_active_bnt.setIconSize(QSize(55, 103))
        self.admin_fn_active_bnt.setCheckable(True)

        self.horizontalLayout_44.addWidget(self.admin_fn_active_bnt)


        self.verticalLayout_5.addLayout(self.horizontalLayout_44)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.admin_par_active_label = QLabel(self.fn_permission_page)
        self.admin_par_active_label.setObjectName(u"admin_par_active_label")
        self.admin_par_active_label.setMinimumSize(QSize(160, 25))
        self.admin_par_active_label.setMaximumSize(QSize(167, 25))
        self.admin_par_active_label.setFont(font8)
        self.admin_par_active_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.admin_par_active_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_4.addWidget(self.admin_par_active_label)

        self.admin_par_active_bnt = QPushButton(self.fn_permission_page)
        self.admin_par_active_bnt.setObjectName(u"admin_par_active_bnt")
        self.admin_par_active_bnt.setMinimumSize(QSize(61, 25))
        self.admin_par_active_bnt.setMaximumSize(QSize(61, 25))
        self.admin_par_active_bnt.setIcon(icon4)
        self.admin_par_active_bnt.setIconSize(QSize(55, 103))
        self.admin_par_active_bnt.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.admin_par_active_bnt)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_19 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_19)


        self.horizontalLayout_5.addLayout(self.verticalLayout_5)

        self.horizontalSpacer_41 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_41)


        self.verticalLayout_6.addLayout(self.horizontalLayout_5)

        self.stackedWidget_2.addWidget(self.fn_permission_page)

        self.horizontalLayout_47.addWidget(self.stackedWidget_2)

        self.stackedWidget.addWidget(self.admin_page_2)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout_32.addLayout(self.verticalLayout_2)


        self.verticalLayout_11.addLayout(self.horizontalLayout_32)


        self.horizontalLayout_58.addLayout(self.verticalLayout_11)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.shutdown_bnt, self.server_ip_input)
        QWidget.setTabOrder(self.server_ip_input, self.server_id_input)
        QWidget.setTabOrder(self.server_id_input, self.server_pw_input)
        QWidget.setTabOrder(self.server_pw_input, self.server_login_bnt)
        QWidget.setTabOrder(self.server_login_bnt, self.labeling_bnt)
        QWidget.setTabOrder(self.labeling_bnt, self.camera_schedule_bnt)
        QWidget.setTabOrder(self.camera_schedule_bnt, self.camera_page_camera_event_box)
        QWidget.setTabOrder(self.camera_page_camera_event_box, self.camera_page_detect_add_bnt)
        QWidget.setTabOrder(self.camera_page_detect_add_bnt, self.camera_page_detect_area_table)
        QWidget.setTabOrder(self.camera_page_detect_area_table, self.camera_page_detect_area_del_bnt)
        QWidget.setTabOrder(self.camera_page_detect_area_del_bnt, self.camera_page_ai_bnt)
        QWidget.setTabOrder(self.camera_page_ai_bnt, self.setting_alarm_bnt)
        QWidget.setTabOrder(self.setting_alarm_bnt, self.setting_user_setting_bnt)
        QWidget.setTabOrder(self.setting_user_setting_bnt, self.setting_ai_bnt)
        QWidget.setTabOrder(self.setting_ai_bnt, self.setting_video_save_alarm_active_bnt)
        QWidget.setTabOrder(self.setting_video_save_alarm_active_bnt, self.setting_event_video_storage_period)
        QWidget.setTabOrder(self.setting_event_video_storage_period, self.setting_popup_alarm_active_bnt)
        QWidget.setTabOrder(self.setting_popup_alarm_active_bnt, self.setting_popup_alarm_cnt)
        QWidget.setTabOrder(self.setting_popup_alarm_cnt, self.setting_user_id_input)
        QWidget.setTabOrder(self.setting_user_id_input, self.setting_user_pw_input)
        QWidget.setTabOrder(self.setting_user_pw_input, self.setting_user_new_pw_input)
        QWidget.setTabOrder(self.setting_user_new_pw_input, self.setting_user_new_pw_input2)
        QWidget.setTabOrder(self.setting_user_new_pw_input2, self.setting_user_save_bnt)
        QWidget.setTabOrder(self.setting_user_save_bnt, self.setting_setting_ai_weight_box)
        QWidget.setTabOrder(self.setting_setting_ai_weight_box, self.setting_self_training_auto_labeling_bnt)
        QWidget.setTabOrder(self.setting_self_training_auto_labeling_bnt, self.setting_self_training_zeroshot_bnt)
        QWidget.setTabOrder(self.setting_self_training_zeroshot_bnt, self.setting_ai_setting_save_bnt)
        QWidget.setTabOrder(self.setting_ai_setting_save_bnt, self.admin_pw_input)
        QWidget.setTabOrder(self.admin_pw_input, self.admin_page_bnt)
        QWidget.setTabOrder(self.admin_page_bnt, self.admin_license_bnt)
        QWidget.setTabOrder(self.admin_license_bnt, self.admin_fn_permission_bnt)
        QWidget.setTabOrder(self.admin_fn_permission_bnt, self.license_add_bnt)
        QWidget.setTabOrder(self.license_add_bnt, self.license_remove_bnt)
        QWidget.setTabOrder(self.license_remove_bnt, self.license_save_bnt)
        QWidget.setTabOrder(self.license_save_bnt, self.admin_fn_active_bnt)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.setting_stack_widget.setCurrentIndex(0)
        self.setting_popup_alarm_cnt.setCurrentIndex(2)
        self.setting_setting_ai_weight_box.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MS-AI 1000", None))
        self.top_logo.setText("")
        self.verson_label.setText(QCoreApplication.translate("MainWindow", u"MS-AI1000 1.4.0", None))
        self.server_icon.setText("")
        self.server_info_label.setText("")
        self.server_ip_label.setText(QCoreApplication.translate("MainWindow", u"\uce74\uba54\ub77c \uc8fc\uc18c", None))
        self.server_ip_input.setText("")
        self.server_id_label.setText(QCoreApplication.translate("MainWindow", u"\uc544\uc774\ub514", None))
        self.server_id_input.setText("")
        self.server_pw_label.setText(QCoreApplication.translate("MainWindow", u"\ube44\ubc00\ubc88\ud638", None))
        self.server_pw_input.setText("")
        self.server_login_bnt.setText(QCoreApplication.translate("MainWindow", u"\uc5f0\uacb0", None))
        self.connected_user_icon_2.setText("")
        self.connected_user_label_2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.shutdown_bnt.setText(QCoreApplication.translate("MainWindow", u"\uc885\ub8cc", None))
        self.camera_bnt.setText(QCoreApplication.translate("MainWindow", u"\uc9c0\ub2a5\ud615 \uce74\uba54\ub77c \uc124\uc815", None))
        self.tab_partion_1.setText(QCoreApplication.translate("MainWindow", u"|", None))
        self.search_bnt.setText(QCoreApplication.translate("MainWindow", u"\uc774\ubca4\ud2b8 \uac80\uc0c9", None))
        self.tab_partion_2.setText(QCoreApplication.translate("MainWindow", u"|", None))
        self.setting_bnt.setText(QCoreApplication.translate("MainWindow", u"\uc124\uc815", None))
        self.tab_partion_3.setText(QCoreApplication.translate("MainWindow", u"|", None))
        self.admin_bnt.setText(QCoreApplication.translate("MainWindow", u"\uad00\ub9ac\uc790 \uc124\uc815", None))
        self.labeling_bnt.setText("")
        self.camera_schedule_bnt.setText("")
        self.camera_page_viewer.setText("")
        self.camera_page_camera_event_label.setText(QCoreApplication.translate("MainWindow", u"\uc774\ubca4\ud2b8 \uc885\ub958", None))
        self.camera_page_camera_event_box.setItemText(0, QCoreApplication.translate("MainWindow", u"\uce68\uc785", None))
        self.camera_page_camera_event_box.setItemText(1, QCoreApplication.translate("MainWindow", u"\ubc30\ud68c", None))
        self.camera_page_camera_event_box.setItemText(2, QCoreApplication.translate("MainWindow", u"\uc4f0\ub7ec\uc9d0", None))
        self.camera_page_camera_event_box.setItemText(3, QCoreApplication.translate("MainWindow", u"\ubc29\ud654", None))

        self.camera_page_detect_add_bnt.setText("")
        ___qtablewidgetitem = self.camera_page_detect_area_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\uac10\uc9c0 \uc601\uc5ed \ub9ac\uc2a4\ud2b8", None));
        self.camera_page_object_setting_bnt.setText(QCoreApplication.translate("MainWindow", u"\uc9c0\ub2a5\ud615 \ubd84\uc11d \uc124\uc815", None))
        self.camera_page_detect_area_del_bnt.setText(QCoreApplication.translate("MainWindow", u"\uc0ad\uc81c", None))
        self.camera_page_ai_bnt.setText(QCoreApplication.translate("MainWindow", u"\uc9c0\ub2a5\ud615 \ubd84\uc11d \uc2dc\uc791", None))
        self.setting_alarm_bnt.setText(QCoreApplication.translate("MainWindow", u"\uc54c\ub9bc \uc124\uc815", None))
        self.setting_user_setting_bnt.setText(QCoreApplication.translate("MainWindow", u"\ub85c\uadf8\uc778 \uc815\ubcf4 \ubcc0\uacbd", None))
        self.setting_ai_bnt.setText(QCoreApplication.translate("MainWindow", u"\uc9c0\ub2a5\ud615 \uc124\uc815", None))
        self.setting_video_save_alarm_active_label.setText(QCoreApplication.translate("MainWindow", u"\uc774\ubca4\ud2b8 \uc601\uc0c1 \uc800\uc7a5 \ud65c\uc131\ud654", None))
        self.setting_video_save_alarm_active_bnt.setText("")
        self.setting_event_video_storage_period_label.setText(QCoreApplication.translate("MainWindow", u"\uc774\ubca4\ud2b8 \uc601\uc0c1 \uc720\uc9c0 \uae30\uac04", None))
        self.setting_event_video_storage_period.setItemText(0, QCoreApplication.translate("MainWindow", u"30\uc77c", None))
        self.setting_event_video_storage_period.setItemText(1, QCoreApplication.translate("MainWindow", u"60\uc77c", None))
        self.setting_event_video_storage_period.setItemText(2, QCoreApplication.translate("MainWindow", u"90\uc77c", None))

        self.setting_popup_alarm_active_label.setText(QCoreApplication.translate("MainWindow", u"\uc774\ubca4\ud2b8 \uba54\uc138\uc9c0 \ud65c\uc131\ud654", None))
        self.setting_popup_alarm_active_bnt.setText("")
        self.setting_popup_alarm_cnt_label.setText(QCoreApplication.translate("MainWindow", u"\uc774\ubca4\ud2b8 \uba54\uc138\uc9c0 \uac1c\uc218", None))
        self.setting_popup_alarm_cnt.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.setting_popup_alarm_cnt.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.setting_popup_alarm_cnt.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.setting_popup_alarm_cnt.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))
        self.setting_popup_alarm_cnt.setItemText(4, QCoreApplication.translate("MainWindow", u"5", None))
        self.setting_popup_alarm_cnt.setItemText(5, QCoreApplication.translate("MainWindow", u"6", None))
        self.setting_popup_alarm_cnt.setItemText(6, QCoreApplication.translate("MainWindow", u"7", None))
        self.setting_popup_alarm_cnt.setItemText(7, QCoreApplication.translate("MainWindow", u"8", None))
        self.setting_popup_alarm_cnt.setItemText(8, QCoreApplication.translate("MainWindow", u"9", None))
        self.setting_popup_alarm_cnt.setItemText(9, QCoreApplication.translate("MainWindow", u"10", None))

        self.setting_user_id_label.setText(QCoreApplication.translate("MainWindow", u"\uc544\uc774\ub514", None))
        self.setting_user_id_input.setText("")
        self.setting_user_pw_label.setText(QCoreApplication.translate("MainWindow", u"\ud604\uc7ac \ube44\ubc00\ubc88\ud638", None))
        self.setting_user_pw_input.setText("")
        self.setting_user_new_pw_label.setText(QCoreApplication.translate("MainWindow", u"\uc2e0\uaddc \ube44\ubc00\ubc88\ud638", None))
        self.setting_user_new_pw_input.setText("")
        self.setting_user_new_pw_label2.setText(QCoreApplication.translate("MainWindow", u"\ube44\ubc00\ubc88\ud638 \ud655\uc778", None))
        self.setting_user_new_pw_input2.setText("")
        self.setting_user_save_bnt.setText(QCoreApplication.translate("MainWindow", u"\ubcc0\uacbd", None))
        self.setting_ai_weight_label.setText(QCoreApplication.translate("MainWindow", u"\uc9c0\ub2a5\ud615 \uac1d\uccb4 \uc778\uc2dd \ubaa8\ub378 \uc120\ud14d", None))
        self.setting_setting_ai_weight_box.setItemText(0, QCoreApplication.translate("MainWindow", u"2024-07-24", None))

        self.setting_setting_ai_weight_box.setPlaceholderText("")
        self.setting_self_training_auto_labeling_label.setText(QCoreApplication.translate("MainWindow", u"Self Auto Labeling \ud65c\uc131\ud654", None))
        self.setting_self_training_auto_labeling_bnt.setText("")
        self.setting_self_training_zeroshot_label.setText(QCoreApplication.translate("MainWindow", u"AI Labeling Assistance \ud65c\uc131\ud654", None))
        self.setting_self_training_zeroshot_bnt.setText("")
        self.setting_page_email_info_label_5.setText(QCoreApplication.translate("MainWindow", u"\u203bAI Labeling Assistance \uc740 \uc0c8\ub85c\uc6b4 \ud658\uacbd\uc5d0\uc11c", None))
        self.setting_page_email_info_label_6.setText(QCoreApplication.translate("MainWindow", u" \ucd08\uae30  \ubaa8\ub378 \ud559\uc2b5 \uc131\ub2a5 \uac1c\uc120\uc744 \ub3c4\uc640\uc90d\ub2c8\ub2e4", None))
        self.setting_ai_setting_save_bnt.setText(QCoreApplication.translate("MainWindow", u"\uc800\uc7a5", None))
        self.admin_pw_label.setText(QCoreApplication.translate("MainWindow", u"\uad00\ub9ac\uc790 \ube44\ubc00\ubc88\ud638", None))
        self.admin_pw_input.setText(QCoreApplication.translate("MainWindow", u"asdsad", None))
        self.admin_page_bnt.setText(QCoreApplication.translate("MainWindow", u"\uc785\ub825", None))
        self.admin_license_bnt.setText(QCoreApplication.translate("MainWindow", u"\uc9c0\ub2a5\ud615 \ub77c\uc774\uc13c\uc2a4 \uc124\uc815", None))
        self.admin_fn_permission_bnt.setText(QCoreApplication.translate("MainWindow", u"\uae30\ub2a5 \uad8c\ud55c \uc124\uc815", None))
        self.non_active_license_label.setText(QCoreApplication.translate("MainWindow", u"\ube44\ud65c\uc131 \ub77c\uc774\uc13c\uc2a4", None))

        __sortingEnabled = self.non_active_license_list.isSortingEnabled()
        self.non_active_license_list.setSortingEnabled(False)
        ___qlistwidgetitem = self.non_active_license_list.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"\uce68\uc785", None));
        ___qlistwidgetitem1 = self.non_active_license_list.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\ubc30\ud68c", None));
        ___qlistwidgetitem2 = self.non_active_license_list.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\ubc29\ud654", None));
        ___qlistwidgetitem3 = self.non_active_license_list.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\uc4f0\ub7ec\uc9d0", None));
        ___qlistwidgetitem4 = self.non_active_license_list.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\uc2f8\uc6c0", None));
        self.non_active_license_list.setSortingEnabled(__sortingEnabled)

        self.license_add_bnt.setText("")
        self.license_remove_bnt.setText("")
        self.active_license_label.setText(QCoreApplication.translate("MainWindow", u"\ud65c\uc131 \ub77c\uc774\uc13c\uc2a4", None))

        __sortingEnabled1 = self.active_license_list.isSortingEnabled()
        self.active_license_list.setSortingEnabled(False)
        ___qlistwidgetitem5 = self.active_license_list.item(0)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem6 = self.active_license_list.item(1)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem7 = self.active_license_list.item(2)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem8 = self.active_license_list.item(3)
        ___qlistwidgetitem8.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        self.active_license_list.setSortingEnabled(__sortingEnabled1)

        self.license_save_bnt.setText(QCoreApplication.translate("MainWindow", u"\uc800\uc7a5", None))
        self.admin_fn_active_label.setText(QCoreApplication.translate("MainWindow", u"\uae30\ud0c0 \uae30\ub2a5 \ud65c\uc131\ud654", None))
        self.admin_fn_active_bnt.setText("")
        self.admin_par_active_label.setText(QCoreApplication.translate("MainWindow", u"\uc18d\uc131 \uac80\ucd9c \uae30\ub2a5 \ud65c\uc131\ud654", None))
        self.admin_par_active_bnt.setText("")
    # retranslateUi

