"""
---- MSU RoboCats ----

This is the file from which everything on the
submarine is ran/tested.

"""
from robot_controller import RobotController
from static_utilities import StaticUtilities


class Main:

    def __init__(self):
        pass

    def main(self):
        StaticUtilities.logger.info("TODO: prompt for run mode and execute accordingly")
        robot_controller: RobotController = RobotController()
        robot_controller.autonomous()


if __name__ == "__main__":
    m = Main()
    m.main()
