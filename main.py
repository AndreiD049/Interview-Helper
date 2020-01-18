import json
import sys
from source.AppView import MainWindow
from PySide2 import QtWidgets

app = QtWidgets.QApplication() 
main = MainWindow()
main.show()
main.startUp()
sys.exit(app.exec_())
