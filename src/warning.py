from PyQt5.QtWidgets import *
from PyQt5 import uic

class Warning(QDialog):
    def __init__(self, parent):
        super().__init__()
        # Set up the UI
        self.parent = parent
        self.layout = QVBoxLayout()
        uic.loadUi("warning.ui", self)

        self.setLayout(self.layout)
        self.deleteButton.clicked.connect(self.accept)
        self.cancelButton.clicked.connect(self.reject)
    
    def komentarDelete(self) :
        self.warningClass = Warning(self.parent)
        self.warningClass.setWindowTitle("Warning")
        self.warningClass.warningLabel.setText("Apakah Anda yakin ingin \n menghapus komentar?")

    def resepDelete(self) :
        self.warningClass = Warning(self.parent)
        self.warningClass.setWindowTitle("Warning")
        self.warningClass.warningLabel.setText("Apakah Anda yakin ingin \n menghapus resep?")
    
    def Back(self) :
        self.warningClass = Warning(self.parent)
        self.warningClass.setWindowTitle("Warning")
        self.warningClass.deleteButton.setText("Kembali")
        self.warningClass.warningLabel.setText("Apakah Anda yakin \ningin kembali?")
    
    def Validasi(self):
        self.warningClass = Warning(self.parent)
        self.warningClass.setWindowTitle("Warning")
        font = self.warningClass.warningLabel.font()
        font.setPointSize(7)
        self.warningClass.warningLabel.setFont(font)
        self.warningClass.deleteButton.deleteLater()
        self.warningClass.cancelButton.setText("Ok")
        self.warningClass.cancelButton.setStyleSheet("background-color: #F75008; border-radius: 0px; color: #FFF6E5;")
    def Exec(self):
        return self.warningClass.exec_()

if __name__ == '__main__':
    app = QApplication([])
    warning = Warning(Warning)
    warning.Back()
    warning.exec_()
