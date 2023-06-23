import os

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QToolButton, QFileDialog, QLineEdit, QLabel

from pages import global_state

current_dir = os.path.dirname(os.path.abspath(__file__))
qt_ui_file = os.path.join(current_dir, "../ui/settings.ui")
Form, Base = uic.loadUiType(qt_ui_file)


class Settings(Base, Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label_font_path_error: QLabel = self.findChild(QLabel, "label_font_path_error")
        self.lineEdit_font_path: QLineEdit = self.findChild(QLineEdit, "lineEdit_font_path")
        self.toolButton_font_path: QToolButton = self.findChild(QToolButton, "toolButton_font_path")
        self.connect_signals()
        self.label_font_path_error.setText(global_state.font_file_dir)

    # noinspection PyUnresolvedReferences
    def connect_signals(self):
        self.lineEdit_font_path.textChanged.connect(self.path_changed)
        self.toolButton_font_path.clicked.connect(self.font_path_callback)

    def font_path_callback(self):
        try:
            folder_path = QFileDialog.getExistingDirectory(self, "Get Font Folder", "")
            global_state.font_file_dir = folder_path
            self.lineEdit_font_path.setText(folder_path)
        except Exception as e:
            print("ERROR: font_path_callback(): ", e)

    def path_changed(self, text):
        if not os.path.exists(text):
            self.label_font_path_error.setText("Path doesn't exists")
        else:
            self.label_font_path_error.setText("")
        global_state.font_file_dir = text


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = Settings()
    window.show()
    app.exec()
