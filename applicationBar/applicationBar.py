import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class ApplicationBar(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Application Bar")
        self.setGeometry(200, 200, 800, 400)

        button = QPushButton("Launch App", self)
        button.setGeometry(350, 180, 100, 40)
        button.clicked.connect(self.launch_app)

    def launch_app(self):
        print("Launching Application...")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = ApplicationBar()
    main_window.show()
    sys.exit(app.exec_())