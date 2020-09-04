from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPlainTextEdit, QHBoxLayout,QTextEdit,QFileDialog
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Plain TextEdit"
        self.top = 200
        self.left = 500
        self.width = 400
        self.height = 300



        self.InitWindow()
        

    def select_file(self):
        dail = QFileDialog()
        fil = dail.getOpenFileName()
        return fil[0]

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
    
        plainText = QTextEdit(self)
    
        plainText.setStyleSheet("background-color:grey")

        #plainText.setReadOnly(True)
        plainText.setGeometry(100,15,600,500)
    
        plainText.setUndoRedoEnabled(False)
        self.show()
        


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())