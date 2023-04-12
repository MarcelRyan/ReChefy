from PyQt5.QtWidgets import *
from PyQt5 import uic, QtWidgets
import sys

class WelcomePage(QtWidgets.QMainWindow):
    
    def __init__(self, main_window):
        super(WelcomePage, self).__init__()
        uic.loadUi("src/welcomePage.ui", self)
        self.main_window = main_window
        self.setFixedHeight(850)
        self.setFixedWidth(1200)

    def mousePressEvent(self, event):
        self.main_window.pages.setCurrentWidget(self.main_window.Menu)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    welcomePage = WelcomePage()
    welcomePage.show()
    sys.exit(app.exec_())