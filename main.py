import json
import sys
from src.AppView import MainWindow
from PyQt5 import QtWidgets

app = QtWidgets.QApplication(sys.argv)
main = MainWindow()
main.show()
main.startUp()
sys.exit(app.exec_())
