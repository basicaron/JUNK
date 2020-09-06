import sys
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtWidgets import QWidget,QApplication,QFrame,QPushButton,QMenu,QAction,QMainWindow,QTextEdit
from PyQt5.QtGui import QPainter,QBrush,QPen
from PyQt5.QtCore import Qt
class window(QWidget):
    def __init__(self):
        super().__init__()
        self.InitUI()
        self.setStyleSheet('background-color:grey')
        self.A = True
    def InitUI(self):
        self.setMouseTracking(True)        
        text = QTextEdit(self)
        text.setGeometry(100,15,600,500)
        text.setText("hello")
        text.setReadOnly(True)
        self.show()
    def paintEvent(self,event):
        painter = QPainter(self)
        painter.setBrush(QBrush(Qt.red,Qt.SolidPattern))
        painter.drawRect((0,0,1000,500))
    def mousePressEvent(self,event):
        if self.A:
            self.setMouseTracking(False)
            self.A = False
        else:
            self.setMouseTracking(True)
            self.A = True

    def contextMenuEvent(self,event):
        menu = QMenu(self)
        self.setStyleSheet("""
        menu{
            background-color:red
            }""")
        menu.setObjectName("menu")
        new = QAction("New",self)
        new.triggered.connect(self.prnt)
        menu.addAction(new)
        exit = menu.addAction("Exit")
        action = menu.exec_(self.mapToGlobal(event.pos()))
    def mouseMoveEvent(self,event):
        print("\r",event.pos(),end ="")
    def prnt(self):
        print("none")
          
app = QApplication([])
w = window()
app.exec_()