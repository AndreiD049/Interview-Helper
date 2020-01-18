from PySide2 import QtWidgets, QtGui, QtCore
from source.start_page.ui_start_page import Ui_StartPage
from source.dialog.Dialog import Dialog

class StartPage(QtWidgets.QWidget):

    def __init__(self, *args, **kwargs):
        QtWidgets.QWidget.__init__(self, *args, **kwargs)
        self.ui = Ui_StartPage()
        self.ui.setupUi(self)
        self.mainWindow = self.parent()
        self.mainWindow.ui.stackedWidget.addWidget(self)
        self.setupSignals()

    def showDialog(self):
        d = Dialog() 
        mov = QtGui.QMovie(r"G:\Interview-Helper\assets\images\cat.gif")
        d.ui.gifLabel.setMovie(mov)
        d.ui.pushButton.clicked.connect(d.close)
        mov.start()
        d.setWindowModality(QtCore.Qt.ApplicationModal)
        d.exec_()

    def startUp(self):
        self.setupSignals()

    def setupSignals(self):
        self.ui.pushButton.clicked.connect(self.btnPress)

    def btnPress(self):
        self.cleanup()
        self.mainWindow.controller.nextScreen()

    def cleanup(self):
        self.ui.pushButton.clicked.disconnect()
        