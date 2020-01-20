# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'start_page.ui'
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

class Ui_StartPage(object):
    def setupUi(self, StartPage):
        if StartPage.objectName():
            StartPage.setObjectName(u"StartPage")
        StartPage.resize(1145, 844)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(StartPage.sizePolicy().hasHeightForWidth())
        StartPage.setSizePolicy(sizePolicy)
        StartPage.setMinimumSize(QSize(0, 0))
        StartPage.setWindowOpacity(1.000000000000000)
        StartPage.setStyleSheet(u"QWidget#StartPage {background-color: #2D3246;}\n"
"QLabel {color: #fff;}\n"
"QLabel#AssistiveText {color: rgba(255, 255, 255, 0.5);}\n"
"QLineEdit {background-color: #3D435E;border-radius: 4px;border: 1px solid #E9E8E8;color: #fff;}\n"
"QPushButton {padding:20px;background-color:#F83E13;color:white;border:none;border-radius:4px;}\n"
"QPushButton:hover {background-color:#CF8349;}\n"
"QPushButton:pressed {margin-top:3px;}")
        self.verticalLayout = QVBoxLayout(StartPage)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.label = QLabel(StartPage)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Roboto Light")
        font.setPointSize(96)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_2 = QLabel(StartPage)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamily(u"Roboto Light")
        font1.setPointSize(60)
        self.label_2.setFont(font1)

        self.verticalLayout.addWidget(self.label_2, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.lineEdit = QLineEdit(StartPage)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy1)
        self.lineEdit.setMinimumSize(QSize(400, 60))
        font2 = QFont()
        font2.setFamily(u"Roboto")
        font2.setPointSize(16)
        self.lineEdit.setFont(font2)

        self.verticalLayout.addWidget(self.lineEdit, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.AssistiveText = QLabel(StartPage)
        self.AssistiveText.setObjectName(u"AssistiveText")
        sizePolicy1.setHeightForWidth(self.AssistiveText.sizePolicy().hasHeightForWidth())
        self.AssistiveText.setSizePolicy(sizePolicy1)
        self.AssistiveText.setMinimumSize(QSize(395, 0))
        font3 = QFont()
        font3.setFamily(u"Roboto")
        font3.setPointSize(12)
        font3.setItalic(False)
        self.AssistiveText.setFont(font3)

        self.verticalLayout.addWidget(self.AssistiveText, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.pushButton = QPushButton(StartPage)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(150, 60))
        font4 = QFont()
        font4.setFamily(u"Roboto Black")
        font4.setPointSize(18)
        font4.setBold(True)
        font4.setWeight(75);
        self.pushButton.setFont(font4)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setLayoutDirection(Qt.LeftToRight)
        self.pushButton.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.pushButton, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(StartPage)

        QMetaObject.connectSlotsByName(StartPage)
    # setupUi

    def retranslateUi(self, StartPage):
        StartPage.setWindowTitle(QCoreApplication.translate("StartPage", u"Form", None))
        self.label.setText(QCoreApplication.translate("StartPage", u"Welcome,", None))
        self.label_2.setText(QCoreApplication.translate("StartPage", u"Please enter your name below:", None))
        self.AssistiveText.setText(QCoreApplication.translate("StartPage", u"* Please enter your name", None))
        self.pushButton.setText(QCoreApplication.translate("StartPage", u"Start", None))
    # retranslateUi

