# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kubus/Pulpit/Wydatkoinator/ui/history_edit.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_history_edit(object):
    def setupUi(self, history_edit):
        history_edit.setObjectName("history_edit")
        history_edit.resize(400, 300)
        history_edit.setStyleSheet("QWidget {\n"
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
"\n"
"QCalendarWidget QWidget { background-color: #c8beb7; }    /* calosc */ \n"
"\n"
"QCalendarWidget QWidget { alternate-background-color: #c8beb7; } /* naglowek z nazwami dni */\n"
"\n"
"QCalendarWidget QToolButton { color: black; }    /* najwyzszy naglowek - czcionka*/\n"
"\n"
"\n"
"\n"
"")
        self.gridLayout = QtWidgets.QGridLayout(history_edit)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(history_edit)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 7, 0, 1, 2)
        self.date_edit = QtWidgets.QDateEdit(history_edit)
        self.date_edit.setCalendarPopup(True)
        self.date_edit.setObjectName("date_edit")
        self.gridLayout.addWidget(self.date_edit, 4, 0, 1, 1)
        self.line_edit = QtWidgets.QLineEdit(history_edit)
        self.line_edit.setObjectName("line_edit")
        self.gridLayout.addWidget(self.line_edit, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(history_edit)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(history_edit)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(history_edit)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1)
        self.combo_box = QtWidgets.QComboBox(history_edit)
        self.combo_box.setObjectName("combo_box")
        self.gridLayout.addWidget(self.combo_box, 6, 0, 1, 1)

        self.retranslateUi(history_edit)
        self.buttonBox.accepted.connect(history_edit.accept) # type: ignore
        self.buttonBox.rejected.connect(history_edit.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(history_edit)

    def retranslateUi(self, history_edit):
        _translate = QtCore.QCoreApplication.translate
        history_edit.setWindowTitle(_translate("history_edit", "Dialog"))
        self.label_2.setText(_translate("history_edit", "Edytuj datę:"))
        self.label.setText(_translate("history_edit", "Edytuj kwotę:"))
        self.label_3.setText(_translate("history_edit", "Edytuj kategorię:"))