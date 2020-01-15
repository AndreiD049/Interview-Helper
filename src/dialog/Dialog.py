from PyQt5 import QtWidgets
from src.dialog.ui_dialog import Ui_Dialog

class Dialog(QtWidgets.QDialog):

    def __init__(self, *args, **kwargs):
        QtWidgets.QDialog.__init__(self, *args, **kwargs)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
