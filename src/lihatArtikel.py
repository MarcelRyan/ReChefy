from database import databaseFunc
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt
import fontLoader

class LihatArtikel(QMainWindow) :
    def __init__(self, parent) :
        super(LihatArtikel, self).__init__()
        uic.loadUi("lihatArtikel.ui", self)
        self.parent = parent
        self.idArtikel = 1
        self.setStyleSheet("background-color: #FDE7BD;")
        self.backButton.clicked.connect(self.goBack)
        self.homeButton.clicked.connect(self.goHome)

        self.setFixedWidth(1200)
        self.setFixedHeight(850)

    def readDatabase(self):
        self.file = r".\database\rechefy.db"
        self.connection = databaseFunc.connectToDatabase(self.file)
        self.artikel = databaseFunc.getArtikel(self.connection,self.idArtikel)
        self.artikelFoto = databaseFunc.artikelBlobToImage(self.connection, self.idArtikel)
        self.fotoArtikel.setPixmap(QtGui.QPixmap(self.artikelFoto))
        self.namaArtikel.setText(str(self.artikel[2]))
        self.namaArtikel.setFont(fontLoader.load_custom_font('../font/Nunito-ExtraBold.ttf'))
        self.namaArtikel.adjustSize()
        self.textEdit.setText(str(self.artikel[3]))
        self.textEdit.setFont(fontLoader.load_custom_font('../font/Nunito-Medium.ttf'))
        self.tanggal.setText(str(self.artikel[4]))
        self.tanggal.setFont(fontLoader.load_custom_font('../font/Nunito-Regular.ttf'))
        self.x = self.textEdit.width()
        self.y = self.textEdit.height()
        self.textEdit.setFixedWidth(1031)
        self.textEdit.setAlignment(Qt.AlignJustify)
        self.widget.setFixedWidth(1154)
        self.textEdit.adjustSize()
        self.x1 = self.textEdit.width()
        self.y1 = self.textEdit.height()
        self.deltax = abs(self.x1 - self.x)
        self.deltay = abs(self.y1 - self.y)
        self.widget.setMinimumSize(QtCore.QSize(1154, 500+self.deltay))
        
    def goBack(self):
        self.textEdit.resize(self.x, self.y)
        self.widget.setMinimumSize(QtCore.QSize(1154, 500))
        self.parent.pages.setCurrentWidget(self.parent.DaftarArtikel)

    def goHome(self):
        self.textEdit.resize(self.x, self.y)
        self.widget.setMinimumSize(QtCore.QSize(1154, 500))
        self.parent.pages.setCurrentWidget(self.parent.WelcomePage)

def main() :
    app = QApplication([])
    window = LihatArtikel()
    app.exec_()


if __name__== '__main__' :
    main ()