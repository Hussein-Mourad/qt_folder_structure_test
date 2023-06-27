import pickle
import os
import logging

current_dir = os.path.dirname(os.path.abspath(__file__))
settings_file = os.path.join(current_dir, "./settings")


class SettingsData:
    font_file_dir: str = ""

    def __init__(self):
        ...

    def get_settings(self):
        raise NotImplementedError

    def load_settings(self):
        try:
            with open(settings_file, "rb") as f:
                s: SettingsData = pickle.load(f)
            return s
        except Exception as e:
            print(e)
            return None

    def save_settings(self):
        with open(settings_file, "wb") as f:
            pickle.dump(self, f)

    def set_font_file_dir(self, value):
        self.font_file_dir = value
        self.save_settings()


if __name__ == "__main__":
    s = SettingsData()
    s: SettingsData = s.load_settings()
    s.set_font_file_dir("./")
    # print(s.font_file_dir)
