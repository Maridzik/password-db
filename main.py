import sys
import os


from PyQt6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QPushButton
from UI.ui_file import Ui_Form

from logic.db import Log
from sec_window import Window as n_window

class Window(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()       
        self.windows = []
        self.filename = "passwords.db"
        self.l = Log()
        if not os.path.exists(os.path.join(self.filename)):
            self.l.create_db(self.filename)
        self.initUI()

    def initUI(self):
        self.ui = Ui_Form() 
        self.ui.setupUi(self) 
        self.ui.lineEdit.textChanged.connect(self.update)

        self.ui.pushButton.clicked.connect(self.add)
        self.update()

    def update(self):
        text = self.ui.lineEdit.text()
        passwords = self.l.con(self.filename, text)

        table = self.ui.tableWidget
        table.clear()
        table.setColumnCount(4) 
        table.setHorizontalHeaderLabels(["id", "web_name", "username", "password"]) 

        if passwords:
            table.setRowCount(len(passwords))
            for i, column in enumerate(passwords):
                for j, item in enumerate(column):
                    table.setItem(i, j, QTableWidgetItem(str(item)))


    def add(self):
        window = n_window(self.filename)
        self.windows.append(window)
        window.update_signal.connect(self.update)
        window.show()


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()