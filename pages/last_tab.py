from __future__ import annotations

import os

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QPushButton, QLineEdit

from pages import global_state
from pages.settings_window import Settings

current_dir = os.path.dirname(os.path.abspath(__file__))
qt_ui_file = os.path.join(current_dir, "../ui/last_tab.ui")
Form, Base = uic.loadUiType(qt_ui_file)


class LastTab(Base, Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.settings: Settings | None = None
        self.lineEdit_font_path: QLineEdit = self.findChild(QLineEdit, "lineEdit_font_path")
        self.pushButton_new_window: QPushButton = self.findChild(QPushButton, "pushButton_new_window")
        self.pushButton_new_window.clicked.connect(self.open_new_window_callback)

    def open_new_window_callback(self):
        self.settings = Settings()
        self.settings.exec()

        if global_state.font_file_dir:
            self.lineEdit_font_path.setText(global_state.font_file_dir)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = LastTab()
    window.show()
    app.exec()
