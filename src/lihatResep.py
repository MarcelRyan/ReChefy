import os
from database import database_func
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtWidgets, QtCore, QtGui
from functools import partial
from PyQt5.QtCore import QDateTime
from PyQt5.QtCore import Qt


class Warning(QDialog):
    def __init__(self):
        super().__init__()
        # Set up the UI
        self.layout = QVBoxLayout()
        uic.loadUi("src/warning.ui", self)

        self.setLayout(self.layout)
        self.deleteButton.clicked.connect(self.accept)
        self.cancelButton.clicked.connect(self.reject) 


class lihatResep(QMainWindow) :
    def __init__(self) :
        super(lihatResep, self).__init__()
        uic.loadUi("src/lihatResep.ui", self)

        self.file = r".\src\database\rechefy.db"
        self.connection = database_func.connectToDatabase(self.file)
        self.resep = database_func.getResep(self.connection, 1)
        self.alatResep = database_func.getAlatResep(self.connection, 1)
        self.bahanResep = database_func.getBahanResep(self.connection, 1)
        self.fotoResep = database_func.resepBlobToImage(self.connection, 1)
        self.komentarResep = database_func.getKomentar(self.connection, 1)
        self.alatResepCombined = self.combineAlat()
        self.bahanResepCombined = self.combineBahan()

        self.fotoMasakan.setPixmap(QtGui.QPixmap(self.fotoResep))
        self.namaMasakan.setText(self.resep[0][2])
        self.deskripsi.setText(self.resep[0][3])
        self.langkahMemasak_isi.setText(self.resep[0][4])
        self.bahan_isi.setText(self.bahanResepCombined)
        self.alat_isi.setText(self.alatResepCombined)


        self.setStyleSheet("background-color: #FDE7BD;")
        self.show()

        self.path = "img/noPhoto.jpg"
        self.text = ""

        self.sendButton.clicked.connect(self.addKomentar)
        self.deleteResepButton.clicked.connect(self.deleteResep)
        self.attachButton.clicked.connect(self.addFotoKomentar)
        self.total = len(self.komentarResep)
        self.counter = 0
        if self.total > 0 :
                self.counter = self.komentarResep[self.total-1][0]
                self.displayKomentar()
        self.judulKomentar.setText(f"Komentar ({self.total})")
        self.setFixedWidth(1200)
        self.setFixedHeight(850)
        self.warningClass = Warning()
        self.warningClass.setWindowTitle("Warning")
        # print(self.komentarResep)
        if self.total == 0 :
                self.komentar.setMinimumSize(QtCore.QSize(1000, 300))

    def combineBahan(self) :
        row = len(self.bahanResep)
        column = len(self.bahanResep[0])
        result = ""
        number = 1
        for i in range(row) :
                if i != 0 :
                        result += "\n"
                result += f"{number}. "
                for j in range (column) :
                        if j != 0 :
                                result += str(self.bahanResep[i][j])
                                if j != column-1 :
                                        result += " "
                number +=1
        return result
                  
         
    
    def combineAlat(self) :
        row = len(self.alatResep)
        column = len(self.alatResep[0])
        result = ""
        number = 1
        for i in range(row) :
                if i != 0 :
                        result += "\n"
                result += f"{number}. "
                for j in range (column) :
                        if j != 0 :
                                result += str(self.alatResep[i][j])
                                if j != column-1 :
                                        result += " "
                number +=1
        return result
         

    def deleteResep(self) :
        self.warningClass.warningLabel.setText("Apakah Anda yakin ingin \n menghapus resep?")
        self.warningClass.exec_()

    def addFotoKomentar(self) :
        filter = "Image Files (*.jpg; *.jpeg; *.png)"
        filePath, _ = QFileDialog.getOpenFileName(self, filter=filter)
        if filePath:
            self.path = filePath
            self.fileName = os.path.basename(self.path)
            self.pathText.setText(self.fileName)
        else :
             self.path = "img/noPhoto.jpg"

    def deleteKomentar(self,count) :
        result = self.warningClass.exec_()
        if result == QDialog.Accepted :
                frame = self.findChild(QFrame, f'komentarFrame_{count}')
                if frame is not None :
                        frame.deleteLater()
                        self.total-=1
                        self.judulKomentar.setText(f"Komentar ({self.total})")
                        database_func.deleteKomentar(self.connection, count)
                        self.komentarResep = database_func.getKomentar(self.connection, 1)
                        # print(self.komentarResep)
                if self.total == 0 :
                        self.komentar.setMinimumSize(QtCore.QSize(1000, 300))

    def displayKomentar(self):
        for i in range (self.total) :
                self.komentarID = int(self.komentarResep[i][0])
                self.komentarFoto = self.komentarResep[i][1]
                self.komentarTeks = self.komentarResep[i][2]
                self.komentarTanggal = self.komentarResep[i][3]

                self.komentar.setMinimumSize(QtCore.QSize(1000, 725))
                self.komentarFrame_0 = QtWidgets.QFrame(self.scrollAreaWidgetContents_8)
                self.komentarFrame_0.setMinimumSize(QtCore.QSize(0, 245))
                self.komentarFrame_0.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.komentarFrame_0.setFrameShadow(QtWidgets.QFrame.Raised)
                self.komentarFrame_0.setObjectName("komentarFrame_" + str(self.komentarID))
                self.tanggalKomentar_0 = QtWidgets.QLabel(self.komentarFrame_0)
                self.tanggalKomentar_0.setGeometry(QtCore.QRect(30, 20, 131, 51))
                current_datetime = QDateTime.currentDateTime()
                self.tanggalKomentar_0.setText(self.komentarTanggal)
                # self.tanggalKomentar_0.setText("23/02/2023 04:22PM")
                self.tanggalKomentar_0.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";\n"
        "color: rgb(211, 164, 145);")
                self.tanggalKomentar_0.setScaledContents(False)
                self.tanggalKomentar_0.setWordWrap(False)
                self.tanggalKomentar_0.setObjectName("namaKomentar_" + str(self.counter+1))
                self.isiKomentar_0 = QtWidgets.QTextEdit(self.komentarFrame_0)
                self.isiKomentar_0.setGeometry(QtCore.QRect(0, 70, 661, 161))
                self.isiKomentar_0.setStyleSheet("border: 0px solid #555;\n"
        "border-radius: 8px;\n"
        "border-style: outset;\n"
        "background-color: rgb(253, 231, 189);\n"
        "padding: 10px;")
                self.isiKomentar_0.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
                self.isiKomentar_0.setWordWrapMode(True)
                self.isiKomentar_0.setReadOnly(True)
                self.isiKomentar_0.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
                self.isiKomentar_0.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
                self.isiKomentar_0.setObjectName("isiKomentar_" + str(self.counter+1))
                self.isiKomentar_0.setText(self.komentarTeks)
                self.isiKomentar_0.setLineWrapMode(QTextEdit.WidgetWidth)
                self.fotoKomentar_0 = QtWidgets.QLabel(self.komentarFrame_0)
                self.fotoKomentar_0.setGeometry(QtCore.QRect(670, 70, 361, 181))
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.fotoKomentar_0.sizePolicy().hasHeightForWidth())
                self.fotoKomentar_0.setSizePolicy(sizePolicy)
                self.fotoKomentar_0.setStyleSheet("border-radius: 8px;\n"
        "border-style: outset;")
                self.fotoKomentar_0.setText("")
                self.fotoKomentar_0.setPixmap(QtGui.QPixmap(self.komentarFoto))
                self.fotoKomentar_0.setScaledContents(True)
                self.fotoKomentar_0.setObjectName("fotoKomentar_" + str(self.counter+1))

                self.deleteButton_0 = QtWidgets.QPushButton(self.komentarFrame_0)
                self.deleteButton_0.setGeometry(QtCore.QRect(940, 40, 81, 21))
                self.deleteButton_0.setStyleSheet("border-radius: 8px;\n"
        "border-style: outset;")
                icon2 = QtGui.QIcon()
                icon2.addPixmap(QtGui.QPixmap("img/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.deleteButton_0.setIcon(icon2)
                self.deleteButton_0.setIconSize(QtCore.QSize(100, 30))
                self.deleteButton_0.setAutoDefault(False)
                self.deleteButton_0.setText("")
                self.deleteButton_0.setObjectName("deleteButton_" + str(self.counter+1) )
                self.deleteButton_0.clicked.connect(partial(self.deleteKomentar, self.komentarID))
                
                self.line_0 = QtWidgets.QFrame(self.komentarFrame_0)
                self.line_0.setGeometry(QtCore.QRect(0, 10, 1057, 16))
                self.line_0.setStyleSheet("border-color: rgb(212, 183, 127);")
                self.line_0.setFrameShape(QtWidgets.QFrame.HLine)
                self.line_0.setFrameShadow(QtWidgets.QFrame.Sunken)
                self.line_0.setObjectName("line_" + str(self.counter+1))
                self.verticalLayout_4.addWidget(self.komentarFrame_0)
              

    def addKomentar(self, event):
        self.text = self.textEdit.toPlainText()
        if (self.path != "img/noPhoto.jpg" and self.text == "") or (self.path == "img/noPhoto.jpg" and self.text != "") or ((self.path != "img/noPhoto.jpg" and self.text != ""))  :
                self.komentar_isi.setStyleSheet("")
                self.komentar.setMinimumSize(QtCore.QSize(1000, 725))
                self.komentarFrame_0 = QtWidgets.QFrame(self.scrollAreaWidgetContents_8)
                self.komentarFrame_0.setMinimumSize(QtCore.QSize(0, 245))
                self.komentarFrame_0.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.komentarFrame_0.setFrameShadow(QtWidgets.QFrame.Raised)
                self.komentarFrame_0.setObjectName("komentarFrame_" + str(self.counter+1))
                self.tanggalKomentar_0 = QtWidgets.QLabel(self.komentarFrame_0)
                self.tanggalKomentar_0.setGeometry(QtCore.QRect(30, 20, 131, 51))
                current_datetime = QDateTime.currentDateTime()
                self.tanggalKomentar_0.setText(f"{current_datetime.toString('yyyy-MM-dd hh:mm:ss')}")
                self.tanggalKomentar_0.setStyleSheet("font: 8pt \"MS Shell Dlg 2\";\n"
        "color: rgb(211, 164, 145);")
                self.tanggalKomentar_0.setScaledContents(False)
                self.tanggalKomentar_0.setWordWrap(False)
                self.tanggalKomentar_0.setObjectName("namaKomentar_" + str(self.counter+1))
                self.isiKomentar_0 = QtWidgets.QTextEdit(self.komentarFrame_0)
                self.isiKomentar_0.setGeometry(QtCore.QRect(0, 70, 661, 161))
                self.isiKomentar_0.setStyleSheet("border: 0px solid #555;\n"
        "border-radius: 8px;\n"
        "border-style: outset;\n"
        "background-color: rgb(253, 231, 189);\n"
        "padding: 10px;")
                self.isiKomentar_0.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignTop)
                self.isiKomentar_0.setWordWrapMode(True)
                self.isiKomentar_0.setReadOnly(True)
                self.isiKomentar_0.setObjectName("isiKomentar_" + str(self.counter+1))
                self.isiKomentar_0.setText(self.text)
                self.isiKomentar_0.setLineWrapMode(QTextEdit.WidgetWidth)
                self.fotoKomentar_0 = QtWidgets.QLabel(self.komentarFrame_0)
                self.fotoKomentar_0.setGeometry(QtCore.QRect(670, 70, 361, 181))
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.fotoKomentar_0.sizePolicy().hasHeightForWidth())
                self.fotoKomentar_0.setSizePolicy(sizePolicy)
                self.fotoKomentar_0.setStyleSheet("border-radius: 8px;\n"
        "border-style: outset;")
                self.fotoKomentar_0.setText("")
                self.fotoKomentar_0.setPixmap(QtGui.QPixmap(self.path))
                self.fotoKomentar_0.setScaledContents(True)
                self.fotoKomentar_0.setObjectName("fotoKomentar_" + str(self.counter+1))

                self.deleteButton_0 = QtWidgets.QPushButton(self.komentarFrame_0)
                self.deleteButton_0.setGeometry(QtCore.QRect(940, 40, 81, 21))
                self.deleteButton_0.setStyleSheet("border-radius: 8px;\n"
        "border-style: outset;")
                icon2 = QtGui.QIcon()
                icon2.addPixmap(QtGui.QPixmap("img/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                self.deleteButton_0.setIcon(icon2)
                self.deleteButton_0.setIconSize(QtCore.QSize(100, 30))
                self.deleteButton_0.setAutoDefault(False)
                self.deleteButton_0.setText("")
                self.deleteButton_0.setObjectName("deleteButton_" + str(self.counter+1) )
                self.deleteButton_0.clicked.connect(partial(self.deleteKomentar, self.counter+1))
                
                self.line_0 = QtWidgets.QFrame(self.komentarFrame_0)
                self.line_0.setGeometry(QtCore.QRect(0, 10, 1057, 16))
                self.line_0.setStyleSheet("border-color: rgb(212, 183, 127);")
                self.line_0.setFrameShape(QtWidgets.QFrame.HLine)
                self.line_0.setFrameShadow(QtWidgets.QFrame.Sunken)
                self.line_0.setObjectName("line_" + str(self.counter+1))
                self.verticalLayout_4.addWidget(self.komentarFrame_0)

                database_func.addKomentar(self.connection, self.path, self.text,1)
                self.komentarResep = database_func.getKomentar(self.connection, 1)
                # print(self.komentarResep)

                self.counter +=1
                self.total +=1
                self.judulKomentar.setText(f"Komentar ({self.total})")
                self.textEdit.setText("")
                self.pathText.setText("")
                self.text = ""
                self.path = "img/noPhoto.jpg"


def main() :
    app = QApplication([])
    window = lihatResep()
    app.exec_()



if __name__== '__main__' :
    main ()