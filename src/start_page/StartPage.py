from PyQt5 import QtWidgets, QtGui, QtCore
from src.start_page.ui_start_page import Ui_StartPage
from src.dialog.Dialog import Dialog

class StartPage(QtWidgets.QWidget, Ui_StartPage):

    def __init__(self, *args, **kwargs):
        QtWidgets.QWidget.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.parent().stackedWidget.addWidget(self)

    def showDialog(self):
        d = Dialog() 
        mov = QtGui.QMovie(r"G:\Interview-Helper\assets\images\cat.gif")
        d.gifLabel.setMovie(mov)
        d.pushButton.clicked.connect(d.close)
        mov.start()
        d.setWindowModality(QtCore.Qt.ApplicationModal)
        d.exec_()

    def setupSignals(self):
        def btnClicked():
            print("button was clicked")
        self.pushButton.clicked.connect(btnClicked)
        