from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

class window(QWidget):
    def __init__(self,res):
        super().__init__()
        self.setGeometry(100,15,600,500)
        self.Abc = []
        self.Abc.append(['first',[500,500],[100,100],None])
        print(res.size().width())
        self.InitUI()

    def InitUI(self):
        
        self.showMaximized()
    
    def paintEvent(self,event):
        temp = self.Abc[0]
        print(temp[2][0],type(temp[1][0]))
        

app = QApplication([])
w = window(app.primaryScreen())
app.exec_()