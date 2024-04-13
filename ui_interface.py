# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
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
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QSizePolicy,
    QWidget)

from Custom_Widgets.AnalogGaugeWidget import AnalogGaugeWidget
from Custom_Widgets.QCustomQPushButton import QCustomQPushButton

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1121, 761)
        font = QFont()
        font.setPointSize(8)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = AnalogGaugeWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 20, 431, 361))
        self.pushButton = QCustomQPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(210, 440, 81, 61))
        self.pushButton.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setPointSize(16)
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"QPushButton#pushButton{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton#pushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 256));\n"
"}\n"
"QPushButton#pushButton:pressed{\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	background-color:rgba(105, 118, 132, 200);\n"
"}")
        icon = QIcon()
        icon.addFile(u"../../../Downloads/caret-up-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(60, 50))
        self.widget_2 = QWebEngineView(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(480, 20, 631, 671))
        self.pushButton_2 = QCustomQPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(290, 510, 81, 61))
        self.pushButton_2.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setStyleSheet(u"QPushButton#pushButton_2{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton#pushButton_2:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 256));\n"
"}\n"
"QPushButton#pushButton_2:pressed{\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	background-color:rgba(105, 118, 132, 200);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"../../../Downloads/caret-right-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QSize(60, 50))
        self.pushButton_3 = QCustomQPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(210, 580, 81, 61))
        self.pushButton_3.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_3.setFont(font1)
        self.pushButton_3.setStyleSheet(u"QPushButton#pushButton_3{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton#pushButton_3:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 256));\n"
"}\n"
"QPushButton#pushButton_3:pressed{\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	background-color:rgba(105, 118, 132, 200);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"../../../Downloads/caret-down-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QSize(60, 50))
        self.pushButton_4 = QCustomQPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(130, 510, 81, 61))
        self.pushButton_4.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_4.setFont(font1)
        self.pushButton_4.setStyleSheet(u"QPushButton#pushButton_4{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton#pushButton_4:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 256));\n"
"}\n"
"QPushButton#pushButton_4:pressed{\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	background-color:rgba(105, 118, 132, 200);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"../../../Downloads/caret-left-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QSize(60, 50))
        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(260, 710, 582, 40))
        self.label_13.setMaximumSize(QSize(600, 40))
        font2 = QFont()
        font2.setFamilies([u"Roboto Light"])
        font2.setPointSize(14)
        self.label_13.setFont(font2)
        self.label_13.setStyleSheet(u"color: rgb(220, 220, 220);\n"
"background-color: rgb(98, 98, 162);\n"
"border-radius: 20px;")
        self.label_13.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.pushButton.raise_()
        self.widget.raise_()
        self.widget_2.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.label_13.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\"If you control the code, you control the world.\"", None))
    # retranslateUi

