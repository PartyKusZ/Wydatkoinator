# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kubus/Pulpit/Wydatkoinator/ui/main_window.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Main_window(object):
    def setupUi(self, Main_window):
        Main_window.setObjectName("Main_window")
        Main_window.resize(760, 518)
        self.gridLayout = QtWidgets.QGridLayout(Main_window)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(Main_window)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tabWidget.addTab(self.tab_5, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(Main_window)
        self.tabWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(Main_window)

    def retranslateUi(self, Main_window):
        _translate = QtCore.QCoreApplication.translate
        Main_window.setWindowTitle(_translate("Main_window", "Form"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Main_window", "Home"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Main_window", "Wpływy"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Main_window", "Wydatki"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Main_window", "Historia"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Main_window", "Analiza"))