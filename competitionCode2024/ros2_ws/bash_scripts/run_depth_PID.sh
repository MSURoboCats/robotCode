#!/bin/bash

# each of these commands starts up a new terminal tab and runs the commands. Optionally add 'bash' as the last command so the tab will stay open after then final command is completed.

gnome-terminal \
	--tab --title="hardware" \
		-- bash -c 'cd /home/robocats/Desktop/developmentEnvironment/robotCode/competitionCode2024/ros2_ws; source install/setup.bash; ros2 launch the_sub hardware_launch.py; bash'

gnome-terminal \
	--tab --title="vision" \
		-- bash -c 'cd /home/robocats/Desktop/developmentEnvironment/robotCode/competitionCode2024/ros2_ws; source install/setup.bash; ros2 launch the_sub forward_detector_launch.py; '

gnome-terminal \
	--tab --title="sub_status" \
		-- bash -c 'cd /home/robocats/Desktop/developmentEnvironment/robotCode/competitionCode2024/ros2_ws; source install/setup.bash; ros2 run the_sub sub_status_observer_node; '

gnome-terminal \
	--tab --title="depth_controller" \
		-- bash -c 'cd /home/robocats/Desktop/developmentEnvironment/robotCode/competitionCode2024/ros2_ws; source install/setup.bash; ros2 run the_sub depth_controller_PID_node -10 0 0; bash'

gnome-terminal \
	--tab --title="depth_commands" \
		-- bash -c 'cd /home/robocats/Desktop/developmentEnvironment/robotCode/competitionCode2024/ros2_ws; source install/setup.bash; bash'
