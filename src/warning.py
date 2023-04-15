from PyQt5.QtWidgets import *
from PyQt5 import uic

class Warning(QDialog):
    def __init__(self):
        super().__init__()
        # Set up the UI
        self.layout = QVBoxLayout()
        uic.loadUi("src/warning.ui", self)

        self.setLayout(self.layout)
        self.deleteButton.clicked.connect(self.accept)
        self.cancelButton.clicked.connect(self.reject) 
    
    def komentarDelete(self) :
        self.warningClass = Warning()
        self.warningClass.setWindowTitle("Warning")
        self.warningClass.warningLabel.setText("Apakah Anda yakin ingin \n menghapus komentar?")
        self.warningClass.exec_()

    def resepDelete(self) :
        self.warningClass = Warning()
        self.warningClass.setWindowTitle("Warning")
        self.warningClass.warningLabel.setText("Apakah Anda yakin ingin \n menghapus resep?")
        self.warningClass.exec_()
    
    def Back(self) :
        self.warningClass = Warning()
        self.warningClass.setWindowTitle("Warning")
        self.warningClass.warningLabel.setText("Apakah Anda yakin ingin \n kembali?")
        self.warningClass.exec_()