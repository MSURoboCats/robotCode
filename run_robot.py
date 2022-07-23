"""
---- MSU RoboCats ----

This is the file from which everything on the
sub is run or tested.

"""
import argparse
import time
from ast import parse
from cmath import log
from multiprocessing import Queue

from Actuators.arduino_serial_interface import ArduinoSerialInterfaceController
from robot_controller import RobotController
from static_utilities import StaticUtilities

# Define argument parser and/handle the 'gui' argument
parser = argparse.ArgumentParser(description="Run the robot in a specified mode")
parser.add_argument("--gui", dest="gui", action="store_true",
                    help="Run the program in testing mode with a GUI (default: false)")

# Set default arguments
parser.set_defaults(gui=False)

# Parse out and define arguments
args = parser.parse_args()
guiFlag = args.gui


def main(gui: bool = False):
    # if gui:
    #     testing_gui: GUI = GUI()
    #     testing_gui.gui()
    # else:
    #     robot_controller: RobotController = RobotController()
    #     robot_controller.autonomous()
    asic = ArduinoSerialInterfaceController()
    asic.run_autonomous(Queue(), Queue())
    time.sleep(5)


if __name__ == "__main__":
    main(guiFlag)
