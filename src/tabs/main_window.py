from PyQt5 import QtCore
from src.ui.main_window import Ui_Main_window
from PyQt5.QtWidgets import QWidget
class Main_window(QWidget, Ui_Main_window):
    def __init__(self, database):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle(" ")
        self.database = database

        self.home_tab.set_database(database)
        self.home_tab.draw_pie_chart()
        self.home_tab.draw_stack_chart()

        self.incomes_tab.set_database(database)
        self.incomes_tab.set_incomes_list()
        self.incomes_tab.show_chart()

        self.expenses_tab.set_database(database)
        self.expenses_tab.set_categories_list()

        self.history_tab.set_database(database)
        self.history_tab.set_default_filters()
        self.history_tab.set_default_history_list()

        self.analysis_tab.set_database(database)
        self.analysis_tab.set_categories_list()



