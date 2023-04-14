from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QSize, Qt
from PyQt5 import uic, QtWidgets
import sys

class DaftarResep(QtWidgets.QMainWindow):

    def __init__(self):
        super(DaftarResep, self).__init__()
        uic.loadUi("daftarResep.ui", self)
        # nge read apa data x
        # for i in x:
            # self.createResep(nama, picture,)
        #self.layoutkosong = QtWidgets.QHBoxLayout()
        self.headerLabel = QtWidgets.QLabel(self)
        self.headerLabel.setGeometry(0,0,1200,125)
        self.headerLabel.setStyleSheet("background-image: url('../img/header.png');")
        
        self.titleLabel = QtWidgets.QLabel(self)
        self.titleLabel.setGeometry(70,102,320,70)
        self.titleLabel.setText("Daftar Resep")
        self.titleLabel.setStyleSheet("font: 75 28pt;")
        
        self.buttonAddResep = QtWidgets.QPushButton()
        #self.buttonAddResep.setIcon(QIcon(QPixmap("../img/button_addResep.png")))
        self.buttonAddResep.setStyleSheet("border-image: url(:/newPrefix/button_addResep.png);background-color:none;border: none")
        self.buttonAddResep.setIconSize(QSize(170, 170))
        self.buttonAddResep.setFixedSize(QSize(170, 170))
        #self.buttonAddResep.setScaledContents(True)
        self.buttonAddResep.move(1020,620)
        
        self.scrollResep = QtWidgets.QWidget()    
        self.gridLayoutResep = QtWidgets.QGridLayout()
        #self.gridLayoutResep.setContentsMargins(10,30,10,30)
        self.gridLayoutResep.setVerticalSpacing(30)
        self.scrollArea.setWidget(self.scrollResep)
        #self.counter = 0
        for i in range(21):
            self.createResep(i)
            
        
        self.buttonAddResep.raise_()
        
            
    def createResep(self, idx):
        resepWidget = QtWidgets.QWidget()       
        resepWidget.setFixedSize(230,280)
        resepWidget.setStyleSheet("background-color: #FDE7BD;border-radius: 15px;")
        
        verticalResep = QtWidgets.QVBoxLayout()
        
        imageWidget = QtWidgets.QWidget()
        imageLayout = QtWidgets.QVBoxLayout()
        imageWidget.setFixedSize(210,210)
        #imageWidget.setStyleSheet("border-radius: 15px;")
        image_makanan = QtWidgets.QLabel(self)
        image_makanan.setPixmap(QPixmap("../img/ayamgoreng.jpg"))
        image_makanan.setScaledContents(True)
        image_makanan.setStyleSheet("background-color: #EE9C20;border-radius: 15px;")
        #image_makanan = QtWidgets.QPushButton()
        #image_makanan.setIcon(QIcon(QPixmap("../img/ayamgoreng.jpg")))
        #image_makanan.setIconSize(QSize(178, 178))
        #image_makanan.setFixedSize(QSize(178, 178))
        #image_makanan.setStyleSheet("background-color: #EE9C20;border-radius: 15px;")
        imageLayout.addWidget(image_makanan)
        imageWidget.setLayout(imageLayout)
        verticalResep.addWidget(imageWidget)

        label_judul = QtWidgets.QLabel()
        label_judul.setText("Judul makanan")
        label_judul.setWordWrap(True)
        label_judul.setStyleSheet("font: 75 12pt;")
        label_judul.setAlignment(Qt.AlignCenter)
        verticalResep.addWidget(label_judul)
        
        resepWidget.setLayout(verticalResep)
        self.gridLayoutResep.addWidget(resepWidget, idx//4, idx%4, alignment=Qt.AlignCenter)
        self.scrollResep.setLayout(self.gridLayoutResep)
        #self.counter += 1
    
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = DaftarResep()
    MainWindow.show()
    sys.exit(app.exec_())
