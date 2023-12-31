import os

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

current_dir = os.path.dirname(os.path.abspath(__file__))
qt_ui_file = os.path.join(current_dir, "../ui/data_tab.ui")
Form, Base = uic.loadUiType(qt_ui_file)


class DataTab(Base, Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = DataTab()
    window.show()
    app.exec()
