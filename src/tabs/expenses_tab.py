from PyQt5.QtWidgets import QWidget, QFileDialog, QMessageBox
from datetime import datetime
from src.ui.expenses_tab import Ui_expenses_tab
from src.database.database import Database
from PyQt5.QtGui import QDoubleValidator
from src.tabs.add_new_category import Add_new_category
from src.tabs.delete_category import Delete_category
from src.tabs.change_category_name_dialog import Change_category_name_dialog
from src.csv.csv_reader_ import Csv_reader_
from .confirm_category_remove import Confirm_category_remove

# klasa do obsługi zakładki "Wydatki"
class Expenses_tab(QWidget, Ui_expenses_tab):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.database = None

        self.date_edit.setDate(datetime.today().date()) # ustawienie domyślnej daty
        
        validator = QDoubleValidator(0.00, 1000000.00, 2)
        self.amount_line_edit.setValidator(validator)

        self.add_category_button.clicked.connect(self.add_new_category)
        self.change_category_button.clicked.connect(self.change_category_name)
        self.delete_category_button.clicked.connect(self.delete_category)
        self.ok_button.clicked.connect(self.confirm_and_write_to_database)
        self.browse_file_button.clicked.connect(self.browse_file)
        self.ok_button_csv.clicked.connect(self.csv_logic)

        self.selected_file_csv = None

        self.message_box = QMessageBox()
        self.message_box.setWindowTitle("Informacja")
        self.message_box.setStyleSheet("color: #c8beb7; background-color: #3e3e3e")
        self.message_box.setIcon(QMessageBox.Information)
        self.message_box.resize(100,100)


    def set_database(self, database: Database):
        self.database = database


    def set_categories_list(self):
        categories = self.database.get_all_categories()
        category_names = [category.name for category in categories]
        self.categories_combobox.addItems(category_names)

        self.categories_list_list.addItems(category_names)
        self.categories_list_list.setSpacing(20)


    def clear_categories_list(self):
        self.categories_combobox.clear()
        self.categories_list_list.clear()


    # obsługa przycisku do dodawania nowej kategorii
    def add_new_category(self):
        add_new_category_dialog = Add_new_category()
        result = add_new_category_dialog.exec_() # wyświetlenie okna dialogowego z wstrzymaniem dzialania reszty aplikacji
        if result == 1:     # jeśli użytkownik zatwierdził przyciskiem "ok"
            if add_new_category_dialog.add_category_line_edit.text().strip():   # sprawdzenie czy został wprowadzony tekst, ktory nie jest bialymi znakami
                self.database.add_category(add_new_category_dialog.add_category_line_edit.text())
                self.clear_categories_list()
                self.set_categories_list()
            else:
                self.message_box.setText("Nie wprowadzono nazwy")
                self.message_box.exec_()


    # obsługa przycisku do usuwania kategorii
    def delete_category(self):
        delete_category = Delete_category() 
        categories = self.database.get_all_categories()
        category_names = [category.name for category in categories]
        delete_category.delete_category_combobox.addItems(category_names)
        result = delete_category.exec_() 
        if result == 1:
            comfirm = Confirm_category_remove()
            val = comfirm.exec_()
            if val == 1:
                self.database.delete_expenses_by_category_id(self.database.get_category_id_by_name(delete_category.delete_category_combobox.currentText()))
                self.database.delete_category(delete_category.delete_category_combobox.currentText())
                self.clear_categories_list()
                self.set_categories_list()


    # obsługa przycisku do zmiany nazwy kategorii
    def change_category_name(self):
        change_category_name_dialog = Change_category_name_dialog()
        categories = self.database.get_all_categories()
        category_names = [category.name for category in categories]
        change_category_name_dialog.change_category_combobox.addItems(category_names)
        result = change_category_name_dialog.exec_()
        if result == 1:
            if change_category_name_dialog.change_category_line_edit.text().strip():
                self.database.change_category_name(change_category_name_dialog.change_category_combobox.currentText(), change_category_name_dialog.change_category_line_edit.text())
                self.clear_categories_list()
                self.set_categories_list()
            else:
                self.message_box.setText("Nie wprowadzono nazwy")
                self.message_box.exec_()

        

    # wpisywanie do bazy danych wydatku
    def confirm_and_write_to_database(self):
        if self.amount_line_edit.text():    # sprawdzenie czy pole z kwotą zostało wypełnione
            date_edit_str = self.date_edit.date().toString("yyyy-MM-dd")
            category_id = self.database.get_category_id_by_name(self.categories_combobox.currentText())
            self.database.add_expense(float(self.amount_line_edit.text().replace(',', '.')), date_edit_str, category_id)
            self.amount_line_edit.clear()
        else:
            self.message_box.setText("Nie wprowadzono kwoty")
            self.message_box.exec_()


    # ładowanie pliku csv
    def browse_file(self):
        options = QFileDialog.Options() 
        options |= QFileDialog.ReadOnly
        
        file_name, _ = QFileDialog.getOpenFileName(self, "Wybierz plik csv", "", "CSV Files (*.csv)", options=options)  # przechwycenie ścieżki pliku, ignorowanie filtru _
        
        if file_name:
            self.browse_file_line_edit.setText(file_name) # wyświetlenie ścieżki do pliku w wybranym miejscu
            self.selected_file_csv = file_name


    # obsługa okien dialogowych po przesłaniu pliku csv 
    def csv_logic(self): 
        if self.selected_file_csv is not None:
            csv_reader_ = Csv_reader_(self.selected_file_csv, self.database)
            if csv_reader_.dialog_modify_csv():
                if csv_reader_.dialog_choose_columns():
                    csv_reader_.csv_read()
        else:
            self.message_box.setText("Nie wybrano pliku csv")
            self.message_box.exec_()
