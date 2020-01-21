import json
import os
from PySide2 import QtCore, QtGui, QtWidgets
from source.utils import getItemsGenerator
from source.error_checking.ui_error_checking import Ui_Form
from source.dialog.Dialog import Dialog
from source.error_checking.OptionControls import CheckButton


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
                self.ui.questionLabel.setText(d["question"])
                self.ui.lcdNumber.setText(str(self.currentCfg["timeLimit"]))
                # Clear previous items
                for i in list(getItemsGenerator(self.ui.selectBox)):
                    i.widget().setParent(None)
                if len(d["answers"]) == 1:
                    # radiobutton
                    for opt in d["options"]:
                        rb = QtWidgets.QRadioButton(opt, self.ui.OptionFrame)
                        rb.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                        rb.setMinimumWidth(250)
                        self.ui.selectBox.addWidget(rb, 0, QtCore.Qt.AlignHCenter)
                else:
                    #checkboxes
                    for opt in d["options"]:
                        rb = CheckButton(opt, self.ui.OptionFrame)
                        rb.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                        rb.setMinimumWidth(250)
                        self.ui.selectBox.addWidget(rb, 0, QtCore.Qt.AlignHCenter)
        except IndexError:
            return False

    def setupSignals(self):
        self.ui.typingNextButton.clicked.connect(self.finishTask)

    def cleanup(self):
        """
        disconnect signals
        """
        self.ui.typingNextButton.clicked.disconnect()

    def finishTask(self):
        self.gatherResults()
        self.cleanup()
        self.mainWindow.controller.nextScreen()

    def gatherResults(self):
        pass