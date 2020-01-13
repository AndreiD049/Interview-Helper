from PyQt5 import QtWidgets, QtCore, QtGui
from src.ui_main import Ui_Main
from src.start_page.StartPage import StartPage
from src.typing_page.TypingPage import TypingPage


class MainWindow(QtWidgets.QMainWindow, Ui_Main):

    """
    This class should be the connection glue between 
    """

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)


    def startUp(self):
        self.startPage = StartPage(self) 
        self.startPage.showDialog()
        TypingPage(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    main = MainWindow()
    main.show()
    main.startUp()
    app.exec_()