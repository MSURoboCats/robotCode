import logging
import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from pyqt5_plugins.examplebuttonplugin import QtGui

from GUI.qt_handler import QTextEditLogger
from Actuators.arduino_controller import ArduinoAction
from robot_controller import RobotController
from static_utilities import StaticUtilities


class GUI(object):

    def __init__(self) -> None:
        self.gui_logging_handler = None
        self.robot_controller = None
        self.file_logging_handler = None
        self.app = QApplication(sys.argv)
        self.resolution = self.app.desktop().screenGeometry()
        self.width, self.height = self.resolution.width(), self.resolution.height()
        self.window_width = self.width/2
        self.window_height = self.height/2
        self.window = QMainWindow()
        # self.window.setFixedWidth(w=1280)
        # self.window.setFixedHeight(h=720)
        # self.window.setGeometry(int(self.window_width/2), int(self.window_height/2), int(self.window_width), int(self.window_height))
        StaticUtilities.logger.info(f"GUI initialized")

    def _setup_logging_handlers(self) -> None:
        self.textBrowser.clear()
        self.gui_logging_handler = QTextEditLogger(self.textBrowser)
        self.gui_logging_handler.setFormatter(
            logging.Formatter('%(message)s'))
        self.gui_logging_handler.setLevel(logging.DEBUG)
        StaticUtilities.logger.addHandler(self.gui_logging_handler)
        self.file_logging_handler = logging.FileHandler('gui_log.log')
        self.file_logging_handler.setFormatter(
            logging.Formatter('%(asctime)s %(levelname)s %(module)s %(funcName)s %(message)s'))
        self.file_logging_handler.setLevel(logging.DEBUG)
        StaticUtilities.logger.addHandler(self.file_logging_handler)

    def gui(self) -> None:
        self._setupUi()
        self._setup_logging_handlers()
        self.robot_controller = RobotController(number_of_processes=1)
        self.window.show()
        # self.robot_controller.arduino_thruster_depth_pressure_controller.send_arduino_command(ArduinoAction.NEUTRAL)
        try:
            self.app.exec_()
        finally:
            self.robot_controller.arduino_thruster_depth_pressure_controller.send_arduino_command(ArduinoAction.NEUTRAL)
            sys.exit()

    def _setupUi(self):
        self.window.setObjectName("MainWindow")
        self.window.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(self.window)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(15, 11, 581, 391))
        self.textBrowser.setObjectName("textBrowser")
        self.window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self.window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 26))
        self.menubar.setObjectName("menubar")
        self.window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self.window)
        self.statusbar.setObjectName("statusbar")
        self.window.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self.window)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.window.setWindowTitle(_translate("MainWindow", "MainWindow"))


if __name__ == "__main__":
    gui: GUI = GUI()
    gui.gui()
