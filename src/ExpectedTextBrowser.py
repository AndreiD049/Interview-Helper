from PyQt5 import QtCore, QtWidgets
import os, sys

class ExpectedTextBrowser(QtWidgets.QTextBrowser):

    def __init__(self, *args, **kwargs):
        super(ExpectedTextBrowser, self).__init__(*args, **kwargs)

    def format_text(self, cw):
        is_highlighted = False
        result = ""
        paragraphs = self.toPlainText().split('\n')
        for p in paragraphs:
            words = p.split()
            if cw <= len(words) and not is_highlighted:
                result += f"<p><span style='color: lightgray'>{' '.join(words[:cw-1])}</span><span style='color: blue;'> {words[cw-1]} </span><span>{' '.join(words[cw:])}</span></p>"
                is_highlighted = True
            elif cw > len(words) and not is_highlighted:
                result += f"<p><span style='color: lightgray;'>{p}</span></p>"
                cw -= len(words)
            else:
                result += f"<p>{p}</p>"
                cw -= len(words)
        self.setHtml(result)
        # text = self.toPlainText().split(" ")
        # if cw <= len(text):
        #     self.setHtml(f"<b><span style='color: lightgray'>{' '.join(text[:cw-1])}</span><span style='color: blue'> {text[cw-1]} </span>{' '.join(text[cw:])}</b>")
