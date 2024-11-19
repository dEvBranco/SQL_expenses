# App design
from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QLineEdit,
    QComboBox,
    QDateEdit,
    QTableWidget,
    QVBoxLayout,
    QHBoxLayout,
    QMessageBox,
    QTableWidgetItem,
    QHeaderView,
)

from PyQt6.QtCore import QDate, Qt


class ExpenseApp(QWidget):
    def __init__(self):
        super().__init__()
        self.settings()

    def settings(self):
        self.setGeometry(300, 300, 550, 500)
        self.setWindowTitle("Expenses Tracker")

    # Design
    def initUI(self):
        # Create all objects
        self.date_box = QDateEdit()
        self.date_box.setDate(QDate.currentDate())
        self.dropdown = QComboBox()
        self.amount = QLineEdit()
        self.description = QLineEdit()
