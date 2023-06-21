from .ui_data_tab import Ui_Form
from PyQt5.QtWidgets import QWidget, QApplication


class DataTab(Ui_Form, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = DataTab()
    window.show()
    app.exec()
