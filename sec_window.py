import sys

from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QApplication, QWidget
from UI.ui_file2 import Ui_Form
from logic.db import Log


class Window(QWidget, Ui_Form):
    update_signal = pyqtSignal()

    def __init__(self, filename):
        super().__init__()
        self.l = Log()
        self.filename = filename
        self.initUI()

    def initUI(self):
        self.ui = Ui_Form() 
        
        self.ui.setupUi(self) 

        self.ui.pushButton.clicked.connect(self.add)

    def add(self):
        self.l.add(self.filename, self.ui.lineEdit.text(), self.ui.lineEdit_2.text(), self.ui.lineEdit_3.text())
        self.update_signal.emit()
        self.hide()


def main():
    app = QApplication(sys.argv)
    window = Window("passwords.db")
    window.show()
    sys.exit(app.exec())

