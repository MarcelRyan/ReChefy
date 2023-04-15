from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QSize, Qt
from PyQt5 import uic, QtWidgets
from database import database_func
import sys

class FormAddResep(QtWidgets.QMainWindow):
    def __init__(self):
        super(FormAddResep, self).__init__()
        uic.loadUi("src/addResep.ui", self)
        #self.parent = parent
        self.setFixedHeight(850)
        self.setFixedWidth(1200)
        self.saveButton_resep.clicked.connect(self.validasiInput)
        self.inputGambar_resep.setIconSize(QSize(113, 98))
        self.inputGambar_resep.setStyleSheet("QPushButton{background-color: #EEC120; border-radius: 25px;}")
        self.inputGambar_resep.setIcon(QIcon(QPixmap("images/icon/pilihFoto.png")))
        self.inputGambar_resep.clicked.connect(self.pilihGambar)

        self.addAlat_button.clicked.connect(self.addAlat)
        self.addBahan_button.clicked.connect(self.addBahan)
        self.addAlat_button.setFixedSize(30, 30)
        self.addBahan_button.setFixedSize(30, 30)
        self.addAlat_button.setIcon(QIcon(QPixmap("images/icon/addIcon.png")))
        self.addBahan_button.setIcon(QIcon(QPixmap("images/icon/addIcon.png")))
        self.addAlat_button.setStyleSheet("background-color: #F75008; border-radius: 15px")
        self.addBahan_button.setStyleSheet("background-color: #F75008; border-radius: 15px")
        self.scrollWidgetAlat = QtWidgets.QWidget()
        self.scrollWidgetBahan = QtWidgets.QWidget()

        self.scrollAlat.setWidget(self.scrollWidgetAlat)
        self.scrollAlat.verticalScrollBar().setStyleSheet("QScrollBar:vertical {background-color: #FDE7BD; border: none; border-radius: 15px; width: 8px; margin: 0px 0px 0px 0px;}\
                                                QScrollBar::handle:vertical {background-color: #EE9C20;border-radius: 15px; min-height: 20px;}\
                                                QScrollBar::add-line:vertical {border: none; background: none;}\
                                                QScrollBar::sub-line:vertical {border: none; background: none;}")
        self.scrollBahan.setWidget(self.scrollWidgetBahan)
        self.scrollBahan.verticalScrollBar().setStyleSheet("QScrollBar:vertical {background-color: #FDE7BD; border: none; border-radius: 15px; width: 8px; margin: 0px 0px 0px 0px;}\
                                                QScrollBar::handle:vertical {background-color: #EE9C20;border-radius: 15px; min-height: 20px;}\
                                                QScrollBar::add-line:vertical {border: none; background: none;}\
                                                QScrollBar::sub-line:vertical {border: none; background: none;}")
        self.verticalAlat = QtWidgets.QVBoxLayout()
        self.verticalBahan = QtWidgets.QVBoxLayout()
        self.verticalBahan.setContentsMargins(0, 0, 10, 0)
        self.listAlat = []
        self.listBahan = []
        self.counterAlat = 1
        self.counterBahan = 1
        self.amountAlat = 0
        self.amountBahan = 0


        # Read database
        self.file = r".\src\database\rechefy.db"
        self.connection = database_func.connectToDatabase(self.file)
        database_func.initializeTable(self.connection)
        self.allAlat = database_func.getAlat(self.connection)
        self.allBahan = database_func.getBahan(self.connection)
        self.satuanBahan = database_func.getSatuanKuantitasBahan(self.connection)
        x = database_func.getLastIdResep(self.connection)
        print(x)
        y = database_func.getResep(self.connection, x)
        print(y[0][0], y[0][2], y[0][3], y[0][4])
        # print(y[2])
        # print(y[3])
        # print(y[4])

    def addAlat(self):
        horizontal_layout = QtWidgets.QHBoxLayout()
        horizontal_layout.setObjectName("Alat_"+str(self.counterAlat))

        dropdown = QtWidgets.QComboBox()
        for i in self.allAlat:
            dropdown.addItem(i[1])
        dropdown.view().setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        dropdown.setObjectName("DropdownAlat_"+str(self.counterAlat))
        dropdown.setFixedSize(132, 30)
        dropdown.setStyleSheet("QComboBox{background-color: #F7EAD3; border: none; border-radius: 10px;} QComboBox::down-arrow {image: url(images/icon/down_arrow.png); height: 30px;} ")
        horizontal_layout.addWidget(dropdown)

        delete = QtWidgets.QPushButton()
        delete.setFixedSize(30, 30)
        delete.setIcon(QIcon(QPixmap("images/icon/deleteIcon.png")))
        delete.setStyleSheet("background-color: #F75008; border-radius: 15px;")
        delete.setObjectName("DeleteAlat_"+str(self.counterAlat))
        horizontal_layout.addWidget(delete)
        horizontal_layout.id = self.counterAlat

        self.listAlat.append(self.counterAlat)
        delete.clicked.connect(lambda _, layout=horizontal_layout: self.deleteAlat(layout))
        self.verticalAlat.insertLayout(self.amountAlat, horizontal_layout)
        self.scrollWidgetAlat.setLayout(self.verticalAlat)
        self.counterAlat += 1
        self.amountAlat += 1
        
    
    def addBahan(self):
        horizontal_layout = QtWidgets.QHBoxLayout()
        horizontal_layout.setObjectName("Bahan_"+str(self.counterAlat))
        horizontal_layout.setSpacing(3)

        amount = QtWidgets.QDoubleSpinBox()
        amount.setObjectName("Jumlah_"+str(self.counterBahan))
        amount.setRange(0.1, 100000.0)
        amount.setFixedSize(45, 30)
        amount.setStyleSheet("QSpinBox{background-color: #F7EAD3; border-radius: 10px;}QSpinBox::up-button{image: url(images/icon/up_arrow.png); width: 7px;} QSpinBox::down-button{image: url(images//icon/down_arrow.png); width: 7px;}")
        horizontal_layout.addWidget(amount)

        unit = QtWidgets.QComboBox()
        for i in self.satuanBahan:
            unit.addItem(i[0])
        unit.addItems(['kg', 'object'])
        unit.setObjectName("Satuan_"+str(self.counterBahan))
        unit.setFixedSize(72, 30)
        unit.setStyleSheet("QComboBox{background-color: #F7EAD3; border: none; border-radius: 10px;} QComboBox::down-arrow {image: url(images/icon/down_arrow.png); height: 5px; width: 5px}")
        horizontal_layout.addWidget(unit)

        dropdown = QtWidgets.QComboBox()
        for i in self.allBahan:
            dropdown.addItem(i[1])
        dropdown.setObjectName("DropdownBahan_"+str(self.counterBahan))
        dropdown.setFixedSize(125, 30)
        dropdown.setStyleSheet("QComboBox{background-color: #F7EAD3; border: none; border-radius: 10px;} QComboBox::down-arrow {image: url(images/icon/down_arrow.png); height: 30px;}")
        dropdown.view().setStyleSheet("QScrollBar:vertical {background-color: #FDE7BD; border: none; border-radius: 15px; width: 8px; margin: 0px 0px 0px 0px;}\
                                                QScrollBar::handle:vertical {background-color: #EE9C20;border-radius: 15px; min-height: 20px;}\
                                                QScrollBar::add-line:vertical {border: none; background: none;}\
                                                QScrollBar::sub-line:vertical {border: none; background: none;}")
        horizontal_layout.addWidget(dropdown)

        delete = QtWidgets.QPushButton()
        delete.setFixedSize(30, 30)
        delete.setIcon(QIcon(QPixmap("images/icon/deleteIcon.png")))
        delete.setStyleSheet("background-color: #F75008; border-radius: 15px;")
        delete.setObjectName("DeleteBahan_"+str(self.counterBahan))
        horizontal_layout.addWidget(delete)
        horizontal_layout.id = self.counterBahan
        self.listBahan.append(self.counterBahan)
        
        delete.clicked.connect(lambda _, layout=horizontal_layout: self.deleteBahan(layout))
        self.verticalBahan.insertLayout(self.amountBahan, horizontal_layout)
        self.scrollWidgetBahan.setLayout(self.verticalBahan)
        self.counterBahan += 1
        self.amountBahan += 1


    def pilihGambar(self):
        self.filePath, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Image Files (*.png *.jpg *.bmp)")
        if self.filePath:
            print(self.filePath)
            self.inputGambar_resep.setIcon(QIcon(QPixmap(self.filePath)))
            self.inputGambar_resep.setIconSize(QSize(self.inputGambar_resep.width(), self.inputGambar_resep.height()))
            self.inputGambar_resep.setStyleSheet("QPushButton{background-color: #FFF6E5; border: none;}")
        else:
            print(self.filePath)
            self.inputGambar_resep.setIcon(QIcon(QPixmap("images/icon/pilihFoto.png")))
            self.inputGambar_resep.setIconSize(QSize(113, 98))
            self.inputGambar_resep.setStyleSheet("QPushButton{background-color: #EEC120; border-radius: 25px;}")

    def deleteAlat(self, layout):
        # Get the layout item that contains the given layout
        layout_item = self.verticalAlat.itemAt(self.verticalAlat.indexOf(layout))

        # Remove the layout item from the vertical layout
        self.verticalAlat.removeItem(layout_item)

        # Delete the layout and its contents
        while layout.count():
            child_item = layout.takeAt(0)

            if child_item.widget():
                child_item.widget().deleteLater()

        # Update widget container after deletion
        self.scrollWidgetAlat.setLayout(self.verticalAlat)
        self.listAlat.remove(layout.id)
        self.amountAlat -= 1

    def deleteBahan(self, layout):

        layout_item = self.verticalBahan.itemAt(self.verticalBahan.indexOf(layout))
        self.verticalBahan.removeItem(layout_item)
        while layout.count():
            child_item = layout.takeAt(0)

            if child_item.widget():
                child_item.widget().deleteLater()

        self.scrollWidgetBahan.setLayout(self.verticalBahan)
        self.listBahan.remove(layout.id)
        self.amountBahan -= 1
    
    # def validasiResep(self):
    #     if ()
    def validasiInput(self):
        if self.inputJudul_resep.toPlainText() == "" or self.inputDeskripsi_resep.toPlainText() == "" or self.filePath == "" or self.inputLangkahMemasak_resep.toPlainText() == "" or len(self.listAlat) == 0 or len(self.listBahan) == 0:
            print("error")
        else:
            self.tambahResep()
            # penambahan warning
    def tambahResep(self):
        # Jika tervalidasi, lakukan add resep.
        # def addResep(connection, nama_masakan, deskripsi_masakan, gambar_masakan, langkah_memasak, isDefault):
        database_func.addResep(self.connection, self.inputJudul_resep.toPlainText(), self.inputDeskripsi_resep.toPlainText(), database_func.imageToBlob(self.filePath), self.inputLangkahMemasak_resep.toPlainText(), 1)
        self.resepID = database_func.getLastIdResep(self.connection)
        
        for count in self.listAlat:
            alat = self.findChild(QComboBox, f'DropdownAlat_{count}')
            idAlat = database_func.getIdAlat(self.connection, alat.currentText())
            database_func.addAlatResep(self.connection, self.resepID, idAlat)
            #addAlatResep(connection, id_resep, id_alat)
        
        for count in self.listBahan:
            print(count)
            bahan = self.findChild(QComboBox, f'DropdownBahan_{count}')
            jumlahBahan = self.findChild(QDoubleSpinBox, f'Jumlah_{count}')
            print(jumlahBahan.value())
            satuanBahan = self.findChild(QComboBox, f'Satuan_{count}')
            idBahan = database_func.getIdBahan(self.connection, bahan.currentText())
            #addBahanResep(connection, id_resep, id_bahan, kuantitas_bahan, satuan_kuantitas_bahan)
            database_func.addBahanResep(self.connection, self.resepID, idBahan, jumlahBahan.value(), satuanBahan.currentText())

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = FormAddResep()
    MainWindow.show()
    sys.exit(app.exec_())
