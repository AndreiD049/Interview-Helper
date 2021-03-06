import json
from time import time
from PySide2 import QtWidgets, QtGui, QtCore
from source.typing_page.ui_typing_page import Ui_Form
from source.dialog.Dialog import Dialog



class CountDownWorker(QtCore.QObject):

    timer_signal = QtCore.Signal(int)
    timer_end = QtCore.Signal()

    def __init__(self, seconds_left):
        super(CountDownWorker, self).__init__()
        self.left = seconds_left

    @QtCore.Slot()
    def updateTimer(self):
        while self.left > 0:
            QtCore.QThread.msleep(1000)
            self.left -= 1
            self.timer_signal.emit(self.left)
            if QtCore.QThread.currentThread().isInterruptionRequested():
                break
        self.timer_end.emit()


class TypingPage(QtWidgets.QWidget):

    def __init__(self, *args, **kwargs):
        QtWidgets.QWidget.__init__(self, *args, **kwargs)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.currentWord = 1
        self.startTime = -1
        self.endTime = -1
        self.mainWindow = self.parent()
        self.mainWindow.typingPage = self
        self.mainWindow.ui.stackedWidget.addWidget(self)

    def startUp(self):
        # show all content get a random file from folder
        cfg = self.mainWindow.controller.config
        self.currentCfg = cfg["screens"][self.mainWindow.controller.curIdx]
        source_file = self.mainWindow.controller.getRandomFiles(cfg["TypingTestsFolder"], 1)[0]
        fp = open(source_file, "r")
        d = json.load(fp)
        self.ui.expectedText.setText(d["expected"])
        # Just in case, clearing and setting editable
        self.secondsLeft = int(cfg["screens"][self.mainWindow.controller.curIdx]["timeLimit"])
        self.ui.lcdNumber.setText(str(self.secondsLeft))
        # setup timer thread
        self.timer = CountDownWorker(self.secondsLeft)
        self.thread = QtCore.QThread(self)
        self.timer.moveToThread(self.thread)
        self.setupSignals()
        # ensure text edit is editable
        self.ui.textEdit.clear()
        self.ui.textEdit.setReadOnly(False)

        # format text and show Tutorial dialog
        self.format_text()
        self.fadeIn(self.showDialog)

    def fadeIn(self, func=None):
        self.eff = QtWidgets.QGraphicsOpacityEffect(self)
        self.setGraphicsEffect(self.eff)
        self.a = QtCore.QPropertyAnimation(self.eff, b"opacity")
        if func:
            self.a.finished.connect(func)
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
        self.a.setDuration(1000)
        self.a.setStartValue(1)
        self.a.setEndValue(0)
        self.a.setEasingCurve(QtCore.QEasingCurve.Linear)
        self.a.start()

    def cleanup(self):
        # cleanup, disconnect signals etc
        self.ui.typingNextButton.clicked.disconnect()
        self.ui.textEdit.textChanged.disconnect()

    def showDialog(self):
        self.d = Dialog() 
        mov = QtGui.QMovie(r"G:\Interview-Helper\assets\images\cat.gif")
        self.d.ui.gifLabel.setMovie(mov)
        mov.start()
        self.d.setWindowModality(QtCore.Qt.ApplicationModal)
        self.d.show()

    def showTimeOutAlert(self):
        d = Dialog()
        d.ui.HeaderLabel.setText("Time over")
        d.ui.pushButton.setText("Ok")
        d.setWindowModality(QtCore.Qt.ApplicationModal)
        d.exec_()

    def setupSignals(self):
        self.ui.typingNextButton.clicked.connect(self.finishTask)
        self.ui.textEdit.textChanged.connect(self.calculateCurrentWord)
        self.ui.textEdit.textChanged.connect(self.format_text)
        self.ui.textEdit.selectionChanged.connect(self.startTyping)
        self.timer.timer_signal.connect(self.updateTimer)
        self.timer.timer_end.connect(self.thread.quit)
        self.thread.started.connect(self.timer.updateTimer)
        self.thread.finished.connect(self.endTyping)

    def finishTask(self):
        """
        Before going forward:
            1. stop the thread
            2. register results
            3. cleanup signals and fields
            4. go forward
        """
        if self.thread.isRunning():
            # if word that you are currently writing is equal or more than total words expected then go forward, else continue typing, you b#!_%ch!
            if self.currentWord < len(self.ui.expectedText.toPlainText().split()):
                return
            # Finish thread
            self.thread.requestInterruption()
            self.thread.quit()
            self.thread.wait()
            # emit the finished event imediately and disconnect it to avoid duplicates
            self.thread.finished.emit()
            self.thread.finished.disconnect()
        if self.thread.isFinished():
            self.gatherResults()
            self.cleanup()
            self.fadeOut(self.mainWindow.controller.nextScreen)

    def format_text(self):
        # TODO: rewrite using regular expressions
        is_highlighted = False
        self.ui.expectedText.moveCursor(QtGui.QTextCursor.End)
        cw = self.currentWord
        result = ""
        paragraphs = self.ui.expectedText.toPlainText().strip().split('\n')
        self.ui.expectedText.clear()
        for p in paragraphs:
            words = p.split()
            if cw <= len(words) and not is_highlighted:
                result += f"<span style='color: {self.currentCfg['passedTextColor']}'>{' '.join(words[:cw-1])}</span><span style='color: {self.currentCfg['highlightColor']};'> {words[cw-1]} </span>"
                is_highlighted = True
                self.ui.expectedText.setHtml(result)
                self.ui.expectedText.moveCursor(QtGui.QTextCursor.End)
                result = f"<span>{' '.join(words[cw:])}</span></p>"
            elif cw > len(words) and not is_highlighted:
                result += f"<span style='color: {self.currentCfg['passedTextColor']};'>{p}</span><br>"
                cw -= len(words)
            else:
                result += f"{p}<br>"
                cw -= len(words)
        self.ui.expectedText.insertHtml(result)
        if not is_highlighted:
            self.ui.expectedText.moveCursor(QtGui.QTextCursor.End)

    def calculateCurrentWord(self):
        words = len((self.ui.textEdit.toPlainText()+'|').split())
        self.currentWord = words if words != 0 else 1

    @QtCore.Slot(int)
    def updateTimer(self, secondsLeft):
        self.secondsLeft = secondsLeft
        self.ui.lcdNumber.setText(str(self.secondsLeft))

    def startTyping(self):
        self.startTime = time() 
        self.thread.start()
        self.ui.textEdit.selectionChanged.disconnect()

    def endTyping(self):
        """
        User stops typing:
            1. Text edit becomes uneditable
            2. self.endTime fills in
            3. Notify user about time end with a popup/smh else
        """
        self.ui.textEdit.setReadOnly(True)
        self.endTime = time()
        if self.secondsLeft == 0:
            self.showTimeOutAlert()

    def gatherResults(self):
        filename = self.mainWindow.controller.getResultFileName()
        with open(filename, "r") as fp:
            d = json.load(fp)
            d.setdefault("TypingTest", dict())
            test = d["TypingTest"]
            test["ExpectedText"] = self.ui.expectedText.toPlainText()
            test["TypedText"] = self.ui.textEdit.toPlainText()
            test["startTime"] = self.startTime
            test["endTime"] = self.endTime
        with open(filename, "w") as fp:
            json.dump(d, fp)
        
