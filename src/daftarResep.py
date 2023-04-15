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
        
        self.backButton = QtWidgets.QPushButton(self)
        self.backButton.setStyleSheet("border-image: url(../img/button_back.png);background-color:none;border: none")
        self.backButton.setIconSize(QSize(31, 31))
        self.backButton.setFixedSize(QSize(31, 31))
        self.backButton.move(52,38)
        
        
        self.titleLabel = QtWidgets.QLabel(self)
        self.titleLabel.setGeometry(70,102,320,70)
        self.titleLabel.setText("Daftar Resep")
        self.titleLabel.setStyleSheet("font: 75 28pt;")
        
        
        self.searchButton.setStyleSheet("border-image: url(../img/button_search.png);background-color:none;border: none")
        self.searchButton.setIconSize(QSize(31, 31))
        self.searchButton.setFixedSize(QSize(31, 31))
        self.searchButton.move(1080,130)
        self.searchButton.clicked.connect(lambda : self.searchResep(""))
        
        self.addResepButton.setStyleSheet("border-image: url(../img/button_addResep.png);background-color:none;border: none")
        self.addResepButton.setIconSize(QSize(170, 170))
        self.addResepButton.setFixedSize(QSize(170, 170))
        self.addResepButton.move(1020,620)
        
        self.scrollResep = QtWidgets.QWidget()    
        self.gridLayoutResep = QtWidgets.QGridLayout()
        #self.gridLayoutResep.setContentsMargins(10,30,10,30)
        self.gridLayoutResep.setVerticalSpacing(30)
        self.scrollArea.setWidget(self.scrollResep)
        self.scrollArea.verticalScrollBar().setStyleSheet("QScrollBar:vertical {background-color: #FDE7BD; border: none; border-radius: 15px; width: 8px; margin: 0px 0px 0px 0px;}\
                                                QScrollBar::handle:vertical {background-color: #EE9C20;border-radius: 15px; min-height: 20px;}\
                                                QScrollBar::add-line:vertical {border: none; background: none;}\
                                                QScrollBar::sub-line:vertical {border: none; background: none;}")
        
        #self.counter = 0
        for i in range(21):
            self.createResep(i)
            
        self.backButton.raise_()
        self.addResepButton.raise_()
        
            
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
        
    def searchResep(self, keyword):
        self.clearGrid()
        
    def clearGrid(self):
        while self.gridLayoutResep.count():
            item = self.gridLayoutResep.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
            else:
                self.gridLayoutResep.removeItem(item)
        if self.gridLayoutResep.count() == 0:
            self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
    
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = DaftarResep()
    MainWindow.show()
    sys.exit(app.exec_())