from PyQt5 import QtCore, QtWidgets

class TypingTextEdit(QtWidgets.QTextEdit):

    def __init__(self, *args, **kwargs):
        super(TypingTextEdit, self).__init__()
        self.currentWord = 1
        

    def keyPressEvent(self, e):
        # Do default behaviour
        super(TypingTextEdit, self).keyPressEvent(e)

    def onTextChange(self):
        words = len(self.toPlainText().split(" "))
        self.currentWord = words if words != 0 else 1

    
