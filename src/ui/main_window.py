# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/zuzanna/Wydatkoinator/ui/main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Main_window(object):
    def setupUi(self, Main_window):
        Main_window.setObjectName("Main_window")
        Main_window.resize(1145, 693)
        Main_window.setStyleSheet("QWidget {\n"
"background: #202020}\n"
"\n"
"QFrame {\n"
"background: #252525 }\n"
"\n"
"QLabel {\n"
"color: #c8beb7;\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: #182B32;\n"
"color: #c8beb7;\n"
"}\n"
"\n"
"QComboBox {\n"
"background-color: #3e3e3e;\n"
"color: #c8beb7;\n"
"}\n"
"\n"
"QLineEdit {\n"
"background-color: #3e3e3e;\n"
"color: #c8beb7;\n"
"}\n"
"\n"
"QDateEdit {\n"
"background-color: #3e3e3e;\n"
"color: #c8beb7;\n"
"}\n"
"\n"
"QListWidget { color: #c8beb7; }\n"
"QTabBar::tab {\n"
"    /* Style dla wszystkich zakładek */\n"
"    color: #c8beb7;  /* Przykładowy kolor tekstu dla zakładek */\n"
"}\n"
"")
        self.gridLayout = QtWidgets.QGridLayout(Main_window)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = TabWidget(Main_window)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabWidget.setUsesScrollButtons(False)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.home_tab = Home_tab()
        self.home_tab.setObjectName("home_tab")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/domek_kolor_32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.home_tab, icon, "")
        self.incomes_tab = Incomes_tab()
        self.incomes_tab.setObjectName("incomes_tab")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/wplywy_kolor_32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.incomes_tab, icon1, "")
        self.expenses_tab = Expenses_tab()
        self.expenses_tab.setObjectName("expenses_tab")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/wydatki_kolor_32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.expenses_tab, icon2, "")
        self.history_tab = History_tab()
        self.history_tab.setObjectName("history_tab")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/historia_kolor_32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.history_tab, icon3, "")
        self.analysis_tab = Analysis_tab()
        self.analysis_tab.setObjectName("analysis_tab")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/analiza_kolor_32.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.analysis_tab, icon4, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(Main_window)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Main_window)

    def retranslateUi(self, Main_window):
        _translate = QtCore.QCoreApplication.translate
        Main_window.setWindowTitle(_translate("Main_window", "Form"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.home_tab), _translate("Main_window", "Start"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.incomes_tab), _translate("Main_window", "Wpływy"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.expenses_tab), _translate("Main_window", "Wydatki"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.history_tab), _translate("Main_window", "Historia"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.analysis_tab), _translate("Main_window", "Analiza"))
from src.tabs.analysis_tab import Analysis_tab
from src.tabs.expenses_tab import Expenses_tab
from src.tabs.history_tab import History_tab
from src.tabs.home_tab import Home_tab
from src.tabs.horizontal_tabs import TabWidget
from src.tabs.incomes_tab import Incomes_tab
import src.resources.res_rc
