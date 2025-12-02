# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainGPoIUt.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QLineEdit, QListView,
    QListWidget, QListWidgetItem, QMainWindow, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QStackedWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
import resourece_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModality.NonModal)
        MainWindow.resize(1284, 720)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1280, 720))
        MainWindow.setMaximumSize(QSize(3840, 2160))
        MainWindow.setContextMenuPolicy(Qt.ContextMenuPolicy.PreventContextMenu)
        icon = QIcon()
        icon.addFile(u":/ui/ui/images/icon2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
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
        self.server_ip_label.setMaximumSize(QSize(38, 41))
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
        self.server_ip_input.setEchoMode(QLineEdit.EchoMode.PasswordEchoOnEdit)

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
        self.server_login_bnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.server_login_bnt.setStyleSheet(u"background-color: qlineargradient(\n"
"    spread:pad,\n"
"    x1:0, y1:0, x2:0, y2:1,\n"
"    stop:0.0 rgba(112, 210, 112, 255),\n"
"    stop:0.3 rgba(0, 196, 0, 255)\n"
");\n"
"\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"")

        self.horizontalLayout.addWidget(self.server_login_bnt)

        self.horizontalSpacer_2 = QSpacerItem(37, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.shutdown_bnt = QPushButton(self.centralwidget)
        self.shutdown_bnt.setObjectName(u"shutdown_bnt")
        self.shutdown_bnt.setMinimumSize(QSize(61, 31))
        self.shutdown_bnt.setMaximumSize(QSize(61, 31))
        font4 = QFont()
        font4.setFamilies([u"NanumSquareRound"])
        font4.setPointSize(10)
        font4.setBold(False)
        self.shutdown_bnt.setFont(font4)
        self.shutdown_bnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.shutdown_bnt.setStyleSheet(u"background-color: rgb(255, 49, 38);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"")

        self.horizontalLayout.addWidget(self.shutdown_bnt)


        self.verticalLayout_11.addLayout(self.horizontalLayout)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.camera_info_side_widget = QWidget(self.centralwidget)
        self.camera_info_side_widget.setObjectName(u"camera_info_side_widget")
        self.camera_info_side_widget.setMaximumSize(QSize(335, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.camera_info_side_widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.camera_list_table = QTableWidget(self.camera_info_side_widget)
        if (self.camera_list_table.columnCount() < 4):
            self.camera_list_table.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.camera_list_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.BrushStyle.NoBrush)
        font5 = QFont()
        font5.setFamilies([u"Ubuntu Light"])
        font5.setPointSize(10)
        font5.setBold(False)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font5);
        __qtablewidgetitem1.setForeground(brush);
        self.camera_list_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        font6 = QFont()
        font6.setFamilies([u"Ubuntu Light"])
        font6.setPointSize(10)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font6);
        self.camera_list_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font5);
        self.camera_list_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.camera_list_table.setObjectName(u"camera_list_table")
        self.camera_list_table.setMinimumSize(QSize(319, 100))
        self.camera_list_table.setMaximumSize(QSize(319, 16777215))
        font7 = QFont()
        font7.setFamilies([u"Sans"])
        font7.setPointSize(10)
        font7.setBold(False)
        self.camera_list_table.setFont(font7)
        self.camera_list_table.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.camera_list_table.setStyleSheet(u"QTableWidget {\n"
"    background-color: rgb(13, 16, 23); /* \ud14c\uc774\ube14 \uc804\uccb4 \ubc30\uacbd\uc0c9 */\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    color: rgb(209, 209, 209); /* \ud5e4\ub354 \ud14d\uc2a4\ud2b8 \uc0c9\uc0c1 - \ud68c\uc0c9 */\n"
"	background-color: rgb(7, 7, 16); \n"
"\n"
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
        self.camera_list_table.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.camera_list_table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.camera_list_table.setTabKeyNavigation(False)
        self.camera_list_table.setDragDropOverwriteMode(False)
        self.camera_list_table.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.camera_list_table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.camera_list_table.setShowGrid(False)
        self.camera_list_table.setGridStyle(Qt.PenStyle.NoPen)
        self.camera_list_table.setWordWrap(False)
        self.camera_list_table.setCornerButtonEnabled(False)
        self.camera_list_table.horizontalHeader().setVisible(True)
        self.camera_list_table.horizontalHeader().setCascadingSectionResizes(False)
        self.camera_list_table.horizontalHeader().setMinimumSectionSize(5)
        self.camera_list_table.horizontalHeader().setDefaultSectionSize(69)
        self.camera_list_table.horizontalHeader().setHighlightSections(False)
        self.camera_list_table.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.camera_list_table.horizontalHeader().setStretchLastSection(True)
        self.camera_list_table.verticalHeader().setVisible(False)
        self.camera_list_table.verticalHeader().setCascadingSectionResizes(False)
        self.camera_list_table.verticalHeader().setMinimumSectionSize(21)
        self.camera_list_table.verticalHeader().setDefaultSectionSize(30)
        self.camera_list_table.verticalHeader().setHighlightSections(False)
        self.camera_list_table.verticalHeader().setProperty(u"showSortIndicator", False)
        self.camera_list_table.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_4.addWidget(self.camera_list_table)


        self.verticalLayout_3.addLayout(self.verticalLayout_4)


        self.horizontalLayout_32.addWidget(self.camera_info_side_widget)

        self.verticalLayout_2 = QVBoxLayout()
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
        font8 = QFont()
        font8.setFamilies([u"Sans"])
        font8.setPointSize(13)
        self.camera_bnt.setFont(font8)
        self.camera_bnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.camera_bnt.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 1px solid rgba(0, 0, 0, 0);\n"
"background-color: rgba(191, 64, 64, 0);")

        self.horizontalLayout_31.addWidget(self.camera_bnt)

        self.tab_partion_11 = QLabel(self.tab_backgournd)
        self.tab_partion_11.setObjectName(u"tab_partion_11")
        sizePolicy1.setHeightForWidth(self.tab_partion_11.sizePolicy().hasHeightForWidth())
        self.tab_partion_11.setSizePolicy(sizePolicy1)
        self.tab_partion_11.setMinimumSize(QSize(3, 0))
        font9 = QFont()
        font9.setFamilies([u"Sans"])
        font9.setPointSize(14)
        self.tab_partion_11.setFont(font9)
        self.tab_partion_11.setStyleSheet(u"color: rgb(119, 118, 123);\n"
"background-color: rgba(191, 64, 64, 0);\n"
"border: 1px solid rgba(0, 0, 0, 0);\n"
"background-color: rgba(0, 0 0, 0);")
        self.tab_partion_11.setTextFormat(Qt.TextFormat.PlainText)
        self.tab_partion_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_31.addWidget(self.tab_partion_11)

        self.search_memu_bnt = QPushButton(self.tab_backgournd)
        self.search_memu_bnt.setObjectName(u"search_memu_bnt")
        self.search_memu_bnt.setMinimumSize(QSize(163, 28))
        self.search_memu_bnt.setMaximumSize(QSize(163, 28))
        self.search_memu_bnt.setFont(font8)
        self.search_memu_bnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.search_memu_bnt.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(191, 64, 64, 0);\n"
"border: 1px solid rgba(0, 0, 0, 0);")

        self.horizontalLayout_31.addWidget(self.search_memu_bnt)

        self.tab_partion_5 = QLabel(self.tab_backgournd)
        self.tab_partion_5.setObjectName(u"tab_partion_5")
        sizePolicy1.setHeightForWidth(self.tab_partion_5.sizePolicy().hasHeightForWidth())
        self.tab_partion_5.setSizePolicy(sizePolicy1)
        self.tab_partion_5.setMinimumSize(QSize(3, 0))
        self.tab_partion_5.setFont(font9)
        self.tab_partion_5.setStyleSheet(u"color: rgb(119, 118, 123);\n"
"background-color: rgba(191, 64, 64, 0);\n"
"border: 1px solid rgba(0, 0, 0, 0);\n"
"background-color: rgba(0, 0 0, 0);")
        self.tab_partion_5.setTextFormat(Qt.TextFormat.PlainText)
        self.tab_partion_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_31.addWidget(self.tab_partion_5)

        self.setting_bnt = QPushButton(self.tab_backgournd)
        self.setting_bnt.setObjectName(u"setting_bnt")
        self.setting_bnt.setMinimumSize(QSize(163, 28))
        self.setting_bnt.setMaximumSize(QSize(163, 28))
        self.setting_bnt.setFont(font8)
        self.setting_bnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.setting_bnt.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(191, 64, 64, 0);\n"
"border: 1px solid rgba(0, 0, 0, 0);")

        self.horizontalLayout_31.addWidget(self.setting_bnt)

        self.tab_partion_4 = QLabel(self.tab_backgournd)
        self.tab_partion_4.setObjectName(u"tab_partion_4")
        sizePolicy1.setHeightForWidth(self.tab_partion_4.sizePolicy().hasHeightForWidth())
        self.tab_partion_4.setSizePolicy(sizePolicy1)
        self.tab_partion_4.setMinimumSize(QSize(3, 0))
        self.tab_partion_4.setFont(font9)
        self.tab_partion_4.setStyleSheet(u"color: rgb(119, 118, 123);\n"
"background-color: rgba(191, 64, 64, 0);\n"
"border: 1px solid rgba(0, 0, 0, 0);\n"
"background-color: rgba(0, 0 0, 0);")
        self.tab_partion_4.setTextFormat(Qt.TextFormat.PlainText)
        self.tab_partion_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_31.addWidget(self.tab_partion_4)

        self.admin_bnt = QPushButton(self.tab_backgournd)
        self.admin_bnt.setObjectName(u"admin_bnt")
        self.admin_bnt.setMinimumSize(QSize(163, 28))
        self.admin_bnt.setMaximumSize(QSize(163, 28))
        self.admin_bnt.setFont(font8)
        self.admin_bnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
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
        self.labeling_bnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.labeling_bnt.setStyleSheet(u"background-color: rgb(3, 3, 13);\n"
"border: 1px solid rgb(3, 3, 13);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/ui/ui/images/ico_ai_setting.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.labeling_bnt.setIcon(icon1)
        self.labeling_bnt.setIconSize(QSize(31, 50))

        self.horizontalLayout_36.addWidget(self.labeling_bnt)

        self.camera_schedule_bnt = QPushButton(self.centralwidget)
        self.camera_schedule_bnt.setObjectName(u"camera_schedule_bnt")
        self.camera_schedule_bnt.setMinimumSize(QSize(37, 52))
        self.camera_schedule_bnt.setFont(font1)
        self.camera_schedule_bnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.camera_schedule_bnt.setStyleSheet(u"background-color: rgb(3, 3, 13);\n"
"border: 1px solid rgb(3, 3, 13);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/ui/ui/images/ico_timer.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
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
        self.stackedWidget.setStyleSheet(u"QScrollBar:vertical {\n"
"    border: 1px solid #999999;\n"
"    background: #b3b3b3c6;\n"
"    width: 8px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"background: #2f2f2f; \n"
"min-height: 10px;\n"
"width: 8px;\n"
"\n"
"}")
        self.camera_page = QWidget()
        self.camera_page.setObjectName(u"camera_page")
        self.verticalLayout_47 = QVBoxLayout(self.camera_page)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.widget = QWidget(self.camera_page)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(301, 351))
        self.widget.setMaximumSize(QSize(350, 9999))
        self.verticalLayout_10 = QVBoxLayout(self.widget)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.horizontalLayout_40 = QHBoxLayout()
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.camera_page_camera_name_label = QLabel(self.widget)
        self.camera_page_camera_name_label.setObjectName(u"camera_page_camera_name_label")
        sizePolicy1.setHeightForWidth(self.camera_page_camera_name_label.sizePolicy().hasHeightForWidth())
        self.camera_page_camera_name_label.setSizePolicy(sizePolicy1)
        self.camera_page_camera_name_label.setMinimumSize(QSize(93, 31))
        font10 = QFont()
        font10.setFamilies([u"Sans"])
        font10.setPointSize(12)
        font10.setBold(True)
        self.camera_page_camera_name_label.setFont(font10)
        self.camera_page_camera_name_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.camera_page_camera_name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_40.addWidget(self.camera_page_camera_name_label)

        self.camera_page_name_box = QComboBox(self.widget)
        self.camera_page_name_box.setObjectName(u"camera_page_name_box")
        self.camera_page_name_box.setMinimumSize(QSize(141, 39))
        self.camera_page_name_box.setMaximumSize(QSize(145, 39))
        font11 = QFont()
        font11.setFamilies([u"Sans"])
        font11.setPointSize(11)
        self.camera_page_name_box.setFont(font11)
        self.camera_page_name_box.setFocusPolicy(Qt.FocusPolicy.WheelFocus)
        self.camera_page_name_box.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(13, 16, 23);\n"
"selection-background-color: rgb(53, 132, 228);\n"
"")
        self.camera_page_name_box.setCurrentText(u"")
        self.camera_page_name_box.setMaxVisibleItems(16)

        self.horizontalLayout_40.addWidget(self.camera_page_name_box)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_40.addItem(self.horizontalSpacer_10)


        self.verticalLayout_15.addLayout(self.horizontalLayout_40)

        self.horizontalLayout_41 = QHBoxLayout()
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_48 = QHBoxLayout()
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.camera_page_camera_event_label = QLabel(self.widget)
        self.camera_page_camera_event_label.setObjectName(u"camera_page_camera_event_label")
        sizePolicy1.setHeightForWidth(self.camera_page_camera_event_label.sizePolicy().hasHeightForWidth())
        self.camera_page_camera_event_label.setSizePolicy(sizePolicy1)
        self.camera_page_camera_event_label.setMinimumSize(QSize(93, 31))
        self.camera_page_camera_event_label.setFont(font10)
        self.camera_page_camera_event_label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.camera_page_camera_event_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_48.addWidget(self.camera_page_camera_event_label)

        self.horizontalLayout_49 = QHBoxLayout()
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.camera_page_camera_event_box = QComboBox(self.widget)
        self.camera_page_camera_event_box.addItem("")
        self.camera_page_camera_event_box.addItem("")
        self.camera_page_camera_event_box.addItem("")
        self.camera_page_camera_event_box.addItem("")
        self.camera_page_camera_event_box.setObjectName(u"camera_page_camera_event_box")
        sizePolicy1.setHeightForWidth(self.camera_page_camera_event_box.sizePolicy().hasHeightForWidth())
        self.camera_page_camera_event_box.setSizePolicy(sizePolicy1)
        self.camera_page_camera_event_box.setMinimumSize(QSize(141, 39))
        self.camera_page_camera_event_box.setMaximumSize(QSize(141, 39))
        font12 = QFont()
        font12.setFamilies([u"Sans"])
        font12.setPointSize(11)
        font12.setBold(False)
        self.camera_page_camera_event_box.setFont(font12)
        self.camera_page_camera_event_box.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(13, 16, 23);\n"
