import json
from PyQt5 import QtWidgets, QtGui, QtCore
from src.typing_page.ui_typing_page import Ui_Form
from src.dialog.Dialog import Dialog


class CountDownThread(QtCore.QThread):

    def __init__(self, widget):
        super(CountDownThread, self).__init__()
        self.widget = widget
        self.lcd = widget.ui.lcdNumber
        
    def run(self):
        while self.lcd.value() > 0:
            QtCore.QThread.msleep(1000)
            self.lcd.display(self.lcd.value() - 1)


class TypingPage(QtWidgets.QWidget):

    def __init__(self, *args, **kwargs):
        QtWidgets.QWidget.__init__(self, *args, **kwargs)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.currentWord = 1
        self.mainWindow = self.parent()
        self.mainWindow.typingPage = self
        self.mainWindow.ui.stackedWidget.addWidget(self)
        self.setupSignals()

    def startUp(self):
        # show all content
        # get a random file from folder
        cfg = self.mainWindow.controller.config
        source_file = self.mainWindow.controller.getRandomFiles(cfg["TypingTestsFolder"], 1)[0]
        fp = open(source_file, "r")
        d = json.load(fp)
        self.ui.expectedText.setText(d["expected"])
        self.ui.textEdit.clear()
        self.ui.textEdit.setReadOnly(False)
        self.countDownThread = CountDownThread(self)
        self.ui.lcdNumber.display(cfg["screens"][self.mainWindow.controller.curIdx]["timeLimit"])
        self.format_text()
        self.showDialog()

    def showDialog(self):
        d = Dialog() 
        mov = QtGui.QMovie(r"G:\Interview-Helper\assets\images\cat.gif")
        d.ui.gifLabel.setMovie(mov)
        d.ui.pushButton.clicked.connect(d.close)
        mov.start()
        d.setWindowModality(QtCore.Qt.ApplicationModal)
        d.exec_()

    def setupSignals(self):
        def onBtnPress():
                self.countDownThread.quit()
                self.countDownThread.wait()
                self.mainWindow.controller.nextScreen()
        self.ui.typingNextButton.clicked.connect(onBtnPress)
        self.ui.textEdit.textChanged.connect(self.calculateCurrentWord)
        self.ui.textEdit.textChanged.connect(self.format_text)
        self.ui.textEdit.selectionChanged.connect(self.startCountdown)

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
                result += f"<span style='color: lightgray'>{' '.join(words[:cw-1])}</span><span style='color: blue;'> {words[cw-1]} </span>"
                is_highlighted = True
                self.ui.expectedText.setHtml(result)
                self.ui.expectedText.moveCursor(QtGui.QTextCursor.End)
                result = f"<span>{' '.join(words[cw:])}</span></p>"
            elif cw > len(words) and not is_highlighted:
                result += f"<span style='color: lightgray;'>{p}</span><br>"
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

    def countDown(self):
        self.countDownThread.finished.connect(lambda: self.ui.textEdit.setReadOnly(True))
        print("starting")
        self.countDownThread.start()

    def startCountdown(self):
        print("setC")
        self.countDown()
        self.ui.textEdit.selectionChanged.disconnect()