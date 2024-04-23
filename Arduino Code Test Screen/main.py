import sys
import os
import folium
from PySide6.QtCore import Qt, QTimer, QUrl, QIODevice, Signal, Slot
from PySide6.QtGui import QColor, QPainter, QLinearGradient, QBrush, QFontDatabase
from PySide6.QtWidgets import QApplication, QMainWindow, QGraphicsDropShadowEffect, QProgressBar, QVBoxLayout, QSlider, QPushButton, QComboBox, QMessageBox
from PySide6.QtSerialPort import QSerialPort, QSerialPortInfo
from collections import deque
import numpy as np

from ui_interface import Ui_MainWindow  # Ana uygulamanın UI'sı
from ui_splash_screen import Ui_SplashScreen  # Splash screen'in UI'sı

class MainWindow(QMainWindow):
    dataReceived = Signal(float, float)  # xDegrees ve AccX için sinyal
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.init_serial_port()
        self.setup_buttons()
        self.QProgressBar()
        self.customize_analog_gauge_2()

        self.dataReceived.connect(self.update_ui_with_data)

        # Veri düzleştirme için değişkenler
        self.xDegrees_history = deque(maxlen=5)
        self.AccX_history = deque(maxlen=5)

    def init_serial_port(self):
        self.serial = QSerialPort()
        self.serial.setBaudRate(115200)
        self.ui.comL = QComboBox()
        self.portList = []
        ports = QSerialPortInfo.availablePorts()
        for port in ports:
            self.portList.append(port.portName())
        self.serial.readyRead.connect(self.read_serial_data)

    @Slot(float, float)
    def update_ui_with_data(self, xDegrees, AccX):
        # Veri geçmişine yeni değerleri ekle
        self.xDegrees_history.append(xDegrees)
        self.AccX_history.append(AccX)

        # Hareketli ortalama hesapla
        avg_xDegrees = np.mean(self.xDegrees_history)
        avg_AccX = np.mean(self.AccX_history)

        # GUI'de gösterilecek değerleri hesapla
        A = 50
        B = 100
        Xmin = -1
        Xmax = 0
        progressBarValue = A + ((avg_AccX - Xmin) * (B - A) / (Xmax - Xmin))
        self.ui.progressBar.setValue(int(progressBarValue))

        degreeLabelValue = 0 + ((progressBarValue - 50) * (90 - 0) / (50))
        self.ui.label_2.setText(f"{degreeLabelValue:.0f}°")

        gaugeValue = 90 - avg_xDegrees
        self.ui.widget_3.updateValue(gaugeValue)

    def read_serial_data(self):
        if self.serial.canReadLine():
            text = self.serial.readLine().data().decode().strip()
            parts = text.split(',')
            try:
                xDegrees = float(parts[0])
                AccX = float(parts[1])
                self.dataReceived.emit(xDegrees, AccX)
            except (IndexError, ValueError) as e:
                print(f"Error parsing data: {e}")  


    def setup_buttons(self):
        self.ui.openB.clicked.connect(self.onOpen)
        self.ui.closeB.clicked.connect(self.onClose)

        # Seri port işlemleri için sinyalleri bağla
        self.ui.pushButton_2.clicked.connect(lambda: self.send_command("right"))
        self.ui.pushButton_4.clicked.connect(lambda: self.send_command("left"))

    def onOpen(self):
        try:
            print(self.portList[0])
            self.serial.setPortName(self.portList[0])
            if not self.serial.open(QIODevice.OpenModeFlag.ReadWrite):
                raise Exception("Port could not be opened!")
            print("Port opened:", self.portList[0])
        except Exception as e:
            print(f"Failed to open port: {e}")
            QMessageBox.critical(self, "Serial Port Error", f"An error occurred: {str(e)}")

    def onClose(self):
        if self.serial.isOpen():
            self.serial.close()
            print("Port closed")

    def send_command(self, command):
        if self.serial.isOpen():
            self.serial.write(command.encode())
            print(f"Sent: {command}")
        else:
            print("Serial port not open")




    def QProgressBar(self):
        self.layout = QVBoxLayout()
        self.progress_bar = QProgressBar()
        self.progress_bar.setOrientation(Qt.Vertical)  # Dikey yönlendirme
        self.progress_bar.setMinimum(0)
        self.progress_bar.setGeometry(50, 100, 50, 200)  # Genişliği 50 piksel olarak ayarlanmıştır.
        self.progress_bar.setMaximum(100)
        self.progress_bar.setValue(50)  # Örnek bir değer
        self.progress_bar.setTextVisible(True)
        self.progress_bar.setStyleSheet("""
           QProgressBar {
                border: 2px solid grey;
                border-radius: 5px;
        background-color: #FFFFFF;
    }
             QProgressBar::chunk {
        background-color: #05B8CC;
        margin: 0px; 
        """)
        self.layout.addWidget(self.progress_bar)
        self.setLayout(self.layout)


    # Background Color Setup
    def paintEvent(self, event):
        painter = QPainter(self)
        gradient = QLinearGradient(0, 0, 0, self.height())
        gradient.setColorAt(0, QColor("#09203F"))
        gradient.setColorAt(1, QColor("#516395"))
        painter.fillRect(self.rect(), QBrush(gradient))
        
    # Anten Analog Setup
    def customize_analog_gauge_2(self):
        self.ui.widget_3.enableBarGraph = True
        self.ui.widget_3.setGaugeTheme(17)
        self.ui.widget_3.units = ""
        self.ui.widget_3.minValue = 0
        self.ui.widget_3.maxValue = 180
        self.ui.widget_3.scalaCount = 2 
        self.ui.widget_3.setBigScaleColor("white")
        self.ui.widget_3.setNeedleColor(255, 255, 255, 255)
        self.ui.widget_3.setScaleValueColor(250, 250, 250, 255)
        self.ui.widget_3.setDisplayValueColor(0, 246, 234, 244)
        self.ui.widget_3.setScaleFontFamily("Verdana")
        self.ui.widget_3.setScaleStartAngle(180)
        self.ui.widget_3.setTotalScaleAngleSize(180)
        self.ui.widget_3.setNeedleCenterColor(
            color1 = "#00516395",  # Orta Yuvarlak Saydam olarak ayarlama
            color2 = "#0009203f",
            color3 = "#00000000",
            color4 = "#00FFFFFF"
        )
        self.ui.widget_3.setOuterCircleColor(
            color1 = "#00516395",  # Orta background Saydam olarak ayarlama
            color2 = "#0009203f",
            color3 = "#00000000",
            color4 = "#00FFFFFF"
        )


# Programı Başlatma
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()  # mainWindow ekranı başlat
    main_window.show()
    sys.exit(app.exec())
