from database import database_func
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtWidgets, QtCore, QtGui

class lihatArtikel(QMainWindow) :
    def __init__(self) :
        super(lihatArtikel, self).__init__()
        uic.loadUi("src/lihatArtikel.ui", self)
         
        self.setStyleSheet("background-color: #FDE7BD;")
        self.show()

        self.file = r".\src\database\rechefy.db"
        self.connection = database_func.connectToDatabase(self.file)
        self.artikel = database_func.getArtikel(self.connection, 1)
        self.artikelFoto = database_func.resepBlobToImage(self.connection, 1)

        self.fotoArtikel.setPixmap(QtGui.QPixmap(self.artikelFoto))
        self.namaArtikel.setText(str(self.artikel[2]))
        self.textEdit.setText(str(self.artikel[3]))
        self.tanggal.setText(str(self.artikel[4]))


        self.setFixedWidth(1200)
        self.setFixedHeight(850)

def main() :
    app = QApplication([])
    window = lihatArtikel()
    app.exec_()



if __name__== '__main__' :
    main ()