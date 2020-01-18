# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(610, 451)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.HeaderLabel = QLabel(Dialog)
        self.HeaderLabel.setObjectName(u"HeaderLabel")
        font = QFont()
        font.setFamily(u"Roboto Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75);
        self.HeaderLabel.setFont(font)

        self.verticalLayout.addWidget(self.HeaderLabel)

        self.gifLabel = QLabel(Dialog)
        self.gifLabel.setObjectName(u"gifLabel")
        sizePolicy.setHeightForWidth(self.gifLabel.sizePolicy().hasHeightForWidth())
        self.gifLabel.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.gifLabel, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.infoLabel = QLabel(Dialog)
        self.infoLabel.setObjectName(u"infoLabel")
        font1 = QFont()
        font1.setFamily(u"Roboto")
        font1.setPointSize(14)
        self.infoLabel.setFont(font1)

        self.verticalLayout.addWidget(self.infoLabel)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(100, 0))
        font2 = QFont()
        font2.setFamily(u"Roboto Black")
        font2.setPointSize(18)
        font2.setBold(True)
        font2.setWeight(75);
        self.pushButton.setFont(font2)
        self.pushButton.setStyleSheet(u"QPushButton {padding:10px;background-color:red;color:white;border:none;}\n"
"QPushButton:hover {background-color:coral;}\n"
"QPushButton:pressed {margin-top:3px;}")
        self.pushButton.setAutoDefault(False)

        self.verticalLayout.addWidget(self.pushButton, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.HeaderLabel.setText("")
        self.gifLabel.setText("")
        self.infoLabel.setText("")
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Got it", None))
    # retranslateUi

