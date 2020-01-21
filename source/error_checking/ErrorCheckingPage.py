import json
import os
from PySide2 import QtCore, QtGui, QtWidgets
from source.utils import getItemsGenerator
from source.error_checking.ui_error_checking import Ui_Form
from source.dialog.Dialog import Dialog
from source.error_checking.OptionControls import CheckButton



class CountDownWorker(QtCore.QObject):

    timer_signal = QtCore.Signal(int)
    timer_end = QtCore.Signal()

    def __init__(self, secondsLeft):
        super(CountDownWorker, self).__init__()
        self.left = secondsLeft

    @QtCore.Slot()
    def updateTimer(self):
        while self.left > 0:
            QtCore.QThread.msleep(1000)
            self.left -= 1
            self.timer_signal.emit(self.left)
            if QtCore.QThread.currentThread().isInterruptionRequested():
                break
        self.timer_end.emit()


class ErrorCheckingScreen(QtWidgets.QWidget):

    def __init__(self, *args, **kwargs):
        super(ErrorCheckingScreen, self).__init__(*args, **kwargs)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.mainWindow = self.parent()
        self.mainWindow.errorCheckingPage = self
        self.mainWindow.ui.stackedWidget.addWidget(self)
        

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
        self.secondsLeft = self.currentCfg["timeLimit"]
        self.filesCount = self.currentCfg["filesCount"]
        self.source_files = self.mainWindow.controller.getRandomFiles(cfg["ErrorCheckingTestsFolder"], self.filesCount)
        self.populateScreen()
        self.setupSignals()
        self.showDialog()
        self.setupThread()
        self.thread.start()

    def showDialog(self):
        d = Dialog() 
        mov = QtGui.QMovie(r".\assets\images\cat.gif")
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
                # reset the time limit
                self.secondsLeft = self.currentCfg["timeLimit"]
                self.ui.lcdNumber.setText(str(self.secondsLeft))

                self.ui.questionCounter.setText(f"{self.filesCount-len(self.source_files)}/{self.filesCount}")
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
        self.ui.typingNextButton.clicked.connect(self.btnClick)


    def setupThread(self):
        # setup a new worker
        self.thread = QtCore.QThread(self)
        self.timer = CountDownWorker(self.secondsLeft)
        self.timer.moveToThread(self.thread)
        self.timer.timer_signal.connect(self.updateTimer)
        self.timer.timer_end.connect(self.thread.quit)
        self.thread.started.connect(self.timer.updateTimer)
        self.thread.finished.connect(self.threadbtnClick)


    def cleanup(self):
        """
        disconnect signals
        """
        self.ui.typingNextButton.clicked.disconnect()

    def btnClick(self):
        """
        When clicking the button, we want just to stop the thread.
        It's finish signal will do the rest
        """
        if self.thread.isRunning():
            self.thread.requestInterruption()
            self.thread.quit()
            self.thread.wait()

    def threadbtnClick(self):
        """
        When thread is finished, we want:
        1. to gather the current results
        2. if there are any more questions, show the next
        3. set up a new thread
        4. start it 
        """
        self.gatherResults()
        if len(self.source_files) != 0:
            self.populateScreen()
            self.setupThread()
            self.thread.start()
        else:
            self.cleanup()
            self.mainWindow.controller.nextScreen()

    @QtCore.Slot(int)
    def updateTimer(self, secondsLeft):
        self.secondsLeft = secondsLeft
        self.ui.lcdNumber.setText(str(self.secondsLeft))

    def gatherResults(self):
        pass