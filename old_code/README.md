# robotCode
## Run the Testing GUI
1. WARNING: The Arduino will not automatically stop (yet) if the code crashes or the code is halted with a keyboard interrupt. Press the x in the GUI window to exit safely.
2. WARNING: Ensure the code on the sub is up-to-date prior to going to the pool. External drive required.
3. Turn on the sub and enable the arduino
4. Connect directly to the sub via ethernet/tether
5. Install Tight VNC Viewer if not already installed
6. Run Tight VNC Viewer and connect to the sub. VNC Server: 169.254.80.130::5900
7. Enter the password for the sub when prompted
8. Enter the desktop password to unlock the Shuttle when prompted by Ubuntu
9. The following should be run in the terminal.
   1. cd Desktop/robotCode-on_sub/
   2. conda activate py39
   3. python3 run_robot.py
10. At this point the GUI should be running. If not ensure that the gui bool is set to True in run_robot.py
