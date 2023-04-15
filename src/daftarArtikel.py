from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QSize, Qt
from PyQt5 import uic, QtWidgets, QtGui
import sys
from database import database_func

class DaftarArtikel(QtWidgets.QMainWindow):
    def __init__(self):
        super(DaftarArtikel, self).__init__()
        uic.loadUi(r".\src\daftarArtikel.ui", self)
        
        # load database
        file = r".\src\database\rechefy.db"
        connection = database_func.connectToDatabase(file)
        database_func.initializeTable(connection)

        self.headerLabel = QtWidgets.QLabel(self)
        self.headerLabel.setGeometry(0,0,1200,125)
        self.headerLabel.setStyleSheet("background-image: url('images/icon/header.png');")
        
        self.backButton = QtWidgets.QPushButton(self)
        self.backButton.setStyleSheet("border-image: url(images/icon/button_back.png);background-color:none;border: none")
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
        
        # load daftar artikel
        dataArtikel = database_func.getDaftarArtikel(connection)
        self.counter = 0
        self.loadArtikel(connection, dataArtikel)
    
    def loadArtikel(self, connection, dataArtikel):
        for idx in range (len(dataArtikel)):
            self.createArtikel(connection, dataArtikel[idx])
    
    def createArtikel(self, connection, artikel):
        artikelLayout = QtWidgets.QHBoxLayout()
        artikelWidget = QtWidgets.QWidget()
        artikelWidget.setFixedSize(1000,260)
        artikelWidget.setStyleSheet("background-color: #FDE7BD;border-radius: 15px;")
        
        horizontalBox = QtWidgets.QHBoxLayout()
        
        image_artikel = QtWidgets.QLabel()
        image_artikel.setFixedSize(470,230)
        gambar = database_func.artikelBlobToImage(connection, artikel[0])
        pixmap = QPixmap(gambar)
        pixmap = pixmap.scaled(image_artikel.width(), image_artikel.height()) # scale the pixmap to the size of the label
        image_artikel.setPixmap(pixmap)
        image_artikel.setPixmap(QPixmap(gambar))
        image_artikel.setScaledContents(True)
        image_artikel.setStyleSheet("background-color: #EE9C20;border-radius: 15px;")
        horizontalBox.addWidget(image_artikel)
        
        verticalWidget = QtWidgets.QWidget()
        verticalBox = QtWidgets.QVBoxLayout()
        label_judul = QtWidgets.QLabel(artikel[2])
        #label_judul.setFixedSize(470,150)
        label_judul.setFixedWidth(470)
        label_judul.setAlignment(Qt.AlignTop)
        self.writeLabelLimited(label_judul)
        label_judul.setWordWrap(True)
        label_judul.setStyleSheet("font: 75 18pt;")
        verticalBox.addWidget(label_judul)
        
        label_tanggal = QtWidgets.QLabel()
        label_tanggal.setText(artikel[4])
        label_tanggal.setStyleSheet("font: 75 10pt;")
        verticalBox.addWidget(label_tanggal)
        
        label_preview = QtWidgets.QLabel(artikel[3])
        self.writeLabelLimited(label_preview)
        #label_preview.setElideMode(Qt.ElidedRight)
        label_preview.setMaximumWidth(400)
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
    
    def writeLabelLimited(self, label):
        text = label.text()
        elided_text = label.fontMetrics().elidedText(text, Qt.ElideRight, label.width())
        #if elided_text != text:
        #    elided_text += "..."
        label.setText(elided_text)
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    DaftarArtikel = DaftarArtikel()
    DaftarArtikel.show()
    sys.exit(app.exec_())
