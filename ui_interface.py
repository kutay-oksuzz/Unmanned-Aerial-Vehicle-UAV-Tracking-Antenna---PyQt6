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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QProgressBar, QPushButton,
    QSizePolicy, QWidget)

from Custom_Widgets.AnalogGaugeWidget import AnalogGaugeWidget
from Custom_Widgets.QCustomQPushButton import QCustomQPushButton

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1756, 908)
        font = QFont()
        font.setPointSize(8)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QCustomQPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(220, 380, 81, 61))
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
        self.widget_2.setGeometry(QRect(940, 110, 751, 591))
        self.pushButton_2 = QCustomQPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(300, 450, 81, 61))
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
        self.pushButton_3.setGeometry(QRect(220, 520, 81, 61))
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
        self.pushButton_4.setGeometry(QRect(140, 450, 81, 61))
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
        self.label_13.setGeometry(QRect(160, 600, 201, 40))
        self.label_13.setMaximumSize(QSize(600, 40))
        font2 = QFont()
        font2.setFamilies([u"Roboto Light"])
        font2.setPointSize(9)
        font2.setBold(True)
        self.label_13.setFont(font2)
        self.label_13.setStyleSheet(u"color: rgb(220, 220, 220);\n"
"background-color: rgb(98, 98, 162);\n"
"border-radius: 20px;")
        self.label_13.setAlignment(Qt.AlignCenter)
        self.widget_3 = AnalogGaugeWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(40, 50, 431, 331))
        self.progressBar = QProgressBar(self.widget_3)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(0, 0, 16, 171))
        font3 = QFont()
        font3.setPointSize(1)
        self.progressBar.setFont(font3)
        self.progressBar.setStyleSheet(u"")
        self.progressBar.setMaximum(100)
        self.progressBar.setValue(0)
        self.progressBar.setOrientation(Qt.Vertical)
        self.line = QFrame(self.widget_3)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(-40, 80, 61, 16))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.label = QLabel(self.widget_3)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 80, 31, 16))
        font4 = QFont()
        font4.setPointSize(10)
        font4.setBold(True)
        font4.setItalic(True)
        self.label.setFont(font4)
        self.label.setStyleSheet(u"color: rgb(220, 220, 220);")
        self.closeB = QPushButton(self.centralwidget)
        self.closeB.setObjectName(u"closeB")
        self.closeB.setGeometry(QRect(100, 790, 61, 61))
        font5 = QFont()
        font5.setPointSize(11)
        font5.setBold(True)
        self.closeB.setFont(font5)
        self.closeB.setStyleSheet(u"QPushButton#closeB{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton#closeB:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 256));\n"
"}\n"
"QPushButton#closeB:pressed{\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	background-color:rgba(105, 118, 132, 200);\n"
"}")
        self.openB = QPushButton(self.centralwidget)
        self.openB.setObjectName(u"openB")
        self.openB.setGeometry(QRect(30, 790, 61, 61))
        self.openB.setFont(font5)
        self.openB.setStyleSheet(u"QPushButton#openB{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton#openB:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 256));\n"
"}\n"
"QPushButton#openB:pressed{\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	background-color:rgba(105, 118, 132, 200);\n"
"}")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 20, 41, 16))
        font6 = QFont()
        font6.setPointSize(12)
        font6.setBold(True)
        self.label_2.setFont(font6)
        self.label_2.setStyleSheet(u"color:rgb(2, 207, 196);")
        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(1290, 720, 141, 40))
        self.label_14.setMaximumSize(QSize(600, 40))
        font7 = QFont()
        font7.setFamilies([u"Roboto Light"])
        font7.setPointSize(9)
        font7.setBold(True)
        font7.setItalic(False)
        font7.setUnderline(False)
        font7.setStrikeOut(False)
        self.label_14.setFont(font7)
        self.label_14.setStyleSheet(u"color: rgb(220, 220, 220);\n"
"background-color: rgb(98, 98, 162);\n"
"border-radius: 20px;")
        self.label_14.setAlignment(Qt.AlignCenter)
        self.widget = AnalogGaugeWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(600, 10, 301, 271))
        self.widget.setStyleSheet(u"background-color: transparent;")
        self.label_15 = QLabel(self.centralwidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(680, 290, 141, 40))
        self.label_15.setMaximumSize(QSize(600, 40))
        self.label_15.setFont(font7)
        self.label_15.setStyleSheet(u"color: rgb(220, 220, 220);\n"
"background-color: rgb(98, 98, 162);\n"
"border-radius: 20px;")
        self.label_15.setAlignment(Qt.AlignCenter)
        self.widget_4 = QWidget(self.centralwidget)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(570, 350, 370, 480))
        self.widget_4.setStyleSheet(u"QPushButton#pushButton{	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton#pushButton:hover{	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
"}\n"
"QPushButton#pushButton:pressed{	\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	background-color:rgba(105, 118, 132, 200);\n"
"}\n"
"\n"
"QPushButton#pushButton_2, #pushButton_3, #pushButton_4, #pushButton_5{	\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	color:rgba(85, 98, 112, 255);\n"
"}\n"
"QPushButton#pushButton_2:hover, #pushButton_3:hover, #pushButton_4:hover, #pushButton_5:hover{	\n"
"	color:rgba(155, 168, 182, 220);\n"
"}\n"
"QPushButton#pushButton_2:pressed, #pushButton_3:pressed, #pushButton_4:pressed, #pushButton_5:pressed{	\n"
"	padding-left:5px;\n"
"	padding-top:5px;"
                        "\n"
"	color:rgba(115, 128, 142, 255);\n"
"}")
        self.label_3 = QLabel(self.widget_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 30, 300, 420))
        self.label_3.setStyleSheet(u"border-image: url(:/images/background.png);\n"
"border-radius:20px;")
        self.label_4 = QLabel(self.widget_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 30, 300, 420))
        self.label_4.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:0.715909, stop:0 rgba(0, 0, 0, 9), stop:0.375 rgba(0, 0, 0, 50), stop:0.835227 rgba(0, 0, 0, 75));\n"
