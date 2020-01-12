# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1072, 780)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("QPushButton\n"
"{\n"
"    color: white;\n"
"    background-color: red;\n"
"    padding: 10px;\n"
"    border:none;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    background-color: coral;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setStyleSheet("QTextBrowser, QTextEdit\n"
"{\n"
"    border-top: none;\n"
"    border-left: 1px solid lightgrey;\n"
"    border-right: 1px solid lightgrey;\n"
"    border-bottom: 2px solid lightgrey;\n"
"}\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.startPage = QtWidgets.QWidget()
        self.startPage.setObjectName("startPage")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.startPage)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.startButton = QtWidgets.QPushButton(self.startPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startButton.sizePolicy().hasHeightForWidth())
        self.startButton.setSizePolicy(sizePolicy)
        self.startButton.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.startButton.setFont(font)
        self.startButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.startButton.setStyleSheet("QPushButton\n"
"{\n"
"    padding: 5px;\n"
"}")
        self.startButton.setObjectName("startButton")
        self.verticalLayout_3.addWidget(self.startButton, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.stackedWidget.addWidget(self.startPage)
        self.typePage = QtWidgets.QWidget()
        self.typePage.setObjectName("typePage")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.typePage)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(30, 10, 30, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lHeader = QtWidgets.QLabel(self.typePage)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.lHeader.setFont(font)
        self.lHeader.setTextFormat(QtCore.Qt.AutoText)
        self.lHeader.setObjectName("lHeader")
        self.verticalLayout.addWidget(self.lHeader, 0, QtCore.Qt.AlignHCenter)
        self.expectedText = ExpectedTextBrowser(self.typePage)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(18)
        self.expectedText.setFont(font)
        self.expectedText.setStyleSheet("")
        self.expectedText.setReadOnly(True)
        self.expectedText.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse)
        self.expectedText.setObjectName("expectedText")
        self.verticalLayout.addWidget(self.expectedText)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.textEdit = TypingTextEdit(self.typePage)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(20)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("")
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem1)
        self.submitButton = QtWidgets.QPushButton(self.typePage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.submitButton.sizePolicy().hasHeightForWidth())
        self.submitButton.setSizePolicy(sizePolicy)
        self.submitButton.setMinimumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.submitButton.setFont(font)
        self.submitButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.submitButton.setAutoFillBackground(False)
        self.submitButton.setStyleSheet("")
        self.submitButton.setAutoDefault(False)
        self.submitButton.setDefault(True)
        self.submitButton.setFlat(False)
        self.submitButton.setObjectName("submitButton")
        self.verticalLayout.addWidget(self.submitButton, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        spacerItem2 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.stackedWidget.addWidget(self.typePage)
        self.verticalLayout_2.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1072, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.startButton.setText(_translate("MainWindow", "Start"))
        self.lHeader.setText(_translate("MainWindow", "Typing Test"))
        self.submitButton.setText(_translate("MainWindow", "Submit"))
from src.ExpectedTextBrowser import ExpectedTextBrowser
from src.TypingTextEdit import TypingTextEdit
