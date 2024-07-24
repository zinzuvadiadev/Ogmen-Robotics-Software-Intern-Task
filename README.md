# Bot_Description
Created by Dev Zinzuvadia for Robot Software Engineer Intern - Coding Round
## Launching the Robot in RViz
1. Navigate to the workspace:
```bash
cd /path/to/your/workspace
```
2. Build your workspace:
```bash
colcon build
source install/setup.bash
```
3. Launching the robot in RViz:
```bash
ros2 launch bot_description rviz.launch.py
```
After launching the robot in rviz the robot should look like this 
![image](https://github.com/user-attachments/assets/ac9f4171-ea65-4d64-82c6-8be5d69b83d2)


## Visualizing the Robot in Gazebo
For visualizing the robot with Gazebo in a demo world, use the following command:
```bash
ros2 launch bot_world my_robot_gazebo.launch.xml
```
The Robot should look like this after launching the world in gazebo
![image](https://github.com/user-attachments/assets/3cc6df22-10ab-48c0-93f6-fcb6c341bf36)

## Navigating the Robot

1. Ensure that the /cmd_vel topic is active:

```bash
ros2 topic list
```

2. After confirming the presence of /cmd_vel, use the following command to navigate the robot in the environment:

``` bash
    ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

![image](https://github.com/user-attachments/assets/bd55c675-ffb7-43b3-b3c3-09b2ac88330b)

![image](https://github.com/user-attachments/assets/bd0f518a-ac25-4f6a-a61a-5c058eb8b439)


## Using the Filter Scan

Launch the Gazebo world using the steps mentioned above.
Navigate to the bot_control directory:
```bash

cd src/bot_control/bot_control
```


Run the reading_laser.py script to visualize the filtered readings in RViz:
```bash
    python3 reading_laser.py
```

![image](https://github.com/user-attachments/assets/f2b5c4b4-dbba-4173-b73d-76169866cccc)

![image](https://github.com/user-attachments/assets/9fc8df67-b35c-4a6e-83cb-cc96ad86e247)


## Important RViz Displays

When using RViz, make sure to add the following important displays:

Camera
Filtered Scan (will appear as /scan but with the topic name of /filtered_scan)

![image](https://github.com/user-attachments/assets/d083c270-4d5b-4044-9974-122085455d2d)
