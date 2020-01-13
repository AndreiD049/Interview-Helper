from PyQt5 import QtWidgets, QtGui
import json

class ErrorCheckingArea(QtWidgets.QScrollArea):

    def __init__(self, *args, **kwargs):
        super(ErrorCheckingArea, self).__init__()

    def setQuestions(self, files, mainwin):
        """
        Receives a list of valid file paths.
        those paths are json files containing the needed information to be displayed
        """
        self.mainwin = mainwin
        self.files = files
        self.c_idx = 0          # current file index (invariant: we need to display item @c_idx + 1)

    def displayNextQuestion(self):
        try:
            with open(self.files[self.c_idx], 'r') as fp:
                d = json.load(fp)
                # set image
                pix = QtGui.QPixmap(d['image'])
                self.mainwin.imgErrorLabel.setPixmap(pix)
                # set question
                self.mainwin.lErrorCheckQuestion.setPlainText(d['question'])
                self.mainwin.cmbErrorCheck.clear()
                self.mainwin.cmbErrorCheck.addItems(d['options'])
        except NameError:
            raise NameError("Method setQuestions should be called first")

    def onSubmitButtonPress(self):
        print(self.c_idx)
        self.c_idx += 1
        if self.c_idx >= len(self.files):
            # show next screen
            self.mainwin.stackedWidget.setCurrentIndex(0)
            self.mainwin.errorCheckNextButton.clicked.disconnect()
        else:
            self.displayNextQuestion()