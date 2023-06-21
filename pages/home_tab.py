from PyQt5.QtWidgets import QWidget, QApplication
from .ui_home_tab import Ui_Form


class HomeTab(Ui_Form, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = HomeTab()
    window.show()
    app.exec()
