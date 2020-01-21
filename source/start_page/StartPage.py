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
        self.fadeIn(self.showDialog)


    def fadeIn(self, func=None):
        self.eff = QtWidgets.QGraphicsOpacityEffect(self)
        self.setGraphicsEffect(self.eff)
        self.a = QtCore.QPropertyAnimation(self.eff, b"opacity")
        if func:
            self.a.finished.connect(func)
        print(self.a.Running.Running)
        self.a.setDuration(1000)
        self.a.setStartValue(0)
        self.a.setEndValue(1)
        self.a.setEasingCurve(QtCore.QEasingCurve.Linear)
        self.a.start()

    def fadeOut(self, func=None):
        self.eff = QtWidgets.QGraphicsOpacityEffect(self)
        self.setGraphicsEffect(self.eff)
        self.a = QtCore.QPropertyAnimation(self.eff, b"opacity")
        if func:
            self.a.finished.connect(func)
        self.a.setDuration(3800)
        self.a.setStartValue(1)
        self.a.setEndValue(0)
        self.a.setEasingCurve(QtCore.QEasingCurve.Linear)
        self.a.start()


    def showDialog(self):
        self.d = Dialog() 
        mov = QtGui.QMovie(r".\assets\images\cat.gif")
        self.d.ui.gifLabel.setMovie(mov)
        self.d.ui.pushButton.clicked.connect(self.d.done)
        mov.start()
        self.d.setWindowModality(QtCore.Qt.ApplicationModal)
        self.d.exec_()

    def startUp(self):
        self.ui.lineEdit.clear()
        self.setupSignals()
        self.fadeIn()

    def setupSignals(self):
        self.ui.pushButton.clicked.connect(self.btnPress)

    def btnPress(self):
        if not self.ui.lineEdit.text().strip():
            self.ui.AssistiveText.setProperty('warning', True)
            self.ui.AssistiveText.style().unpolish(self.ui.AssistiveText)
            self.ui.AssistiveText.style().polish(self.ui.AssistiveText)
        else:
            self.cleanup()
            self.fadeOut(self.mainWindow.controller.nextScreen)

    def cleanup(self):
        self.ui.AssistiveText.setProperty('warning', False)
        self.ui.AssistiveText.style().unpolish(self.ui.AssistiveText)
        self.ui.AssistiveText.style().polish(self.ui.AssistiveText)
        self.ui.pushButton.clicked.disconnect()
        