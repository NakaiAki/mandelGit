# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'param_form.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SubWindow(object):
    def setupUi(self, SubWindow):
        SubWindow.setObjectName("SubWindow")
        SubWindow.resize(390, 390)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SubWindow.sizePolicy().hasHeightForWidth())
        SubWindow.setSizePolicy(sizePolicy)
        SubWindow.setMinimumSize(QtCore.QSize(390, 390))
        SubWindow.setMaximumSize(QtCore.QSize(390, 390))
        font = QtGui.QFont()
        font.setKerning(True)
        SubWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/param.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SubWindow.setWindowIcon(icon)
        SubWindow.setStyleSheet("QLabel\n"
"{\n"
"font: 75 11pt \"Meiryo UI\";\n"
"}\n"
"\n"
"\n"
"QToolTip\n"
"{\n"
"     border: 1px solid black;\n"
"     background-color: #ffa02f;\n"
"     padding: 1px;\n"
"     border-radius: 3px;\n"
"     opacity: 100;\n"
"}\n"
"\n"
"QWidget\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QWidget:item:hover\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #ca0619);\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:item:selected\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QMenuBar::item\n"
"{\n"
"    background: transparent;\n"
"}\n"
"\n"
"QMenuBar::item:selected\n"
"{\n"
"    background: transparent;\n"
"    border: 1px solid #ffaa00;\n"
"}\n"
"\n"
"QMenuBar::item:pressed\n"
"{\n"
"    background: #444;\n"
"    border: 1px solid #000;\n"
"    background-color: QLinearGradient(\n"
"        x1:0, y1:0,\n"
"        x2:0, y2:1,\n"
"        stop:1 #212121,\n"
"        stop:0.4 #343434/*,\n"
"        stop:0.2 #343434,\n"
"        stop:0.1 #ffaa00*/\n"
"    );\n"
"    margin-bottom:-1px;\n"
"    padding-bottom:1px;\n"
"}\n"
"\n"
"QMenu\n"
"{\n"
"    border: 1px solid #000;\n"
"}\n"
"\n"
"QMenu::item\n"
"{\n"
"    padding: 2px 20px 2px 20px;\n"
"}\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:disabled\n"
"{\n"
"    color: #404040;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QAbstractItemView\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0.1 #646464, stop: 1 #5d5d5d);\n"
"}\n"
"\n"
"QWidget:focus\n"
"{\n"
"    /*border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);*/\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0 #646464, stop: 1 #5d5d5d);\n"
"    padding: 1px;\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-width: 1px;\n"
"    border-color: #1e1e1e;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"    padding: 3px;\n"
"    font: 11pt \"Meiryo UI\";\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    selection-background-color: #ffaa00;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QComboBox:hover,QPushButton:hover\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"\n"
"QComboBox:on\n"
"{\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"    selection-background-color: #ffaa00;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    border: 2px solid darkgray;\n"
"    selection-background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"     subcontrol-origin: padding;\n"
"     subcontrol-position: top right;\n"
"     width: 15px;\n"
"\n"
"     border-left-width: 0px;\n"
"     border-left-color: darkgray;\n"
"     border-left-style: solid; /* just a single line */\n"
"     border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"     border-bottom-right-radius: 3px;\n"
" }\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"     image: url(:/down_arrow.png);\n"
"}\n"
"\n"
"QGroupBox:focus\n"
"{\n"
"border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QTextEdit:focus\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"     border: 1px solid #222222;\n"
"     background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
"     height: 7px;\n"
"     margin: 0px 16px 0 16px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      width: 14px;\n"
"      subcontrol-position: right;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      width: 14px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal, QScrollBar::left-arrow:horizontal\n"
"{\n"
"      border: 1px solid black;\n"
"      width: 1px;\n"
"      height: 1px;\n"
"      background: white;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
"      width: 7px;\n"
"      margin: 16px 0 16px 0;\n"
"      border: 1px solid #222222;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      height: 14px;\n"
"      subcontrol-position: bottom;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #d7801a, stop: 1 #ffa02f);\n"
"      height: 14px;\n"
"      subcontrol-position: top;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"{\n"
"      border: 1px solid black;\n"
"      width: 1px;\n"
"      height: 1px;\n"
"      background: white;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QTextEdit\n"
"{\n"
"    background-color: #242424;\n"
"}\n"
"\n"
"QPlainTextEdit\n"
"{\n"
"    background-color: #242424;\n"
"}\n"
"\n"
"QHeaderView::section\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #616161, stop: 0.5 #505050, stop: 0.6 #434343, stop:1 #656565);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"}\n"
"\n"
"QCheckBox:disabled\n"
"{\n"
"color: #414141;\n"
"}\n"
"\n"
"QDockWidget::title\n"
"{\n"
"    text-align: center;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
"}\n"
"\n"
"QDockWidget::close-button, QDockWidget::float-button\n"
"{\n"
"    text-align: center;\n"
"    spacing: 1px; /* spacing between items in the tool bar */\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
"}\n"
"\n"
"QDockWidget::close-button:hover, QDockWidget::float-button:hover\n"
"{\n"
"    background: #242424;\n"
"}\n"
"\n"
"QDockWidget::close-button:pressed, QDockWidget::float-button:pressed\n"
"{\n"
"    padding: 1px -1px -1px 1px;\n"
"}\n"
"\n"
"QMainWindow::separator\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #4c4c4c;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QMainWindow::separator:hover\n"
"{\n"
"\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #d7801a, stop:0.5 #b56c17 stop:1 #ffa02f);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QToolBar::handle\n"
"{\n"
"     spacing: 3px; /* spacing between items in the tool bar */\n"
"     background: url(:/images/handle.png);\n"
"}\n"
"\n"
"QMenu::separator\n"
"{\n"
"    height: 2px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"QProgressBar\n"
"{\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: #d7801a;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #444;\n"
"    border-bottom-style: none;\n"
"    background-color: #323232;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    padding-top: 3px;\n"
"    padding-bottom: 2px;\n"
"    margin-right: -1px;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: 1px solid #444;\n"
"    top: 1px;\n"
"}\n"
"\n"
"QTabBar::tab:last\n"
"{\n"
"    margin-right: 0; /* the last selected tab has nothing to overlap with on the right */\n"
"    border-top-right-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:first:!selected\n"
"{\n"
" margin-left: 0px; /* the last selected tab has nothing to overlap with on the right */\n"
"\n"
"\n"
"    border-top-left-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    border-bottom-style: solid;\n"
"    margin-top: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:.4 #343434);\n"
"}\n"
"\n"
"QTabBar::tab:selected\n"
"{\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    margin-bottom: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover\n"
"{\n"
"    /*border-top: 2px solid #ffaa00;\n"
"    padding-bottom: 3px;*/\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:0.4 #343434, stop:0.2 #343434, stop:0.1 #ffaa00);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked, QRadioButton::indicator:unchecked{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked\n"
"{\n"
"    background-color: qradialgradient(\n"
"        cx: 0.5, cy: 0.5,\n"
"        fx: 0.5, fy: 0.5,\n"
"        radius: 1.0,\n"
"        stop: 0.25 #ffaa00,\n"
"        stop: 0.3 #323232\n"
"    );\n"
"}\n"
"\n"
"QCheckBox::indicator{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    width: 9px;\n"
"    height: 9px;\n"
"}\n"
"\n"
"QRadioButton::indicator\n"
"{\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:hover, QCheckBox::indicator:hover\n"
"{\n"
"    border: 1px solid #ffaa00;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    image:url(:/images/checkbox.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:disabled, QRadioButton::indicator:disabled\n"
"{\n"
"    border: 1px solid #444;\n"
"}\n"
"\n"
"QSlider {\n"
"    border: none;\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"    height: 5px;\n"
"    margin: 4px 0px 4px 0px;\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    width: 5px;\n"
"    margin: 0px 4px 0px 4px;\n"
"}\n"
"\n"
"QSlider::handle {\n"
"    border: 1px solid #5A5A5A;\n"
"    background: #999c99;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    width: 15px;\n"
"    margin: -4px 0px -4px 0px;\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    height: 15px;\n"
"    margin: 0px -4px 0px -4px;\n"
"}")
        SubWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(SubWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.param_tab = QtWidgets.QTabWidget(self.centralwidget)
        self.param_tab.setGeometry(QtCore.QRect(0, 0, 390, 391))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.param_tab.sizePolicy().hasHeightForWidth())
        self.param_tab.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.param_tab.setFont(font)
        self.param_tab.setTabPosition(QtWidgets.QTabWidget.North)
        self.param_tab.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.param_tab.setTabBarAutoHide(False)
        self.param_tab.setObjectName("param_tab")
        self.mandel = QtWidgets.QWidget()
        self.mandel.setObjectName("mandel")
        self.pushButton_4 = QtWidgets.QPushButton(self.mandel)
        self.pushButton_4.setGeometry(QtCore.QRect(210, 256, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton\n"
"{\n"
"font: 11pt \"Meiryo UI\";\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.mPosXText = QtWidgets.QLineEdit(self.mandel)
        self.mPosXText.setGeometry(QtCore.QRect(11, 204, 167, 25))
        font = QtGui.QFont()
        font.setFamily("07ロゴたいぷゴシック7")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.mPosXText.setFont(font)
        self.mPosXText.setObjectName("mPosXText")
        self.mSizeText = QtWidgets.QLineEdit(self.mandel)
        self.mSizeText.setGeometry(QtCore.QRect(11, 148, 167, 25))
        font = QtGui.QFont()
        font.setFamily("07ロゴたいぷゴシック7")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.mSizeText.setFont(font)
        self.mSizeText.setObjectName("mSizeText")
        self.mdgText = QtWidgets.QLineEdit(self.mandel)
        self.mdgText.setGeometry(QtCore.QRect(11, 92, 167, 25))
        font = QtGui.QFont()
        font.setFamily("07ロゴたいぷゴシック7")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.mdgText.setFont(font)
        self.mdgText.setObjectName("mdgText")
        self.label_2 = QtWidgets.QLabel(self.mandel)
        self.label_2.setGeometry(QtCore.QRect(11, 11, 90, 19))
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self.mandel)
        self.label_5.setGeometry(QtCore.QRect(11, 179, 83, 19))
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.mandel)
        self.label_6.setGeometry(QtCore.QRect(11, 235, 83, 19))
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.label_3 = QtWidgets.QLabel(self.mandel)
        self.label_3.setGeometry(QtCore.QRect(11, 67, 60, 19))
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.mandel)
        self.label_4.setGeometry(QtCore.QRect(11, 123, 69, 19))
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.mPosYText = QtWidgets.QLineEdit(self.mandel)
        self.mPosYText.setGeometry(QtCore.QRect(11, 260, 167, 25))
        font = QtGui.QFont()
        font.setFamily("07ロゴたいぷゴシック7")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.mPosYText.setFont(font)
        self.mPosYText.setObjectName("mPosYText")
        self.mCalcLimitText = QtWidgets.QLineEdit(self.mandel)
        self.mCalcLimitText.setGeometry(QtCore.QRect(11, 36, 167, 25))
        font = QtGui.QFont()
        font.setFamily("07ロゴたいぷゴシック7")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.mCalcLimitText.setFont(font)
        self.mCalcLimitText.setClearButtonEnabled(False)
        self.mCalcLimitText.setObjectName("mCalcLimitText")
        self.param_tab.addTab(self.mandel, "")
        self.julia = QtWidgets.QWidget()
        self.julia.setObjectName("julia")
        self.realText = QtWidgets.QLineEdit(self.julia)
        self.realText.setGeometry(QtCore.QRect(210, 34, 167, 25))
        font = QtGui.QFont()
        font.setFamily("07ロゴたいぷゴシック7")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.realText.setFont(font)
        self.realText.setObjectName("realText")
        self.pushButton_5 = QtWidgets.QPushButton(self.julia)
        self.pushButton_5.setGeometry(QtCore.QRect(210, 256, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton\n"
"{\n"
"font: 11pt \"Meiryo UI\";\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_8 = QtWidgets.QLabel(self.julia)
        self.label_8.setGeometry(QtCore.QRect(11, 67, 60, 19))
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.julia)
        self.label_9.setGeometry(QtCore.QRect(11, 123, 69, 19))
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.jCalcLimitText = QtWidgets.QLineEdit(self.julia)
        self.jCalcLimitText.setGeometry(QtCore.QRect(11, 36, 167, 25))
        font = QtGui.QFont()
        font.setFamily("07ロゴたいぷゴシック7")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.jCalcLimitText.setFont(font)
        self.jCalcLimitText.setClearButtonEnabled(False)
        self.jCalcLimitText.setObjectName("jCalcLimitText")
        self.jSizeText = QtWidgets.QLineEdit(self.julia)
        self.jSizeText.setGeometry(QtCore.QRect(11, 148, 167, 25))
        font = QtGui.QFont()
        font.setFamily("07ロゴたいぷゴシック7")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.jSizeText.setFont(font)
        self.jSizeText.setObjectName("jSizeText")
        self.jdgText = QtWidgets.QLineEdit(self.julia)
        self.jdgText.setGeometry(QtCore.QRect(11, 92, 167, 25))
        font = QtGui.QFont()
        font.setFamily("07ロゴたいぷゴシック7")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.jdgText.setFont(font)
        self.jdgText.setObjectName("jdgText")
        self.label_12 = QtWidgets.QLabel(self.julia)
        self.label_12.setGeometry(QtCore.QRect(210, 9, 54, 19))
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_12.setFont(font)
        self.label_12.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_12.setTextFormat(QtCore.Qt.AutoText)
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.jPosXText = QtWidgets.QLineEdit(self.julia)
        self.jPosXText.setGeometry(QtCore.QRect(11, 204, 167, 25))
        font = QtGui.QFont()
        font.setFamily("07ロゴたいぷゴシック7")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.jPosXText.setFont(font)
        self.jPosXText.setObjectName("jPosXText")
        self.imText = QtWidgets.QLineEdit(self.julia)
        self.imText.setGeometry(QtCore.QRect(210, 90, 167, 25))
        font = QtGui.QFont()
        font.setFamily("07ロゴたいぷゴシック7")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.imText.setFont(font)
        self.imText.setObjectName("imText")
        self.label_10 = QtWidgets.QLabel(self.julia)
        self.label_10.setGeometry(QtCore.QRect(11, 179, 83, 19))
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.julia)
        self.label_11.setGeometry(QtCore.QRect(11, 235, 83, 19))
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.jPosYText = QtWidgets.QLineEdit(self.julia)
        self.jPosYText.setGeometry(QtCore.QRect(11, 260, 167, 25))
        font = QtGui.QFont()
        font.setFamily("07ロゴたいぷゴシック7")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.jPosYText.setFont(font)
        self.jPosYText.setObjectName("jPosYText")
        self.label_13 = QtWidgets.QLabel(self.julia)
        self.label_13.setGeometry(QtCore.QRect(210, 65, 54, 19))
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_13.setFont(font)
        self.label_13.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_13.setTextFormat(QtCore.Qt.AutoText)
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.label_7 = QtWidgets.QLabel(self.julia)
        self.label_7.setGeometry(QtCore.QRect(11, 11, 90, 19))
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.param_tab.addTab(self.julia, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_15 = QtWidgets.QLabel(self.tab)
        self.label_15.setGeometry(QtCore.QRect(20, 100, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.brightBox = QtWidgets.QCheckBox(self.tab)
        self.brightBox.setGeometry(QtCore.QRect(20, 190, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(11)
        self.brightBox.setFont(font)
        self.brightBox.setChecked(False)
        self.brightBox.setTristate(False)
        self.brightBox.setObjectName("brightBox")
        self.hueSlider = QtWidgets.QSlider(self.tab)
        self.hueSlider.setGeometry(QtCore.QRect(20, 140, 291, 22))
        self.hueSlider.setMaximum(360)
        self.hueSlider.setPageStep(1)
        self.hueSlider.setProperty("value", 100)
        self.hueSlider.setOrientation(QtCore.Qt.Horizontal)
        self.hueSlider.setObjectName("hueSlider")
        self.colorbar = QtWidgets.QGraphicsView(self.tab)
        self.colorbar.setGeometry(QtCore.QRect(20, 250, 351, 30))
        self.colorbar.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.colorbar.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.colorbar.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.colorbar.setObjectName("colorbar")
        self.hueText = QtWidgets.QLineEdit(self.tab)
        self.hueText.setGeometry(QtCore.QRect(330, 140, 41, 25))
        font = QtGui.QFont()
        font.setFamily("07ロゴたいぷゴシック7")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.hueText.setFont(font)
        self.hueText.setObjectName("hueText")
        self.chromaText = QtWidgets.QLineEdit(self.tab)
        self.chromaText.setGeometry(QtCore.QRect(330, 60, 41, 25))
        font = QtGui.QFont()
        font.setFamily("07ロゴたいぷゴシック7")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.chromaText.setFont(font)
        self.chromaText.setClearButtonEnabled(False)
        self.chromaText.setObjectName("chromaText")
        self.chromaSlider = QtWidgets.QSlider(self.tab)
        self.chromaSlider.setGeometry(QtCore.QRect(20, 60, 291, 22))
        self.chromaSlider.setMaximum(255)
        self.chromaSlider.setSingleStep(1)
        self.chromaSlider.setPageStep(10)
        self.chromaSlider.setProperty("value", 255)
        self.chromaSlider.setSliderPosition(255)
        self.chromaSlider.setOrientation(QtCore.Qt.Horizontal)
        self.chromaSlider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.chromaSlider.setTickInterval(0)
        self.chromaSlider.setObjectName("chromaSlider")
        self.label_14 = QtWidgets.QLabel(self.tab)
        self.label_14.setGeometry(QtCore.QRect(20, 20, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.changecol = QtWidgets.QPushButton(self.tab)
        self.changecol.setGeometry(QtCore.QRect(260, 300, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Meiryo UI")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.changecol.setFont(font)
        self.changecol.setStyleSheet("QPushButton\n"
"{\n"
"font: 11pt \"Meiryo UI\";\n"
"}")
        self.changecol.setObjectName("changecol")
        self.param_tab.addTab(self.tab, "")
        SubWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SubWindow)
        self.param_tab.setCurrentIndex(2)
        self.pushButton_4.clicked.connect(SubWindow.confirm_mandel_param)
        self.pushButton_5.clicked.connect(SubWindow.confirm_julia_param)
        self.chromaSlider.sliderMoved['int'].connect(SubWindow.move_slider)
        self.hueSlider.sliderMoved['int'].connect(SubWindow.move_slider)
        self.brightBox.stateChanged['int'].connect(SubWindow.move_slider)
        self.changecol.clicked.connect(SubWindow.chenge_color)
        QtCore.QMetaObject.connectSlotsByName(SubWindow)
        SubWindow.setTabOrder(self.mCalcLimitText, self.mdgText)
        SubWindow.setTabOrder(self.mdgText, self.mSizeText)
        SubWindow.setTabOrder(self.mSizeText, self.mPosXText)
        SubWindow.setTabOrder(self.mPosXText, self.mPosYText)
        SubWindow.setTabOrder(self.mPosYText, self.pushButton_4)
        SubWindow.setTabOrder(self.pushButton_4, self.jCalcLimitText)
        SubWindow.setTabOrder(self.jCalcLimitText, self.jdgText)
        SubWindow.setTabOrder(self.jdgText, self.jSizeText)
        SubWindow.setTabOrder(self.jSizeText, self.jPosXText)
        SubWindow.setTabOrder(self.jPosXText, self.jPosYText)
        SubWindow.setTabOrder(self.jPosYText, self.realText)
        SubWindow.setTabOrder(self.realText, self.imText)
        SubWindow.setTabOrder(self.imText, self.pushButton_5)
        SubWindow.setTabOrder(self.pushButton_5, self.chromaText)
        SubWindow.setTabOrder(self.chromaText, self.hueText)
        SubWindow.setTabOrder(self.hueText, self.colorbar)
        SubWindow.setTabOrder(self.colorbar, self.hueSlider)
        SubWindow.setTabOrder(self.hueSlider, self.chromaSlider)

    def retranslateUi(self, SubWindow):
        _translate = QtCore.QCoreApplication.translate
        SubWindow.setWindowTitle(_translate("SubWindow", "パラメータ"))
        self.pushButton_4.setText(_translate("SubWindow", "パラメータ決定"))
        self.mPosXText.setText(_translate("SubWindow", "0"))
        self.mSizeText.setText(_translate("SubWindow", "4"))
        self.mdgText.setText(_translate("SubWindow", "2"))
        self.label_2.setText(_translate("SubWindow", "計算回数上限"))
        self.label_5.setText(_translate("SubWindow", "中心のx座標"))
        self.label_6.setText(_translate("SubWindow", "中心のy座標"))
        self.label_3.setText(_translate("SubWindow", "発散基準"))
        self.label_4.setText(_translate("SubWindow", "1辺の長さ"))
        self.mPosYText.setText(_translate("SubWindow", "0"))
        self.mCalcLimitText.setText(_translate("SubWindow", "30"))
        self.param_tab.setTabText(self.param_tab.indexOf(self.mandel), _translate("SubWindow", "マンデルブロ集合"))
        self.realText.setText(_translate("SubWindow", "-0.8"))
        self.pushButton_5.setText(_translate("SubWindow", "パラメータ決定"))
        self.label_8.setText(_translate("SubWindow", "発散基準"))
        self.label_9.setText(_translate("SubWindow", "1辺の長さ"))
        self.jCalcLimitText.setText(_translate("SubWindow", "80"))
        self.jSizeText.setText(_translate("SubWindow", "4"))
        self.jdgText.setText(_translate("SubWindow", "2"))
        self.label_12.setText(_translate("SubWindow", "Cの実部"))
        self.jPosXText.setText(_translate("SubWindow", "0"))
        self.imText.setText(_translate("SubWindow", "0.156"))
        self.label_10.setText(_translate("SubWindow", "中心のx座標"))
        self.label_11.setText(_translate("SubWindow", "中心のy座標"))
        self.jPosYText.setText(_translate("SubWindow", "0"))
        self.label_13.setText(_translate("SubWindow", "Cの虚部"))
        self.label_7.setText(_translate("SubWindow", "計算回数上限"))
        self.param_tab.setTabText(self.param_tab.indexOf(self.julia), _translate("SubWindow", "ジュリア集合"))
        self.label_15.setText(_translate("SubWindow", "色相の初期値"))
        self.brightBox.setText(_translate("SubWindow", "徐々に暗くする"))
        self.hueText.setText(_translate("SubWindow", "100"))
        self.chromaText.setText(_translate("SubWindow", "255"))
        self.label_14.setText(_translate("SubWindow", "彩度"))
        self.changecol.setText(_translate("SubWindow", "色の変更"))
        self.param_tab.setTabText(self.param_tab.indexOf(self.tab), _translate("SubWindow", "パレット"))

import myresource_rc
