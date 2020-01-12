import json
from src.MainWin import Ui_MainWindow
from PyQt5 import QtWidgets

class App(Ui_MainWindow):

    def __init__(self, app):
        self.app = app
        self.mainWindow = QtWidgets.QMainWindow()
        self.setupUi(self.mainWindow)
        self.setupTextEditSignal()
        self.setupStartButtonSignal()


    def initExpectedWindow(self):
        exp = self.expectedText
        # select a random file from the configuration path
        fp = open("./data/typing/sample.json")
        d = json.load(fp)
        exp.insertHtml(f"{d['expected']}")
        exp.format_text(self.textEdit.currentWord)

    def setupTextEditSignal(self):
        textEdit = self.textEdit
        textEdit.textChanged.connect(textEdit.onTextChange)
        textEdit.textChanged.connect(lambda : self.expectedText.format_text(textEdit.currentWord))

    def setupStartButtonSignal(self):
        def startPressed():
            self.initExpectedWindow()
            self.stackedWidget.setCurrentIndex(1)
            # connect the next button
            self.setupTypingNextButton()
        self.startButton.clicked.connect(startPressed)

    def setupTypingNextButton(self):
        def nextPressed():
            self.stackedWidget.setCurrentIndex(2)
        self.typingNextButton.clicked.connect(nextPressed)
