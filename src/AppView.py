from PyQt5 import QtWidgets, QtCore, QtGui
from src.ui_main import Ui_Main
from src.start_page.StartPage import StartPage
from src.typing_page.TypingPage import TypingPage
from src.controller.Controller import Controller
from src.model.Model import Model

class MainWindow(QtWidgets.QMainWindow):

    """
    This class should be the connection glue between 
    """

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_Main()
        self.ui.setupUi(self)
        self.controller = Controller(self)
        self.model = Model(self.controller)
        self.controller.setModel(self.model)


    def startUp(self):
        self.startPage = StartPage(self) 
        self.startPage.showDialog()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    main = MainWindow()
    main.show()
    main.startUp()
    app.exec_()