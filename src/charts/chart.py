# Abstract class to draw graphs

from abc import ABC, abstractmethod
from PyQt5 import QtWidgets

import sys
sys.path.insert(0, '../../')  # Dodaj katalog nadrzędny do ścieżki

from src.ui.chart import Ui_Chart
from datetime import datetime


class Chart_meta(QtWidgets.QWidget.__class__, ABC.__class__):
    pass

class Chart(QtWidgets.QWidget, metaclass=Chart_meta):


    def __init__(self,chartview):
        super().__init__()
        self.chartview = chartview
    @abstractmethod
    def draw_chart(self, expenses: list):
        pass

    def sum_expenses_by_category(self, expenses: list) -> dict:
        category_sums = {}
        for expense in expenses:
            category_name = expense.category.name
            if category_name not in category_sums:
                category_sums[category_name] = 0
            category_sums[category_name] += expense.amount
        return category_sums
    
    def sum_expenses_by_category_in_date_range(self, expenses: list, date1, date2) -> dict:
        category_sums = {}
        for expense in expenses:
            if date1 <= expense.date <= date2:
                category_name = expense.category.name
                if category_name not in category_sums:
                    category_sums[category_name] = 0
                category_sums[category_name] += expense.amount
        return category_sums
    
    # def sum_expenses_by_category_in_date_range(self, expenses: list, date1, date2) -> dict:
    #     category_month_sums = {}
    #     for expense in expenses:
    #         if date1 <= expense.date <= date2:
    #             category_name = expense.category.name
    #             expense_month = expense.date.strftime('%Y-%m')  # Format YYYY-MM
    #             if category_name not in category_month_sums:
    #                 category_month_sums[category_name] = {}
    #             if expense_month not in category_month_sums[category_name]:
    #                 category_month_sums[category_name][expense_month] = 0

    #             category_month_sums[category_name][expense_month] += float(expense.amount)
    #     return category_month_sums
    
    def get_date_range(self, dates_list: list) -> tuple:
        return min(dates_list), max(dates_list)
