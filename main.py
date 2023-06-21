import sys
import os
from PyQt5 import uic
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit

current_dir = os.path.dirname(os.path.abspath(__file__))
qt_ui_file = os.path.join(current_dir, "ui/main.ui")
Form, Base = uic.loadUiType(qt_ui_file)


class MainWindow(Base, Form):
    """Main App window
    """

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.username: str = ""
        self.password: str = ""
        self.lineEdit_username: QLineEdit = self.findChild(QLineEdit, "lineEdit_username")
        self.lineEdit_password: QLineEdit = self.findChild(QLineEdit, "lineEdit_password")
        self.pushButton_login: QPushButton = self.findChild(QPushButton, "pushButton_login")
        self.connect_signals()

    # noinspection PyUnresolvedReferences
    def connect_signals(self):
        self.lineEdit_username.textChanged.connect(self.validate_username)
        self.lineEdit_password.textChanged.connect(self.validate_password)
        self.pushButton_login.clicked.connect(self.login)

    def validate_username(self):
        self.username = self.lineEdit_username.text()

    def validate_password(self):
        self.password = self.lineEdit_password.text()

    def login(self):
        if self.username and self.password:
            print(self.username, self.password)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
