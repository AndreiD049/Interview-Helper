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
        StartPage.resize(568, 407)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(StartPage.sizePolicy().hasHeightForWidth())
        StartPage.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(StartPage)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(StartPage)
        self.pushButton.setObjectName(u"pushButton")
        font = QFont()
        font.setFamily(u"Roboto Black")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75);
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setLayoutDirection(Qt.LeftToRight)
        self.pushButton.setStyleSheet(u"QPushButton {padding:10px;background-color:red;color:white;border:none;}\n"
"QPushButton:hover {background-color:coral;}\n"
"QPushButton:pressed {margin-top:3px;}")

        self.horizontalLayout.addWidget(self.pushButton, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.retranslateUi(StartPage)

        QMetaObject.connectSlotsByName(StartPage)
    # setupUi

    def retranslateUi(self, StartPage):
        StartPage.setWindowTitle(QCoreApplication.translate("StartPage", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("StartPage", u"PushButton", None))
    # retranslateUi

