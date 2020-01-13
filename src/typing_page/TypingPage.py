from PyQt5 import QtWidgets, QtGui, QtCore
from src.typing_page.ui_typing_page import Ui_Form
from src.dialog.Dialog import Dialog

class TypingPage(QtWidgets.QWidget, Ui_Form):

    def __init__(self, *args, **kwargs):
        QtWidgets.QWidget.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.parent().typingPage = self
        self.parent().stackedWidget.addWidget(self)

    def startUp(self):
        self.showDialog()

    def showDialog(self):
        d = Dialog() 
        mov = QtGui.QMovie(r"G:\Interview-Helper\assets\images\cat.gif")
        d.gifLabel.setMovie(mov)
        d.pushButton.clicked.connect(d.close)
        mov.start()
        d.setWindowModality(QtCore.Qt.ApplicationModal)
        d.exec_()
