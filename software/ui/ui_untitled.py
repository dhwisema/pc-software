# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledHvTHKF.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(330, 282, 149, 28))
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(330, 198, 149, 77))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.TeamA_Number = QComboBox(self.layoutWidget)
        self.TeamA_Number.addItem("")
        self.TeamA_Number.addItem("")
        self.TeamA_Number.addItem("")
        self.TeamA_Number.addItem("")
        self.TeamA_Number.addItem("")
        self.TeamA_Number.addItem("")
        self.TeamA_Number.addItem("")
        self.TeamA_Number.addItem("")
        self.TeamA_Number.setObjectName(u"TeamA_Number")

        self.gridLayout.addWidget(self.TeamA_Number, 0, 0, 1, 1)

        self.TeamB_Number = QComboBox(self.layoutWidget)
        self.TeamB_Number.addItem("")
        self.TeamB_Number.addItem("")
        self.TeamB_Number.addItem("")
        self.TeamB_Number.addItem("")
        self.TeamB_Number.addItem("")
        self.TeamB_Number.addItem("")
        self.TeamB_Number.addItem("")
        self.TeamB_Number.addItem("")
        self.TeamB_Number.setObjectName(u"TeamB_Number")

        self.gridLayout.addWidget(self.TeamB_Number, 0, 1, 1, 1)

        self.TeamA = QLabel(self.layoutWidget)
        self.TeamA.setObjectName(u"TeamA")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TeamA.sizePolicy().hasHeightForWidth())
        self.TeamA.setSizePolicy(sizePolicy)
        self.TeamA.setMinimumSize(QSize(60, 10))
        self.TeamA.setStyleSheet(u"    #TeamA {\n"
"       background-color: white;\n"
"		\n"
"	font: 10pt \"MS Shell Dlg 2\";\n"
"    }")

        self.gridLayout.addWidget(self.TeamA, 1, 0, 1, 1)

        self.TeamB = QLabel(self.layoutWidget)
        self.TeamB.setObjectName(u"TeamB")
        sizePolicy.setHeightForWidth(self.TeamB.sizePolicy().hasHeightForWidth())
        self.TeamB.setSizePolicy(sizePolicy)
        self.TeamB.setMinimumSize(QSize(0, 0))
        self.TeamB.setBaseSize(QSize(60, 10))
        self.TeamB.setStyleSheet(u"    #TeamB {\n"
"    background-color: white;	\n"
"	font: 10pt \"MS Shell Dlg 2\";\n"
"    }")
        self.TeamB.setScaledContents(False)

        self.gridLayout.addWidget(self.TeamB, 1, 1, 1, 1)

        self.descript1 = QLabel(self.centralwidget)
        self.descript1.setObjectName(u"descript1")
        self.descript1.setGeometry(QRect(330, 170, 106, 21))
        sizePolicy.setHeightForWidth(self.descript1.sizePolicy().hasHeightForWidth())
        self.descript1.setSizePolicy(sizePolicy)
        self.descript1.setStyleSheet(u"    #descript1 {\n"
"    background-color: white;	\n"
"	font: 10pt \"MS Shell Dlg 2\";\n"
"    }")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 26))
        self.menuSettings = QMenu(self.menubar)
        self.menuSettings.setObjectName(u"menuSettings")
        self.menuManual_Queue = QMenu(self.menubar)
        self.menuManual_Queue.setObjectName(u"menuManual_Queue")
        self.menuManual_Queue.setAutoFillBackground(True)
        self.menuAutomatic = QMenu(self.menubar)
        self.menuAutomatic.setObjectName(u"menuAutomatic")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuManual_Queue.menuAction())
        self.menubar.addAction(self.menuAutomatic.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Send Message", None))
        self.TeamA_Number.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.TeamA_Number.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.TeamA_Number.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.TeamA_Number.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))
        self.TeamA_Number.setItemText(4, QCoreApplication.translate("MainWindow", u"5", None))
        self.TeamA_Number.setItemText(5, QCoreApplication.translate("MainWindow", u"6", None))
        self.TeamA_Number.setItemText(6, QCoreApplication.translate("MainWindow", u"7", None))
        self.TeamA_Number.setItemText(7, QCoreApplication.translate("MainWindow", u"8", None))

        self.TeamB_Number.setItemText(0, QCoreApplication.translate("MainWindow", u"1", None))
        self.TeamB_Number.setItemText(1, QCoreApplication.translate("MainWindow", u"2", None))
        self.TeamB_Number.setItemText(2, QCoreApplication.translate("MainWindow", u"3", None))
        self.TeamB_Number.setItemText(3, QCoreApplication.translate("MainWindow", u"4", None))
        self.TeamB_Number.setItemText(4, QCoreApplication.translate("MainWindow", u"5", None))
        self.TeamB_Number.setItemText(5, QCoreApplication.translate("MainWindow", u"6", None))
        self.TeamB_Number.setItemText(6, QCoreApplication.translate("MainWindow", u"7", None))
        self.TeamB_Number.setItemText(7, QCoreApplication.translate("MainWindow", u"8", None))

        self.TeamA.setText(QCoreApplication.translate("MainWindow", u"Team A", None))
        self.TeamB.setText(QCoreApplication.translate("MainWindow", u"Team B", None))
        self.descript1.setText(QCoreApplication.translate("MainWindow", u"Manual Queue", None))
        self.menuSettings.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.menuManual_Queue.setTitle(QCoreApplication.translate("MainWindow", u"Manual Queue", None))
        self.menuAutomatic.setTitle(QCoreApplication.translate("MainWindow", u"Automatic", None))
    # retranslateUi

