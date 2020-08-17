from PyQt5 import QtCore,QtWidgets,QtGui
class window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Graph")
        self.initUI()
        self.showMaximized()
    
    def initUI(self):
        b1 = QtWidgets.QPushButton("Button")
        vbox = QtWidgets.QVBoxLayout()
        hbox = QtWidgets.QHBoxLayout()
        hbox.addStretch(1)
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        hbox.addWidget(b1)
        self.setLayout(vbox)
    
app = QtWidgets.QApplication([])
w = window()
app.exec()