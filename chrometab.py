import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QUrl
import subprocess

def run_oled_code():
    oled_script_path = r"OLED_Module_Code/OLED_Module_Code/RaspberryPi/python/example/OLED_1in51_search_test.py"
    subprocess.run(["python", oled_script_path])

run_oled_code()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Calculate window size
        screen_width = QApplication.desktop().screenGeometry().width()
        window_width = int(0.8 * screen_width)
        window_height = int(window_width / 2)

        # Set window dimensions
        self.setGeometry(0, 0, window_width, window_height)

        # Create button
        self.button = QPushButton('Toggle', self)
        self.button.setGeometry(10, 10, int(window_width*.1), int(window_height*.07))
        self.button.setCheckable(True)
        self.button.setChecked(True)  # Set initially checked
        self.button.clicked.connect(self.toggle)

        chrome_tab_height = int(window_height * 0.9)
        chrome_tab_width = int(window_width * 0.85)

        # Create web engine view
        self.web_view = QWebEngineView(self)
        self.web_view.setGeometry(window_width - int(chrome_tab_width*1.03), window_height - chrome_tab_height - 10, chrome_tab_width, chrome_tab_height)
        self.web_view.setUrl(QUrl("https://www.google.com"))  # Example URL


    def toggle(self):
        if self.button.isChecked():
            self.web_view.show()
            run_oled_code()
        else:
            self.web_view.hide()
            run_oled_code()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
