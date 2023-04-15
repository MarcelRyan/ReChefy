from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QSize, Qt
from PyQt5 import uic, QtWidgets
import sys
from database import database_func

class DaftarResep(QtWidgets.QMainWindow):
    def __init__(self):
        #self.parent = parent
        super(DaftarResep, self).__init__()
        uic.loadUi(r".\src\daftarResep.ui", self)
        
        # load database
        file = r".\src\database\rechefy.db"
        connection = database_func.connectToDatabase(file)
        database_func.initializeTable(connection)
                
        # nge read apa data x
        # for i in x:
            # self.createResep(nama, picture,)
        #self.layoutkosong = QtWidgets.QHBoxLayout()
        
        # load header label
        self.headerLabel = QtWidgets.QLabel(self)
        self.headerLabel.setGeometry(0,0,1200,125)
        self.headerLabel.setStyleSheet("background-image: url('images/icon/header.png');")
        
        # load back button
        self.backButton = QtWidgets.QPushButton(self)
        self.backButton.setStyleSheet("border-image: url(images/icon/button_back.png);background-color:none;border: none")
        self.backButton.setIconSize(QSize(31, 31))
        self.backButton.setFixedSize(QSize(31, 31))
        self.backButton.move(52,38)
        
        # load title "Daftar Resep" label
        self.titleLabel = QtWidgets.QLabel(self)
        self.titleLabel.setGeometry(70,102,320,70)
        self.titleLabel.setText("Daftar Resep")
        self.titleLabel.setStyleSheet("font: 75 28pt;")
        
        # load search button
        self.searchButton.setStyleSheet("border-image: url(images/icon/button_search.png);background-color:none;border: none")
        self.searchButton.setIconSize(QSize(31, 31))
        self.searchButton.setFixedSize(QSize(31, 31))
        self.searchButton.move(1080,130)
        self.searchButton.clicked.connect(lambda : self.searchResep(database_func.searchResepView(connection, self.searchBar.text()), connection, len(dataResep)))
        
        # load add resep button
        self.addResepButton.setStyleSheet("border-image: url(images/icon/button_addResep.png);background-color:none;border: none")
        self.addResepButton.setIconSize(QSize(170, 170))
        self.addResepButton.setFixedSize(QSize(170, 170))
        self.addResepButton.move(1020,620)
        
        # load scroll area
        self.scrollResep = QtWidgets.QWidget()
        self.scrollResep.setGeometry(70,200,1041,601)
        self.gridLayoutResep = QtWidgets.QGridLayout()
        #self.gridLayoutResep.setContentsMargins(10,30,10,30)
        self.gridLayoutResep.setVerticalSpacing(30)
        self.scrollArea.setWidget(self.scrollResep)
        self.scrollArea.verticalScrollBar().setStyleSheet("QScrollBar:vertical {background-color: #FDE7BD; border: none; border-radius: 15px; width: 8px; margin: 0px 0px 0px 0px;}\
                                                QScrollBar::handle:vertical {background-color: #EE9C20;border-radius: 15px; min-height: 20px;}\
                                                QScrollBar::add-line:vertical {border: none; background: none;}\
                                                QScrollBar::sub-line:vertical {border: none; background: none;}")
        
        # load daftar resep
        dataResep = database_func.getDaftarResep(connection)
        self.loadDaftarResep(connection, dataResep, len(dataResep))
            
        self.backButton.raise_()
        self.addResepButton.raise_()
    
    def loadDaftarResep(self, connection, dataResep, countDaftarResep):
        for idx in range(countDaftarResep):
            gambar = database_func.resepBlobToImage(connection, dataResep[idx][0])
            self.createResep(idx, dataResep[idx][2], gambar, dataResep[idx][5], False)
        if (countDaftarResep<4):
            for counter in range (countDaftarResep,5):
                self.createResep(counter, 0, 0, 0, True)
            
    def createResep(self, idx, namaResep, gambarResep, isDefault, isEmpty):
        resepWidget = QtWidgets.QWidget()
        resepWidget.setFixedSize(230,280)
        verticalResep = QtWidgets.QVBoxLayout()
        
        if (not isEmpty):
            resepWidget.setStyleSheet("background-color: #FDE7BD;border-radius: 15px;")
            
            imageWidget = QtWidgets.QWidget()
            imageLayout = QtWidgets.QVBoxLayout()
            imageWidget.setFixedSize(210,210)
            #imageWidget.setStyleSheet("border-radius: 15px;")
            image_makanan = QtWidgets.QLabel(self)
            image_makanan.setPixmap(QPixmap(gambarResep))
            image_makanan.setScaledContents(True)
            image_makanan.setStyleSheet("background-color: #EE9C20;border-radius: 15px;")
            #image_makanan = QtWidgets.QPushButton()
            #image_makanan.setIcon(QIcon(QPixmap("images/icon/ayamgoreng.jpg")))
            #image_makanan.setIconSize(QSize(178, 178))
            #image_makanan.setFixedSize(QSize(178, 178))
            #image_makanan.setStyleSheet("background-color: #EE9C20;border-radius: 15px;")
            imageLayout.addWidget(image_makanan)
            imageWidget.setLayout(imageLayout)
            verticalResep.addWidget(imageWidget)

            label_judul = QtWidgets.QLabel()
            label_judul.setText(namaResep)                
            label_judul.setWordWrap(True)
            label_judul.setStyleSheet("font: 75 12pt;")
            label_judul.setAlignment(Qt.AlignCenter)
            verticalResep.addWidget(label_judul)
                    
        resepWidget.setLayout(verticalResep)
        if (isDefault==1):
            labelResepku = QtWidgets.QLabel(resepWidget)
            labelResepku.setFixedSize(120,120)
            labelResepku.setStyleSheet("border-image: url('images/icon/icon_resepku2.png');background-color: none;")
            labelResepku.move(110,0)
            labelResepku.raise_()
        #verticalResep.addWidget(labelResepku)
        self.gridLayoutResep.addWidget(resepWidget, idx//4, idx%4, alignment=Qt.AlignCenter)
        self.scrollResep.setLayout(self.gridLayoutResep)
        
    def searchResep(self, newDaftarResep, connection, countOriginalDaftarResep):
        self.clearGrid()
        if (len(newDaftarResep) != 0):
            if (len(newDaftarResep) < countOriginalDaftarResep):
                self.titleLabel.setText("Hasil Pencarian")
            else:
                self.titleLabel.setText("Daftar Resep")
            self.loadDaftarResep(connection, newDaftarResep, len(newDaftarResep))       
        else:
            self.titleLabel.setText("Hasil Pencarian")
            self.labelNotFound = QtWidgets.QLabel(self)
            self.labelNotFound.setGeometry(70,200,571,51)
            self.labelNotFound.setText("\n      Kami tidak memiliki resep masakan tersebut :(")
            self.labelNotFound.setStyleSheet("font: 75 20pt;color: black")
            self.labelNotFound.setAlignment(Qt.AlignTop)
            self.labelNotFound.raise_()
            self.gridLayoutResep.addWidget(self.labelNotFound,0,0,1,4)
            #print("...")
        
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