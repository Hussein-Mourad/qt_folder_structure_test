import os
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QTabWidget, QMenuBar, QStatusBar

from pages.login_tab import LoginTab

current_dir = os.path.dirname(os.path.abspath(__file__))
qt_ui_file = os.path.join(current_dir, "ui/main.ui")
Form, Base = uic.loadUiType(qt_ui_file)


class MainWindow(Base, Form):
    """Main App window
    """

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.menu_bar: QMenuBar = self.findChild(QMenuBar, "menubar")
        self.status_bar: QStatusBar = self.findChild(QStatusBar, "statusbar")
        self.tab_widget: QTabWidget = self.findChild(QTabWidget, "tabWidget")
        self.tab_login: LoginTab = self.findChild(LoginTab, "tab_login")
        self.tab_home: QWidget = self.findChild(QWidget, "tab_home")
        self.tab_data: QWidget = self.findChild(QWidget, "tab_data")
        self.tab_last_page: QWidget = self.findChild(QWidget, "tab_last_page")
        self.pushButton_home_next: QPushButton = self.findChild(QPushButton, "pushButton_home_next")
        self.pushButton_data_next: QPushButton = self.findChild(QPushButton, "pushButton_data_next")
        self.pushButton_login: QPushButton = self.findChild(QPushButton, "pushButton_login")
        self.connect_signals()

        for tab_index in range(1, self.tab_widget.count()):
            self.tab_widget.setTabEnabled(tab_index, False)

    # noinspection PyUnresolvedReferences
    def connect_signals(self):
        self.pushButton_login.clicked.connect(self.login)
        self.pushButton_home_next.clicked.connect(self.next_tab)
        self.pushButton_data_next.clicked.connect(self.next_tab)

    def login(self):
        username = self.tab_login.username
        password = self.tab_login.password
        if username and password:
            self.next_tab()
        else:
            self.status_bar.showMessage("Invalid Username and/or password", 2000)

    def next_tab(self):
        current_tab_index = self.tab_widget.currentIndex()
        self.tab_widget.setTabEnabled(current_tab_index, False)
        self.tab_widget.setTabEnabled(current_tab_index + 1, True)
        self.tab_widget.setCurrentIndex(current_tab_index + 1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
