from PyQt5.QtWidgets import *
from PyQt5 import uic, QtWidgets
import sys

class Menu(QtWidgets.QMainWindow):
    
    def __init__(self, main_window):
        super(Menu, self).__init__()
        uic.loadUi("src/menu.ui", self)
        self.main_window = main_window
        self.setFixedWidth(1200)
        self.setFixedHeight(850)
        self.resepButton.clicked.connect(self.gotoResep)
        self.artikelButton.clicked.connect(self.gotoArtikel)

    def gotoArtikel(self):
        self.main_window.pages.setCurrentWidget(self.main_window.WelcomePage)

    def gotoResep(self):
        self.main_window.pages.setCurrentWidget(self.main_window.WelcomePage)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    menu = Menu()
    menu.show()
    sys.exit(app.exec_())