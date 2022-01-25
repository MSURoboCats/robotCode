import sys

import PyQt5  # use this for gui
from PyQt5.QtWidgets import QApplication, QMainWindow

from static_utilities import StaticUtilities


class GUI:

    def __init__(self) -> None:
        self.app = QApplication(sys.argv)
        self.resolution = self.app.desktop().screenGeometry()
        self.width, self.height = self.resolution.width(), self.resolution.height()
        self.window_width = self.width/2
        self.window_height = self.height/2
        self.window = QMainWindow()
        self.window.setGeometry(int(self.window_width/2), int(self.window_height/2), int(self.window_width), int(self.window_height))
        self.window.setWindowTitle("Robocats Testing GUI")
        StaticUtilities.logger.info(f"GUI initialized")

    def gui(self) -> None:
        self.window.show()
        sys.exit(self.app.exec_())


if __name__ == "__main__":
    gui = GUI()
    gui.gui()

