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
    QRadialGradient)
from PySide2.QtWidgets import *

class Ui_Form(object):
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(879, 770)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet(u"\n"
"QPushButton {padding:10px;background-color:red;color:white;border:none;}\n"
"QPushButton:hover {background-color:coral;}\n"
"QPushButton:pressed {margin-top:3px;}\n"
"QTextBrowser, QTextEdit { border-top: none; border-left: 1px solid lightgrey; border-right: 1px solid lightgrey; border-bottom: 2px solid lightgrey;}\n"
"")
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(20, -1, 20, -1)
        self.scrollArea = QScrollArea(Form)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 839, 752))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.HeaderLabel = QLabel(self.scrollAreaWidgetContents)
        self.HeaderLabel.setObjectName(u"HeaderLabel")
        font = QFont()
        font.setFamily(u"Roboto Black")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75);
        self.HeaderLabel.setFont(font)

        self.verticalLayout.addWidget(self.HeaderLabel, 0, Qt.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.introLabel = QLabel(self.scrollAreaWidgetContents)
        self.introLabel.setObjectName(u"introLabel")
        font1 = QFont()
        font1.setFamily(u"Roboto Black")
        font1.setPointSize(18)
        font1.setBold(True)
        font1.setWeight(75);
        self.introLabel.setFont(font1)

        self.verticalLayout.addWidget(self.introLabel, 0, Qt.AlignLeft|Qt.AlignTop)

        self.verticalSpacer_4 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.lcdNumber = QLCDNumber(self.scrollAreaWidgetContents)
        self.lcdNumber.setObjectName(u"lcdNumber")
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(161, 159, 159, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Light, brush)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush2 = QBrush(QColor(0, 0, 0, 128))
        brush2.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.lcdNumber.setPalette(palette)
        self.lcdNumber.setFrameShape(QFrame.NoFrame)
        self.lcdNumber.setFrameShadow(QFrame.Plain)

        self.verticalLayout.addWidget(self.lcdNumber, 0, Qt.AlignRight|Qt.AlignTop)

        self.imgLabel = QLabel(self.scrollAreaWidgetContents)
        self.imgLabel.setObjectName(u"imgLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imgLabel.sizePolicy().hasHeightForWidth())
        self.imgLabel.setSizePolicy(sizePolicy)
        self.imgLabel.setMinimumSize(QSize(100, 200))

        self.verticalLayout.addWidget(self.imgLabel, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.verticalSpacer_5 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.textBrowser = QTextBrowser(self.scrollAreaWidgetContents)
        self.textBrowser.setObjectName(u"textBrowser")
        font2 = QFont()
        font2.setFamily(u"Roboto")
        font2.setPointSize(18)
        self.textBrowser.setFont(font2)

        self.verticalLayout.addWidget(self.textBrowser)

        self.verticalSpacer_6 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_6)

        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName(u"frame")
        font3 = QFont()
        font3.setFamily(u"Roboto")
        font3.setPointSize(12)
        self.frame.setFont(font3)
        self.frame.setStyleSheet(u"QRadioButton::indicator {\n"
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
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Sunken)
        self.radioButtonsLayout = QVBoxLayout(self.frame)
        self.radioButtonsLayout.setObjectName(u"radioButtonsLayout")

        self.verticalLayout.addWidget(self.frame)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.pushButton = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font1)

        self.verticalLayout.addWidget(self.pushButton, 0, Qt.AlignHCenter|Qt.AlignVCenter)

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
        self.introLabel.setText(QCoreApplication.translate("Form", u"See image, read the question, and choose the right answer below:", None))
#if QT_CONFIG(accessibility)
        self.imgLabel.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.imgLabel.setText("")
        self.pushButton.setText(QCoreApplication.translate("Form", u"Submit", None))
    # retranslateUi

