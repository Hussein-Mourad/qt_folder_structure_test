import os
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication

current_dir = os.path.dirname(os.path.abspath(__file__))
qt_ui_file = os.path.join(current_dir, "../ui/home_tab.ui")
Form, Base = uic.loadUiType(qt_ui_file)


class HomeTab(Base, Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = HomeTab()
    window.show()
    app.exec()
