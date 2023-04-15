from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QSize, Qt
from PyQt5 import uic, QtWidgets
import sys

class DaftarArtikel(QtWidgets.QMainWindow):
    def __init__(self):
        super(DaftarArtikel, self).__init__()
        uic.loadUi("daftarArtikel.ui", self)
        # nge read apa data x
        # for i in x:
            # self.createResep(nama, picture,)
        #self.layoutkosong = QtWidgets.QHBoxLayout()
        #self.window = QtWidgets.QWidget()
        self.headerLabel = QtWidgets.QLabel(self)
        self.headerLabel.setGeometry(0,0,1200,125)
        self.headerLabel.setStyleSheet("background-image: url('../img/header.png');")
        
        self.backButton = QtWidgets.QPushButton(self)
        self.backButton.setStyleSheet("border-image: url(../img/button_back.png);background-color:none;border: none")
        self.backButton.setIconSize(QSize(31, 31))
        self.backButton.setFixedSize(QSize(31, 31))
        self.backButton.move(52,38)
        
        self.titleLabel = QtWidgets.QLabel(self)
        self.titleLabel.setGeometry(70,102,320,70)
        self.titleLabel.setText("Daftar Artikel")
        self.titleLabel.setStyleSheet("font: 75 28pt;")
        
        self.scrollArtikel = QtWidgets.QWidget()    
        self.layoutScroll = QtWidgets.QVBoxLayout()    
        self.scrollArea.setWidget(self.scrollArtikel)
        self.scrollArea.verticalScrollBar().setStyleSheet("QScrollBar:vertical {background-color: #FDE7BD; border: none; border-radius: 15px; width: 8px; margin: 0px 0px 0px 0px;}\
                                                QScrollBar::handle:vertical {background-color: #EE9C20;border-radius: 15px; min-height: 20px;}\
                                                QScrollBar::add-line:vertical {border: none; background: none;}\
                                                QScrollBar::sub-line:vertical {border: none; background: none;}")

        
        self.counter = 0
        for i in range(4):
            self.createArtikel()
            
    def createArtikel(self):
        artikelLayout = QtWidgets.QHBoxLayout()
        artikelWidget = QtWidgets.QWidget()
        artikelWidget.setFixedSize(1000,250)
        artikelWidget.setStyleSheet("background-color: #FDE7BD;border-radius: 15px;")
        
        horizontalBox = QtWidgets.QHBoxLayout()
        
        image_artikel = QtWidgets.QPushButton()
        image_artikel.setIcon(QIcon(QPixmap("../img/ayamgoreng.jpg")))
        image_artikel.setIconSize(QSize(300,220))
        image_artikel.setStyleSheet("background-color: #EE9C20;")
        horizontalBox.addWidget(image_artikel)
        
        verticalWidget = QtWidgets.QWidget()
        verticalBox = QtWidgets.QVBoxLayout()
        label_judul = QtWidgets.QLabel()
        label_judul.setText("Judul Artikel Keren Banget Deh Pokoknya")
        label_judul.setWordWrap(True)
        label_judul.setStyleSheet("font: 75 20pt;")
        verticalBox.addWidget(label_judul)
        
        label_tanggal = QtWidgets.QLabel()
        label_tanggal.setText("XX April 20XX")
        label_tanggal.setStyleSheet("font: 75 10pt;")
        verticalBox.addWidget(label_tanggal)
        
        label_preview = QtWidgets.QLabel()
        label_preview.setText("Lorem ipsum dolor sit amet ya ini contoh preview artikel aja sih, jadi nanti bakal ada preview isi artikelnya di sini gitu.... apa lagi ya. pokoknya gitu aja")
        label_preview.setWordWrap(True)
        label_preview.setStyleSheet("font: 75 11pt;")
        verticalBox.addWidget(label_preview)
        verticalWidget.setLayout(verticalBox)
        
        horizontalBox.addWidget(verticalWidget)
        artikelWidget.setLayout(horizontalBox)
        artikelLayout.addWidget(artikelWidget)
        
        self.layoutScroll.insertLayout(self.counter, artikelLayout)
        self.scrollArtikel.setLayout(self.layoutScroll)
        self.counter += 1
    
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    DaftarArtikel = DaftarArtikel()
    DaftarArtikel.show()
    sys.exit(app.exec_())