"border-radius:20px;")
        self.label_5 = QLabel(self.widget_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(40, 60, 280, 390))
        self.label_5.setStyleSheet(u"background-color:rgba(0, 0, 0, 100);\n"
"border-radius:15px;")
        self.label_6 = QLabel(self.widget_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(110, 80, 151, 40))
        font8 = QFont()
        font8.setPointSize(20)
        font8.setBold(True)
        self.label_6.setFont(font8)
        self.label_6.setStyleSheet(u"color:rgba(255, 255, 255, 210);")
        self.lineEdit = QLineEdit(self.widget_4)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(80, 200, 200, 40))
        font9 = QFont()
        font9.setPointSize(12)
        font9.setBold(True)
        font9.setItalic(False)
        font9.setStrikeOut(False)
        self.lineEdit.setFont(font9)
        self.lineEdit.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105, 118, 132, 255);\n"
"color:rgba(255, 255, 255, 230);\n"
"padding-bottom:7px;")
        self.pushButton_5 = QPushButton(self.widget_4)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(80, 310, 200, 40))
        self.pushButton_5.setFont(font6)
        self.pushButton_5.setStyleSheet(u"QPushButton#pushButton_5{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton#pushButton_5:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
"}\n"
"QPushButton#pushButton_5:pressed{\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	background-color:rgba(105, 118, 132, 200);\n"
"}")
        self.horizontalLayoutWidget = QWidget(self.widget_4)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(110, 370, 141, 32))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_6 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMaximumSize(QSize(30, 30))
        font10 = QFont()
        font10.setFamilies([u"Social Media Circled"])
        font10.setPointSize(15)
        self.pushButton_6.setFont(font10)

        self.horizontalLayout.addWidget(self.pushButton_6)

        self.pushButton_7 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMaximumSize(QSize(30, 30))
        self.pushButton_7.setFont(font10)

        self.horizontalLayout.addWidget(self.pushButton_7)

        self.pushButton_8 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMaximumSize(QSize(30, 30))
        self.pushButton_8.setFont(font10)

        self.horizontalLayout.addWidget(self.pushButton_8)

        self.lineEdit_3 = QLineEdit(self.widget_4)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(80, 150, 200, 40))
        self.lineEdit_3.setFont(font6)
        self.lineEdit_3.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105, 118, 132, 255);\n"
"color:rgba(255, 255, 255, 230);\n"
"padding-bottom:7px;")
        self.lineEdit_2 = QLineEdit(self.widget_4)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(80, 250, 200, 40))
        self.lineEdit_2.setFont(font9)
        self.lineEdit_2.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105, 118, 132, 255);\n"
"color:rgba(255, 255, 255, 230);\n"
"padding-bottom:7px;")
        self.label_16 = QLabel(self.centralwidget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(650, 820, 201, 40))
        self.label_16.setMaximumSize(QSize(600, 40))
        self.label_16.setFont(font2)
        self.label_16.setStyleSheet(u"color: rgb(220, 220, 220);\n"
"background-color: rgb(98, 98, 162);\n"
"border-radius: 20px;")
        self.label_16.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"ANTENNA CONTROL", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"0 \u00b0", None))
        self.closeB.setText(QCoreApplication.translate("MainWindow", u"CLOSE", None))
        self.openB.setText(QCoreApplication.translate("MainWindow", u"OPEN", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"0\u00b0", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"UAV MAP", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"UAV SPEED", None))
        self.label_3.setText("")
        self.label_4.setText("")
        self.label_5.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Coordinate", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"CALCULATE", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"T", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"S", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"X", None))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"H", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"CALCULATE ROUTE", None))
    # retranslateUi

