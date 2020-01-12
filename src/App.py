import json

class App:

    def __init__(self, app, ui):
        self.app = app
        self.ui = ui
        self.initExpectedWindow()
        self.setupTextEditSignal()
        self.setupStartButtonSignal()

    def initExpectedWindow(self):
        exp = self.ui.expectedText
        fp = open("./data/typing/sample.json")
        d = json.load(fp)
        exp.insertHtml(f"{d['expected']}")
        exp.format_text(self.ui.textEdit.currentWord)

    def setupTextEditSignal(self):
        textEdit = self.ui.textEdit
        textEdit.textChanged.connect(textEdit.onTextChange)
        textEdit.textChanged.connect(lambda : self.ui.expectedText.format_text(textEdit.currentWord))

    def setupStartButtonSignal(self):
        self.ui.startButton.clicked.connect(lambda : self.ui.stackedWidget.setCurrentIndex(1))
