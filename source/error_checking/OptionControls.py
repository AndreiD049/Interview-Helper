from PySide2 import QtWidgets

class CheckButton(QtWidgets.QCheckBox):

    def __init__(self, *args, **kwargs):
        super(CheckButton, self).__init__(*args, **kwargs)

    def hitButton(self, obj):
        return True
