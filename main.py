# Running the app
import sys
from PyQt6.QtWidgets import QApplication, QMessageBox
from app import ExpenseApp


def main():
    app = QApplication(sys.argv)  # Also could be QApplication([])

    window = ExpenseApp()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
