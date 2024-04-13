import sys
import os
import folium
from PySide6.QtCore import Qt, QTimer, QUrl
from PySide6.QtGui import QColor, QPainter, QLinearGradient, QBrush, QFontDatabase
from PySide6.QtWidgets import QApplication, QMainWindow, QGraphicsDropShadowEffect

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
        self.timer.start(15)
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
            self.main_window = MainWindow()  # mainWindow ekranı başlat
            self.main_window.show()
            self.close()  # Splash Ekranını kapat
        self.counter += 5

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.customize_analog_gauge()
        self.initialize_map()

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

    def initialize_map(self):
        web_view = self.ui.widget_2
        ankara_coords = (39.9334, 32.8597)
        m = folium.Map(location=ankara_coords, tiles='CartoDB dark_matter', zoom_start=15)
        folium.Marker(ankara_coords, popup='Ankara, Türkiye\'nin başkenti!', tooltip='Tıkla daha fazla bilgi için!').add_to(m)
        map_file_path = os.path.abspath('map.html')
        m.save(map_file_path)
        port = 8000
        os.system(f"start cmd /c python -m http.server {port}")
        url = f'http://localhost:{port}/map.html'
        web_view.load(QUrl(url))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    splash_screen = SplashScreen()
    sys.exit(app.exec())
