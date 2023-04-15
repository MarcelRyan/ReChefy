from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QSize
from PyQt5 import uic, QtWidgets
from database import database_func
import sys

class FormAddResep(QtWidgets.QMainWindow):
    def __init__(self):
        super(FormAddResep, self).__init__()
        uic.loadUi("src/addResep.ui", self)
        self.setFixedHeight(850)
        self.setFixedWidth(1200)
        self.inputGambar_resep.setIconSize(QSize(113, 98))
        self.inputGambar_resep.setStyleSheet("QPushButton{background-color: #EEC120; border: none;}")
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
        self.scrollBahan.setWidget(self.scrollWidgetBahan)
        self.verticalAlat = QtWidgets.QVBoxLayout()
        self.verticalBahan = QtWidgets.QVBoxLayout()
        self.verticalBahan.setContentsMargins(0, 0, 10, 0)
        self.listAlat = []
        self.listBahan = []
        self.counterAlat = 1
        self.counterBahan = 1
        self.amountAlat = 0
        self.amountBahan = 0

    def addAlat(self):
        horizontal_layout = QtWidgets.QHBoxLayout()
        horizontal_layout.setObjectName("Alat_"+str(self.counterAlat))

        dropdown = QtWidgets.QComboBox()
        dropdown.addItems(['1', '2', '3', '4', '5', '6'])
        dropdown.setObjectName("DropdownAlat_"+str(self.counterAlat))
        dropdown.setFixedSize(150, 30)
        dropdown.setStyleSheet("QComboBox{background-color: #F7EAD3; border: none; border-radius: 10px;} QComboBox::down-arrow {image: url(images/icon/down_arrow.png); height: 30px;}")
        horizontal_layout.addWidget(dropdown)

        delete = QtWidgets.QPushButton()
        delete.setFixedSize(30, 30)
        delete.setIcon(QIcon(QPixmap("images/icon/deleteIcon.png")))
        delete.setStyleSheet("background-color: #F75008; border-radius: 15px;")
        delete.setObjectName("DeleteAlat_"+str(self.counterAlat))
        horizontal_layout.addWidget(delete)

        self.listAlat.append(horizontal_layout)
        delete.clicked.connect(lambda _, layout=horizontal_layout: self.deleteAlat(layout))
        self.verticalAlat.insertLayout(self.amountAlat, horizontal_layout)
        self.scrollWidgetAlat.setLayout(self.verticalAlat)
        self.counterAlat += 1
        self.amountAlat += 1
    
    def addBahan(self):
        horizontal_layout = QtWidgets.QHBoxLayout()

        amount = QtWidgets.QSpinBox()
        amount.setObjectName("Jumlah_"+str(self.counterBahan))
        amount.setRange(0, 100)
        amount.setFixedSize(30, 30)
        amount.setStyleSheet("QSpinBox{background-color: #F7EAD3; border-radius: 10px;}QSpinBox::up-button{image: url(images/icon/up_arrow.png); width: 7px;} QSpinBox::down-button{image: url(images//icon/down_arrow.png); width: 7px;}")
        horizontal_layout.addWidget(amount)

        unit = QtWidgets.QComboBox()
        unit.addItems(['kg', 'object'])
        unit.setObjectName("Satuan_"+str(self.counterBahan))
        unit.setFixedSize(55, 30)
        unit.setStyleSheet("QComboBox{background-color: #F7EAD3; border: none; border-radius: 10px;} QComboBox::down-arrow {image: url(images/icon/down_arrow.png); height: 5px; width: 5px}")
        horizontal_layout.addWidget(unit)

        dropdown = QtWidgets.QComboBox()
        dropdown.addItems(['Option 1', 'Option 2', 'Option 3', 'Option 4', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k'])
        dropdown.setObjectName("DropdownBahan_"+str(self.counterBahan))
        dropdown.setFixedSize(80, 30)
        dropdown.setStyleSheet("QComboBox{background-color: #F7EAD3; border: none; border-radius: 10px;} QComboBox::down-arrow {image: url(images/icon/down_arrow.png); height: 30px;}")
        horizontal_layout.addWidget(dropdown)

        delete = QtWidgets.QPushButton()
        delete.setFixedSize(30, 30)
        delete.setIcon(QIcon(QPixmap("images/icon/deleteIcon.png")))
        delete.setStyleSheet("background-color: #F75008; border-radius: 15px;")
        delete.setObjectName("DeleteBahan_"+str(self.counterBahan))
        horizontal_layout.addWidget(delete)
        self.listBahan.append(horizontal_layout)
        
        delete.clicked.connect(lambda _, layout=horizontal_layout: self.deleteBahan(layout))
        self.verticalBahan.insertLayout(self.amountBahan, horizontal_layout)
        self.scrollWidgetBahan.setLayout(self.verticalBahan)
        self.counterBahan += 1
        self.amountBahan += 1


    def pilihGambar(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Image Files (*.png *.jpg *.bmp)")
        if filePath:
            self.inputGambar_resep.setIcon(QIcon(QPixmap(filePath)))
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
        self.listAlat.remove(layout)
        self.amountAlat -= 1

    def deleteBahan(self, layout):

        layout_item = self.verticalBahan.itemAt(self.verticalBahan.indexOf(layout))
        self.verticalBahan.removeItem(layout_item)
        while layout.count():
            child_item = layout.takeAt(0)

            if child_item.widget():
                child_item.widget().deleteLater()

        self.scrollWidgetBahan.setLayout(self.verticalBahan)
        self.listBahan.remove(layout)
        self.amountBahan -= 1

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = FormAddResep()
    # Mari kita coba data pertama gan
    MainWindow.show()
    sys.exit(app.exec_())
