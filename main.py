import sys
import os
import serial
import math
import folium
from PySide6.QtCore import Qt, QTimer, QUrl, QIODevice, Signal, Slot
from PySide6.QtGui import QColor, QPainter, QLinearGradient, QBrush, QFontDatabase
from PySide6.QtWidgets import QApplication, QMainWindow, QGraphicsDropShadowEffect, QProgressBar, QVBoxLayout, QComboBox, QMessageBox
from PySide6.QtSerialPort import QSerialPort, QSerialPortInfo
import threading
import numpy as np
import http.server
import socketserver

from ui_interface import Ui_MainWindow  # Ana uygulamanın UI'sı
from ui_splash_screen import Ui_SplashScreen  # Splash screen'in UI'sı

class SplashScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 120))
        self.ui.circularBg.setGraphicsEffect(self.shadow)
        self.counter = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(2)
        self.show()

    def progressBarValue(self, value, widget):
        progress = (100 - value) / 100.0
        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)
        styleSheet = f"""
        QFrame{{
            border-radius: 150px;
            background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{stop_1} rgba(255, 0, 127, 0), stop:{stop_2} rgba(85, 170, 255, 255));
        }}
        """
        widget.setStyleSheet(styleSheet)

    def progress(self):
        value = self.counter
        self.progressBarValue(value, self.ui.circularProgress)
        self.ui.labelPercentage.setText(f"<p><span style='font-size:68pt;'>{int(value)}</span><span style='font-size:58pt; vertical-align:super;'>%</span></p>")
        if value >= 100:
            self.timer.stop()
            self.main_window = MainWindow()  # Initialize the main window
            self.main_window.show()
            self.close()  # Close the splash screen
        self.counter += 0.3

