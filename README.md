# tcebot_slam Package

## Overview

The `tcebot_slam` package is a ROS 2 package for integrating SLAM functionalities into the `tcebot` robot. It includes necessary configurations, launch files, and dependencies for setting up and running SLAM.

## Installation

To install this package in your ROS 2 workspace:

```bash
cd ~/ros2_ws/src
git clone https://github.com/dhanushshettigar/tcebot_slam.git
cd ~/ros2_ws
colcon build --packages-select tcebot_slam
source install/setup.bash
```


## Running SLAM with a Robot in Simulation

![tcebot slam](https://raw.githubusercontent.com/dhanushshettigar/tcebot_slam/refs/heads/main/media/gz-slam.png)

If using a Gazebo-based simulation, launch both the simulation and SLAM:

```bash
export QT_QPA_PLATFORM=xcb && ros2 launch tcebot_sim simulation.launch.py headless:=False
```
Run Slam_toolbox

```bash
ros2 launch tcebot_slam slam_toolbox_async.launch.py
```

## Saving Map

After mapping an area, you can save the map:

```bash
ros2 run nav2_map_server map_saver_cli -f ~/map
```

