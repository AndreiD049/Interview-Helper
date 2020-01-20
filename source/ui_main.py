# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\untitled_main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(1200, 800)
        Main.showMaximized()
        self.centralwidget = QtWidgets.QWidget(Main)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget#centralwidget {background-color: '#2D3246'}"
"QWidget#StartPage {background-color: #2D3246;}\n"
"QLabel {color: #fff;}\n"
"QLabel#AssistiveText {color: rgba(255, 255, 255, 0.5);}\n"
"QLineEdit {background-color: #3D435E;border-radius: 4px;border: 1px solid #E9E8E8;color: #fff;}\n"
"QPushButton {padding:20px;background-color:#F83E13;color:white;border:none;border-radius:4px;}\n"
"QPushButton:hover {background-color:#CF8349;}\n"
"QPushButton:pressed {margin-top:3px;}")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.horizontalLayout.addWidget(self.stackedWidget)
        Main.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        Main.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Main)
        self.statusbar.setObjectName("statusbar")
        Main.setStatusBar(self.statusbar)

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "MainWindow"))
