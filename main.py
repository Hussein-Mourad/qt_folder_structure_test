import os
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from ui_main import Ui_MainWindow


class MainWindow(Ui_MainWindow, QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.connect_signals()
        for tab_index in range(1, self.tab_widget.count()):
            self.tab_widget.setTabEnabled(tab_index, False)

    # noinspection PyUnresolvedReferences
    def connect_signals(self):
        self.tab_login.pushButton_login.clicked.connect(self.login)
        self.tab_home.pushButton_home_next.clicked.connect(self.next_tab)
        self.tab_data.pushButton_data_next.clicked.connect(self.next_tab)

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
