from PyQt5 import QtCore, QtWidgets

class ExpectedTextBrowser(QtWidgets.QTextBrowser):

    def __init__(self, *args, **kwargs):
        super(ExpectedTextBrowser, self).__init__(*args, **kwargs)

    def format_text(self, cw):
        text = self.toPlainText().split(" ")
        if cw <= len(text):
            self.setHtml(f"<b><span style='color: lightgray'>{' '.join(text[:cw-1])}</span><span style='color: blue'> {text[cw-1]} </span>{' '.join(text[cw:])}</b>")