class MainWindow(QMainWindow):
    dataReceived = Signal(float, float)  # xDegrees ve AccX için sinyal
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Enable Port
        self.init_serial_port()
        self.setup_buttons()

        # Progress Başlatma
        self.QProgressBar()

        # İki analog göstergenin özelleştirilmesi
        self.customize_analog_gauge()
        self.customize_analog_gauge_2()

        # Map Config
        self.start_http_server()
        self.triangle_route = self.create_triangle_route()
        self.current_index = 0

        # Timer ile koordinatları düzenli olarak güncelle
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_coords)
        self.timer.start(2000)  # 2 saniyede bir koordinatları güncelle

        # Data GUI Güncelleme
        self.dataReceived.connect(self.update_ui_with_data)

        # pushButton_5 tıklandığında self.on_calculate_button_clicked fonksiyonunu çağır
        self.ui.pushButton_5.clicked.connect(self.on_calculate_button_clicked)

    def init_serial_port(self):
        self.serial = QSerialPort()
        self.serial.setBaudRate(115200)
        self.ui.comL = QComboBox()  # Combobox'ı UI'a ekleyin
        self.portList = []
        ports = QSerialPortInfo.availablePorts()
        for port in ports:
            self.portList.append(port.portName())
        self.serial.readyRead.connect(self.read_serial_data)    

    @Slot(float, float)
    def update_ui_with_data(self, xDegrees, AccX):
        # ProgressBar değerini ayarla
        A = 50
        B = 100
        Xmin = -1
        Xmax = 0
        progressBarValue = A + ((AccX - Xmin) * (B - A) / (Xmax - Xmin))
        self.ui.progressBar.setValue(int(progressBarValue))

        # Derece etiketini ayarla
        # Derece, ProgressBar değerinin 50-100 arasındaki değerini 0°-90° arasına ölçeklemek için kullanılır
        degreeLabelValue = 0 + ((progressBarValue - 50) * (90 - 0) / (50))
        self.ui.label_2.setText(f"{degreeLabelValue:.0f}°")

        gaugeValue = 90 - xDegrees
        self.ui.widget_3.updateValue(gaugeValue)

    def read_serial_data(self):
        if self.serial.canReadLine():
            text = self.serial.readLine().data().decode().strip()
            if text.startswith("Current Angle:"):  # Sadece mevcut açıyı içeren satırları işle
                parts = text.split(':')
                try:
                    currentAngle = float(parts[1].strip())
                    self.ui.widget_3.updateValue(currentAngle)
                    #progressBarValue = self.map_value_to_range(currentAngle, 40, 45)
                    #╣self.ui.progressBar.setValue(int(progressBarValue))
                    # Gelen veriyi uygun şekilde işle
                    print(f"Current Angle from Arduino: {currentAngle}")
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
        self.progress_bar.setMinimum(50)
        self.progress_bar.setGeometry(50, 100, 50, 200)  # Genişliği 50 piksel olarak ayarlanmıştır.
        self.progress_bar.setMaximum(100)
        self.progress_bar.setValue(70)  # Örnek bir değer
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
	
    def paintEvent(self, event):
        painter = QPainter(self)
        gradient = QLinearGradient(0, 0, 0, self.height())
        gradient.setColorAt(0, QColor("#09203F"))
        gradient.setColorAt(1, QColor("#516395"))
        painter.fillRect(self.rect(), QBrush(gradient))

    def customize_analog_gauge(self):
        self.ui.widget.enableBarGraph = True
        self.ui.widget.units = "Km/h"
        self.ui.widget.minValue = 0
        self.ui.widget.maxValue = 20
        self.ui.widget.scalaCount = 10
        self.ui.widget.updateValue(self.ui.widget.minValue)
        self.ui.widget.setGaugeTheme(24)
        self.ui.widget.setBigScaleColor("white")
        self.ui.widget.setNeedleColor(255, 255, 255, 255)
        self.ui.widget.setScaleValueColor(250, 250, 250, 255)
        self.ui.widget.setDisplayValueColor(0, 246, 234, 244)
        QFontDatabase.addApplicationFont(os.path.join(os.path.dirname(__file__), 'fonts/DS-DIGIB.TTF'))
        self.ui.widget.setValueFontFamily("DS-Digital")
        self.ui.widget.setScaleFontFamily("Verdana")

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

    def start_http_server(self):
        port = 8000
        directory = os.path.dirname(os.path.abspath(__file__))
        os.chdir(directory)  # HTTP sunucusunun çalışacağı dizini ayarla
        handler = http.server.SimpleHTTPRequestHandler
        self.httpd = socketserver.TCPServer(("", port), handler)
        thread = threading.Thread(target=self.httpd.serve_forever)
        thread.daemon = True
        thread.start()

    def create_triangle_route(self):
            # Belirtilen üçgen rotayı oluştur
        point1 = [39.932312, 32.824375]  # İlk nokta
        point2 = [39.926383, 32.822291]  # İkinci nokta
        point3 = [39.926592, 32.828031]  # Üçüncü nokta

        # Üçgenin kenarları arasında koordinatları hesapla
        route = []
        route += self.interpolate_coords(point1, point2, steps=100)
        route += self.interpolate_coords(point2, point3, steps=100)
        route += self.interpolate_coords(point3, point1, steps=100)
        return route
    
    def interpolate_coords(self, start, end, steps):
        lats = np.linspace(start[0], end[0], steps)
        lons = np.linspace(start[1], end[1], steps)
        return list(zip(lats, lons))

    def initialize_map(self, coords):
        # Harita oluşturuluyor
        web_view = self.ui.widget_2
        mapbox_url = "https://api.mapbox.com/styles/v1/kutayoksuzz/clm6kss5200yr01r4fkao7vzq/tiles/256/{z}/{x}/{y}?access_token=pk.eyJ1Ijoia3V0YXlva3N1enoiLCJhIjoiY2xtNmVtZDc0MGJwcDNkbXZoOXFleDdrNiJ9.HwKLX08_1xUhK-nJI2X1HQ"
        m = folium.Map(location=coords, zoom_start=15,tiles='CartoDB dark_matter', attr='Map data © Mapbox')
        folium.Marker(coords, tooltip='Konum').add_to(m)
        map_file_path = 'map.html'
        m.save(map_file_path)
        port = 8000
        # Harita widget_2 üzerinden yükleniyor
        url = f'http://localhost:{port}/map.html'
        web_view.load(QUrl(url))

    def update_map(self, coords):
        self.initialize_map(coords)

    def update_coords(self):
        self.current_coords = self.triangle_route[self.current_index]
        self.current_index = (self.current_index + 1) % len(self.triangle_route)
        self.update_map(self.current_coords)

        # Kullanıcı tarafından girilen anten konumunu kontrol et ve açı hesapla
        if hasattr(self, 'antenna_coords'):
            angle = self.calculate_angle(self.antenna_coords, self.current_coords)
            y_coord = self.calculate_y_angle(self.antenna_coords, self.current_coords, self.antenna_h_coord)
            print(f"Angle: {angle:.2f}")  # Açıyı terminale yazdır
            print(f"Y Angle: {y_coord}")
            self.send_angle_to_arduino(angle, y_coord)  # Açıyı Arduino'ya gönder

    def send_angle_to_arduino(self, angle, y_coord):
        if self.serial.isOpen():
            # Açıyı string olarak gönderiyoruz
            self.serial.write(f"H:{angle}\n".encode())
            #self.serial.write(f"V:{y_coord}\n".encode())
            print(f"Sent Angle to Arduino: {angle}")

    @Slot()
    def on_calculate_button_clicked(self):
        try:
            x_coord = float(self.ui.lineEdit_3.text())
            y_coord = float(self.ui.lineEdit.text())
            h_coord = float(self.ui.lineEdit_2.text())

            self.antenna_coords = (x_coord, y_coord)
            self.antenna_h_coord = h_coord

            print(f"Antenna Coordinates: X={x_coord}, Y={y_coord}")
        except ValueError:
            print("Invalid input. Please enter numeric values for coordinates.")

    def calculate_angle(self, antenna_coords, uav_coords):
        dx = uav_coords[1] - antenna_coords[1]
        dy = uav_coords[0] - antenna_coords[0]
        angle = math.degrees(math.atan2(dx, dy))
        angle = (angle + 360) % 360  # Açıyı 0-360 aralığına getir
        return angle

    import math

    def calculate_y_angle(self, antenna_coords, current_coords, antenna_h_coord):
        # İki nokta arasındaki yatay mesafeyi hesapla
        horizontal_distance = math.sqrt((current_coords[0] - antenna_coords[0]) ** 2 + (current_coords[1] - antenna_coords[1]) ** 2) * 1000
        # Yükseklik farkını hesapla
        height_difference = antenna_h_coord  # Anten yüksekliği
        
        # Açıyı hesapla (radyan cinsinden)
        angle_radians = math.atan2(height_difference, horizontal_distance)

        # Açıyı dereceye çevir
        angle_degrees = math.degrees(angle_radians)
        
        return angle_degrees




if __name__ == '__main__':
    app = QApplication(sys.argv)
    splash_screen = SplashScreen()
    sys.exit(app.exec())
