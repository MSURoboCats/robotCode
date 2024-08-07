#!/bin/bash

# each of these commands starts up a new terminal tab and runs the commands. Optionally add 'bash' as the last command so the tab will stay open after then final command is completed.

sleep 1

gnome-terminal \
	--tab --title="mega_launch" \
		-- bash -c 'cd /home/robocats/Desktop/developmentEnvironment/robotCode/competitionCode2024/ros2_ws; source install/setup.bash; ros2 launch the_sub mega_launch.py; bash'