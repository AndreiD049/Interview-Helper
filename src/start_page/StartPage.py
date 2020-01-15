from PyQt5 import QtWidgets, QtGui, QtCore
from src.start_page.ui_start_page import Ui_StartPage
from src.dialog.Dialog import Dialog

class StartPage(QtWidgets.QWidget):

    def __init__(self, *args, **kwargs):
        QtWidgets.QWidget.__init__(self, *args, **kwargs)
        self.ui = Ui_StartPage()
        self.ui.setupUi(self)
        self.mainWindow = self.parent()
        self.setupSignals()
        self.mainWindow.ui.stackedWidget.addWidget(self)

    def showDialog(self):
        d = Dialog() 
        mov = QtGui.QMovie(r"G:\Interview-Helper\assets\images\cat.gif")
        d.ui.gifLabel.setMovie(mov)
        d.ui.pushButton.clicked.connect(d.close)
        mov.start()
        d.setWindowModality(QtCore.Qt.ApplicationModal)
        d.exec_()

    def startUp(self):
        pass

    def setupSignals(self):
        self.ui.pushButton.clicked.connect(self.mainWindow.controller.nextScreen)
        