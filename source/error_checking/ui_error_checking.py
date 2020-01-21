# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'error_checking.ui'
##
## Created by: Qt User Interface Compiler version 5.14.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient, QCursor)
from PySide2.QtWidgets import *

class Ui_Form(object):
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1083, 828)
        Form.setCursor(QCursor(Qt.ArrowCursor))
        Form.setAutoFillBackground(False)
        Form.setStyleSheet(u"QWidget#Form, QWidget#scrollAreaWidgetContents {\n"
"background-color:#2D3246;\n"
"}\n"
"QWidget#OptionFrame, QFrame#QuestionFrame { \n"
"background-color: #3D435E;\n"
"color: #fff;\n"
"border-radius: 4px;\n"
"border: 1px solid #E9E8E8;\n"
"}\n"
"QLabel {\n"
"color: #fff;\n"
"}\n"
"QLabel#questionLabel, QLabel#lcdNumber {\n"
"font: 16px \"Roboto\", Arial, Helvetica, sans-serif;\n"
"}\n"
"QLabel#questionCounter, QLabel#questionHeader {\n"
"font: 24px \"Roboto Light\", Arial, Helvetica, sans-serif;\n"
"}\n"
"QLabel#HeaderLabel {\n"
"font: 60px \"Roboto Light\", Arial, Helvetica, sans-serif;\n"
"}\n"
"QFrame#timeFrame {\n"
"background-color: #3D435E;\n"
"border-radius: 16px;\n"
"}\n"
"QPushButton {padding:20px;background-color:#F83E13;color:white;border:none;border-radius:4px;}\n"
"QPushButton:hover {background-color:#CF8349;}\n"
"QPushButton:pressed {margin-top:3px;}\n"
"QCheckBox, QRadioButton {\n"
"font: 16px \"Roboto\", Arial, Helvetica, sans-serif;\n"
"color: #fff;\n"
"border: none;\n"
"border-radius: 4px;\n"
""
                        "background-color: #CF8349;\n"
"padding: 5px 20px 5px 10px;\n"
"}\n"
"QPushButton#typingNextButton {\n"
"font: 16px \"Roboto black\", Arial, Helvetica, sans-serif;\n"
"}")
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(Form)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1083, 828))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, -1, 20, -1)
        self.HeaderLabel = QLabel(self.scrollAreaWidgetContents)
        self.HeaderLabel.setObjectName(u"HeaderLabel")
        font = QFont()
        font.setFamily(u"Roboto Light")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50);
        self.HeaderLabel.setFont(font)

        self.verticalLayout.addWidget(self.HeaderLabel, 0, Qt.AlignHCenter)

        self.topFrame = QFrame(self.scrollAreaWidgetContents)
        self.topFrame.setObjectName(u"topFrame")
        font1 = QFont()
        font1.setFamily(u"Roboto")
        font1.setPointSize(12)
        self.topFrame.setFont(font1)
        self.topFrame.setStyleSheet(u"QRadioButton::indicator {\n"
"width: 20px;\n"
"height:20px;\n"
"}\n"
"\n"
"QRadioButton::indicator::checked {\n"
"image: url(G:/Interview-Helper/assets/images/radio_checked.png);\n"
"}\n"
"\n"
"QRadioButton::indicator::unchecked {\n"
"image: url(G:/Interview-Helper/assets/images/radio_unchecked.png);\n"
"}")
        self.topFrame.setFrameShape(QFrame.NoFrame)
        self.topFrame.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_2 = QHBoxLayout(self.topFrame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.questionCounter = QLabel(self.topFrame)
        self.questionCounter.setObjectName(u"questionCounter")
        self.questionCounter.setFont(font)

        self.horizontalLayout_2.addWidget(self.questionCounter, 0, Qt.AlignLeft)

        self.timeFrame = QFrame(self.topFrame)
        self.timeFrame.setObjectName(u"timeFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.timeFrame.sizePolicy().hasHeightForWidth())
        self.timeFrame.setSizePolicy(sizePolicy1)
        self.timeFrame.setMinimumSize(QSize(103, 32))
        self.timeFrame.setMaximumSize(QSize(16777215, 16777215))
        self.timeFrame.setFrameShape(QFrame.StyledPanel)
        self.timeFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.timeFrame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(15, 3, 15, 3)
        self.label_2 = QLabel(self.timeFrame)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setMinimumSize(QSize(0, 0))
        self.label_2.setPixmap(QPixmap(u"./assets/icons/timer_white_1x.png"))
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_2.setMargin(0)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.lcdNumber = QLabel(self.timeFrame)
        self.lcdNumber.setObjectName(u"lcdNumber")
        font2 = QFont()
        font2.setFamily(u"Roboto")
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(50);
        self.lcdNumber.setFont(font2)
        self.lcdNumber.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.lcdNumber, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.horizontalLayout_2.addWidget(self.timeFrame)


        self.verticalLayout.addWidget(self.topFrame)

        self.QuestionFrame = QFrame(self.scrollAreaWidgetContents)
        self.QuestionFrame.setObjectName(u"QuestionFrame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.QuestionFrame.sizePolicy().hasHeightForWidth())
        self.QuestionFrame.setSizePolicy(sizePolicy2)
        self.QuestionFrame.setMinimumSize(QSize(0, 0))
        self.QuestionFrame.setFrameShape(QFrame.StyledPanel)
        self.QuestionFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.QuestionFrame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.imgLabel = QLabel(self.QuestionFrame)
        self.imgLabel.setObjectName(u"imgLabel")
        self.imgLabel.setMaximumSize(QSize(16777215, 16777215))
        self.imgLabel.setPixmap(QPixmap(u"./assets/images/cat.jpg"))
        self.imgLabel.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.imgLabel, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.line = QFrame(self.QuestionFrame)
        self.line.setObjectName(u"line")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy3)
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_4.addWidget(self.line)

        self.frame = QFrame(self.QuestionFrame)
        self.frame.setObjectName(u"frame")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy4)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.questionHeader = QLabel(self.frame)
        self.questionHeader.setObjectName(u"questionHeader")
        self.questionHeader.setFont(font)

        self.verticalLayout_2.addWidget(self.questionHeader, 0, Qt.AlignLeft|Qt.AlignTop)

        self.questionLabel = QLabel(self.frame)
        self.questionLabel.setObjectName(u"questionLabel")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.questionLabel.sizePolicy().hasHeightForWidth())
        self.questionLabel.setSizePolicy(sizePolicy5)
        self.questionLabel.setFont(font2)
        self.questionLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.questionLabel.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.questionLabel)


        self.horizontalLayout_4.addWidget(self.frame)


        self.verticalLayout.addWidget(self.QuestionFrame)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.OptionFrame = QFrame(self.scrollAreaWidgetContents)
        self.OptionFrame.setObjectName(u"OptionFrame")
        self.OptionFrame.setMinimumSize(QSize(0, 0))
        font3 = QFont()
        font3.setFamily(u"Roboto")
        font3.setPointSize(14)
        self.OptionFrame.setFont(font3)
        self.OptionFrame.setFrameShape(QFrame.StyledPanel)
        self.OptionFrame.setFrameShadow(QFrame.Raised)
        self.selectControls = QVBoxLayout(self.OptionFrame)
        self.selectControls.setSpacing(15)
        self.selectControls.setObjectName(u"selectControls")
        self.selectControls.setContentsMargins(-1, 20, -1, 20)
        self.checkFrame = QFrame(self.OptionFrame)
        self.checkFrame.setObjectName(u"checkFrame")
        self.checkFrame.setMinimumSize(QSize(0, 0))
        self.checkFrame.setCursor(QCursor(Qt.PointingHandCursor))
        self.checkFrame.setFrameShape(QFrame.StyledPanel)
        self.checkFrame.setFrameShadow(QFrame.Raised)
        self.selectBox = QVBoxLayout(self.checkFrame)
        self.selectBox.setSpacing(10)
        self.selectBox.setObjectName(u"selectBox")
        self.selectBox.setContentsMargins(0, 0, 0, 0)

        self.selectControls.addWidget(self.checkFrame, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout.addWidget(self.OptionFrame)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.typingNextButton = QPushButton(self.scrollAreaWidgetContents)
        self.typingNextButton.setObjectName(u"typingNextButton")
        sizePolicy1.setHeightForWidth(self.typingNextButton.sizePolicy().hasHeightForWidth())
        self.typingNextButton.setSizePolicy(sizePolicy1)
        self.typingNextButton.setMinimumSize(QSize(150, 60))
        font4 = QFont()
        font4.setFamily(u"Roboto black")
        font4.setBold(False)
        font4.setItalic(False)
        font4.setWeight(50);
        self.typingNextButton.setFont(font4)

        self.verticalLayout.addWidget(self.typingNextButton, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout.addWidget(self.scrollArea)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.HeaderLabel.setText(QCoreApplication.translate("Form", u"Error Checking", None))
        self.questionCounter.setText(QCoreApplication.translate("Form", u"1/4", None))
        self.label_2.setText("")
        self.lcdNumber.setText(QCoreApplication.translate("Form", u"55", None))
        self.imgLabel.setText("")
        self.questionHeader.setText(QCoreApplication.translate("Form", u"Question:", None))
        self.questionLabel.setText(QCoreApplication.translate("Form", u"To convert the earlier example to a unittest test case, you would have to:\n"
"\n"
"Import unittest from the standard library\n"
"Create a class called TestSum that inherits from the TestCase class\n"
"Convert the test functions into methods by adding self as the first argument\n"
"Change the assertions to use the self.assertEqual() method on the TestCase class\n"
"Change the command-line entry point to call unittest.main()", None))
        self.typingNextButton.setText(QCoreApplication.translate("Form", u"Submit", None))
    # retranslateUi

