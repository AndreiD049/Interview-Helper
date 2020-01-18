from PySide2 import QtWidgets, QtCore, QtGui
from source.ui_main import Ui_Main
from source.start_page.StartPage import StartPage
from source.typing_page.TypingPage import TypingPage
from source.controller.Controller import Controller
from source.model.Model import Model

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