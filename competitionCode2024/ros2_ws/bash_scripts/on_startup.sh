#!/bin/bash

# each of these commands starts up a new terminal tab and runs the commands. Optionally add 'bash' as the last command so the tab will stay open after then final command is completed.

gnome-terminal \
	--tab --title="hardware" \
		-- bash -c 'cd /home/robocats/Desktop/developmentEnvironment/robotCode/competitionCode2024/ros2_ws; source install/setup.bash; ros2 launch the_sub hardware_launch.py; '
