import os
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
         
        self.setStyleSheet("background-color: #FDE7BD;")
        self.show()

        self.sendButton.clicked.connect(self.addKomentar)
        self.deleteResepButton.clicked.connect(self.deleteResep)
        self.attachButton.clicked.connect(self.addFotoKomentar)
        self.counter = 0
        self.total = 0
        self.setFixedWidth(1200)
        self.setFixedHeight(850)
        self.path = "img/noPhoto.jpg"
        self.warningClass = Warning()
        self.warningClass.setWindowTitle("Warning")
        if self.total == 0 :
                self.komentar.setMinimumSize(QtCore.QSize(1000, 300))

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
                if self.total == 0 :
                        self.komentar.setMinimumSize(QtCore.QSize(1000, 300))
    
    def addKomentar(self, event):
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
        text = self.textEdit.toPlainText()
        self.isiKomentar_0.setText(text)
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
        self.counter +=1
        self.total +=1
        self.judulKomentar.setText(f"Komentar ({self.total})")
        self.textEdit.setText("")
        self.pathText.setText("")


def main() :
    app = QApplication([])
    window = lihatResep()
    app.exec_()



if __name__== '__main__' :
    main ()