# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'naver_login2ixlqzm.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(321, 599)
        icon = QIcon()
        icon.addFile(u"icon.jpg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.LOGIN_Button = QPushButton(self.centralwidget)
        self.LOGIN_Button.setObjectName(u"LOGIN_Button")
        self.LOGIN_Button.setGeometry(QRect(200, 20, 51, 51))
        self.LOGIN_Button.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 195, 75);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(50, 170, 75);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(0, 105, 25);\n"
"}")
        self.BACKGROUND = QLabel(self.centralwidget)
        self.BACKGROUND.setObjectName(u"BACKGROUND")
        self.BACKGROUND.setEnabled(True)
        self.BACKGROUND.setGeometry(QRect(0, 0, 851, 411))
        self.BACKGROUND.setStyleSheet(u"background-color:white;\n"
"")
        self.N_ID_Input = QLineEdit(self.centralwidget)
        self.N_ID_Input.setObjectName(u"N_ID_Input")
        self.N_ID_Input.setGeometry(QRect(20, 20, 171, 20))
        self.N_PW_Input = QLineEdit(self.centralwidget)
        self.N_PW_Input.setObjectName(u"N_PW_Input")
        self.N_PW_Input.setGeometry(QRect(20, 50, 171, 20))
        self.N_PW_Input.setEchoMode(QLineEdit.Password)
        self.FRI_Group = QGroupBox(self.centralwidget)
        self.FRI_Group.setObjectName(u"FRI_Group")
        self.FRI_Group.setEnabled(True)
        self.FRI_Group.setGeometry(QRect(20, 90, 281, 121))
        self.FRI_Group.setBaseSize(QSize(0, 0))
        font = QFont()
        font.setFamily(u"G\ub9c8\ucf13 \uc0b0\uc2a4 Bold")
        font.setPointSize(12)
        self.FRI_Group.setFont(font)
        self.FRI_Group.setStyleSheet(u"")
        self.label = QLabel(self.FRI_Group)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 71, 20))
        font1 = QFont()
        font1.setFamily(u"G\ub9c8\ucf13 \uc0b0\uc2a4 Medium")
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setWeight(QFont.Weight.Normal)
        self.label.setFont(font1)
        self.FRI_Count = QSpinBox(self.FRI_Group)
        self.FRI_Count.setObjectName(u"FRI_Count")
        self.FRI_Count.setGeometry(QRect(90, 20, 51, 22))
        font2 = QFont()
        font2.setFamily(u"G\ub9c8\ucf13 \uc0b0\uc2a4 Medium")
        font2.setPointSize(9)
        self.FRI_Count.setFont(font2)
        self.FRI_Count.setMinimum(1)
        self.FRI_Count.setMaximum(150)
        self.label_2 = QLabel(self.FRI_Group)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(150, 20, 21, 20))
        self.label_2.setFont(font1)
        self.label_3 = QLabel(self.FRI_Group)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 50, 101, 20))
        self.label_3.setFont(font1)
        self.label_4 = QLabel(self.FRI_Group)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(180, 50, 21, 20))
        self.label_4.setFont(font1)
        self.FRI_Interval = QSpinBox(self.FRI_Group)
        self.FRI_Interval.setObjectName(u"FRI_Interval")
        self.FRI_Interval.setGeometry(QRect(120, 50, 51, 22))
        self.FRI_Interval.setFont(font2)
        self.FRI_Interval.setMaximum(300)
        self.FRI_Ment_Button = QPushButton(self.FRI_Group)
        self.FRI_Ment_Button.setObjectName(u"FRI_Ment_Button")
        self.FRI_Ment_Button.setGeometry(QRect(10, 80, 91, 31))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        self.FRI_Ment_Button.setPalette(palette)
        self.FRI_Ment_Button.setFont(font2)
        self.FRI_Ment_Button.setStyleSheet(u"QPushButton {\n"
"	border-radius : 10px;\n"
"	border-color: rgb(0, 0, 0);\n"
"	border-style : inset;\n"
"	border-width : 1.2px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(245, 245, 245);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(230, 230, 230);\n"
"}")
        self.FRI_Start_Button = QPushButton(self.FRI_Group)
        self.FRI_Start_Button.setObjectName(u"FRI_Start_Button")
        self.FRI_Start_Button.setGeometry(QRect(110, 80, 151, 31))
        font3 = QFont()
        font3.setFamily(u"G\ub9c8\ucf13 \uc0b0\uc2a4 Medium")
        font3.setPointSize(11)
        self.FRI_Start_Button.setFont(font3)
        self.FRI_Start_Button.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(80, 80, 80);\n"
