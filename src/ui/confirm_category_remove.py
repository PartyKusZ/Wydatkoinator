# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kubus/Pulpit/Wydatkoinator/ui/Confirm_category_remove.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Confirm_category_remove(object):
    def setupUi(self, Confirm_category_remove):
        Confirm_category_remove.setObjectName("Confirm_category_remove")
        Confirm_category_remove.resize(392, 148)
        Confirm_category_remove.setStyleSheet("QWidget {\n"
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
"")
        self.gridLayout = QtWidgets.QGridLayout(Confirm_category_remove)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Confirm_category_remove)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Confirm_category_remove)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(Confirm_category_remove)
        self.buttonBox.accepted.connect(Confirm_category_remove.accept) # type: ignore
        self.buttonBox.rejected.connect(Confirm_category_remove.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Confirm_category_remove)

    def retranslateUi(self, Confirm_category_remove):
        _translate = QtCore.QCoreApplication.translate
        Confirm_category_remove.setWindowTitle(_translate("Confirm_category_remove", "Dialog"))
        self.label.setText(_translate("Confirm_category_remove", "Czy na pewno chcesz usunąć wybraną kategorie? Zostaną również usuniętę wszysykie wydatki z nią związane"))