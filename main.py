import json
import sys
from src.App import App
from src.MainWin import Ui_MainWindow
from PyQt5 import QtWidgets

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
wrap = App(app, ui)
MainWindow.show()


sys.exit(wrap.app.exec_())
