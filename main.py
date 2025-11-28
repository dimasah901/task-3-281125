import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (QWidget, QApplication, QLabel, QTableWidgetItem, QDialog)
from main_ui import Ui_Form
from addEditCoffeeForm_ui import Ui_Dialog
from sqlite3 import Connection

class Car(QWidget):

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.connection = Connection("coffee.sqlite")
        self.connection.autocommit = True
        self.connection.cursor().execute("""
            CREATE TABLE IF NOT EXISTS coffee (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                sort TEXT,
                rarity TEXT,
                state TEXT,
                taste TEXT,
                price TEXT,
                volume TEXT
            )
        """).fetchall()
        self.update()
        self.ui.pushButton.clicked.connect(self.create_new)
    
    def update(self):
        self.data = self.connection.cursor().execute("SELECT * FROM coffee").fetchall()
        self.ui.tableWidget.setRowCount(len(self.data))
        for i, row in enumerate(self.data):
            for j, item in enumerate(row):
                self.ui.tableWidget.setItem(i, j, QTableWidgetItem(str(item)))
    
    def create_new(self):
        dialog = QDialog(self)
        dialog.ui = Ui_Dialog()
        dialog.ui.setupUi(dialog)
        dialog.accepted.connect(lambda: self.add_new(dialog))
        dialog.rejected.connect(lambda: dialog.close())
        dialog.show()
    
    def add_new(self, dialog):
        self.connection.execute(
            "INSERT INTO coffee (sort, rarity, state, taste, price, volume) VALUES (?, ?, ?, ?, ?, ?)",
            (dialog.ui.sort.text(), dialog.ui.rare.text(), dialog.ui.state.text(), dialog.ui.taste.text(), dialog.ui.price.text(), dialog.ui.volume.text())
        )
        dialog.close()
        
    def modify_existing(self):
        dialog = QDialog(self)
        dialog.ui = Ui_Dialog()
        dialog.ui.setupUi(dialog)
        
        data = self.connection.cursor().execute("SELECT * FROM coffee WHERE id = ?",
                                                (int(self.ui.tableWidget.item(self.ui.tableWidget.currentRow(), 0).text()),)
                                                ).fetchone()
        
        dialog.ui.sort.setText(data[1])
        dialog.ui.rare.setText(data[2])
        dialog.ui.state.setText(data[3])
        dialog.ui.taste.setText(data[4])
        dialog.ui.price.setText(data[5])
        dialog.ui.volume.setText(data[6])
        
        dialog.accepted.connect(lambda: self.modified_existing(dialog, int(self.ui.tableWidget.item(self.ui.tableWidget.currentRow(), 0).text())))
        dialog.rejected.connect(lambda: dialog.close())
        dialog.show()
    
    def modified_existing(self, dialog, id):
        self.connection.execute(
            "UPDATE coffee SET sort = ?, rarity = ?, state = ?, taste = ?, price = ?, volume = ? WHERE id = ?",
            (dialog.ui.sort.text(), dialog.ui.rare.text(), dialog.ui.state.text(), dialog.ui.taste.text(), dialog.ui.price.text(), dialog.ui.volume.text(), id)
        )
        dialog.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Car()
    ex.show()
    sys.exit(app.exec())