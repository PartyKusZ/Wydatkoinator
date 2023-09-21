# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/zuzanna/Wydatkoinator/ui/history_tab.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_history_tab(object):
    def setupUi(self, history_tab):
        history_tab.setObjectName("history_tab")
        history_tab.resize(596, 412)
        history_tab.setStyleSheet("QWidget {\n"
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
"QHeaderView::section {\n"
"    background-color: transparent;  /* brak tła */\n"
"    color:#C8BEB7;  /* kolor napisu */\n"
"     border-top: 4px solid  #182B32;\n"
"    border-bottom: 4px solid  #182B32;;\n"
"    border-left: none;\n"
"    border-right: none;\n"
" font-size: 20px;  /* Ustawienie rozmiaru czcionki */\n"
"}\n"
"\n"
"QTableWidget::item {\n"
"    font-size: 20px;\n"
"     color:#C8BEB7\n"
"}\n"
"QTableWidget::item:selected {\n"
"        background-color:  #252525; \n"
"color:#C8BEB7 ;\n"
"        border: 2px solid #C8BEB7;     \n"
"    }")
        self.gridLayout = QtWidgets.QGridLayout(history_tab)
        self.gridLayout.setObjectName("gridLayout")
        self.remove_filters_button = QtWidgets.QPushButton(history_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.remove_filters_button.sizePolicy().hasHeightForWidth())
        self.remove_filters_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.remove_filters_button.setFont(font)
        self.remove_filters_button.setObjectName("remove_filters_button")
        self.gridLayout.addWidget(self.remove_filters_button, 3, 1, 1, 1)
        self.filter_button = QtWidgets.QPushButton(history_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filter_button.sizePolicy().hasHeightForWidth())
        self.filter_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.filter_button.setFont(font)
        self.filter_button.setObjectName("filter_button")
        self.gridLayout.addWidget(self.filter_button, 3, 0, 1, 1)
        self.history_tansaction_label = QtWidgets.QLabel(history_tab)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.history_tansaction_label.setFont(font)
        self.history_tansaction_label.setAlignment(QtCore.Qt.AlignCenter)
        self.history_tansaction_label.setObjectName("history_tansaction_label")
        self.gridLayout.addWidget(self.history_tansaction_label, 0, 0, 1, 3)
        self.table = QtWidgets.QTableWidget(history_tab)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.table.setFont(font)
        self.table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table.setTabKeyNavigation(False)
        self.table.setProperty("showDropIndicator", False)
        self.table.setDragDropOverwriteMode(False)
        self.table.setShowGrid(False)
        self.table.setRowCount(0)
        self.table.setColumnCount(5)
        self.table.setObjectName("table")
        self.table.horizontalHeader().setVisible(True)
        self.table.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.table, 1, 0, 1, 3)

        self.retranslateUi(history_tab)
        QtCore.QMetaObject.connectSlotsByName(history_tab)

    def retranslateUi(self, history_tab):
        _translate = QtCore.QCoreApplication.translate
        history_tab.setWindowTitle(_translate("history_tab", "Form"))
        self.remove_filters_button.setText(_translate("history_tab", "Usuń filtry"))
        self.filter_button.setText(_translate("history_tab", "Filtruj"))
        self.history_tansaction_label.setText(_translate("history_tab", "Historia transakcji"))
