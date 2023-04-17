from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QSize, Qt
from PyQt5 import uic, QtWidgets
from database import database_func
import sys

class FormEditResep(QtWidgets.QMainWindow):
    def __init__(self):
        super(FormEditResep, self).__init__()
        uic.loadUi("src/editResep.ui", self)
        self.idResep = 1
        self.setFixedHeight(850)
        self.setFixedWidth(1200)
        self.inputGambar_resep.setIconSize(QSize(113, 98))
        self.inputGambar_resep.setStyleSheet("QPushButton{background-color: #EEC120; border: none;}")
        self.inputGambar_resep.clicked.connect(self.selectPicture)
        self.saveButton_resep.clicked.connect(self.inputValidation)

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
        self.scrollAlat.setStyleSheet("QScrollBar:vertical { width: 15px; }")
        self.scrollBahan.setStyleSheet("QScrollBar:vertical { width: 15px; }")

        self.verticalAlat = QtWidgets.QVBoxLayout()
        self.verticalBahan = QtWidgets.QVBoxLayout()
        self.listAlat = []
        self.listBahan = []
        self.counterAlat = 1
        self.counterBahan = 1
        self.amountAlat = 0
        self.amountBahan = 0

        ## EDIT RESEP DATABASE
        self.file = r"src\database\rechefy.db"
        self.connection = database_func.connectToDatabase(self.file)
        self.dataResep = database_func.getResep(self.connection, self.idResep)
        #foto = x[0][1]
        nama = self.dataResep[0][2]
        deskripsi = self.dataResep[0][3]
        langkah = self.dataResep[0][4]
        self.inputJudul_resep.setText(nama)
        self.inputDeskripsi_resep.setText(deskripsi)
        self.inputLangkahMemasak_resep.setText(langkah)
        self.filePath = database_func.resepBlobToImage(self.connection, 1)
        self.inputGambar_resep.setIcon(QIcon(QPixmap(self.filePath)))
        self.inputGambar_resep.setIconSize(QSize(self.inputGambar_resep.width(), self.inputGambar_resep.height()))
        self.inputGambar_resep.setStyleSheet("QPushButton{background-color: #FFF6E5; border: none;}")

        self.allAlat = database_func.getAlat(self.connection)
        self.allBahan = database_func.getBahan(self.connection)
        self.satuanBahan = database_func.getSatuanKuantitasBahan(self.connection)
        y = database_func.getAlatResep(self.connection, 1)
        z = database_func.getBahanResep(self.connection, 1)
        for i in y:
            self.addAlat(i[1])
        for i in z:
            self.addBahan(i[1], i[2], i[3])
        self.addAlat_button.clicked.connect(lambda: self.addAlat(self.allAlat[0][1]))
        self.addBahan_button.clicked.connect(lambda: self.addBahan(self.allBahan[0][1], 0, self.satuanBahan[0][0]))

        
    def addAlat(self, opsi):
        horizontal_layout = QtWidgets.QHBoxLayout()
        horizontal_layout.setObjectName("Alat_"+str(self.counterAlat))

        dropdown = QtWidgets.QComboBox()
        for i in self.allAlat:
            dropdown.addItem(i[1])
        dropdown.setCurrentIndex(dropdown.findText(opsi))
        dropdown.view().setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        dropdown.setObjectName("DropdownAlat_"+str(self.counterAlat))
        dropdown.setFixedSize(133, 30)
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
        
    
    def addBahan(self, opsi, jumlah, satuan):
        horizontal_layout = QtWidgets.QHBoxLayout()

        amount = QtWidgets.QDoubleSpinBox()
        amount.setObjectName("Jumlah_"+str(self.counterBahan))
        amount.setRange(0.1, 100000.0)
        amount.setValue(jumlah)
        amount.setFixedSize(45, 30)
        amount.setStyleSheet("QSpinBox{background-color: #F7EAD3; border-radius: 10px;}QSpinBox::up-button{image: url(images/icon/up_arrow.png); width: 7px;} QSpinBox::down-button{image: url(images//icon/down_arrow.png); width: 7px;}")
        horizontal_layout.addWidget(amount)

        unit = QtWidgets.QComboBox()
        for i in self.satuanBahan:
            unit.addItem(i[0])
        unit.setObjectName("Satuan_"+str(self.counterBahan))
        #if satuan != "none":
        unit.setCurrentIndex(unit.findText(satuan))
        unit.setFixedSize(72, 30)
        unit.setStyleSheet("QComboBox{background-color: #F7EAD3; border: none; border-radius: 10px;} QComboBox::down-arrow {image: url(images/icon/down_arrow.png); height: 5px; width: 5px}")
        horizontal_layout.addWidget(unit)

        dropdown = QtWidgets.QComboBox()
        for i in self.allBahan:
            dropdown.addItem(i[1])
        dropdown.setCurrentIndex(dropdown.findText(opsi))
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


    def selectPicture(self):
        self.filePath, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Image Files (*.png *.jpg *.bmp)")
        if self.filePath:
            self.inputGambar_resep.setIcon(QIcon(QPixmap(self.filePath)))
            self.inputGambar_resep.setIconSize(QSize(self.inputGambar_resep.width(), self.inputGambar_resep.height()))
            self.inputGambar_resep.setStyleSheet("QPushButton{background-color: #FFF6E5; border: none;}")
        else:
            self.inputGambar_resep.setIcon(QIcon(QPixmap("images/icon/pilihFoto.png")))
            self.inputGambar_resep.setIconSize(QSize(113, 98))
            self.inputGambar_resep.setStyleSheet("QPushButton{background-color: #EEC120; border: none;}")

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
    
    def alatValidation(self):
        alat = set()
        for count in self.listAlat:
            nama = self.findChild(QComboBox, f'DropdownAlat_{count}').currentText()
            if nama in alat: return False
            alat.add(nama)
        return True
    
    def bahanValidation(self):
        bahan = set()
        for count in self.listBahan:
            nama = self.findChild(QComboBox, f'DropdownBahan_{count}').currentText()
            if nama in bahan: return False
            bahan.add(nama)
        return True

    def inputValidation(self):
        if self.inputJudul_resep.toPlainText() == "" or self.inputDeskripsi_resep.toPlainText() == "" or self.filePath == "" or self.inputLangkahMemasak_resep.toPlainText() == "" or len(self.listAlat) == 0 or len(self.listBahan) == 0 or not self.alatValidation() or not self.bahanValidation():
            if self.inputJudul_resep.toPlainText() == "":
                print("Judul masakan masih kosong")
            if (self.inputDeskripsi_resep.toPlainText() == ""):
                print("Deskripsi masakan masih kosong")
            if self.filePath == "":
                print("Gambar masakan belum ada")
            if self.inputLangkahMemasak_resep.toPlainText() == "":
                print("Langkah memasak masakan masih kosong")
            if len(self.listAlat) == 0:
                print("Alat masih kosong")
            if len(self.listBahan) == 0:
                print("Bahan masih kosong")
            if not self.alatValidation():
                print("Terdapat alat yang sama")
            if not self.bahanValidation():
                print("Terdapat bahan yang sama")
        else:
            print("Berhasil edit")
            self.editResep()
        # penambahan warning
    def editResep(self):
        # Jika tervalidasi, lakukan add resep.
        database_func.editResep(self.connection, self.idResep, database_func.imageToBlob(self.filePath), self.inputJudul_resep.toPlainText(), self.inputDeskripsi_resep.toPlainText(), self.inputLangkahMemasak_resep.toPlainText())
        database_func.deleteAlatResep(self.connection, self.idResep)
        database_func.deleteBahanResep(self.connection, self.idResep)
        for count in self.listAlat:
            alat = self.findChild(QComboBox, f'DropdownAlat_{count}')
            idAlat = database_func.getIdAlat(self.connection, alat.currentText())
            database_func.addAlatResep(self.connection, self.idResep, idAlat)
        
        for count in self.listBahan:
            bahan = self.findChild(QComboBox, f'DropdownBahan_{count}')
            jumlahBahan = self.findChild(QDoubleSpinBox, f'Jumlah_{count}')
            satuanBahan = self.findChild(QComboBox, f'Satuan_{count}')
            idBahan = database_func.getIdBahan(self.connection, bahan.currentText())
            database_func.addBahanResep(self.connection, self.idResep, idBahan, jumlahBahan.value(), satuanBahan.currentText())

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = FormEditResep()
    MainWindow.show()
    sys.exit(app.exec_())
