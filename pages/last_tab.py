from PyQt5.QtWidgets import QApplication, QWidget

from .ui_last_tab import Ui_Form


class LastTab(Ui_Form, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = LastTab()
    window.show()
    app.exec()
