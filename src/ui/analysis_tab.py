# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kubus/Pulpit/Wydatkoinator/ui/analysis_tab.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_analisys_tab(object):
    def setupUi(self, analisys_tab):
        analisys_tab.setObjectName("analisys_tab")
        analisys_tab.resize(1130, 693)
        analisys_tab.setStyleSheet("QWidget{\n"
"background-color:#202020;\n"
"color:#C8BEB7\n"
"}\n"
"QFrame{\n"
"background-color:#252525;\n"
"}\n"
"QChartView{\n"
"background-color:#252525;\n"
"color:#252525;\n"
"}\n"
"QRadioButton{\n"
"background-color:#252525;\n"
"}\n"
"\n"
"")
        self.gridLayout = QtWidgets.QGridLayout(analisys_tab)
        self.gridLayout.setObjectName("gridLayout")
        self.select_date = QtWidgets.QFrame(analisys_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.select_date.sizePolicy().hasHeightForWidth())
        self.select_date.setSizePolicy(sizePolicy)
        self.select_date.setMinimumSize(QtCore.QSize(0, 100))
        self.select_date.setStyleSheet("QCalendarWidget QWidget { alternate-background-color: #c8beb7; } /* naglowek z nazwami dni */\n"
"\n"
"QCalendarWidget QToolButton { color: black; }    /* najwyzszy naglowek - czcionka*/QCalendarWidget QWidget { background-color: #c8beb7; }    /* calosc */ \n"
"\n"
"")
        self.select_date.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.select_date.setFrameShadow(QtWidgets.QFrame.Raised)
        self.select_date.setObjectName("select_date")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.select_date)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.date_from = QtWidgets.QDateEdit(self.select_date)
        self.date_from.setStyleSheet("")
        self.date_from.setCalendarPopup(True)
        self.date_from.setObjectName("date_from")
        self.gridLayout_4.addWidget(self.date_from, 4, 1, 1, 1)
        self.title_select_date = QtWidgets.QLabel(self.select_date)
        self.title_select_date.setAlignment(QtCore.Qt.AlignCenter)
        self.title_select_date.setObjectName("title_select_date")
        self.gridLayout_4.addWidget(self.title_select_date, 0, 0, 1, 4)
        self.date_to = QtWidgets.QDateEdit(self.select_date)
        self.date_to.setStyleSheet("QCalendarWidget QWidget { background-color: #c8beb7; }    /* calosc */ \n"
"\n"
"QCalendarWidget QWidget { alternate-background-color: #c8beb7; } /* naglowek z nazwami dni */\n"
"\n"
"QCalendarWidget QToolButton { color: black; }    /* najwyzszy naglowek - czcionka*/")
        self.date_to.setCalendarPopup(True)
        self.date_to.setObjectName("date_to")
        self.gridLayout_4.addWidget(self.date_to, 4, 3, 1, 1)
        self.from_label = QtWidgets.QLabel(self.select_date)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.from_label.sizePolicy().hasHeightForWidth())
        self.from_label.setSizePolicy(sizePolicy)
        self.from_label.setAlignment(QtCore.Qt.AlignCenter)
        self.from_label.setObjectName("from_label")
        self.gridLayout_4.addWidget(self.from_label, 4, 0, 1, 1)
        self.to = QtWidgets.QLabel(self.select_date)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.to.sizePolicy().hasHeightForWidth())
        self.to.setSizePolicy(sizePolicy)
        self.to.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.to.setObjectName("to")
        self.gridLayout_4.addWidget(self.to, 4, 2, 1, 1)
        self.gridLayout.addWidget(self.select_date, 0, 2, 1, 1)
        self.select_categories = QtWidgets.QFrame(analisys_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.select_categories.sizePolicy().hasHeightForWidth())
        self.select_categories.setSizePolicy(sizePolicy)
        self.select_categories.setMinimumSize(QtCore.QSize(0, 100))
        self.select_categories.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.select_categories.setFrameShadow(QtWidgets.QFrame.Raised)
        self.select_categories.setObjectName("select_categories")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.select_categories)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.title_select_categories = QtWidgets.QLabel(self.select_categories)
        self.title_select_categories.setAlignment(QtCore.Qt.AlignCenter)
        self.title_select_categories.setObjectName("title_select_categories")
        self.gridLayout_3.addWidget(self.title_select_categories, 0, 0, 1, 1)
        self.categories_list = QtWidgets.QComboBox(self.select_categories)
        self.categories_list.setEditable(False)
        self.categories_list.setObjectName("categories_list")
        self.gridLayout_3.addWidget(self.categories_list, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.select_categories, 0, 1, 1, 1)
        self.chart = QChartView(analisys_tab)
        self.chart.setObjectName("chart")
        self.gridLayout.addWidget(self.chart, 2, 0, 1, 3)
        self.select_chart_type = QtWidgets.QFrame(analisys_tab)
        self.select_chart_type.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.select_chart_type.sizePolicy().hasHeightForWidth())
        self.select_chart_type.setSizePolicy(sizePolicy)
        self.select_chart_type.setMinimumSize(QtCore.QSize(0, 100))
        self.select_chart_type.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.select_chart_type.setFrameShadow(QtWidgets.QFrame.Raised)
        self.select_chart_type.setObjectName("select_chart_type")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.select_chart_type)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.title_select_chart_type = QtWidgets.QLabel(self.select_chart_type)
        self.title_select_chart_type.setAlignment(QtCore.Qt.AlignCenter)
        self.title_select_chart_type.setObjectName("title_select_chart_type")
        self.gridLayout_2.addWidget(self.title_select_chart_type, 0, 0, 1, 1)
        self.pie_chart_button = QtWidgets.QRadioButton(self.select_chart_type)
        self.pie_chart_button.setChecked(False)
        self.pie_chart_button.setObjectName("pie_chart_button")
        self.gridLayout_2.addWidget(self.pie_chart_button, 1, 0, 1, 1)
        self.stack_chart_button = QtWidgets.QRadioButton(self.select_chart_type)
        self.stack_chart_button.setObjectName("stack_chart_button")
        self.gridLayout_2.addWidget(self.stack_chart_button, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.select_chart_type, 0, 0, 1, 1)
        self.confirm_button = QtWidgets.QPushButton(analisys_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.confirm_button.sizePolicy().hasHeightForWidth())
        self.confirm_button.setSizePolicy(sizePolicy)
        self.confirm_button.setMouseTracking(False)
        self.confirm_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.confirm_button.setAutoDefault(False)
        self.confirm_button.setDefault(False)
        self.confirm_button.setFlat(False)
        self.confirm_button.setObjectName("confirm_button")
        self.gridLayout.addWidget(self.confirm_button, 1, 2, 1, 1, QtCore.Qt.AlignRight)

        self.retranslateUi(analisys_tab)
        QtCore.QMetaObject.connectSlotsByName(analisys_tab)

    def retranslateUi(self, analisys_tab):
        _translate = QtCore.QCoreApplication.translate
        analisys_tab.setWindowTitle(_translate("analisys_tab", "Form"))
        self.title_select_date.setText(_translate("analisys_tab", "Wybierz okres"))
        self.from_label.setText(_translate("analisys_tab", "Od:"))
        self.to.setText(_translate("analisys_tab", "Do:"))
        self.title_select_categories.setText(_translate("analisys_tab", "Wybierz kategorie"))
        self.title_select_chart_type.setText(_translate("analisys_tab", "Wybierz typ wykresu"))
        self.pie_chart_button.setText(_translate("analisys_tab", "Wykres kołowy"))
        self.stack_chart_button.setText(_translate("analisys_tab", "Wykres stosowy"))
        self.confirm_button.setText(_translate("analisys_tab", "Zatwierdź"))
from PyQt5.QtChart import QChartView
