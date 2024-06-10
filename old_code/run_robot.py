"""
---- MSU RoboCats ----

This is the file from which everything on the
submarine is ran/tested.

"""
import argparse
from ast import parse
from cmath import log
from GUI.gui import GUI
from robot_controller import RobotController
from static_utilities import StaticUtilities 

# Define argument parser and/handle the 'gui' argument
parser = argparse.ArgumentParser(description="Run the robot in a specified mode")
parser.add_argument("--gui", dest="gui", action="store_true", help="Run the program in testing mode with a GUI (default: false)")

# Set default arguments
parser.set_defaults(gui=False)

# Parse out and define arguments
args = parser.parse_args()
guiFlag = args.gui

def main(gui: bool = False):
    StaticUtilities.logger.info("TODO: prompt for run mode and execute accordingly")
    if gui:
        testing_gui: GUI = GUI()
        testing_gui.gui()
    else:
        robot_controller: RobotController = RobotController(number_of_processes=3)
        robot_controller.autonomous()

if __name__ == "__main__":
    main(guiFlag)