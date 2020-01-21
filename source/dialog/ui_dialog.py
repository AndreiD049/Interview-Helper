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
        Dialog.resize(629, 645)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setStyleSheet(u"QDialog {background-color: #3D435E;}\n"
"QLabel {color: #fff;}\n"
"QPushButton {padding:20px;background-color:#F83E13;color:white;border:none;border-radius:4px;font: 16px \"Roboto Black\", Arial, Helvetica, sans-serif;}\n"
"QPushButton:hover {background-color:#CF8349;}\n"
"QPushButton:pressed {margin-top:3px;}\n"
"QLabel#HeaderLabel {\n"
"font: 60px \"Roboto Light\", Arial, Helvetica, sans-serif;\n"
"}\n"
"QLabel#infoLabel {\n"
"font: 16px \"Roboto\", Arial, Helvetica, sans-serif;\n"
"}")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.HeaderLabel = QLabel(Dialog)
        self.HeaderLabel.setObjectName(u"HeaderLabel")
        font = QFont()
        font.setFamily(u"Roboto Light")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50);
        self.HeaderLabel.setFont(font)

        self.verticalLayout.addWidget(self.HeaderLabel, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.gifLabel = QLabel(Dialog)
        self.gifLabel.setObjectName(u"gifLabel")
        sizePolicy.setHeightForWidth(self.gifLabel.sizePolicy().hasHeightForWidth())
        self.gifLabel.setSizePolicy(sizePolicy)
        self.gifLabel.setMinimumSize(QSize(592, 0))
        self.gifLabel.setMaximumSize(QSize(16777215, 300))
        self.gifLabel.setPixmap(QPixmap(u"C:/Users/\u0410\u043d\u0434\u0440\u0435\u0439/Desktop/cat.jpg"))
        self.gifLabel.setScaledContents(True)

        self.verticalLayout.addWidget(self.gifLabel, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.infoLabel = QLabel(Dialog)
        self.infoLabel.setObjectName(u"infoLabel")
        sizePolicy.setHeightForWidth(self.infoLabel.sizePolicy().hasHeightForWidth())
        self.infoLabel.setSizePolicy(sizePolicy)
        self.infoLabel.setMinimumSize(QSize(0, 100))
        font1 = QFont()
        font1.setFamily(u"Roboto")
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(50);
        self.infoLabel.setFont(font1)
        self.infoLabel.setAlignment(Qt.AlignCenter)
        self.infoLabel.setWordWrap(True)

        self.verticalLayout.addWidget(self.infoLabel, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(150, 60))
        font2 = QFont()
        font2.setFamily(u"Roboto Black")
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(50);
        self.pushButton.setFont(font2)
        self.pushButton.setStyleSheet(u"")
        self.pushButton.setAutoDefault(False)

        self.verticalLayout.addWidget(self.pushButton, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.HeaderLabel.setText(QCoreApplication.translate("Dialog", u"Useful info", None))
        self.gifLabel.setText("")
        self.infoLabel.setText(QCoreApplication.translate("Dialog", u"Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Got it", None))
    # retranslateUi

