from PyQt5.QtWidgets import QWidget, QApplication
from .ui_login_tab import Ui_Form


class LoginTab(Ui_Form, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.username: str = ""
        self.password: str = ""
        self.connect_signals()

    # noinspection PyUnresolvedReferences
    def connect_signals(self):
        self.lineEdit_username.textChanged.connect(self.validate_username)
        self.lineEdit_password.textChanged.connect(self.validate_password)

    def validate_username(self):
        self.username = self.lineEdit_username.text()

    def validate_password(self):
        self.password = self.lineEdit_password.text()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = LoginTab()
    window.show()
    app.exec()
