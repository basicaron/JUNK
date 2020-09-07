from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

class window(QWidget):
    def __init__(self,res):
        super().__init__()
        self.setGeometry(100,15,600,500)
        self.Abc = []
        self.newnode = False
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
            B = True
        if self.newnode:
            temp = self.node_form(self.mousepos)
            paint.drawRect(temp[1][0]-temp[2][0],temp[1][1]-temp[2][1],temp[2][0]*2,temp[2][1]*2)

    def mousePressEvent(self,event):
        if self.newnode:
            self.newnode = False
            self.Abc.append(self.node_form(event.pos()))
            self.update()
        print(self.Abc)

    def contextMenuEvent(self,event):
        menu = QMenu(self)
        new = QAction("New")
        new.triggered.connect(self.new_node)
        menu.addAction(new)
        menu.exec(self.mapToGlobal(event.pos()))

    def mouseMoveEvent(self,event):
        self.mousepos = event.pos()
        self.update()

    def node_form(self,pos):
        temp = []
        temp.append('')
        a = self.mapToGlobal(pos)
        temp.append([int(a.x()),int(a.y())])
        temp.append([100,50])
        temp.append(None)
        return temp

    def new_node(self):
        self.setMouseTracking(True)
        self.newnode = True
app = QApplication([])
w = window(app.primaryScreen().size())
app.exec_()