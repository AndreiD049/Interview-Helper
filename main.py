import sys
from ui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets

def hello():
    print("Hello there")

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

ui.pushButton.clicked.connect(hello)

sys.exit(app.exec_())
