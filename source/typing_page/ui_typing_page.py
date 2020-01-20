# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'typing_page.ui'
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
        Form.resize(1067, 839)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setStyleSheet(u"QTextBrowser, QTextEdit { \n"
"background-color: #3D435E;\n"
"color: #fff;\n"
"border-radius: 4px;\n"
"border: 1px solid #E9E8E8;\n"
"}\n"
"QWidget#Form {\n"
"background-color: #2D3246;\n"
"}\n"
"QLabel {\n"
"color: #fff;\n"
"}\n"
"QFrame#timeFrame {\n"
"background-color: #3D435E;\n"
"border-radius: 16px;\n"
"}\n"
"QPushButton {padding:20px;background-color:#F83E13;color:white;border:none;border-radius:4px;}\n"
"QPushButton:hover {background-color:#CF8349;}\n"
"QPushButton:pressed {margin-top:3px;}\n"
"")
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(30, 10, 30, -1)
        self.lHeader = QLabel(Form)
        self.lHeader.setObjectName(u"lHeader")
        font = QFont()
        font.setFamily(u"Roboto Light")
        font.setPointSize(60)
        font.setBold(False)
        font.setWeight(50);
        self.lHeader.setFont(font)
        self.lHeader.setTextFormat(Qt.AutoText)
        self.lHeader.setMargin(10)

        self.verticalLayout.addWidget(self.lHeader, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.timeFrame = QFrame(Form)
        self.timeFrame.setObjectName(u"timeFrame")
        self.timeFrame.setMinimumSize(QSize(103, 32))
        self.timeFrame.setMaximumSize(QSize(16777215, 16777215))
        self.timeFrame.setFrameShape(QFrame.StyledPanel)
        self.timeFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.timeFrame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(15, 3, 15, 3)
        self.label_2 = QLabel(self.timeFrame)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setMinimumSize(QSize(0, 0))
        self.label_2.setPixmap(QPixmap(u"G:/Interview-Helper/assets/icons/timer_white_1x.png"))
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_2.setMargin(0)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lcdNumber = QLabel(self.timeFrame)
        self.lcdNumber.setObjectName(u"lcdNumber")
        font1 = QFont()
        font1.setFamily(u"Roboto")
        font1.setPointSize(14)
        self.lcdNumber.setFont(font1)
        self.lcdNumber.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.lcdNumber)


        self.verticalLayout.addWidget(self.timeFrame, 0, Qt.AlignRight|Qt.AlignTop)

        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")

        self.verticalLayout.addWidget(self.widget)

        self.verticalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.expectedText = QTextBrowser(Form)
        self.expectedText.setObjectName(u"expectedText")
        self.expectedText.setMinimumSize(QSize(0, 200))
        font2 = QFont()
        font2.setFamily(u"Roboto")
        font2.setPointSize(18)
        self.expectedText.setFont(font2)
        self.expectedText.setStyleSheet(u"")
        self.expectedText.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.expectedText.setReadOnly(True)
        self.expectedText.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout.addWidget(self.expectedText)

        self.verticalSpacer_4 = QSpacerItem(20, 68, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.textEdit = QTextEdit(Form)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(0, 200))
        font3 = QFont()
        font3.setFamily(u"Roboto")
        font3.setPointSize(20)
        self.textEdit.setFont(font3)
        self.textEdit.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.textEdit)

        self.verticalSpacer_2 = QSpacerItem(20, 68, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.typingNextButton = QPushButton(Form)
        self.typingNextButton.setObjectName(u"typingNextButton")
        sizePolicy1.setHeightForWidth(self.typingNextButton.sizePolicy().hasHeightForWidth())
        self.typingNextButton.setSizePolicy(sizePolicy1)
        self.typingNextButton.setMinimumSize(QSize(150, 60))
        font4 = QFont()
        font4.setFamily(u"Roboto Black")
        font4.setPointSize(18)
        font4.setBold(True)
        font4.setWeight(75);
        self.typingNextButton.setFont(font4)
        self.typingNextButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.typingNextButton.setAutoFillBackground(False)
        self.typingNextButton.setStyleSheet(u"")
        self.typingNextButton.setAutoDefault(False)
        self.typingNextButton.setFlat(False)

        self.verticalLayout.addWidget(self.typingNextButton, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.verticalSpacer_3 = QSpacerItem(20, 68, QSizePolicy.Minimum, QSizePolicy.Preferred)

        self.verticalLayout.addItem(self.verticalSpacer_3)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.retranslateUi(Form)

        self.typingNextButton.setDefault(True)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lHeader.setText(QCoreApplication.translate("Form", u"Typing Test", None))
        self.label_2.setText("")
        self.lcdNumber.setText(QCoreApplication.translate("Form", u"55", None))
        self.expectedText.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Roboto'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.textEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Place cursor here and start typing...", None))
        self.typingNextButton.setText(QCoreApplication.translate("Form", u"Submit", None))
    # retranslateUi

