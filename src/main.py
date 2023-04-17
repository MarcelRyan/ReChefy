from PyQt5.QtWidgets import *
from PyQt5 import uic, QtWidgets
import sys
import menu
import welcomePage

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.pages = QtWidgets.QStackedWidget()
        self.pages.setFixedHeight(850)
        self.pages.setFixedWidth(1200)
        self.setCentralWidget(self.pages)

        self.WelcomePage = welcomePage.WelcomePage(self)
        self.pages.addWidget(self.WelcomePage)
        
        self.Menu = menu.Menu(self)
        self.pages.addWidget(self.Menu)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())
