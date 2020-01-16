import json
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from src.error_checking.ui_error_checking import Ui_Form
from src.dialog.Dialog import Dialog


class ErrorCheckingScreen(QtWidgets.QWidget):

    def __init__(self, *args, **kwargs):
        super(ErrorCheckingScreen, self).__init__(*args, **kwargs)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.mainWindow = self.parent()
        self.mainWindow.errorCheckingPage = self
        self.mainWindow.ui.stackedWidget.addWidget(self)
        # TODO: setup thread that will countdown

    def startUp(self):
        """
        Starts up the error checking screen:
        1. Get random files from folder and set the filePointer to begining
        2. Read current file index into widgets (separate method)
        3. setup signals
        4. show dialog
        """
        cfg = self.mainWindow.controller.config
        self.currentCfg = cfg["screens"][self.mainWindow.controller.curIdx]
        self.filesCount = self.currentCfg["filesCount"]
        self.source_files = self.mainWindow.controller.getRandomFiles(cfg["ErrorCheckingTestsFolder"], self.filesCount)
        self.populateScreen()
        self.setupSignals()
        self.showDialog()
        # print(self.source_files)
        # print(self.filesCount)

    def showDialog(self):
        d = Dialog() 
        mov = QtGui.QMovie(r"G:\Interview-Helper\assets\images\cat.gif")
        d.ui.gifLabel.setMovie(mov)
        mov.start()
        d.setWindowModality(QtCore.Qt.ApplicationModal)
        d.exec_()

    def populateScreen(self):
        """
        Populates the screen from the source files, pops the last item.
        Returns bool: True if there are items in the source files, False if no more files
        """
        try:
            with open(self.source_files.pop(), "r") as fp:
                d = json.load(fp)
                pix = QtGui.QPixmap(d["image"])
                self.ui.imgLabel.setPixmap(pix)
                self.ui.textBrowser.setPlainText(d["question"])
                self.ui.comboBox.clear()
                self.ui.comboBox.addItems(d["options"])
        except IndexError:
            return False

    def setupSignals(self):
        self.ui.pushButton.clicked.connect(self.finishTask)

    def cleanup(self):
        """
        disconnect signals
        """
        self.ui.pushButton.clicked.disconnect()

    def finishTask(self):
        self.gatherResults()
        self.cleanup()
        self.mainWindow.controller.nextScreen()

    def gatherResults(self):
        pass