"	color: rgb(0, 0, 0);\n"
"	border-style:;\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(200, 200, 200);\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.COM_Group = QGroupBox(self.centralwidget)
        self.COM_Group.setObjectName(u"COM_Group")
        self.COM_Group.setEnabled(True)
        self.COM_Group.setGeometry(QRect(20, 230, 191, 131))
        self.COM_Group.setBaseSize(QSize(0, 0))
        self.COM_Group.setFont(font)
        self.COM_Group.setStyleSheet(u"")
        self.label_7 = QLabel(self.COM_Group)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 60, 101, 20))
        self.label_7.setFont(font1)
        self.label_8 = QLabel(self.COM_Group)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(130, 60, 21, 20))
        self.label_8.setFont(font1)
        self.COM_Interval = QSpinBox(self.COM_Group)
        self.COM_Interval.setObjectName(u"COM_Interval")
        self.COM_Interval.setGeometry(QRect(70, 60, 51, 22))
        self.COM_Interval.setFont(font2)
        self.COM_Interval.setMaximum(300)
        self.COM_Start_Button = QPushButton(self.COM_Group)
        self.COM_Start_Button.setObjectName(u"COM_Start_Button")
        self.COM_Start_Button.setGeometry(QRect(10, 90, 141, 31))
        self.COM_Start_Button.setFont(font3)
        self.COM_Start_Button.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(80, 80, 80);\n"
"	color: rgb(0, 0, 0);\n"
"	border-style:;\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(200, 200, 200);\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.label_6 = QLabel(self.COM_Group)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(150, 30, 21, 20))
        self.label_6.setFont(font1)
        self.label_5 = QLabel(self.COM_Group)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 30, 71, 20))
        self.label_5.setFont(font1)
        self.COM_Count = QSpinBox(self.COM_Group)
        self.COM_Count.setObjectName(u"COM_Count")
        self.COM_Count.setGeometry(QRect(90, 30, 51, 22))
        self.COM_Count.setFont(font2)
        self.COM_Count.setMinimum(1)
        self.COM_Count.setMaximum(150)
        MainWindow.setCentralWidget(self.centralwidget)
        self.BACKGROUND.raise_()
        self.LOGIN_Button.raise_()
        self.N_ID_Input.raise_()
        self.N_PW_Input.raise_()
        self.FRI_Group.raise_()
        self.COM_Group.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 321, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.LOGIN_Button.clicked.connect(MainWindow.start)
        self.COM_Start_Button.clicked.connect(MainWindow.auto_start)
        self.FRI_Start_Button.clicked.connect(MainWindow.fri_start)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\ub69d\ub531\ub9e8 \ub9e4\ud06c\ub85c", None))
        self.LOGIN_Button.setText(QCoreApplication.translate("MainWindow", u"\ub124\uc774\ubc84\n"
"\ub85c\uadf8\uc778", None))
        self.BACKGROUND.setText("")
        self.N_ID_Input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\uc544\uc774\ub514\ub97c \uc785\ub825\ud558\uc138\uc694", None))
        self.N_PW_Input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\ube44\ubc00\ubc88\ud638\ub97c \uc785\ub825\ud558\uc138\uc694", None))
        self.FRI_Group.setTitle(QCoreApplication.translate("MainWindow", u"\uc11c\ub85c\uc774\uc6c3 \ucd94\uac00", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\uc11c\uc774\ucd94 \ud69f\uc218", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\ubc88", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\uc11c\uc774\ucd94 \uc2dc\uac04 \uac04\uaca9", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\ucd08", None))
        self.FRI_Ment_Button.setText(QCoreApplication.translate("MainWindow", u"\uba58\ud2b8 \ud30c\uc77c", None))
        self.FRI_Start_Button.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.COM_Group.setTitle(QCoreApplication.translate("MainWindow", u"\uc624\ud1a0 \ub313\uae00, \uacf5\uac10", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\uc2dc\uac04 \uac04\uaca9", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\ucd08", None))
        self.COM_Start_Button.setText(QCoreApplication.translate("MainWindow", u"START", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\ubc88", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\ub9e4\ud06c\ub85c \ud69f\uc218", None))
    # retranslateUi

