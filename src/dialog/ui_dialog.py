# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(610, 451)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.HeaderLabel = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.HeaderLabel.setFont(font)
        self.HeaderLabel.setText("")
        self.HeaderLabel.setObjectName("HeaderLabel")
        self.verticalLayout.addWidget(self.HeaderLabel, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.gifLabel = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gifLabel.sizePolicy().hasHeightForWidth())
        self.gifLabel.setSizePolicy(sizePolicy)
        self.gifLabel.setText("")
        self.gifLabel.setObjectName("gifLabel")
        self.verticalLayout.addWidget(self.gifLabel, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.infoLabel = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        self.infoLabel.setFont(font)
        self.infoLabel.setText("")
        self.infoLabel.setObjectName("infoLabel")
        self.verticalLayout.addWidget(self.infoLabel)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {padding:10px;background-color:red;color:white;border:none;}\n"
"QPushButton:hover {background-color:coral;}\n"
"QPushButton:pressed {margin-top:3px;}")
        self.pushButton.setAutoDefault(False)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Got it"))
