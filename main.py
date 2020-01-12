import json
import sys
from src.App import App
from src.MainWin import Ui_MainWindow
from PyQt5 import QtWidgets

wrapper = App(QtWidgets.QApplication(sys.argv))
wrapper.mainWindow.show()
sys.exit(wrapper.app.exec_())
