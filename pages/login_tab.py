import os

from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QPushButton

current_dir = os.path.dirname(os.path.abspath(__file__))
qt_ui_file = os.path.join(current_dir, "../ui/login_tab.ui")
Form, Base = uic.loadUiType(qt_ui_file)


# class LoginTab(Base,Form):
class LoginTab(Base, Form):
    def __init__(self):
        super().__init__()
        # uic.loadUi(qt_ui_file)
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


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = LoginTab()
    window.show()
    app.exec()
