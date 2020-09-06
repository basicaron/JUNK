from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

class window(QWidget):
    def __init__(self,res):
        super().__init__()
        self.setGeometry(100,15,600,500)
        self.Abc = []
        self.screensize = [res.width(),res.height()]
        self.Abc.append(['first',[int(self.screensize[0]/2),int(self.screensize[1]/8)],[100,50],None])
        self.InitUI()

    def InitUI(self):

        self.showMaximized()
    
    def paintEvent(self,event):
        A,B = True,True
        i = 0
        paint = QPainter(self)
        paint.setBrush(QBrush(Qt.gray,Qt.SolidPattern))
        for temp in self.Abc:   
            while B:
                paint.drawRect(temp[1][0]-temp[2][0],temp[1][1]-temp[2][1],temp[2][0]*2,temp[2][1]*2)
                temp = temp[3]
                if temp == None:
                    B = False
                    
    def contextMenuEvent(self,event):
        menu = QMenu(self)
        new = QAction("New")
        menu.addAction(new)
        menu.exec(self.mapToGlobal(event.pos()))
app = QApplication([])
w = window(app.primaryScreen().size())
app.exec_()