"selection-background-color: rgb(53, 132, 228);\n"
"")
        self.camera_page_camera_event_box.setMaxVisibleItems(16)
        self.camera_page_camera_event_box.setMinimumContentsLength(0)

        self.horizontalLayout_49.addWidget(self.camera_page_camera_event_box)

        self.camera_page_detect_add_bnt = QPushButton(self.widget)
        self.camera_page_detect_add_bnt.setObjectName(u"camera_page_detect_add_bnt")
        sizePolicy1.setHeightForWidth(self.camera_page_detect_add_bnt.sizePolicy().hasHeightForWidth())
        self.camera_page_detect_add_bnt.setSizePolicy(sizePolicy1)
        self.camera_page_detect_add_bnt.setMinimumSize(QSize(31, 31))
        self.camera_page_detect_add_bnt.setFont(font1)
        self.camera_page_detect_add_bnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.camera_page_detect_add_bnt.setStyleSheet(u"background-color: rgb(3, 3, 13);\n"
"border: 1px solid rgb(3, 3, 13);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/ui/ui/images/ico_add_circle.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.camera_page_detect_add_bnt.setIcon(icon3)
        self.camera_page_detect_add_bnt.setIconSize(QSize(31, 50))

        self.horizontalLayout_49.addWidget(self.camera_page_detect_add_bnt)


        self.horizontalLayout_48.addLayout(self.horizontalLayout_49)


        self.horizontalLayout_41.addLayout(self.horizontalLayout_48)

        self.horizontalSpacer_31 = QSpacerItem(46, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_41.addItem(self.horizontalSpacer_31)


        self.verticalLayout_15.addLayout(self.horizontalLayout_41)

        self.horizontalLayout_50 = QHBoxLayout()
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setSpacing(6)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.camera_page_detect_area_table = QTableWidget(self.widget)
        if (self.camera_page_detect_area_table.columnCount() < 1):
            self.camera_page_detect_area_table.setColumnCount(1)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.camera_page_detect_area_table.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        self.camera_page_detect_area_table.setObjectName(u"camera_page_detect_area_table")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.camera_page_detect_area_table.sizePolicy().hasHeightForWidth())
        self.camera_page_detect_area_table.setSizePolicy(sizePolicy3)
        self.camera_page_detect_area_table.setMinimumSize(QSize(231, 273))
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

        self.verticalLayout_22.addWidget(self.camera_page_detect_area_table)

        self.horizontalLayout_51 = QHBoxLayout()
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.horizontalSpacer_33 = QSpacerItem(166, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_51.addItem(self.horizontalSpacer_33)

        self.camera_page_object_setting_bnt = QPushButton(self.widget)
        self.camera_page_object_setting_bnt.setObjectName(u"camera_page_object_setting_bnt")
        sizePolicy1.setHeightForWidth(self.camera_page_object_setting_bnt.sizePolicy().hasHeightForWidth())
        self.camera_page_object_setting_bnt.setSizePolicy(sizePolicy1)
        self.camera_page_object_setting_bnt.setMinimumSize(QSize(100, 30))
        self.camera_page_object_setting_bnt.setMaximumSize(QSize(100, 30))
        self.camera_page_object_setting_bnt.setFont(font1)
        self.camera_page_object_setting_bnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.camera_page_object_setting_bnt.setStyleSheet(u"background-color: rgb(36, 39, 44);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 12px;\n"
"\n"
"")

        self.horizontalLayout_51.addWidget(self.camera_page_object_setting_bnt)

        self.camera_page_detect_area_del_bnt = QPushButton(self.widget)
        self.camera_page_detect_area_del_bnt.setObjectName(u"camera_page_detect_area_del_bnt")
        sizePolicy1.setHeightForWidth(self.camera_page_detect_area_del_bnt.sizePolicy().hasHeightForWidth())
        self.camera_page_detect_area_del_bnt.setSizePolicy(sizePolicy1)
        self.camera_page_detect_area_del_bnt.setMinimumSize(QSize(61, 31))
        self.camera_page_detect_area_del_bnt.setMaximumSize(QSize(61, 31))
        self.camera_page_detect_area_del_bnt.setFont(font1)
        self.camera_page_detect_area_del_bnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.camera_page_detect_area_del_bnt.setStyleSheet(u"background-color: rgb(255, 49, 38);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 12px;\n"
"")

        self.horizontalLayout_51.addWidget(self.camera_page_detect_area_del_bnt)


        self.verticalLayout_22.addLayout(self.horizontalLayout_51)

        self.horizontalLayout_52 = QHBoxLayout()
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.horizontalSpacer_14 = QSpacerItem(129, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_52.addItem(self.horizontalSpacer_14)

        self.camera_page_ai_bnt = QPushButton(self.widget)
        self.camera_page_ai_bnt.setObjectName(u"camera_page_ai_bnt")
        sizePolicy1.setHeightForWidth(self.camera_page_ai_bnt.sizePolicy().hasHeightForWidth())
        self.camera_page_ai_bnt.setSizePolicy(sizePolicy1)
        self.camera_page_ai_bnt.setMinimumSize(QSize(122, 33))
        self.camera_page_ai_bnt.setFont(font1)
        self.camera_page_ai_bnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.camera_page_ai_bnt.setStyleSheet(u"background-color: qlineargradient(\n"
"    spread:pad,\n"
"    x1:0, y1:0, x2:0, y2:1,\n"
"    stop:0.0 rgba(112, 210, 112, 255),\n"
"    stop:0.3 rgba(0, 196, 0, 255)\n"
");\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"\n"
"")

        self.horizontalLayout_52.addWidget(self.camera_page_ai_bnt)


        self.verticalLayout_22.addLayout(self.horizontalLayout_52)


        self.horizontalLayout_50.addLayout(self.verticalLayout_22)

        self.horizontalSpacer_44 = QSpacerItem(63, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_50.addItem(self.horizontalSpacer_44)


        self.verticalLayout_15.addLayout(self.horizontalLayout_50)

        self.verticalSpacer_7 = QSpacerItem(20, 270, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_15.addItem(self.verticalSpacer_7)


        self.verticalLayout_10.addLayout(self.verticalLayout_15)


        self.horizontalLayout_16.addWidget(self.widget)

        self.horizontalLayout_53 = QHBoxLayout()
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.widget_5 = QWidget(self.camera_page)
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
        self.camera_page_block_label = QLabel(self.widget_5)
        self.camera_page_block_label.setObjectName(u"camera_page_block_label")
        sizePolicy1.setHeightForWidth(self.camera_page_block_label.sizePolicy().hasHeightForWidth())
        self.camera_page_block_label.setSizePolicy(sizePolicy1)
        self.camera_page_block_label.setMinimumSize(QSize(63, 21))
        self.camera_page_block_label.setMaximumSize(QSize(260, 21))
        self.camera_page_block_label.setFont(font11)
        self.camera_page_block_label.setStyleSheet(u"color: rgb(242, 18, 94);")
        self.camera_page_block_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_63.addWidget(self.camera_page_block_label)


        self.horizontalLayout_54.addLayout(self.horizontalLayout_63)

        self.horizontalSpacer_45 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_54.addItem(self.horizontalSpacer_45)

        self.camera_page_ai_active_icon = QLabel(self.widget_5)
        self.camera_page_ai_active_icon.setObjectName(u"camera_page_ai_active_icon")
        sizePolicy1.setHeightForWidth(self.camera_page_ai_active_icon.sizePolicy().hasHeightForWidth())
        self.camera_page_ai_active_icon.setSizePolicy(sizePolicy1)
        self.camera_page_ai_active_icon.setMinimumSize(QSize(21, 21))
        self.camera_page_ai_active_icon.setMaximumSize(QSize(21, 21))
        self.camera_page_ai_active_icon.setFont(font)
        self.camera_page_ai_active_icon.setStyleSheet(u"color: rgb(242, 18, 94);")
        self.camera_page_ai_active_icon.setPixmap(QPixmap(u":/ui/ui/images/ico_analysis_on.svg"))
        self.camera_page_ai_active_icon.setScaledContents(True)

        self.horizontalLayout_54.addWidget(self.camera_page_ai_active_icon)

        self.camera_page_ai_active_label = QLabel(self.widget_5)
        self.camera_page_ai_active_label.setObjectName(u"camera_page_ai_active_label")
        sizePolicy1.setHeightForWidth(self.camera_page_ai_active_label.sizePolicy().hasHeightForWidth())
        self.camera_page_ai_active_label.setSizePolicy(sizePolicy1)
        self.camera_page_ai_active_label.setMinimumSize(QSize(130, 21))
        self.camera_page_ai_active_label.setMaximumSize(QSize(130, 21))
        self.camera_page_ai_active_label.setFont(font11)
        self.camera_page_ai_active_label.setStyleSheet(u"color: rgb(242, 18, 94);")

        self.horizontalLayout_54.addWidget(self.camera_page_ai_active_label)


        self.verticalLayout_30.addLayout(self.horizontalLayout_54)


        self.verticalLayout_23.addWidget(self.widget_5)

        self.ai_camera_page_verticalLayout = QVBoxLayout()
        self.ai_camera_page_verticalLayout.setSpacing(0)
        self.ai_camera_page_verticalLayout.setObjectName(u"ai_camera_page_verticalLayout")
        self.verticalSpacer_26 = QSpacerItem(20, 3, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.ai_camera_page_verticalLayout.addItem(self.verticalSpacer_26)

        self.camera_page_viewer = QLabel(self.camera_page)
        self.camera_page_viewer.setObjectName(u"camera_page_viewer")
        sizePolicy2.setHeightForWidth(self.camera_page_viewer.sizePolicy().hasHeightForWidth())
        self.camera_page_viewer.setSizePolicy(sizePolicy2)
        self.camera_page_viewer.setMinimumSize(QSize(325, 360))
        self.camera_page_viewer.setMaximumSize(QSize(9999, 9999))
        self.camera_page_viewer.setFont(font11)
        self.camera_page_viewer.setStyleSheet(u"border: 1px solid rgb(119, 118, 123);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.camera_page_viewer.setScaledContents(False)

        self.ai_camera_page_verticalLayout.addWidget(self.camera_page_viewer)


        self.verticalLayout_23.addLayout(self.ai_camera_page_verticalLayout)


        self.horizontalLayout_53.addLayout(self.verticalLayout_23)


        self.horizontalLayout_16.addLayout(self.horizontalLayout_53)


        self.verticalLayout_47.addLayout(self.horizontalLayout_16)

        self.stackedWidget.addWidget(self.camera_page)
        self.setting_page = QWidget()
        self.setting_page.setObjectName(u"setting_page")
        self.verticalLayout_53 = QVBoxLayout(self.setting_page)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.setting_scrollArea = QScrollArea(self.setting_page)
        self.setting_scrollArea.setObjectName(u"setting_scrollArea")
        self.setting_scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 891, 1415))
        self.verticalLayout_6 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_34 = QVBoxLayout()
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.widget_13 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_13.setObjectName(u"widget_13")
        self.verticalLayout_51 = QVBoxLayout(self.widget_13)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.horizontalLayout_61 = QHBoxLayout()
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.horizontalSpacer_51 = QSpacerItem(13, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_61.addItem(self.horizontalSpacer_51)

        self.setting_detect_info_label = QLabel(self.widget_13)
        self.setting_detect_info_label.setObjectName(u"setting_detect_info_label")
        self.setting_detect_info_label.setMinimumSize(QSize(197, 28))
        self.setting_detect_info_label.setMaximumSize(QSize(9999, 28))
        font13 = QFont()
        font13.setFamilies([u"Sans"])
        font13.setPointSize(11)
        font13.setBold(True)
        self.setting_detect_info_label.setFont(font13)
        self.setting_detect_info_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.setting_detect_info_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_61.addWidget(self.setting_detect_info_label)

        self.horizontalSpacer_32 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_61.addItem(self.horizontalSpacer_32)


        self.verticalLayout_51.addLayout(self.horizontalLayout_61)

        self.horizontalLayout_76 = QHBoxLayout()
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.horizontalSpacer_34 = QSpacerItem(232, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_76.addItem(self.horizontalSpacer_34)

        self.setting_detect_bbox_active_label = QLabel(self.widget_13)
        self.setting_detect_bbox_active_label.setObjectName(u"setting_detect_bbox_active_label")
        self.setting_detect_bbox_active_label.setMinimumSize(QSize(91, 28))
        self.setting_detect_bbox_active_label.setMaximumSize(QSize(91, 28))
        self.setting_detect_bbox_active_label.setFont(font11)
        self.setting_detect_bbox_active_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.setting_detect_bbox_active_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_76.addWidget(self.setting_detect_bbox_active_label)

        self.setting_detect_bbox_active_bnt = QPushButton(self.widget_13)
        self.setting_detect_bbox_active_bnt.setObjectName(u"setting_detect_bbox_active_bnt")
        self.setting_detect_bbox_active_bnt.setMinimumSize(QSize(61, 25))
        self.setting_detect_bbox_active_bnt.setMaximumSize(QSize(61, 25))
        self.setting_detect_bbox_active_bnt.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    padding: 0px; /* \ud328\ub529\ub3c4 0\uc73c\ub85c \uc124\uc815 */\n"
"    outline: none;\n"
"}\n"
"\n"
"/* hover, pressed \uc0c1\ud0dc\uc5d0\ub3c4 \uc544\ubb34 \ud6a8\uacfc \uc5c6\uc74c */\n"
"QPushButton:hover {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/ui/ui/images/icon-switch-off.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon4.addFile(u":/ui/ui/images/icon-switch-on.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        icon4.addFile(u":/ui/ui/images/icon-switch-off.png", QSize(), QIcon.Mode.Selected, QIcon.State.Off)
        icon4.addFile(u":/ui/ui/images/icon-switch-on.png", QSize(), QIcon.Mode.Selected, QIcon.State.On)
        self.setting_detect_bbox_active_bnt.setIcon(icon4)
        self.setting_detect_bbox_active_bnt.setIconSize(QSize(55, 103))
        self.setting_detect_bbox_active_bnt.setCheckable(True)

        self.horizontalLayout_76.addWidget(self.setting_detect_bbox_active_bnt)

        self.horizontalSpacer_35 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_76.addItem(self.horizontalSpacer_35)


        self.verticalLayout_51.addLayout(self.horizontalLayout_76)

        self.horizontalLayout_77 = QHBoxLayout()
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.horizontalSpacer_107 = QSpacerItem(232, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_77.addItem(self.horizontalSpacer_107)

        self.setting_detect_label_active_label = QLabel(self.widget_13)
        self.setting_detect_label_active_label.setObjectName(u"setting_detect_label_active_label")
        self.setting_detect_label_active_label.setMinimumSize(QSize(91, 28))
        self.setting_detect_label_active_label.setMaximumSize(QSize(91, 28))
        self.setting_detect_label_active_label.setFont(font11)
        self.setting_detect_label_active_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.setting_detect_label_active_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_77.addWidget(self.setting_detect_label_active_label)

        self.setting_detect_label_active_bnt = QPushButton(self.widget_13)
        self.setting_detect_label_active_bnt.setObjectName(u"setting_detect_label_active_bnt")
        self.setting_detect_label_active_bnt.setMinimumSize(QSize(61, 25))
        self.setting_detect_label_active_bnt.setMaximumSize(QSize(61, 25))
        self.setting_detect_label_active_bnt.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    padding: 0px; /* \ud328\ub529\ub3c4 0\uc73c\ub85c \uc124\uc815 */\n"
"    outline: none;\n"
"}\n"
"\n"
"/* hover, pressed \uc0c1\ud0dc\uc5d0\ub3c4 \uc544\ubb34 \ud6a8\uacfc \uc5c6\uc74c */\n"
"QPushButton:hover {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.setting_detect_label_active_bnt.setIcon(icon4)
        self.setting_detect_label_active_bnt.setIconSize(QSize(55, 103))
        self.setting_detect_label_active_bnt.setCheckable(True)

        self.horizontalLayout_77.addWidget(self.setting_detect_label_active_bnt)

        self.horizontalSpacer_108 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_77.addItem(self.horizontalSpacer_108)


        self.verticalLayout_51.addLayout(self.horizontalLayout_77)

        self.horizontalLayout_78 = QHBoxLayout()
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.horizontalSpacer_109 = QSpacerItem(216, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_78.addItem(self.horizontalSpacer_109)

        self.setting_detect_roi_active_label = QLabel(self.widget_13)
        self.setting_detect_roi_active_label.setObjectName(u"setting_detect_roi_active_label")
        self.setting_detect_roi_active_label.setMinimumSize(QSize(107, 28))
        self.setting_detect_roi_active_label.setMaximumSize(QSize(117, 28))
        self.setting_detect_roi_active_label.setFont(font11)
        self.setting_detect_roi_active_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.setting_detect_roi_active_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_78.addWidget(self.setting_detect_roi_active_label)

        self.setting_detect_roi_active_bnt = QPushButton(self.widget_13)
        self.setting_detect_roi_active_bnt.setObjectName(u"setting_detect_roi_active_bnt")
        self.setting_detect_roi_active_bnt.setMinimumSize(QSize(61, 25))
        self.setting_detect_roi_active_bnt.setMaximumSize(QSize(61, 25))
        self.setting_detect_roi_active_bnt.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    padding: 0px; /* \ud328\ub529\ub3c4 0\uc73c\ub85c \uc124\uc815 */\n"
"    outline: none;\n"
"}\n"
"\n"
"/* hover, pressed \uc0c1\ud0dc\uc5d0\ub3c4 \uc544\ubb34 \ud6a8\uacfc \uc5c6\uc74c */\n"
"QPushButton:hover {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.setting_detect_roi_active_bnt.setIcon(icon4)
        self.setting_detect_roi_active_bnt.setIconSize(QSize(55, 103))
        self.setting_detect_roi_active_bnt.setCheckable(True)

        self.horizontalLayout_78.addWidget(self.setting_detect_roi_active_bnt)

        self.horizontalSpacer_110 = QSpacerItem(38, 25, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_78.addItem(self.horizontalSpacer_110)


        self.verticalLayout_51.addLayout(self.horizontalLayout_78)

        self.setting_partion_6 = QFrame(self.widget_13)
        self.setting_partion_6.setObjectName(u"setting_partion_6")
        sizePolicy1.setHeightForWidth(self.setting_partion_6.sizePolicy().hasHeightForWidth())
        self.setting_partion_6.setSizePolicy(sizePolicy1)
        self.setting_partion_6.setMinimumSize(QSize(246, 3))
        self.setting_partion_6.setMaximumSize(QSize(434, 3))
        font14 = QFont()
        font14.setFamilies([u"Sans"])
        font14.setPointSize(5)
        font14.setStrikeOut(False)
        self.setting_partion_6.setFont(font14)
        self.setting_partion_6.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.setting_partion_6.setAutoFillBackground(False)
        self.setting_partion_6.setStyleSheet(u"background-color: rgb(36, 39, 44)")
        self.setting_partion_6.setFrameShape(QFrame.Shape.HLine)
        self.setting_partion_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_51.addWidget(self.setting_partion_6)


        self.verticalLayout_34.addWidget(self.widget_13)

        self.widget_14 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_14.setObjectName(u"widget_14")
        self.widget_14.setMaximumSize(QSize(16777215, 309))
        self.verticalLayout_62 = QVBoxLayout(self.widget_14)
        self.verticalLayout_62.setSpacing(8)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.verticalLayout_62.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_62 = QHBoxLayout()
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.horizontalSpacer_56 = QSpacerItem(13, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_62.addItem(self.horizontalSpacer_56)

        self.setting_event_pop_up_label = QLabel(self.widget_14)
        self.setting_event_pop_up_label.setObjectName(u"setting_event_pop_up_label")
        self.setting_event_pop_up_label.setMinimumSize(QSize(197, 28))
        self.setting_event_pop_up_label.setMaximumSize(QSize(9999, 28))
        self.setting_event_pop_up_label.setFont(font13)
        self.setting_event_pop_up_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.setting_event_pop_up_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_62.addWidget(self.setting_event_pop_up_label)

        self.horizontalSpacer_50 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_62.addItem(self.horizontalSpacer_50)


        self.verticalLayout_62.addLayout(self.horizontalLayout_62)

        self.horizontalLayout_100 = QHBoxLayout()
        self.horizontalLayout_100.setObjectName(u"horizontalLayout_100")
        self.horizontalSpacer_58 = QSpacerItem(202, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_100.addItem(self.horizontalSpacer_58)

        self.setting_event_pop_up_active_label = QLabel(self.widget_14)
        self.setting_event_pop_up_active_label.setObjectName(u"setting_event_pop_up_active_label")
        self.setting_event_pop_up_active_label.setMinimumSize(QSize(91, 28))
        self.setting_event_pop_up_active_label.setMaximumSize(QSize(140, 28))
        self.setting_event_pop_up_active_label.setFont(font11)
        self.setting_event_pop_up_active_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.setting_event_pop_up_active_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_100.addWidget(self.setting_event_pop_up_active_label)

        self.setting_event_pop_up_active_bnt = QPushButton(self.widget_14)
        self.setting_event_pop_up_active_bnt.setObjectName(u"setting_event_pop_up_active_bnt")
        self.setting_event_pop_up_active_bnt.setMinimumSize(QSize(61, 25))
        self.setting_event_pop_up_active_bnt.setMaximumSize(QSize(61, 25))
        self.setting_event_pop_up_active_bnt.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    padding: 0px; /* \ud328\ub529\ub3c4 0\uc73c\ub85c \uc124\uc815 */\n"
"    outline: none;\n"
"}\n"
"\n"
"/* hover, pressed \uc0c1\ud0dc\uc5d0\ub3c4 \uc544\ubb34 \ud6a8\uacfc \uc5c6\uc74c */\n"
"QPushButton:hover {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.setting_event_pop_up_active_bnt.setIcon(icon4)
        self.setting_event_pop_up_active_bnt.setIconSize(QSize(55, 103))
        self.setting_event_pop_up_active_bnt.setCheckable(True)

        self.horizontalLayout_100.addWidget(self.setting_event_pop_up_active_bnt)

        self.horizontalSpacer_59 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_100.addItem(self.horizontalSpacer_59)


        self.verticalLayout_62.addLayout(self.horizontalLayout_100)

        self.horizontalLayout_101 = QHBoxLayout()
        self.horizontalLayout_101.setObjectName(u"horizontalLayout_101")
        self.horizontalSpacer_139 = QSpacerItem(202, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_101.addItem(self.horizontalSpacer_139)

        self.setting_event_pop_up_duration_bnt = QLabel(self.widget_14)
        self.setting_event_pop_up_duration_bnt.setObjectName(u"setting_event_pop_up_duration_bnt")
        self.setting_event_pop_up_duration_bnt.setMinimumSize(QSize(91, 28))
        self.setting_event_pop_up_duration_bnt.setMaximumSize(QSize(120, 28))
        self.setting_event_pop_up_duration_bnt.setFont(font11)
        self.setting_event_pop_up_duration_bnt.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.setting_event_pop_up_duration_bnt.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_101.addWidget(self.setting_event_pop_up_duration_bnt)

        self.setting_event_pop_up_duration_box = QComboBox(self.widget_14)
        self.setting_event_pop_up_duration_box.addItem("")
        self.setting_event_pop_up_duration_box.addItem("")
        self.setting_event_pop_up_duration_box.addItem("")
        self.setting_event_pop_up_duration_box.addItem("")
        self.setting_event_pop_up_duration_box.addItem("")
        self.setting_event_pop_up_duration_box.setObjectName(u"setting_event_pop_up_duration_box")
        sizePolicy1.setHeightForWidth(self.setting_event_pop_up_duration_box.sizePolicy().hasHeightForWidth())
        self.setting_event_pop_up_duration_box.setSizePolicy(sizePolicy1)
        self.setting_event_pop_up_duration_box.setMinimumSize(QSize(80, 24))
        self.setting_event_pop_up_duration_box.setMaximumSize(QSize(68, 24))
        self.setting_event_pop_up_duration_box.setFont(font7)
        self.setting_event_pop_up_duration_box.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(13, 16, 23);\n"
"\n"
"")
        self.setting_event_pop_up_duration_box.setEditable(True)
        self.setting_event_pop_up_duration_box.setMinimumContentsLength(0)

        self.horizontalLayout_101.addWidget(self.setting_event_pop_up_duration_box)

        self.horizontalSpacer_140 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_101.addItem(self.horizontalSpacer_140)


        self.verticalLayout_62.addLayout(self.horizontalLayout_101)

        self.horizontalLayout_102 = QHBoxLayout()
        self.horizontalLayout_102.setObjectName(u"horizontalLayout_102")
        self.horizontalSpacer_141 = QSpacerItem(338, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_102.addItem(self.horizontalSpacer_141)

        self.setting_event_pop_up_save_bnt = QPushButton(self.widget_14)
        self.setting_event_pop_up_save_bnt.setObjectName(u"setting_event_pop_up_save_bnt")
        sizePolicy.setHeightForWidth(self.setting_event_pop_up_save_bnt.sizePolicy().hasHeightForWidth())
        self.setting_event_pop_up_save_bnt.setSizePolicy(sizePolicy)
        self.setting_event_pop_up_save_bnt.setMinimumSize(QSize(71, 41))
        self.setting_event_pop_up_save_bnt.setMaximumSize(QSize(71, 41))
        self.setting_event_pop_up_save_bnt.setFont(font1)
        self.setting_event_pop_up_save_bnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.setting_event_pop_up_save_bnt.setStyleSheet(u"background-color: qlineargradient(\n"
"    spread:pad,\n"
"    x1:0, y1:0, x2:0, y2:1,\n"
"    stop:0.0 rgba(112, 210, 112, 255),\n"
"    stop:0.3 rgba(0, 196, 0, 255)\n"
");\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 19px;\n"
"\n"
"")

        self.horizontalLayout_102.addWidget(self.setting_event_pop_up_save_bnt)

        self.horizontalSpacer_142 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_102.addItem(self.horizontalSpacer_142)


        self.verticalLayout_62.addLayout(self.horizontalLayout_102)


        self.verticalLayout_34.addWidget(self.widget_14)

        self.setting_partion_4 = QFrame(self.scrollAreaWidgetContents_2)
        self.setting_partion_4.setObjectName(u"setting_partion_4")
        sizePolicy1.setHeightForWidth(self.setting_partion_4.sizePolicy().hasHeightForWidth())
        self.setting_partion_4.setSizePolicy(sizePolicy1)
        self.setting_partion_4.setMinimumSize(QSize(246, 3))
        self.setting_partion_4.setMaximumSize(QSize(434, 3))
        self.setting_partion_4.setFont(font14)
        self.setting_partion_4.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.setting_partion_4.setAutoFillBackground(False)
        self.setting_partion_4.setStyleSheet(u"background-color: rgb(36, 39, 44)")
        self.setting_partion_4.setFrameShape(QFrame.Shape.HLine)
        self.setting_partion_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_34.addWidget(self.setting_partion_4)

        self.setting_self_labeling_widget = QWidget(self.scrollAreaWidgetContents_2)
        self.setting_self_labeling_widget.setObjectName(u"setting_self_labeling_widget")
        self.verticalLayout_52 = QVBoxLayout(self.setting_self_labeling_widget)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.horizontalLayout_79 = QHBoxLayout()
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.horizontalSpacer_52 = QSpacerItem(13, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_79.addItem(self.horizontalSpacer_52)

        self.setting_label_4 = QLabel(self.setting_self_labeling_widget)
        self.setting_label_4.setObjectName(u"setting_label_4")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.setting_label_4.sizePolicy().hasHeightForWidth())
        self.setting_label_4.setSizePolicy(sizePolicy4)
        self.setting_label_4.setMinimumSize(QSize(122, 22))
        self.setting_label_4.setMaximumSize(QSize(208, 22))
        self.setting_label_4.setFont(font13)
        self.setting_label_4.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.setting_label_4.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_79.addWidget(self.setting_label_4)

        self.horizontalSpacer_36 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_79.addItem(self.horizontalSpacer_36)


        self.verticalLayout_52.addLayout(self.horizontalLayout_79)

        self.horizontalLayout_80 = QHBoxLayout()
        self.horizontalLayout_80.setObjectName(u"horizontalLayout_80")
        self.horizontalSpacer_69 = QSpacerItem(36, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_80.addItem(self.horizontalSpacer_69)

        self.setting_ai_weight_label = QLabel(self.setting_self_labeling_widget)
        self.setting_ai_weight_label.setObjectName(u"setting_ai_weight_label")
        sizePolicy1.setHeightForWidth(self.setting_ai_weight_label.sizePolicy().hasHeightForWidth())
        self.setting_ai_weight_label.setSizePolicy(sizePolicy1)
        self.setting_ai_weight_label.setMinimumSize(QSize(176, 28))
        self.setting_ai_weight_label.setMaximumSize(QSize(9999, 28))
        self.setting_ai_weight_label.setFont(font11)
        self.setting_ai_weight_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.setting_ai_weight_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_80.addWidget(self.setting_ai_weight_label)

        self.horizontalSpacer_111 = QSpacerItem(59, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_80.addItem(self.horizontalSpacer_111)

        self.setting_setting_ai_weight_box = QComboBox(self.setting_self_labeling_widget)
        self.setting_setting_ai_weight_box.addItem("")
        self.setting_setting_ai_weight_box.setObjectName(u"setting_setting_ai_weight_box")
        sizePolicy1.setHeightForWidth(self.setting_setting_ai_weight_box.sizePolicy().hasHeightForWidth())
        self.setting_setting_ai_weight_box.setSizePolicy(sizePolicy1)
        self.setting_setting_ai_weight_box.setMinimumSize(QSize(105, 31))
        self.setting_setting_ai_weight_box.setMaximumSize(QSize(105, 31))
        self.setting_setting_ai_weight_box.setFont(font7)
        self.setting_setting_ai_weight_box.setFocusPolicy(Qt.FocusPolicy.WheelFocus)
        self.setting_setting_ai_weight_box.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(13, 16, 23);\n"
"selection-background-color: rgb(53, 132, 228);\n"
"")
        self.setting_setting_ai_weight_box.setCurrentText(u"2024-07-24")
        self.setting_setting_ai_weight_box.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContentsOnFirstShow)

        self.horizontalLayout_80.addWidget(self.setting_setting_ai_weight_box)

        self.horizontalSpacer_112 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_80.addItem(self.horizontalSpacer_112)


        self.verticalLayout_52.addLayout(self.horizontalLayout_80)

        self.horizontalLayout_81 = QHBoxLayout()
        self.horizontalLayout_81.setObjectName(u"horizontalLayout_81")
        self.horizontalSpacer_113 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_81.addItem(self.horizontalSpacer_113)

        self.setting_self_training_auto_labeling_label = QLabel(self.setting_self_labeling_widget)
        self.setting_self_training_auto_labeling_label.setObjectName(u"setting_self_training_auto_labeling_label")
        sizePolicy1.setHeightForWidth(self.setting_self_training_auto_labeling_label.sizePolicy().hasHeightForWidth())
        self.setting_self_training_auto_labeling_label.setSizePolicy(sizePolicy1)
        self.setting_self_training_auto_labeling_label.setMinimumSize(QSize(1, 28))
        self.setting_self_training_auto_labeling_label.setMaximumSize(QSize(194, 28))
        self.setting_self_training_auto_labeling_label.setFont(font11)
        self.setting_self_training_auto_labeling_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.setting_self_training_auto_labeling_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_81.addWidget(self.setting_self_training_auto_labeling_label)

        self.horizontalSpacer_114 = QSpacerItem(92, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_81.addItem(self.horizontalSpacer_114)

        self.setting_self_training_auto_labeling_bnt = QPushButton(self.setting_self_labeling_widget)
        self.setting_self_training_auto_labeling_bnt.setObjectName(u"setting_self_training_auto_labeling_bnt")
        sizePolicy1.setHeightForWidth(self.setting_self_training_auto_labeling_bnt.sizePolicy().hasHeightForWidth())
        self.setting_self_training_auto_labeling_bnt.setSizePolicy(sizePolicy1)
        self.setting_self_training_auto_labeling_bnt.setMinimumSize(QSize(61, 25))
        self.setting_self_training_auto_labeling_bnt.setMaximumSize(QSize(187, 25))
        self.setting_self_training_auto_labeling_bnt.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    padding: 0px; /* \ud328\ub529\ub3c4 0\uc73c\ub85c \uc124\uc815 */\n"
"    outline: none;\n"
"}\n"
"\n"
"/* hover, pressed \uc0c1\ud0dc\uc5d0\ub3c4 \uc544\ubb34 \ud6a8\uacfc \uc5c6\uc74c */\n"
"QPushButton:hover {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.setting_self_training_auto_labeling_bnt.setIcon(icon4)
        self.setting_self_training_auto_labeling_bnt.setIconSize(QSize(55, 103))
        self.setting_self_training_auto_labeling_bnt.setCheckable(True)

        self.horizontalLayout_81.addWidget(self.setting_self_training_auto_labeling_bnt)

        self.horizontalSpacer_115 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_81.addItem(self.horizontalSpacer_115)


        self.verticalLayout_52.addLayout(self.horizontalLayout_81)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_135 = QSpacerItem(199, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_135)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(9)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.setting_auto_label_time_start_box = QComboBox(self.setting_self_labeling_widget)
        self.setting_auto_label_time_start_box.addItem("")
        self.setting_auto_label_time_start_box.addItem("")
        self.setting_auto_label_time_start_box.addItem("")
        self.setting_auto_label_time_start_box.addItem("")
        self.setting_auto_label_time_start_box.addItem("")
        self.setting_auto_label_time_start_box.addItem("")
        self.setting_auto_label_time_start_box.addItem("")
        self.setting_auto_label_time_start_box.addItem("")
        self.setting_auto_label_time_start_box.addItem("")
        self.setting_auto_label_time_start_box.addItem("")
        self.setting_auto_label_time_start_box.addItem("")
        self.setting_auto_label_time_start_box.addItem("")
        self.setting_auto_label_time_start_box.addItem("")
        self.setting_auto_label_time_start_box.addItem("")
        self.setting_auto_label_time_start_box.addItem("")
        self.setting_auto_label_time_start_box.addItem("")
        self.setting_auto_label_time_start_box.addItem("")
        self.setting_auto_label_time_start_box.addItem("")
        self.setting_auto_label_time_start_box.addItem("")
        self.setting_auto_label_time_start_box.addItem("")
        self.setting_auto_label_time_start_box.addItem("")
        self.setting_auto_label_time_start_box.addItem("")
        self.setting_auto_label_time_start_box.addItem("")
        self.setting_auto_label_time_start_box.addItem("")
        self.setting_auto_label_time_start_box.setObjectName(u"setting_auto_label_time_start_box")
        sizePolicy1.setHeightForWidth(self.setting_auto_label_time_start_box.sizePolicy().hasHeightForWidth())
        self.setting_auto_label_time_start_box.setSizePolicy(sizePolicy1)
        self.setting_auto_label_time_start_box.setMinimumSize(QSize(80, 24))
        self.setting_auto_label_time_start_box.setMaximumSize(QSize(68, 24))
        self.setting_auto_label_time_start_box.setFont(font7)
        self.setting_auto_label_time_start_box.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(13, 16, 23);\n"
"\n"
"")
        self.setting_auto_label_time_start_box.setEditable(True)
        self.setting_auto_label_time_start_box.setMinimumContentsLength(0)

        self.horizontalLayout_5.addWidget(self.setting_auto_label_time_start_box)

        self.time_tilde_2 = QLabel(self.setting_self_labeling_widget)
        self.time_tilde_2.setObjectName(u"time_tilde_2")
        sizePolicy1.setHeightForWidth(self.time_tilde_2.sizePolicy().hasHeightForWidth())
        self.time_tilde_2.setSizePolicy(sizePolicy1)
        font15 = QFont()
        font15.setFamilies([u"Sans"])
        font15.setPointSize(12)
        self.time_tilde_2.setFont(font15)
        self.time_tilde_2.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(191, 64, 64, 0);")
        self.time_tilde_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_5.addWidget(self.time_tilde_2)

        self.setting_auto_label_time_end_box = QComboBox(self.setting_self_labeling_widget)
        self.setting_auto_label_time_end_box.addItem("")
        self.setting_auto_label_time_end_box.addItem("")
        self.setting_auto_label_time_end_box.addItem("")
        self.setting_auto_label_time_end_box.addItem("")
        self.setting_auto_label_time_end_box.addItem("")
        self.setting_auto_label_time_end_box.addItem("")
        self.setting_auto_label_time_end_box.addItem("")
        self.setting_auto_label_time_end_box.addItem("")
        self.setting_auto_label_time_end_box.addItem("")
        self.setting_auto_label_time_end_box.addItem("")
        self.setting_auto_label_time_end_box.addItem("")
        self.setting_auto_label_time_end_box.addItem("")
        self.setting_auto_label_time_end_box.addItem("")
        self.setting_auto_label_time_end_box.addItem("")
        self.setting_auto_label_time_end_box.addItem("")
        self.setting_auto_label_time_end_box.addItem("")
        self.setting_auto_label_time_end_box.addItem("")
        self.setting_auto_label_time_end_box.addItem("")
        self.setting_auto_label_time_end_box.addItem("")
        self.setting_auto_label_time_end_box.addItem("")
        self.setting_auto_label_time_end_box.addItem("")
        self.setting_auto_label_time_end_box.addItem("")
        self.setting_auto_label_time_end_box.addItem("")
        self.setting_auto_label_time_end_box.addItem("")
        self.setting_auto_label_time_end_box.setObjectName(u"setting_auto_label_time_end_box")
        sizePolicy1.setHeightForWidth(self.setting_auto_label_time_end_box.sizePolicy().hasHeightForWidth())
        self.setting_auto_label_time_end_box.setSizePolicy(sizePolicy1)
        self.setting_auto_label_time_end_box.setMinimumSize(QSize(80, 24))
        self.setting_auto_label_time_end_box.setMaximumSize(QSize(68, 24))
        self.setting_auto_label_time_end_box.setFont(font7)
        self.setting_auto_label_time_end_box.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"selection-background-color: rgb(13, 16, 23);\n"
"\n"
"")
        self.setting_auto_label_time_end_box.setEditable(True)
        self.setting_auto_label_time_end_box.setMinimumContentsLength(0)

        self.horizontalLayout_5.addWidget(self.setting_auto_label_time_end_box)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_5)

        self.horizontalSpacer_136 = QSpacerItem(11, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_136)


        self.verticalLayout_52.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_116 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_116)

        self.setting_page_email_info_label_10 = QLabel(self.setting_self_labeling_widget)
        self.setting_page_email_info_label_10.setObjectName(u"setting_page_email_info_label_10")
        sizePolicy1.setHeightForWidth(self.setting_page_email_info_label_10.sizePolicy().hasHeightForWidth())
        self.setting_page_email_info_label_10.setSizePolicy(sizePolicy1)
        self.setting_page_email_info_label_10.setMinimumSize(QSize(12, 21))
        self.setting_page_email_info_label_10.setMaximumSize(QSize(9999, 21))
        self.setting_page_email_info_label_10.setFont(font1)
        self.setting_page_email_info_label_10.setStyleSheet(u"color: rgb(242, 18, 94);")

        self.horizontalLayout_7.addWidget(self.setting_page_email_info_label_10)

        self.horizontalSpacer_117 = QSpacerItem(4, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_117)


        self.verticalLayout_52.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_82 = QHBoxLayout()
        self.horizontalLayout_82.setObjectName(u"horizontalLayout_82")
        self.horizontalSpacer_118 = QSpacerItem(41, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_82.addItem(self.horizontalSpacer_118)

        self.setting_self_training_zeroshot_label = QLabel(self.setting_self_labeling_widget)
        self.setting_self_training_zeroshot_label.setObjectName(u"setting_self_training_zeroshot_label")
        sizePolicy1.setHeightForWidth(self.setting_self_training_zeroshot_label.sizePolicy().hasHeightForWidth())
        self.setting_self_training_zeroshot_label.setSizePolicy(sizePolicy1)
        self.setting_self_training_zeroshot_label.setMinimumSize(QSize(9, 28))
        self.setting_self_training_zeroshot_label.setMaximumSize(QSize(300, 28))
        self.setting_self_training_zeroshot_label.setFont(font11)
        self.setting_self_training_zeroshot_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.setting_self_training_zeroshot_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_82.addWidget(self.setting_self_training_zeroshot_label)

        self.horizontalSpacer_119 = QSpacerItem(60, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_82.addItem(self.horizontalSpacer_119)

        self.setting_self_training_zeroshot_bnt = QPushButton(self.setting_self_labeling_widget)
        self.setting_self_training_zeroshot_bnt.setObjectName(u"setting_self_training_zeroshot_bnt")
        sizePolicy1.setHeightForWidth(self.setting_self_training_zeroshot_bnt.sizePolicy().hasHeightForWidth())
        self.setting_self_training_zeroshot_bnt.setSizePolicy(sizePolicy1)
        self.setting_self_training_zeroshot_bnt.setMinimumSize(QSize(61, 25))
        self.setting_self_training_zeroshot_bnt.setMaximumSize(QSize(151, 25))
        self.setting_self_training_zeroshot_bnt.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    padding: 0px; /* \ud328\ub529\ub3c4 0\uc73c\ub85c \uc124\uc815 */\n"
"    outline: none;\n"
"}\n"
"\n"
"/* hover, pressed \uc0c1\ud0dc\uc5d0\ub3c4 \uc544\ubb34 \ud6a8\uacfc \uc5c6\uc74c */\n"
"QPushButton:hover {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.setting_self_training_zeroshot_bnt.setIcon(icon4)
        self.setting_self_training_zeroshot_bnt.setIconSize(QSize(55, 103))
        self.setting_self_training_zeroshot_bnt.setCheckable(True)

        self.horizontalLayout_82.addWidget(self.setting_self_training_zeroshot_bnt)

        self.horizontalSpacer_120 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_82.addItem(self.horizontalSpacer_120)


        self.verticalLayout_52.addLayout(self.horizontalLayout_82)

        self.horizontalLayout_83 = QHBoxLayout()
        self.horizontalLayout_83.setObjectName(u"horizontalLayout_83")
        self.horizontalSpacer_121 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_83.addItem(self.horizontalSpacer_121)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.setting_page_email_info_label_9 = QLabel(self.setting_self_labeling_widget)
        self.setting_page_email_info_label_9.setObjectName(u"setting_page_email_info_label_9")
        sizePolicy1.setHeightForWidth(self.setting_page_email_info_label_9.sizePolicy().hasHeightForWidth())
        self.setting_page_email_info_label_9.setSizePolicy(sizePolicy1)
        self.setting_page_email_info_label_9.setMinimumSize(QSize(12, 21))
        self.setting_page_email_info_label_9.setMaximumSize(QSize(9999, 21))
        self.setting_page_email_info_label_9.setFont(font1)
        self.setting_page_email_info_label_9.setStyleSheet(u"color: rgb(242, 18, 94);")

        self.verticalLayout_5.addWidget(self.setting_page_email_info_label_9)

        self.setting_page_email_info_label_11 = QLabel(self.setting_self_labeling_widget)
        self.setting_page_email_info_label_11.setObjectName(u"setting_page_email_info_label_11")
        sizePolicy1.setHeightForWidth(self.setting_page_email_info_label_11.sizePolicy().hasHeightForWidth())
        self.setting_page_email_info_label_11.setSizePolicy(sizePolicy1)
        self.setting_page_email_info_label_11.setMinimumSize(QSize(12, 21))
        self.setting_page_email_info_label_11.setMaximumSize(QSize(9999, 21))
        self.setting_page_email_info_label_11.setFont(font1)
        self.setting_page_email_info_label_11.setStyleSheet(u"color: rgb(242, 18, 94);")

        self.verticalLayout_5.addWidget(self.setting_page_email_info_label_11)


        self.horizontalLayout_83.addLayout(self.verticalLayout_5)

        self.horizontalSpacer_122 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_83.addItem(self.horizontalSpacer_122)


        self.verticalLayout_52.addLayout(self.horizontalLayout_83)

        self.horizontalLayout_84 = QHBoxLayout()
        self.horizontalLayout_84.setObjectName(u"horizontalLayout_84")
        self.horizontalSpacer_123 = QSpacerItem(338, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_84.addItem(self.horizontalSpacer_123)

        self.setting_ai_setting_save_bnt = QPushButton(self.setting_self_labeling_widget)
        self.setting_ai_setting_save_bnt.setObjectName(u"setting_ai_setting_save_bnt")
        sizePolicy.setHeightForWidth(self.setting_ai_setting_save_bnt.sizePolicy().hasHeightForWidth())
        self.setting_ai_setting_save_bnt.setSizePolicy(sizePolicy)
        self.setting_ai_setting_save_bnt.setMinimumSize(QSize(71, 41))
        self.setting_ai_setting_save_bnt.setMaximumSize(QSize(71, 41))
        self.setting_ai_setting_save_bnt.setFont(font1)
        self.setting_ai_setting_save_bnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.setting_ai_setting_save_bnt.setStyleSheet(u"background-color: qlineargradient(\n"
"    spread:pad,\n"
"    x1:0, y1:0, x2:0, y2:1,\n"
"    stop:0.0 rgba(112, 210, 112, 255),\n"
"    stop:0.3 rgba(0, 196, 0, 255)\n"
");\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 19px;\n"
"\n"
"")

        self.horizontalLayout_84.addWidget(self.setting_ai_setting_save_bnt)

        self.horizontalSpacer_124 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_84.addItem(self.horizontalSpacer_124)


        self.verticalLayout_52.addLayout(self.horizontalLayout_84)

        self.setting_partion_5 = QFrame(self.setting_self_labeling_widget)
        self.setting_partion_5.setObjectName(u"setting_partion_5")
        sizePolicy1.setHeightForWidth(self.setting_partion_5.sizePolicy().hasHeightForWidth())
        self.setting_partion_5.setSizePolicy(sizePolicy1)
        self.setting_partion_5.setMinimumSize(QSize(246, 3))
        self.setting_partion_5.setMaximumSize(QSize(434, 3))
        self.setting_partion_5.setFont(font14)
        self.setting_partion_5.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.setting_partion_5.setAutoFillBackground(False)
        self.setting_partion_5.setStyleSheet(u"background-color: rgb(36, 39, 44)")
        self.setting_partion_5.setFrameShape(QFrame.Shape.HLine)
        self.setting_partion_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_52.addWidget(self.setting_partion_5)

        self.setting_notion_widget = QWidget(self.setting_self_labeling_widget)
        self.setting_notion_widget.setObjectName(u"setting_notion_widget")
        self.verticalLayout_17 = QVBoxLayout(self.setting_notion_widget)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalSpacer_61 = QSpacerItem(13, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_61)

        self.setting_notice_label_3 = QLabel(self.setting_notion_widget)
        self.setting_notice_label_3.setObjectName(u"setting_notice_label_3")
        sizePolicy1.setHeightForWidth(self.setting_notice_label_3.sizePolicy().hasHeightForWidth())
        self.setting_notice_label_3.setSizePolicy(sizePolicy1)
        self.setting_notice_label_3.setMinimumSize(QSize(153, 31))
        self.setting_notice_label_3.setFont(font10)
        self.setting_notice_label_3.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.setting_notice_label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_15.addWidget(self.setting_notice_label_3)

        self.horizontalSpacer_150 = QSpacerItem(142, 13, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_150)

        self.setting_notice_phone_active_bnt = QPushButton(self.setting_notion_widget)
        self.setting_notice_phone_active_bnt.setObjectName(u"setting_notice_phone_active_bnt")
        self.setting_notice_phone_active_bnt.setMinimumSize(QSize(61, 25))
        self.setting_notice_phone_active_bnt.setMaximumSize(QSize(61, 25))
        self.setting_notice_phone_active_bnt.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    padding: 0px; /* \ud328\ub529\ub3c4 0\uc73c\ub85c \uc124\uc815 */\n"
"    outline: none;\n"
"}\n"
"\n"
"/* hover, pressed \uc0c1\ud0dc\uc5d0\ub3c4 \uc544\ubb34 \ud6a8\uacfc \uc5c6\uc74c */\n"
"QPushButton:hover {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.setting_notice_phone_active_bnt.setIcon(icon4)
        self.setting_notice_phone_active_bnt.setIconSize(QSize(55, 103))
        self.setting_notice_phone_active_bnt.setCheckable(True)

        self.horizontalLayout_15.addWidget(self.setting_notice_phone_active_bnt)

        self.horizontalSpacer_62 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_62)


        self.verticalLayout_17.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalSpacer_145 = QSpacerItem(26, 13, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_145)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.setting_notice_phone_num_input = QLineEdit(self.setting_notion_widget)
        self.setting_notice_phone_num_input.setObjectName(u"setting_notice_phone_num_input")
        self.setting_notice_phone_num_input.setMaximumSize(QSize(121, 41))
        self.setting_notice_phone_num_input.setFont(font1)
        self.setting_notice_phone_num_input.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.setting_notice_phone_num_input.setStyleSheet(u"qproperty-frame: false;\n"
"font-size:10pt;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")

        self.horizontalLayout_19.addWidget(self.setting_notice_phone_num_input)

        self.setting_notice_phone_add_bnt = QPushButton(self.setting_notion_widget)
        self.setting_notice_phone_add_bnt.setObjectName(u"setting_notice_phone_add_bnt")
        sizePolicy1.setHeightForWidth(self.setting_notice_phone_add_bnt.sizePolicy().hasHeightForWidth())
        self.setting_notice_phone_add_bnt.setSizePolicy(sizePolicy1)
        self.setting_notice_phone_add_bnt.setMinimumSize(QSize(31, 31))
        self.setting_notice_phone_add_bnt.setFont(font1)
        self.setting_notice_phone_add_bnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.setting_notice_phone_add_bnt.setStyleSheet(u"background-color: rgb(3, 3, 13);\n"
"border: 1px solid rgb(3, 3, 13);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        self.setting_notice_phone_add_bnt.setIcon(icon3)
        self.setting_notice_phone_add_bnt.setIconSize(QSize(31, 50))

        self.horizontalLayout_19.addWidget(self.setting_notice_phone_add_bnt)

        self.setting_notice_phone_del_bnt = QPushButton(self.setting_notion_widget)
        self.setting_notice_phone_del_bnt.setObjectName(u"setting_notice_phone_del_bnt")
        sizePolicy1.setHeightForWidth(self.setting_notice_phone_del_bnt.sizePolicy().hasHeightForWidth())
        self.setting_notice_phone_del_bnt.setSizePolicy(sizePolicy1)
        self.setting_notice_phone_del_bnt.setMinimumSize(QSize(31, 31))
        self.setting_notice_phone_del_bnt.setFont(font1)
        self.setting_notice_phone_del_bnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.setting_notice_phone_del_bnt.setStyleSheet(u"background-color: rgb(3, 3, 13);\n"
"border: 1px solid rgb(3, 3, 13);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        icon5 = QIcon()
        icon5.addFile(u":/ui/ui/images/ico_delete.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.setting_notice_phone_del_bnt.setIcon(icon5)
        self.setting_notice_phone_del_bnt.setIconSize(QSize(31, 50))

        self.horizontalLayout_19.addWidget(self.setting_notice_phone_del_bnt)

        self.horizontalSpacer_146 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_146)


        self.verticalLayout_18.addLayout(self.horizontalLayout_19)


        self.horizontalLayout_17.addLayout(self.verticalLayout_18)


        self.verticalLayout_17.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setSpacing(1)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalSpacer_147 = QSpacerItem(13, 13, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_147)

        self.setting_notice_phone_list = QTableWidget(self.setting_notion_widget)
        if (self.setting_notice_phone_list.columnCount() < 1):
            self.setting_notice_phone_list.setColumnCount(1)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.setting_notice_phone_list.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        self.setting_notice_phone_list.setObjectName(u"setting_notice_phone_list")
        sizePolicy3.setHeightForWidth(self.setting_notice_phone_list.sizePolicy().hasHeightForWidth())
        self.setting_notice_phone_list.setSizePolicy(sizePolicy3)
        self.setting_notice_phone_list.setMinimumSize(QSize(203, 273))
        self.setting_notice_phone_list.setMaximumSize(QSize(203, 9999))
        self.setting_notice_phone_list.setFont(font)
        self.setting_notice_phone_list.setStyleSheet(u"QTableWidget {\n"
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
        self.setting_notice_phone_list.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.setting_notice_phone_list.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.setting_notice_phone_list.setDragDropOverwriteMode(False)
        self.setting_notice_phone_list.setAlternatingRowColors(False)
        self.setting_notice_phone_list.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.setting_notice_phone_list.setShowGrid(False)
        self.setting_notice_phone_list.setGridStyle(Qt.PenStyle.NoPen)
        self.setting_notice_phone_list.setWordWrap(False)
        self.setting_notice_phone_list.setCornerButtonEnabled(False)
        self.setting_notice_phone_list.horizontalHeader().setHighlightSections(False)
        self.setting_notice_phone_list.horizontalHeader().setStretchLastSection(True)
        self.setting_notice_phone_list.verticalHeader().setVisible(False)
        self.setting_notice_phone_list.verticalHeader().setHighlightSections(False)

        self.horizontalLayout_20.addWidget(self.setting_notice_phone_list)

        self.widget_7 = QWidget(self.setting_notion_widget)
        self.widget_7.setObjectName(u"widget_7")
        self.verticalLayout_19 = QVBoxLayout(self.widget_7)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.setting_notice_label_4 = QLabel(self.widget_7)
        self.setting_notice_label_4.setObjectName(u"setting_notice_label_4")
        sizePolicy4.setHeightForWidth(self.setting_notice_label_4.sizePolicy().hasHeightForWidth())
        self.setting_notice_label_4.setSizePolicy(sizePolicy4)
        self.setting_notice_label_4.setMinimumSize(QSize(104, 27))
        self.setting_notice_label_4.setMaximumSize(QSize(104, 27))
        self.setting_notice_label_4.setFont(font11)
        self.setting_notice_label_4.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.setting_notice_label_4.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_19.addWidget(self.setting_notice_label_4)

        self.setting_notion_detect_type_widget = QWidget(self.widget_7)
        self.setting_notion_detect_type_widget.setObjectName(u"setting_notion_detect_type_widget")
        self.gridLayout = QGridLayout(self.setting_notion_detect_type_widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.setting_notion_detect_type_bnt1 = QPushButton(self.setting_notion_detect_type_widget)
        self.setting_notion_detect_type_bnt1.setObjectName(u"setting_notion_detect_type_bnt1")
        self.setting_notion_detect_type_bnt1.setStyleSheet(u"color: rgb(179,179,179);\n"
"")
        icon6 = QIcon()
        icon6.addFile(u":/ui/ui/images/check_off.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon6.addFile(u":/ui/ui/images/check.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.setting_notion_detect_type_bnt1.setIcon(icon6)
        self.setting_notion_detect_type_bnt1.setCheckable(True)

        self.gridLayout.addWidget(self.setting_notion_detect_type_bnt1, 0, 0, 1, 1)

        self.setting_notion_detect_type_bnt2 = QPushButton(self.setting_notion_detect_type_widget)
        self.setting_notion_detect_type_bnt2.setObjectName(u"setting_notion_detect_type_bnt2")
        self.setting_notion_detect_type_bnt2.setStyleSheet(u"color: rgb(179,179,179);\n"
"")
        self.setting_notion_detect_type_bnt2.setIcon(icon6)
        self.setting_notion_detect_type_bnt2.setCheckable(True)

        self.gridLayout.addWidget(self.setting_notion_detect_type_bnt2, 0, 1, 1, 1)

        self.setting_notion_detect_type_bnt3 = QPushButton(self.setting_notion_detect_type_widget)
        self.setting_notion_detect_type_bnt3.setObjectName(u"setting_notion_detect_type_bnt3")
        self.setting_notion_detect_type_bnt3.setStyleSheet(u"color: rgb(179,179,179);\n"
"")
        self.setting_notion_detect_type_bnt3.setIcon(icon6)
        self.setting_notion_detect_type_bnt3.setCheckable(True)

        self.gridLayout.addWidget(self.setting_notion_detect_type_bnt3, 1, 0, 1, 1)

        self.setting_notion_detect_type_bnt4 = QPushButton(self.setting_notion_detect_type_widget)
        self.setting_notion_detect_type_bnt4.setObjectName(u"setting_notion_detect_type_bnt4")
        self.setting_notion_detect_type_bnt4.setStyleSheet(u"color: rgb(179,179,179);\n"
"")
        self.setting_notion_detect_type_bnt4.setIcon(icon6)
        self.setting_notion_detect_type_bnt4.setCheckable(True)

        self.gridLayout.addWidget(self.setting_notion_detect_type_bnt4, 1, 1, 1, 1)


        self.verticalLayout_19.addWidget(self.setting_notion_detect_type_widget)

        self.verticalSpacer = QSpacerItem(20, 162, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer)


        self.horizontalLayout_20.addWidget(self.widget_7)

        self.horizontalSpacer_151 = QSpacerItem(40, 13, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_151)


        self.verticalLayout_17.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_97 = QHBoxLayout()
        self.horizontalLayout_97.setObjectName(u"horizontalLayout_97")
        self.horizontalSpacer_148 = QSpacerItem(324, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_97.addItem(self.horizontalSpacer_148)

        self.setting_notice_phone_save_bnt = QPushButton(self.setting_notion_widget)
        self.setting_notice_phone_save_bnt.setObjectName(u"setting_notice_phone_save_bnt")
        sizePolicy.setHeightForWidth(self.setting_notice_phone_save_bnt.sizePolicy().hasHeightForWidth())
        self.setting_notice_phone_save_bnt.setSizePolicy(sizePolicy)
        self.setting_notice_phone_save_bnt.setMinimumSize(QSize(76, 41))
        self.setting_notice_phone_save_bnt.setMaximumSize(QSize(71, 41))
        self.setting_notice_phone_save_bnt.setFont(font1)
        self.setting_notice_phone_save_bnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.setting_notice_phone_save_bnt.setStyleSheet(u"background-color: qlineargradient(\n"
"    spread:pad,\n"
"    x1:0, y1:0, x2:0, y2:1,\n"
"    stop:0.0 rgba(112, 210, 112, 255),\n"
"    stop:0.3 rgba(0, 196, 0, 255)\n"
");\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 19px;\n"
"\n"
"")

        self.horizontalLayout_97.addWidget(self.setting_notice_phone_save_bnt)

        self.horizontalSpacer_149 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_97.addItem(self.horizontalSpacer_149)


        self.verticalLayout_17.addLayout(self.horizontalLayout_97)


        self.verticalLayout_52.addWidget(self.setting_notion_widget)


        self.verticalLayout_34.addWidget(self.setting_self_labeling_widget)

        self.setting_partion_8 = QFrame(self.scrollAreaWidgetContents_2)
        self.setting_partion_8.setObjectName(u"setting_partion_8")
        sizePolicy1.setHeightForWidth(self.setting_partion_8.sizePolicy().hasHeightForWidth())
        self.setting_partion_8.setSizePolicy(sizePolicy1)
        self.setting_partion_8.setMinimumSize(QSize(246, 3))
        self.setting_partion_8.setMaximumSize(QSize(434, 3))
        self.setting_partion_8.setFont(font14)
        self.setting_partion_8.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.setting_partion_8.setAutoFillBackground(False)
        self.setting_partion_8.setStyleSheet(u"background-color: rgb(36, 39, 44)")
        self.setting_partion_8.setFrameShape(QFrame.Shape.HLine)
        self.setting_partion_8.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_34.addWidget(self.setting_partion_8)

        self.widget_15 = QWidget(self.scrollAreaWidgetContents_2)
        self.widget_15.setObjectName(u"widget_15")
        self.verticalLayout_54 = QVBoxLayout(self.widget_15)
        self.verticalLayout_54.setSpacing(7)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.horizontalLayout_85 = QHBoxLayout()
        self.horizontalLayout_85.setObjectName(u"horizontalLayout_85")
        self.horizontalSpacer_53 = QSpacerItem(13, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_85.addItem(self.horizontalSpacer_53)

        self.setting_label_5 = QLabel(self.widget_15)
        self.setting_label_5.setObjectName(u"setting_label_5")
        sizePolicy4.setHeightForWidth(self.setting_label_5.sizePolicy().hasHeightForWidth())
        self.setting_label_5.setSizePolicy(sizePolicy4)
        self.setting_label_5.setMinimumSize(QSize(135, 22))
        self.setting_label_5.setMaximumSize(QSize(179, 22))
        self.setting_label_5.setFont(font13)
        self.setting_label_5.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.setting_label_5.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_85.addWidget(self.setting_label_5)

        self.horizontalSpacer_54 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_85.addItem(self.horizontalSpacer_54)


        self.verticalLayout_54.addLayout(self.horizontalLayout_85)

        self.horizontalLayout_86 = QHBoxLayout()
        self.horizontalLayout_86.setSpacing(6)
        self.horizontalLayout_86.setObjectName(u"horizontalLayout_86")
        self.horizontalSpacer_55 = QSpacerItem(36, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_86.addItem(self.horizontalSpacer_55)

        self.horizontalLayout_87 = QHBoxLayout()
        self.horizontalLayout_87.setSpacing(5)
        self.horizontalLayout_87.setObjectName(u"horizontalLayout_87")
        self.setting_user_id_label = QLabel(self.widget_15)
        self.setting_user_id_label.setObjectName(u"setting_user_id_label")
        sizePolicy4.setHeightForWidth(self.setting_user_id_label.sizePolicy().hasHeightForWidth())
        self.setting_user_id_label.setSizePolicy(sizePolicy4)
        self.setting_user_id_label.setMinimumSize(QSize(104, 22))
        self.setting_user_id_label.setMaximumSize(QSize(104, 22))
        self.setting_user_id_label.setFont(font11)
        self.setting_user_id_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.setting_user_id_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_87.addWidget(self.setting_user_id_label)

        self.verticalLayout_56 = QVBoxLayout()
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.setting_user_id_input = QLineEdit(self.widget_15)
        self.setting_user_id_input.setObjectName(u"setting_user_id_input")
        sizePolicy1.setHeightForWidth(self.setting_user_id_input.sizePolicy().hasHeightForWidth())
        self.setting_user_id_input.setSizePolicy(sizePolicy1)
        self.setting_user_id_input.setMinimumSize(QSize(246, 19))
        self.setting_user_id_input.setMaximumSize(QSize(9999, 19))
        self.setting_user_id_input.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.setting_user_id_input.setReadOnly(True)

        self.verticalLayout_56.addWidget(self.setting_user_id_input)

        self.setting_user_id_input_line = QFrame(self.widget_15)
        self.setting_user_id_input_line.setObjectName(u"setting_user_id_input_line")
        sizePolicy1.setHeightForWidth(self.setting_user_id_input_line.sizePolicy().hasHeightForWidth())
        self.setting_user_id_input_line.setSizePolicy(sizePolicy1)
        self.setting_user_id_input_line.setMinimumSize(QSize(246, 3))
        self.setting_user_id_input_line.setMaximumSize(QSize(246, 3))
        self.setting_user_id_input_line.setFont(font14)
        self.setting_user_id_input_line.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.setting_user_id_input_line.setAutoFillBackground(False)
        self.setting_user_id_input_line.setStyleSheet(u"background-color: rgb(36, 39, 44)")
        self.setting_user_id_input_line.setFrameShape(QFrame.Shape.HLine)
        self.setting_user_id_input_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_56.addWidget(self.setting_user_id_input_line)


        self.horizontalLayout_87.addLayout(self.verticalLayout_56)


        self.horizontalLayout_86.addLayout(self.horizontalLayout_87)

        self.horizontalSpacer_125 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_86.addItem(self.horizontalSpacer_125)


        self.verticalLayout_54.addLayout(self.horizontalLayout_86)

        self.horizontalLayout_88 = QHBoxLayout()
        self.horizontalLayout_88.setObjectName(u"horizontalLayout_88")
        self.horizontalSpacer_126 = QSpacerItem(36, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_88.addItem(self.horizontalSpacer_126)

        self.horizontalLayout_89 = QHBoxLayout()
        self.horizontalLayout_89.setObjectName(u"horizontalLayout_89")
        self.setting_user_pw_label = QLabel(self.widget_15)
        self.setting_user_pw_label.setObjectName(u"setting_user_pw_label")
        sizePolicy4.setHeightForWidth(self.setting_user_pw_label.sizePolicy().hasHeightForWidth())
        self.setting_user_pw_label.setSizePolicy(sizePolicy4)
        self.setting_user_pw_label.setMinimumSize(QSize(104, 22))
        self.setting_user_pw_label.setMaximumSize(QSize(104, 22))
        self.setting_user_pw_label.setFont(font11)
        self.setting_user_pw_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.setting_user_pw_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_89.addWidget(self.setting_user_pw_label)

        self.verticalLayout_57 = QVBoxLayout()
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.setting_user_pw_input = QLineEdit(self.widget_15)
        self.setting_user_pw_input.setObjectName(u"setting_user_pw_input")
        sizePolicy1.setHeightForWidth(self.setting_user_pw_input.sizePolicy().hasHeightForWidth())
        self.setting_user_pw_input.setSizePolicy(sizePolicy1)
        self.setting_user_pw_input.setMinimumSize(QSize(246, 19))
        self.setting_user_pw_input.setMaximumSize(QSize(9999, 19))
        self.setting_user_pw_input.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.setting_user_pw_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout_57.addWidget(self.setting_user_pw_input)

        self.setting_user_pw_input_line = QFrame(self.widget_15)
        self.setting_user_pw_input_line.setObjectName(u"setting_user_pw_input_line")
        sizePolicy1.setHeightForWidth(self.setting_user_pw_input_line.sizePolicy().hasHeightForWidth())
        self.setting_user_pw_input_line.setSizePolicy(sizePolicy1)
        self.setting_user_pw_input_line.setMinimumSize(QSize(246, 3))
        self.setting_user_pw_input_line.setMaximumSize(QSize(246, 3))
        self.setting_user_pw_input_line.setFont(font14)
        self.setting_user_pw_input_line.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.setting_user_pw_input_line.setAutoFillBackground(False)
        self.setting_user_pw_input_line.setStyleSheet(u"background-color: rgb(36, 39, 44)")
        self.setting_user_pw_input_line.setFrameShape(QFrame.Shape.HLine)
        self.setting_user_pw_input_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_57.addWidget(self.setting_user_pw_input_line)


        self.horizontalLayout_89.addLayout(self.verticalLayout_57)


        self.horizontalLayout_88.addLayout(self.horizontalLayout_89)

        self.horizontalSpacer_127 = QSpacerItem(40, 13, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_88.addItem(self.horizontalSpacer_127)


        self.verticalLayout_54.addLayout(self.horizontalLayout_88)

        self.horizontalLayout_90 = QHBoxLayout()
        self.horizontalLayout_90.setObjectName(u"horizontalLayout_90")
        self.horizontalSpacer_128 = QSpacerItem(36, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_90.addItem(self.horizontalSpacer_128)

        self.horizontalLayout_91 = QHBoxLayout()
        self.horizontalLayout_91.setObjectName(u"horizontalLayout_91")
        self.setting_user_new_pw_label = QLabel(self.widget_15)
        self.setting_user_new_pw_label.setObjectName(u"setting_user_new_pw_label")
        sizePolicy4.setHeightForWidth(self.setting_user_new_pw_label.sizePolicy().hasHeightForWidth())
        self.setting_user_new_pw_label.setSizePolicy(sizePolicy4)
        self.setting_user_new_pw_label.setMinimumSize(QSize(104, 22))
        self.setting_user_new_pw_label.setMaximumSize(QSize(104, 22))
        self.setting_user_new_pw_label.setFont(font11)
        self.setting_user_new_pw_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.setting_user_new_pw_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_91.addWidget(self.setting_user_new_pw_label)

        self.verticalLayout_58 = QVBoxLayout()
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.setting_user_new_pw_input = QLineEdit(self.widget_15)
        self.setting_user_new_pw_input.setObjectName(u"setting_user_new_pw_input")
        sizePolicy1.setHeightForWidth(self.setting_user_new_pw_input.sizePolicy().hasHeightForWidth())
        self.setting_user_new_pw_input.setSizePolicy(sizePolicy1)
        self.setting_user_new_pw_input.setMinimumSize(QSize(246, 19))
        self.setting_user_new_pw_input.setMaximumSize(QSize(9999, 19))
        self.setting_user_new_pw_input.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.setting_user_new_pw_input.setFrame(True)
        self.setting_user_new_pw_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout_58.addWidget(self.setting_user_new_pw_input)

        self.setting_user_new_pw_input_line = QFrame(self.widget_15)
        self.setting_user_new_pw_input_line.setObjectName(u"setting_user_new_pw_input_line")
        sizePolicy1.setHeightForWidth(self.setting_user_new_pw_input_line.sizePolicy().hasHeightForWidth())
        self.setting_user_new_pw_input_line.setSizePolicy(sizePolicy1)
        self.setting_user_new_pw_input_line.setMinimumSize(QSize(246, 3))
        self.setting_user_new_pw_input_line.setMaximumSize(QSize(246, 3))
        self.setting_user_new_pw_input_line.setFont(font14)
        self.setting_user_new_pw_input_line.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.setting_user_new_pw_input_line.setAutoFillBackground(False)
        self.setting_user_new_pw_input_line.setStyleSheet(u"background-color: rgb(36, 39, 44)")
        self.setting_user_new_pw_input_line.setFrameShape(QFrame.Shape.HLine)
        self.setting_user_new_pw_input_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_58.addWidget(self.setting_user_new_pw_input_line)


        self.horizontalLayout_91.addLayout(self.verticalLayout_58)


        self.horizontalLayout_90.addLayout(self.horizontalLayout_91)

        self.horizontalSpacer_129 = QSpacerItem(40, 13, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_90.addItem(self.horizontalSpacer_129)


        self.verticalLayout_54.addLayout(self.horizontalLayout_90)

        self.horizontalLayout_92 = QHBoxLayout()
        self.horizontalLayout_92.setObjectName(u"horizontalLayout_92")
        self.horizontalSpacer_130 = QSpacerItem(36, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_92.addItem(self.horizontalSpacer_130)

        self.horizontalLayout_93 = QHBoxLayout()
        self.horizontalLayout_93.setObjectName(u"horizontalLayout_93")
        self.setting_user_new_pw_label2 = QLabel(self.widget_15)
        self.setting_user_new_pw_label2.setObjectName(u"setting_user_new_pw_label2")
        sizePolicy4.setHeightForWidth(self.setting_user_new_pw_label2.sizePolicy().hasHeightForWidth())
        self.setting_user_new_pw_label2.setSizePolicy(sizePolicy4)
        self.setting_user_new_pw_label2.setMinimumSize(QSize(104, 27))
        self.setting_user_new_pw_label2.setMaximumSize(QSize(104, 27))
        self.setting_user_new_pw_label2.setFont(font11)
        self.setting_user_new_pw_label2.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.setting_user_new_pw_label2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_93.addWidget(self.setting_user_new_pw_label2)

        self.verticalLayout_59 = QVBoxLayout()
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.setting_user_new_pw_input2 = QLineEdit(self.widget_15)
        self.setting_user_new_pw_input2.setObjectName(u"setting_user_new_pw_input2")
        sizePolicy1.setHeightForWidth(self.setting_user_new_pw_input2.sizePolicy().hasHeightForWidth())
        self.setting_user_new_pw_input2.setSizePolicy(sizePolicy1)
        self.setting_user_new_pw_input2.setMinimumSize(QSize(246, 19))
        self.setting_user_new_pw_input2.setMaximumSize(QSize(9999, 19))
        self.setting_user_new_pw_input2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.setting_user_new_pw_input2.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout_59.addWidget(self.setting_user_new_pw_input2)

        self.setting_user_new_pw_input2_line = QFrame(self.widget_15)
        self.setting_user_new_pw_input2_line.setObjectName(u"setting_user_new_pw_input2_line")
        sizePolicy1.setHeightForWidth(self.setting_user_new_pw_input2_line.sizePolicy().hasHeightForWidth())
        self.setting_user_new_pw_input2_line.setSizePolicy(sizePolicy1)
        self.setting_user_new_pw_input2_line.setMinimumSize(QSize(246, 3))
        self.setting_user_new_pw_input2_line.setMaximumSize(QSize(246, 3))
        self.setting_user_new_pw_input2_line.setFont(font14)
        self.setting_user_new_pw_input2_line.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.setting_user_new_pw_input2_line.setAutoFillBackground(False)
        self.setting_user_new_pw_input2_line.setStyleSheet(u"background-color: rgb(36, 39, 44)")
        self.setting_user_new_pw_input2_line.setFrameShape(QFrame.Shape.HLine)
        self.setting_user_new_pw_input2_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_59.addWidget(self.setting_user_new_pw_input2_line)


        self.horizontalLayout_93.addLayout(self.verticalLayout_59)


        self.horizontalLayout_92.addLayout(self.horizontalLayout_93)

        self.horizontalSpacer_131 = QSpacerItem(40, 13, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_92.addItem(self.horizontalSpacer_131)


        self.verticalLayout_54.addLayout(self.horizontalLayout_92)

        self.horizontalLayout_94 = QHBoxLayout()
        self.horizontalLayout_94.setObjectName(u"horizontalLayout_94")
        self.horizontalSpacer_57 = QSpacerItem(338, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_94.addItem(self.horizontalSpacer_57)

        self.setting_user_save_bnt = QPushButton(self.widget_15)
        self.setting_user_save_bnt.setObjectName(u"setting_user_save_bnt")
        self.setting_user_save_bnt.setMinimumSize(QSize(71, 41))
        self.setting_user_save_bnt.setMaximumSize(QSize(71, 41))
        self.setting_user_save_bnt.setFont(font1)
        self.setting_user_save_bnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.setting_user_save_bnt.setStyleSheet(u"background-color: qlineargradient(\n"
"    spread:pad,\n"
"    x1:0, y1:0, x2:0, y2:1,\n"
"    stop:0.0 rgba(112, 210, 112, 255),\n"
"    stop:0.3 rgba(0, 196, 0, 255)\n"
");\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 19px;\n"
"\n"
"")

        self.horizontalLayout_94.addWidget(self.setting_user_save_bnt)

        self.horizontalSpacer_132 = QSpacerItem(40, 13, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_94.addItem(self.horizontalSpacer_132)


        self.verticalLayout_54.addLayout(self.horizontalLayout_94)


        self.verticalLayout_34.addWidget(self.widget_15)


        self.verticalLayout_7.addLayout(self.verticalLayout_34)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_3)


        self.horizontalLayout_6.addLayout(self.verticalLayout_7)

        self.horizontalSpacer_3 = QSpacerItem(13, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)


        self.verticalLayout_6.addLayout(self.horizontalLayout_6)

        self.setting_scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_53.addWidget(self.setting_scrollArea)

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
        self.admin_pw_label.setFont(font15)
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
        self.admin_pw_input_line.setFont(font14)
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
        self.admin_page_bnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.admin_page_bnt.setStyleSheet(u"background-color: qlineargradient(\n"
"    spread:pad,\n"
"    x1:0, y1:0, x2:0, y2:1,\n"
"    stop:0.0 rgba(112, 210, 112, 255),\n"
"    stop:0.3 rgba(0, 196, 0, 255)\n"
");\n"
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
        self.admin_license_bnt.setFont(font11)
        self.admin_license_bnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
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
        self.admin_fn_permission_bnt.setFont(font11)
        self.admin_fn_permission_bnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
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
        self.horizontalLayout_95 = QHBoxLayout()
        self.horizontalLayout_95.setObjectName(u"horizontalLayout_95")
        self.horizontalSpacer_133 = QSpacerItem(36, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_95.addItem(self.horizontalSpacer_133)

        self.horizontalLayout_96 = QHBoxLayout()
        self.horizontalLayout_96.setObjectName(u"horizontalLayout_96")
        self.license_camera_allow_num_label = QLabel(self.license_page)
        self.license_camera_allow_num_label.setObjectName(u"license_camera_allow_num_label")
        sizePolicy4.setHeightForWidth(self.license_camera_allow_num_label.sizePolicy().hasHeightForWidth())
        self.license_camera_allow_num_label.setSizePolicy(sizePolicy4)
        self.license_camera_allow_num_label.setMinimumSize(QSize(166, 27))
        self.license_camera_allow_num_label.setMaximumSize(QSize(166, 27))
        self.license_camera_allow_num_label.setFont(font11)
        self.license_camera_allow_num_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.license_camera_allow_num_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_96.addWidget(self.license_camera_allow_num_label)

        self.verticalLayout_60 = QVBoxLayout()
        self.verticalLayout_60.setSpacing(1)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.license_camera_allow_num_input = QLineEdit(self.license_page)
        self.license_camera_allow_num_input.setObjectName(u"license_camera_allow_num_input")
        sizePolicy1.setHeightForWidth(self.license_camera_allow_num_input.sizePolicy().hasHeightForWidth())
        self.license_camera_allow_num_input.setSizePolicy(sizePolicy1)
        self.license_camera_allow_num_input.setMinimumSize(QSize(94, 19))
        self.license_camera_allow_num_input.setMaximumSize(QSize(94, 19))
        self.license_camera_allow_num_input.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.license_camera_allow_num_input.setEchoMode(QLineEdit.EchoMode.Normal)
        self.license_camera_allow_num_input.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_60.addWidget(self.license_camera_allow_num_input)

        self.license_camera_allow_num_input_line = QFrame(self.license_page)
        self.license_camera_allow_num_input_line.setObjectName(u"license_camera_allow_num_input_line")
        sizePolicy1.setHeightForWidth(self.license_camera_allow_num_input_line.sizePolicy().hasHeightForWidth())
        self.license_camera_allow_num_input_line.setSizePolicy(sizePolicy1)
        self.license_camera_allow_num_input_line.setMinimumSize(QSize(94, 3))
        self.license_camera_allow_num_input_line.setMaximumSize(QSize(94, 3))
        self.license_camera_allow_num_input_line.setFont(font14)
        self.license_camera_allow_num_input_line.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.license_camera_allow_num_input_line.setAutoFillBackground(False)
        self.license_camera_allow_num_input_line.setStyleSheet(u"background-color: rgb(36, 39, 44)")
        self.license_camera_allow_num_input_line.setFrameShape(QFrame.Shape.HLine)
        self.license_camera_allow_num_input_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_60.addWidget(self.license_camera_allow_num_input_line)


        self.horizontalLayout_96.addLayout(self.verticalLayout_60)


        self.horizontalLayout_95.addLayout(self.horizontalLayout_96)

        self.horizontalSpacer_134 = QSpacerItem(40, 13, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_95.addItem(self.horizontalSpacer_134)


        self.verticalLayout_46.addLayout(self.horizontalLayout_95)

        self.horizontalLayout_46 = QHBoxLayout()
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalSpacer_42 = QSpacerItem(130, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

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
        font16 = QFont()
        font16.setFamilies([u"Ubuntu Light"])
        font16.setPointSize(11)
        font16.setBold(True)
        self.non_active_license_label.setFont(font16)
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
        font17 = QFont()
        font17.setPointSize(11)
        font17.setBold(False)
        font17.setItalic(False)
        font17.setUnderline(False)
        font17.setStrikeOut(False)
        font17.setKerning(True)
        self.non_active_license_list.setFont(font17)
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
        self.non_active_license_list.setProperty(u"showDropIndicator", True)
        self.non_active_license_list.setDragEnabled(True)
        self.non_active_license_list.setDragDropMode(QAbstractItemView.DragDropMode.NoDragDrop)
        self.non_active_license_list.setDefaultDropAction(Qt.DropAction.IgnoreAction)
        self.non_active_license_list.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.non_active_license_list.setTextElideMode(Qt.TextElideMode.ElideLeft)
        self.non_active_license_list.setVerticalScrollMode(QAbstractItemView.ScrollMode.ScrollPerItem)
        self.non_active_license_list.setMovement(QListView.Movement.Static)
        self.non_active_license_list.setFlow(QListView.Flow.TopToBottom)
        self.non_active_license_list.setProperty(u"isWrapping", False)
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
        font18 = QFont()
        font18.setPointSize(10)
        self.license_add_bnt.setFont(font18)
        self.license_add_bnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.license_add_bnt.setStyleSheet(u"background-color: rgb(3, 3, 13);\n"
"border: 1px solid rgb(3, 3, 13);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"")
        icon7 = QIcon()
        icon7.addFile(u":/ui/ui/images/ico_arrow_right.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.license_add_bnt.setIcon(icon7)
        self.license_add_bnt.setIconSize(QSize(31, 50))

        self.verticalLayout_41.addWidget(self.license_add_bnt)

        self.license_remove_bnt = QPushButton(self.license_page)
        self.license_remove_bnt.setObjectName(u"license_remove_bnt")
        self.license_remove_bnt.setMinimumSize(QSize(41, 41))
        self.license_remove_bnt.setMaximumSize(QSize(41, 41))
        self.license_remove_bnt.setFont(font18)
        self.license_remove_bnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.license_remove_bnt.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.license_remove_bnt.setStyleSheet(u"background-color: rgb(3, 3, 13);\n"
"border: 1px solid rgb(3, 3, 13);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"Rotation: ( origin.x: 25; origin.y: 25; angle: 45);")
        icon8 = QIcon()
        icon8.addFile(u":/ui/ui/images/ico_arrow_left.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.license_remove_bnt.setIcon(icon8)
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
        self.active_license_label.setFont(font16)
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
        self.active_license_list.setFont(font17)
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
        self.active_license_list.setProperty(u"showDropIndicator", False)
        self.active_license_list.setDragEnabled(True)
        self.active_license_list.setDragDropMode(QAbstractItemView.DragDropMode.NoDragDrop)
        self.active_license_list.setDefaultDropAction(Qt.DropAction.IgnoreAction)
        self.active_license_list.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.active_license_list.setTextElideMode(Qt.TextElideMode.ElideLeft)
        self.active_license_list.setVerticalScrollMode(QAbstractItemView.ScrollMode.ScrollPerItem)
        self.active_license_list.setMovement(QListView.Movement.Static)
        self.active_license_list.setFlow(QListView.Flow.TopToBottom)
        self.active_license_list.setProperty(u"isWrapping", False)
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
        self.license_save_bnt.setFont(font18)
        self.license_save_bnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.license_save_bnt.setStyleSheet(u"background-color: qlineargradient(\n"
"    spread:pad,\n"
"    x1:0, y1:0, x2:0, y2:1,\n"
"    stop:0.0 rgba(112, 210, 112, 255),\n"
"    stop:0.3 rgba(0, 196, 0, 255)\n"
");\n"
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
        self.verticalLayout_45 = QVBoxLayout(self.fn_permission_page)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_44 = QVBoxLayout()
        self.verticalLayout_44.setSpacing(9)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalSpacer_20 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_44.addItem(self.verticalSpacer_20)

        self.horizontalLayout_45 = QHBoxLayout()
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalSpacer_40 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_45.addItem(self.horizontalSpacer_40)

        self.horizontalLayout_44 = QHBoxLayout()
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.admin_sms_alarm_fn_active_label = QLabel(self.fn_permission_page)
        self.admin_sms_alarm_fn_active_label.setObjectName(u"admin_sms_alarm_fn_active_label")
        self.admin_sms_alarm_fn_active_label.setMinimumSize(QSize(160, 25))
        self.admin_sms_alarm_fn_active_label.setMaximumSize(QSize(200, 25))
        self.admin_sms_alarm_fn_active_label.setFont(font11)
        self.admin_sms_alarm_fn_active_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.admin_sms_alarm_fn_active_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_44.addWidget(self.admin_sms_alarm_fn_active_label)

        self.admin_sms_alarm_fn_active_bnt = QPushButton(self.fn_permission_page)
        self.admin_sms_alarm_fn_active_bnt.setObjectName(u"admin_sms_alarm_fn_active_bnt")
        self.admin_sms_alarm_fn_active_bnt.setMinimumSize(QSize(61, 25))
        self.admin_sms_alarm_fn_active_bnt.setMaximumSize(QSize(61, 25))
        icon9 = QIcon()
        icon9.addFile(u":/ui/ui/images/icon-switch-off.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon9.addFile(u":/ui/ui/images/icon-switch-on.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.admin_sms_alarm_fn_active_bnt.setIcon(icon9)
        self.admin_sms_alarm_fn_active_bnt.setIconSize(QSize(55, 103))
        self.admin_sms_alarm_fn_active_bnt.setCheckable(True)

        self.horizontalLayout_44.addWidget(self.admin_sms_alarm_fn_active_bnt)


        self.horizontalLayout_45.addLayout(self.horizontalLayout_44)

        self.horizontalSpacer_41 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_45.addItem(self.horizontalSpacer_41)


        self.verticalLayout_44.addLayout(self.horizontalLayout_45)

        self.horizontalLayout_98 = QHBoxLayout()
        self.horizontalLayout_98.setObjectName(u"horizontalLayout_98")
        self.horizontalSpacer_137 = QSpacerItem(98, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_98.addItem(self.horizontalSpacer_137)

        self.horizontalLayout_99 = QHBoxLayout()
        self.horizontalLayout_99.setObjectName(u"horizontalLayout_99")
        self.admin_sms_alarm_allow_phone_num_label = QLabel(self.fn_permission_page)
        self.admin_sms_alarm_allow_phone_num_label.setObjectName(u"admin_sms_alarm_allow_phone_num_label")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.admin_sms_alarm_allow_phone_num_label.sizePolicy().hasHeightForWidth())
        self.admin_sms_alarm_allow_phone_num_label.setSizePolicy(sizePolicy5)
        self.admin_sms_alarm_allow_phone_num_label.setMinimumSize(QSize(129, 27))
        self.admin_sms_alarm_allow_phone_num_label.setMaximumSize(QSize(155, 27))
        self.admin_sms_alarm_allow_phone_num_label.setFont(font11)
        self.admin_sms_alarm_allow_phone_num_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.admin_sms_alarm_allow_phone_num_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_99.addWidget(self.admin_sms_alarm_allow_phone_num_label)

        self.verticalLayout_61 = QVBoxLayout()
        self.verticalLayout_61.setSpacing(1)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.admin_sms_alarm_allow_phone_num_input = QLineEdit(self.fn_permission_page)
        self.admin_sms_alarm_allow_phone_num_input.setObjectName(u"admin_sms_alarm_allow_phone_num_input")
        sizePolicy1.setHeightForWidth(self.admin_sms_alarm_allow_phone_num_input.sizePolicy().hasHeightForWidth())
        self.admin_sms_alarm_allow_phone_num_input.setSizePolicy(sizePolicy1)
        self.admin_sms_alarm_allow_phone_num_input.setMinimumSize(QSize(94, 19))
        self.admin_sms_alarm_allow_phone_num_input.setMaximumSize(QSize(94, 19))
        self.admin_sms_alarm_allow_phone_num_input.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.admin_sms_alarm_allow_phone_num_input.setEchoMode(QLineEdit.EchoMode.Normal)
        self.admin_sms_alarm_allow_phone_num_input.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_61.addWidget(self.admin_sms_alarm_allow_phone_num_input)

        self.admin_sms_alarm_allow_phone_num_input_line = QFrame(self.fn_permission_page)
        self.admin_sms_alarm_allow_phone_num_input_line.setObjectName(u"admin_sms_alarm_allow_phone_num_input_line")
        sizePolicy1.setHeightForWidth(self.admin_sms_alarm_allow_phone_num_input_line.sizePolicy().hasHeightForWidth())
        self.admin_sms_alarm_allow_phone_num_input_line.setSizePolicy(sizePolicy1)
        self.admin_sms_alarm_allow_phone_num_input_line.setMinimumSize(QSize(94, 3))
        self.admin_sms_alarm_allow_phone_num_input_line.setMaximumSize(QSize(94, 3))
        self.admin_sms_alarm_allow_phone_num_input_line.setFont(font14)
        self.admin_sms_alarm_allow_phone_num_input_line.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.admin_sms_alarm_allow_phone_num_input_line.setAutoFillBackground(False)
        self.admin_sms_alarm_allow_phone_num_input_line.setStyleSheet(u"background-color: rgb(36, 39, 44)")
        self.admin_sms_alarm_allow_phone_num_input_line.setFrameShape(QFrame.Shape.HLine)
        self.admin_sms_alarm_allow_phone_num_input_line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_61.addWidget(self.admin_sms_alarm_allow_phone_num_input_line)


        self.horizontalLayout_99.addLayout(self.verticalLayout_61)


        self.horizontalLayout_98.addLayout(self.horizontalLayout_99)

        self.horizontalSpacer_138 = QSpacerItem(40, 13, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_98.addItem(self.horizontalSpacer_138)


        self.verticalLayout_44.addLayout(self.horizontalLayout_98)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalSpacer_46 = QSpacerItem(43, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_46)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setSpacing(17)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.admin_self_labeling_fn_active_label = QLabel(self.fn_permission_page)
        self.admin_self_labeling_fn_active_label.setObjectName(u"admin_self_labeling_fn_active_label")
        self.admin_self_labeling_fn_active_label.setMinimumSize(QSize(160, 25))
        self.admin_self_labeling_fn_active_label.setMaximumSize(QSize(167, 25))
        self.admin_self_labeling_fn_active_label.setFont(font11)
        self.admin_self_labeling_fn_active_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.admin_self_labeling_fn_active_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_22.addWidget(self.admin_self_labeling_fn_active_label)

        self.admin_self_labeling_fn_active_bnt = QPushButton(self.fn_permission_page)
        self.admin_self_labeling_fn_active_bnt.setObjectName(u"admin_self_labeling_fn_active_bnt")
        self.admin_self_labeling_fn_active_bnt.setMinimumSize(QSize(61, 25))
        self.admin_self_labeling_fn_active_bnt.setMaximumSize(QSize(61, 25))
        self.admin_self_labeling_fn_active_bnt.setIcon(icon9)
        self.admin_self_labeling_fn_active_bnt.setIconSize(QSize(55, 103))
        self.admin_self_labeling_fn_active_bnt.setCheckable(True)

        self.horizontalLayout_22.addWidget(self.admin_self_labeling_fn_active_bnt)


        self.horizontalLayout_21.addLayout(self.horizontalLayout_22)

        self.horizontalSpacer_47 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_47)


        self.verticalLayout_44.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_60 = QSpacerItem(43, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_60)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setSpacing(17)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.admin_live_viewer_block_label = QLabel(self.fn_permission_page)
        self.admin_live_viewer_block_label.setObjectName(u"admin_live_viewer_block_label")
        self.admin_live_viewer_block_label.setMinimumSize(QSize(160, 25))
        self.admin_live_viewer_block_label.setMaximumSize(QSize(167, 25))
        self.admin_live_viewer_block_label.setFont(font11)
        self.admin_live_viewer_block_label.setStyleSheet(u"color: rgb(179,179,179);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.admin_live_viewer_block_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_23.addWidget(self.admin_live_viewer_block_label)

        self.admin_live_viewer_block_bnt = QPushButton(self.fn_permission_page)
        self.admin_live_viewer_block_bnt.setObjectName(u"admin_live_viewer_block_bnt")
        self.admin_live_viewer_block_bnt.setMinimumSize(QSize(61, 25))
        self.admin_live_viewer_block_bnt.setMaximumSize(QSize(61, 25))
        self.admin_live_viewer_block_bnt.setIcon(icon9)
        self.admin_live_viewer_block_bnt.setIconSize(QSize(55, 103))
        self.admin_live_viewer_block_bnt.setCheckable(True)

        self.horizontalLayout_23.addWidget(self.admin_live_viewer_block_bnt)


        self.horizontalLayout_2.addLayout(self.horizontalLayout_23)

        self.horizontalSpacer_63 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_63)


        self.verticalLayout_44.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_55 = QHBoxLayout()
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalSpacer_48 = QSpacerItem(267, 0, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_55.addItem(self.horizontalSpacer_48)

        self.admin_fn_save_bnt = QPushButton(self.fn_permission_page)
        self.admin_fn_save_bnt.setObjectName(u"admin_fn_save_bnt")
        sizePolicy2.setHeightForWidth(self.admin_fn_save_bnt.sizePolicy().hasHeightForWidth())
        self.admin_fn_save_bnt.setSizePolicy(sizePolicy2)
        self.admin_fn_save_bnt.setMinimumSize(QSize(71, 41))
        self.admin_fn_save_bnt.setMaximumSize(QSize(71, 41))
        self.admin_fn_save_bnt.setFont(font18)
        self.admin_fn_save_bnt.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.admin_fn_save_bnt.setStyleSheet(u"background-color: qlineargradient(\n"
"    spread:pad,\n"
"    x1:0, y1:0, x2:0, y2:1,\n"
"    stop:0.0 rgba(112, 210, 112, 255),\n"
"    stop:0.3 rgba(0, 196, 0, 255)\n"
");\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"\n"
"")

        self.horizontalLayout_55.addWidget(self.admin_fn_save_bnt)

        self.horizontalSpacer_49 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_55.addItem(self.horizontalSpacer_49)


        self.verticalLayout_44.addLayout(self.horizontalLayout_55)

        self.verticalSpacer_19 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_44.addItem(self.verticalSpacer_19)


        self.verticalLayout_45.addLayout(self.verticalLayout_44)

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
        QWidget.setTabOrder(self.camera_schedule_bnt, self.admin_pw_input)
        QWidget.setTabOrder(self.admin_pw_input, self.admin_page_bnt)
        QWidget.setTabOrder(self.admin_page_bnt, self.admin_license_bnt)
        QWidget.setTabOrder(self.admin_license_bnt, self.admin_fn_permission_bnt)
        QWidget.setTabOrder(self.admin_fn_permission_bnt, self.license_add_bnt)
        QWidget.setTabOrder(self.license_add_bnt, self.license_remove_bnt)
        QWidget.setTabOrder(self.license_remove_bnt, self.license_save_bnt)
        QWidget.setTabOrder(self.license_save_bnt, self.admin_sms_alarm_fn_active_bnt)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.setting_setting_ai_weight_box.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MS-AI 1000", None))
        self.top_logo.setText("")
        self.verson_label.setText(QCoreApplication.translate("MainWindow", u"MS-AI1000 1.6.0", None))
        self.server_icon.setText("")
        self.server_info_label.setText(QCoreApplication.translate("MainWindow", u"NVR\uc11c\ubc84\uc815\ubcf4", None))
        self.server_ip_label.setText(QCoreApplication.translate("MainWindow", u"\uc8fc\uc18c", None))
        self.server_ip_input.setText("")
        self.server_id_label.setText(QCoreApplication.translate("MainWindow", u"\uc544\uc774\ub514", None))
        self.server_id_input.setText("")
        self.server_pw_label.setText(QCoreApplication.translate("MainWindow", u"\ube44\ubc00\ubc88\ud638", None))
        self.server_pw_input.setText("")
        self.server_login_bnt.setText(QCoreApplication.translate("MainWindow", u"\uc5f0\uacb0", None))
        self.shutdown_bnt.setText(QCoreApplication.translate("MainWindow", u"\uc885\ub8cc", None))
        ___qtablewidgetitem = self.camera_list_table.horizontalHeaderItem(1)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Num", None));
        ___qtablewidgetitem1 = self.camera_list_table.horizontalHeaderItem(2)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem2 = self.camera_list_table.horizontalHeaderItem(3)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Address", None));
        self.camera_bnt.setText(QCoreApplication.translate("MainWindow", u"AI Camera", None))
        self.tab_partion_11.setText(QCoreApplication.translate("MainWindow", u"|", None))
        self.search_memu_bnt.setText(QCoreApplication.translate("MainWindow", u"Event Search", None))
        self.tab_partion_5.setText(QCoreApplication.translate("MainWindow", u"|", None))
        self.setting_bnt.setText(QCoreApplication.translate("MainWindow", u"Setting", None))
        self.tab_partion_4.setText(QCoreApplication.translate("MainWindow", u"|", None))
        self.admin_bnt.setText(QCoreApplication.translate("MainWindow", u"Admin", None))
        self.labeling_bnt.setText("")
        self.camera_schedule_bnt.setText("")
        self.camera_page_camera_name_label.setText(QCoreApplication.translate("MainWindow", u"\uce74\uba54\ub77c \uc774\ub984", None))
        self.camera_page_camera_event_label.setText(QCoreApplication.translate("MainWindow", u"\uc774\ubca4\ud2b8 \uc885\ub958", None))
        self.camera_page_camera_event_box.setItemText(0, QCoreApplication.translate("MainWindow", u"\uce68\uc785", None))
        self.camera_page_camera_event_box.setItemText(1, QCoreApplication.translate("MainWindow", u"\ubc30\ud68c", None))
        self.camera_page_camera_event_box.setItemText(2, QCoreApplication.translate("MainWindow", u"\uc4f0\ub7ec\uc9d0", None))
        self.camera_page_camera_event_box.setItemText(3, QCoreApplication.translate("MainWindow", u"\ubc29\ud654", None))

        self.camera_page_detect_add_bnt.setText("")
        ___qtablewidgetitem3 = self.camera_page_detect_area_table.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\uac10\uc9c0 \uc601\uc5ed \ub9ac\uc2a4\ud2b8", None));
        self.camera_page_object_setting_bnt.setText(QCoreApplication.translate("MainWindow", u"\uc9c0\ub2a5\ud615 \ubd84\uc11d \uc124\uc815", None))
        self.camera_page_detect_area_del_bnt.setText(QCoreApplication.translate("MainWindow", u"\uc0ad\uc81c", None))
        self.camera_page_ai_bnt.setText(QCoreApplication.translate("MainWindow", u"\uc9c0\ub2a5\ud615 \ubd84\uc11d \uc2dc\uc791", None))
        self.camera_page_block_label.setText(QCoreApplication.translate("MainWindow", u"\u203b\uc6b4\uc601 \uc815\ucc45\uc0c1 LIVE \ud654\uba74\uc744 \ucc28\ub2e8\ud569\ub2c8\ub2e4.", None))
        self.camera_page_ai_active_icon.setText("")
        self.camera_page_ai_active_label.setText(QCoreApplication.translate("MainWindow", u"\uc9c0\ub2a5\ud615 \ubd84\uc11d \uc9c4\ud589\uc911", None))
        self.camera_page_viewer.setText("")
        self.setting_detect_info_label.setText(QCoreApplication.translate("MainWindow", u"\uc9c0\ub2a5\ud615 \uac80\ucd9c \uc815\ubcf4 \ud45c\uc2dc \uc124\uc815", None))
        self.setting_detect_bbox_active_label.setText(QCoreApplication.translate("MainWindow", u"BBox \ud65c\uc131\ud654", None))
        self.setting_detect_bbox_active_bnt.setText("")
        self.setting_detect_label_active_label.setText(QCoreApplication.translate("MainWindow", u"Label \ud65c\uc131\ud654", None))
        self.setting_detect_label_active_bnt.setText("")
        self.setting_detect_roi_active_label.setText(QCoreApplication.translate("MainWindow", u"\uad00\uc2ec\uc601\uc5ed \ud65c\uc131\ud654", None))
        self.setting_detect_roi_active_bnt.setText("")
        self.setting_event_pop_up_label.setText(QCoreApplication.translate("MainWindow", u"\uc774\ubca4\ud2b8 \uc54c\ub9bc \ud31d\uc5c5 \uc124\uc815", None))
        self.setting_event_pop_up_active_label.setText(QCoreApplication.translate("MainWindow", u"\uc54c\ub9bc \ud31d\uc5c5 \ud65c\uc131\ud654", None))
        self.setting_event_pop_up_active_bnt.setText("")
        self.setting_event_pop_up_duration_bnt.setText(QCoreApplication.translate("MainWindow", u"\uc54c\ub9bc \uc9c0\uc18d \uc2dc\uac04", None))
        self.setting_event_pop_up_duration_box.setItemText(0, QCoreApplication.translate("MainWindow", u"3\ucd08", None))
        self.setting_event_pop_up_duration_box.setItemText(1, QCoreApplication.translate("MainWindow", u"5\ucd08", None))
        self.setting_event_pop_up_duration_box.setItemText(2, QCoreApplication.translate("MainWindow", u"10\ucd08", None))
        self.setting_event_pop_up_duration_box.setItemText(3, QCoreApplication.translate("MainWindow", u"60\ucd08", None))
        self.setting_event_pop_up_duration_box.setItemText(4, QCoreApplication.translate("MainWindow", u"\uc5c6\uc74c", None))

        self.setting_event_pop_up_save_bnt.setText(QCoreApplication.translate("MainWindow", u"\uc800\uc7a5", None))
        self.setting_label_4.setText(QCoreApplication.translate("MainWindow", u"\uc9c0\ub2a5\ud615 AI \uc5d4\uc9c4 \uc124\uc815", None))
        self.setting_ai_weight_label.setText(QCoreApplication.translate("MainWindow", u"\uc9c0\ub2a5\ud615 \uac1d\uccb4 \uc778\uc2dd \ubaa8\ub378 \uc120\ud14d", None))
        self.setting_setting_ai_weight_box.setItemText(0, QCoreApplication.translate("MainWindow", u"2024-07-24", None))

        self.setting_setting_ai_weight_box.setPlaceholderText("")
        self.setting_self_training_auto_labeling_label.setText(QCoreApplication.translate("MainWindow", u"Self Auto Labeling \ud65c\uc131\ud654", None))
        self.setting_self_training_auto_labeling_bnt.setText("")
        self.setting_auto_label_time_start_box.setItemText(0, QCoreApplication.translate("MainWindow", u"00:00", None))
        self.setting_auto_label_time_start_box.setItemText(1, QCoreApplication.translate("MainWindow", u"01:00", None))
        self.setting_auto_label_time_start_box.setItemText(2, QCoreApplication.translate("MainWindow", u"02:00", None))
        self.setting_auto_label_time_start_box.setItemText(3, QCoreApplication.translate("MainWindow", u"03:00", None))
        self.setting_auto_label_time_start_box.setItemText(4, QCoreApplication.translate("MainWindow", u"04:00", None))
        self.setting_auto_label_time_start_box.setItemText(5, QCoreApplication.translate("MainWindow", u"05:00", None))
        self.setting_auto_label_time_start_box.setItemText(6, QCoreApplication.translate("MainWindow", u"06:00", None))
        self.setting_auto_label_time_start_box.setItemText(7, QCoreApplication.translate("MainWindow", u"07:00", None))
        self.setting_auto_label_time_start_box.setItemText(8, QCoreApplication.translate("MainWindow", u"08:00", None))
        self.setting_auto_label_time_start_box.setItemText(9, QCoreApplication.translate("MainWindow", u"09:00", None))
        self.setting_auto_label_time_start_box.setItemText(10, QCoreApplication.translate("MainWindow", u"10:00", None))
        self.setting_auto_label_time_start_box.setItemText(11, QCoreApplication.translate("MainWindow", u"11:00", None))
        self.setting_auto_label_time_start_box.setItemText(12, QCoreApplication.translate("MainWindow", u"12:00", None))
        self.setting_auto_label_time_start_box.setItemText(13, QCoreApplication.translate("MainWindow", u"13:00", None))
        self.setting_auto_label_time_start_box.setItemText(14, QCoreApplication.translate("MainWindow", u"14:00", None))
        self.setting_auto_label_time_start_box.setItemText(15, QCoreApplication.translate("MainWindow", u"15:00", None))
        self.setting_auto_label_time_start_box.setItemText(16, QCoreApplication.translate("MainWindow", u"16:00", None))
        self.setting_auto_label_time_start_box.setItemText(17, QCoreApplication.translate("MainWindow", u"17:00", None))
        self.setting_auto_label_time_start_box.setItemText(18, QCoreApplication.translate("MainWindow", u"18:00", None))
        self.setting_auto_label_time_start_box.setItemText(19, QCoreApplication.translate("MainWindow", u"19:00", None))
        self.setting_auto_label_time_start_box.setItemText(20, QCoreApplication.translate("MainWindow", u"20:00", None))
        self.setting_auto_label_time_start_box.setItemText(21, QCoreApplication.translate("MainWindow", u"21:00", None))
        self.setting_auto_label_time_start_box.setItemText(22, QCoreApplication.translate("MainWindow", u"22:00", None))
        self.setting_auto_label_time_start_box.setItemText(23, QCoreApplication.translate("MainWindow", u"23:00", None))

        self.time_tilde_2.setText(QCoreApplication.translate("MainWindow", u"~", None))
        self.setting_auto_label_time_end_box.setItemText(0, QCoreApplication.translate("MainWindow", u"00:00", None))
        self.setting_auto_label_time_end_box.setItemText(1, QCoreApplication.translate("MainWindow", u"01:00", None))
        self.setting_auto_label_time_end_box.setItemText(2, QCoreApplication.translate("MainWindow", u"02:00", None))
        self.setting_auto_label_time_end_box.setItemText(3, QCoreApplication.translate("MainWindow", u"03:00", None))
        self.setting_auto_label_time_end_box.setItemText(4, QCoreApplication.translate("MainWindow", u"04:00", None))
        self.setting_auto_label_time_end_box.setItemText(5, QCoreApplication.translate("MainWindow", u"05:00", None))
        self.setting_auto_label_time_end_box.setItemText(6, QCoreApplication.translate("MainWindow", u"06:00", None))
        self.setting_auto_label_time_end_box.setItemText(7, QCoreApplication.translate("MainWindow", u"07:00", None))
        self.setting_auto_label_time_end_box.setItemText(8, QCoreApplication.translate("MainWindow", u"08:00", None))
        self.setting_auto_label_time_end_box.setItemText(9, QCoreApplication.translate("MainWindow", u"09:00", None))
        self.setting_auto_label_time_end_box.setItemText(10, QCoreApplication.translate("MainWindow", u"10:00", None))
        self.setting_auto_label_time_end_box.setItemText(11, QCoreApplication.translate("MainWindow", u"11:00", None))
        self.setting_auto_label_time_end_box.setItemText(12, QCoreApplication.translate("MainWindow", u"12:00", None))
        self.setting_auto_label_time_end_box.setItemText(13, QCoreApplication.translate("MainWindow", u"13:00", None))
        self.setting_auto_label_time_end_box.setItemText(14, QCoreApplication.translate("MainWindow", u"14:00", None))
        self.setting_auto_label_time_end_box.setItemText(15, QCoreApplication.translate("MainWindow", u"15:00", None))
        self.setting_auto_label_time_end_box.setItemText(16, QCoreApplication.translate("MainWindow", u"16:00", None))
        self.setting_auto_label_time_end_box.setItemText(17, QCoreApplication.translate("MainWindow", u"17:00", None))
        self.setting_auto_label_time_end_box.setItemText(18, QCoreApplication.translate("MainWindow", u"18:00", None))
        self.setting_auto_label_time_end_box.setItemText(19, QCoreApplication.translate("MainWindow", u"19:00", None))
        self.setting_auto_label_time_end_box.setItemText(20, QCoreApplication.translate("MainWindow", u"20:00", None))
        self.setting_auto_label_time_end_box.setItemText(21, QCoreApplication.translate("MainWindow", u"21:00", None))
        self.setting_auto_label_time_end_box.setItemText(22, QCoreApplication.translate("MainWindow", u"22:00", None))
        self.setting_auto_label_time_end_box.setItemText(23, QCoreApplication.translate("MainWindow", u"23:00", None))

        self.setting_page_email_info_label_10.setText(QCoreApplication.translate("MainWindow", u"\u203bSelf Auto Labeling \ud65c\uc131\ud654\uc2dc \uc9c0\uc815\ub41c \uc2dc\uac04\uc5d0 \uc790\ub3d9\uc73c\ub85c Labeling\uc744 \uc2dc\uc791\ud569\ub2c8\ub2e4.", None))
        self.setting_self_training_zeroshot_label.setText(QCoreApplication.translate("MainWindow", u"AI Labeling Assistance \ud65c\uc131\ud654", None))
        self.setting_self_training_zeroshot_bnt.setText("")
        self.setting_page_email_info_label_9.setText(QCoreApplication.translate("MainWindow", u"\u203bAI Labeling Assistance \uc740 \uc0c8\ub85c\uc6b4 \ud658\uacbd\uc5d0\uc11c  \ucd08\uae30  \ubaa8\ub378 \ud559\uc2b5 \uc131\ub2a5 \uac1c\uc120\uc744 \ub3c4\uc640\uc90d\ub2c8\ub2e4.", None))
        self.setting_page_email_info_label_11.setText(QCoreApplication.translate("MainWindow", u"  (\uc8fc\uc758 : AI Labeling \uc18c\uc694 \uc2dc\uac04 \uc99d\uac00)", None))
        self.setting_ai_setting_save_bnt.setText(QCoreApplication.translate("MainWindow", u"\uc800\uc7a5", None))
        self.setting_notice_label_3.setText(QCoreApplication.translate("MainWindow", u"\uc54c\ub9bc \uc804\ub2ec \uc5f0\ub77d\ucc98 \uc124\uc815", None))
        self.setting_notice_phone_active_bnt.setText("")
#if QT_CONFIG(whatsthis)
        self.setting_notice_phone_num_input.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.setting_notice_phone_num_input.setInputMask("")
        self.setting_notice_phone_num_input.setText("")
        self.setting_notice_phone_num_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"010-xxxx-xxxx", None))
        self.setting_notice_phone_add_bnt.setText("")
        self.setting_notice_phone_del_bnt.setText("")
        ___qtablewidgetitem4 = self.setting_notice_phone_list.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\uc54c\ub78c \uc804\uc1a1 \uc804\ud654\ubc88\ud638 \ub9ac\uc2a4\ud2b8", None));
        self.setting_notice_label_4.setText(QCoreApplication.translate("MainWindow", u"\uc54c\ub9bc \uc885\ub958 \uc120\ud0dd", None))
        self.setting_notion_detect_type_bnt1.setText(QCoreApplication.translate("MainWindow", u"\uce68\uc785", None))
        self.setting_notion_detect_type_bnt2.setText(QCoreApplication.translate("MainWindow", u"\uce68\uc785", None))
        self.setting_notion_detect_type_bnt3.setText(QCoreApplication.translate("MainWindow", u"\uce68\uc785", None))
        self.setting_notion_detect_type_bnt4.setText(QCoreApplication.translate("MainWindow", u"\uce68\uc785", None))
        self.setting_notice_phone_save_bnt.setText(QCoreApplication.translate("MainWindow", u"\uc800\uc7a5", None))
        self.setting_label_5.setText(QCoreApplication.translate("MainWindow", u"\uc0ac\uc6a9\uc790 \ub85c\uadf8\uc778 \ubcc0\uacbd", None))
        self.setting_user_id_label.setText(QCoreApplication.translate("MainWindow", u"\ud604\uc7ac \uc544\uc774\ub514", None))
        self.setting_user_id_input.setText("")
        self.setting_user_pw_label.setText(QCoreApplication.translate("MainWindow", u"\uae30\uc874 \ube44\ubc00\ubc88\ud638", None))
        self.setting_user_pw_input.setText("")
        self.setting_user_new_pw_label.setText(QCoreApplication.translate("MainWindow", u"\uc2e0\uaddc \ube44\ubc00\ubc88\ud638", None))
        self.setting_user_new_pw_input.setText("")
        self.setting_user_new_pw_label2.setText(QCoreApplication.translate("MainWindow", u"\ube44\ubc00\ubc88\ud638 \ud655\uc778", None))
        self.setting_user_new_pw_input2.setText("")
        self.setting_user_save_bnt.setText(QCoreApplication.translate("MainWindow", u"\ubcc0\uacbd", None))
        self.admin_pw_label.setText(QCoreApplication.translate("MainWindow", u"\uad00\ub9ac\uc790 \ube44\ubc00\ubc88\ud638", None))
        self.admin_pw_input.setText(QCoreApplication.translate("MainWindow", u"asdsad", None))
        self.admin_page_bnt.setText(QCoreApplication.translate("MainWindow", u"\uc785\ub825", None))
        self.admin_license_bnt.setText(QCoreApplication.translate("MainWindow", u"\uc9c0\ub2a5\ud615 \ub77c\uc774\uc13c\uc2a4 \uc124\uc815", None))
        self.admin_fn_permission_bnt.setText(QCoreApplication.translate("MainWindow", u"\uae30\ub2a5 \uad8c\ud55c \uc124\uc815", None))
        self.license_camera_allow_num_label.setText(QCoreApplication.translate("MainWindow", u"\uc9c0\ub2a5\ud615 \uad6c\ub3d9 \uce74\uba54\ub77c \ud5c8\uc6a9 \uc218", None))
        self.license_camera_allow_num_input.setText("")
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
        self.admin_sms_alarm_fn_active_label.setText(QCoreApplication.translate("MainWindow", u"SMS \uc54c\ub9bc \uc804\uc1a1 \uae30\ub2a5 \ud65c\uc131\ud654", None))
        self.admin_sms_alarm_fn_active_bnt.setText("")
        self.admin_sms_alarm_allow_phone_num_label.setText(QCoreApplication.translate("MainWindow", u"\uc804\ud654\ubc88\ud638 \ub4f1\ub85d \ud5c8\uc6a9 \uc218", None))
        self.admin_sms_alarm_allow_phone_num_input.setText("")
        self.admin_self_labeling_fn_active_label.setText(QCoreApplication.translate("MainWindow", u"\uc790\uac00\ud559\uc2b5 \uae30\ub2a5 \ud65c\uc131\ud654", None))
        self.admin_self_labeling_fn_active_bnt.setText("")
        self.admin_live_viewer_block_label.setText(QCoreApplication.translate("MainWindow", u"\ub77c\uc774\ube0c \ud654\uba74 \ucc28\ub2e8 \ud65c\uc131\ud654", None))
        self.admin_live_viewer_block_bnt.setText("")
        self.admin_fn_save_bnt.setText(QCoreApplication.translate("MainWindow", u"\uc800\uc7a5", None))
    # retranslateUi

