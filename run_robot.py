"""
---- MSU RoboCats ----

This is the file from which everything on the
submarine is ran/tested.

"""
from GUI.gui import GUI
from robot_controller import RobotController
from static_utilities import StaticUtilities


def main(gui: bool = True):
    StaticUtilities.logger.info("TODO: prompt for run mode and execute accordingly")
    if gui:
        testing_gui: GUI = GUI()
        testing_gui.gui()
    else:
        robot_controller: RobotController = RobotController(number_of_processes=3)
        robot_controller.autonomous()


if __name__ == "__main__":
    main(gui=True)

