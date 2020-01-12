import json
from src.utils import select_n_valid_files
from src.validators import ValidatorErrorChecking, ValidatorTyping
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
        fp = open(select_n_valid_files(ValidatorTyping.validate, 1, r"G:\Interview-Helper\data\typing", "json")[0])
        d = json.load(fp)
        exp.insertHtml(f"{d['expected']}")
        exp.format_text(self.textEdit.currentWord)

    def initErrorCheckingArea(self):
        print("initErrorChecking")
        err_area = self.errorCheckArea
        err_area.setQuestions(select_n_valid_files(ValidatorErrorChecking.validate, 3, r"G:\Interview-Helper\data\error_checking", "json"), self)
        err_area.displayNextQuestion()

    def setupTextEditSignal(self):
        textEdit = self.textEdit
        textEdit.textChanged.connect(textEdit.onTextChange)
        textEdit.textChanged.connect(lambda : self.expectedText.format_text(textEdit.currentWord))

    def setupStartButtonSignal(self):
        def startPressed():
            self.initExpectedWindow()
            # in any case
            self.textEdit.clear()
            self.stackedWidget.setCurrentIndex(1)
            # connect the next button
            self.setupTypingNextButton()
        self.startButton.clicked.connect(startPressed)

    def setupTypingNextButton(self):
        def nextPressed():
            self.initErrorCheckingArea()
            self.stackedWidget.setCurrentIndex(2)
            self.setupErrorCheckNextButton()
            self.typingNextButton.clicked.disconnect()
        self.typingsignal = self.typingNextButton.clicked.connect(nextPressed)

    def setupErrorCheckNextButton(self):
        self.errorCheckNextButton.clicked.connect(self.errorCheckArea.onSubmitButtonPress)