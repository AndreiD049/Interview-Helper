# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\start_page.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_StartPage(object):
    def setupUi(self, StartPage):
        StartPage.setObjectName("StartPage")
        StartPage.resize(568, 407)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(StartPage.sizePolicy().hasHeightForWidth())
        StartPage.setSizePolicy(sizePolicy)
        self.horizontalLayout = QtWidgets.QHBoxLayout(StartPage)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(StartPage)
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton.setStyleSheet("QPushButton {padding:10px;background-color:red;color:white;border:none;}\n"
"QPushButton:hover {background-color:coral;}\n"
"QPushButton:pressed {margin-top:3px;}")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)

        self.retranslateUi(StartPage)
        QtCore.QMetaObject.connectSlotsByName(StartPage)

    def retranslateUi(self, StartPage):
        _translate = QtCore.QCoreApplication.translate
        StartPage.setWindowTitle(_translate("StartPage", "Form"))
        self.pushButton.setText(_translate("StartPage", "PushButton"))
