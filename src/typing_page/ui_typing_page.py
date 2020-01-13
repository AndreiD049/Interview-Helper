# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\typing_page.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(896, 643)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setStyleSheet("QPushButton { color: white;background-color: red; padding: 10px; border:none;}\n"
"QPushButton:hover { background-color: coral;}\n"
"QTextBrowser, QTextEdit { border-top: none; border-left: 1px solid lightgrey; border-right: 1px solid lightgrey; border-bottom: 2px solid lightgrey;}\n"
"")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(30, 10, 30, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lHeader = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.lHeader.setFont(font)
        self.lHeader.setTextFormat(QtCore.Qt.AutoText)
        self.lHeader.setObjectName("lHeader")
        self.verticalLayout.addWidget(self.lHeader, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.expectedText = QtWidgets.QTextBrowser(Form)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(18)
        self.expectedText.setFont(font)
        self.expectedText.setStyleSheet("")
        self.expectedText.setReadOnly(True)
        self.expectedText.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.expectedText.setObjectName("expectedText")
        self.verticalLayout.addWidget(self.expectedText)
        self.textEdit = QtWidgets.QTextEdit(Form)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(20)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("")
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem1)
        self.typingNextButton = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.typingNextButton.sizePolicy().hasHeightForWidth())
        self.typingNextButton.setSizePolicy(sizePolicy)
        self.typingNextButton.setMinimumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.typingNextButton.setFont(font)
        self.typingNextButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.typingNextButton.setAutoFillBackground(False)
        self.typingNextButton.setStyleSheet("")
        self.typingNextButton.setAutoDefault(False)
        self.typingNextButton.setDefault(True)
        self.typingNextButton.setFlat(False)
        self.typingNextButton.setObjectName("typingNextButton")
        self.verticalLayout.addWidget(self.typingNextButton, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        spacerItem2 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lHeader.setText(_translate("Form", "Typing Test"))
        self.expectedText.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Roboto\'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.typingNextButton.setText(_translate("Form", "Submit"))
