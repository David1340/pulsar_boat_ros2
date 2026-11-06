# Pulsar Boat ROS 2

ROS 2 package for the Pulsar Boat platform, providing robot visualization, sensor integration, and system bringup.

## 1. Overview

This repository contains the ROS 2 package responsible for the Pulsar Boat robot description, visualization, and system bringup.

The package includes:

- Boat 3D model.
- URDF robot description.
- LiDAR mounting structure and TF frames.
- RViz visualization configuration.
- Launch files for visualization and system bringup.
- Shell scripts for environment setup and system execution.

## 2. Requirements

The following software is required:

- Ubuntu 22.04
- ROS 2 Humble
- Livox SDK2
- Livox ROS Driver 2

### 2.1 ROS 2 Humble

Follow the official installation instructions:

https://docs.ros.org/en/humble/Installation.html

### 2.2 Livox SDK2

Follow the official installation instructions:

https://github.com/Livox-SDK/Livox-SDK2

### 2.3 Livox ROS Driver 2

Follow the official installation instructions:

https://github.com/Livox-SDK/livox_ros_driver2

## 3. Workspace Setup

Clone this repository into your ROS 2 workspace:

```bash
mkdir -p ~/pulsar_boat_ws/src
cd ~/pulsar_boat_ws/src

git clone https://github.com/David1340/pulsar_boat_ros2.git
```

Build the package:

```bash
cd ~/pulsar_boat_ws

source /opt/ros/humble/setup.bash

colcon build --packages-select pulsar_boat

source install/setup.bash
```

## 4. Package Structure

```text
pulsar_boat_ros2/
├── launch/
├── meshes/
├── urdf/
├── rviz/
├── package.xml
├── setup.py
└── README.md
```

## 5. Usage

Before executing any launch file, source the ROS 2 and workspace environments:

```bash
source /opt/ros/humble/setup.bash
source ~/ws_livox/install/setup.bash
source ~/pulsar_boat_ws/install/setup.bash
```

### 5.1 Boat Visualization

Launch the boat visualization:

```bash
ros2 launch pulsar_boat boat_visualization.launch.py
```

This launch file starts the robot description and RViz visualization.

The boat model, LiDAR mounting mast, and Livox sensor are represented in RViz.

### 5.2 Livox MID-360 Visualization

Launch the Livox ROS Driver 2 visualization:

```bash
ros2 launch livox_ros_driver2 rviz_MID360_launch.py
```

This launch file starts the Livox MID-360 driver and its RViz visualization.

### 5.3 System Bringup

Launch the complete Pulsar Boat system:

```bash
ros2 launch pulsar_boat bringup.launch.py
```

The bringup launch file integrates the required components, including the boat visualization, MAVROS, and Livox driver.

## 6. Shell Scripts

The repository provides two shell scripts to simplify the operation of the boat's motors.

### 6.1 First-Time Setup

Before using the scripts for the first time, make sure they have the appropriate permissions:

```bash
chmod +x guided.sh
chmod +x arming.sh
```

### 6.2 Guided Mode

**`guided.sh`**

Enables Guided mode through a ROS 2 service call.

Usage:

```bash
./guided.sh
```

### 6.3 Motor Arming

**`arming.sh`**

Arms the boat's motors through a ROS 2 service call.

Usage:

```bash
./arming.sh
```

## 7. TF Frames

The robot description defines the following TF structure:

```text
world
 └── base_link
      └── lidar_mast_link
           └── livox_frame
```

- `world`: Global reference frame.
- `base_link`: Main reference frame of the boat.
- `lidar_mast_link`: Reference frame of the LiDAR mounting mast.
- `livox_frame`: Reference frame of the Livox MID-360 sensor.

The transformations between the boat and sensor are defined using fixed joints in the URDF and published by `robot_state_publisher`.

## 8. Useful Commands

List active ROS 2 nodes:

```bash
ros2 node list
```

List available topics:

```bash
ros2 topic list
```

Check TF transformations:

```bash
ros2 run tf2_ros tf2_echo base_link livox_frame
```

Generate the TF tree:

```bash
ros2 run tf2_tools view_frames
```

---

## 9. Troubleshooting

### Package not found

Make sure the ROS 2 and workspace setup files have been sourced:

```bash
source /opt/ros/humble/setup.bash
source ~/pulsar_boat_ws/install/setup.bash
```

### Livox driver initialization failure

Check the network configuration, the host IP address in the MID-360 configuration file, and whether another Livox driver instance is already running.

### Changes to the URDF or launch files are not reflected

Rebuild the package and source the workspace again:

```bash
cd ~/pulsar_boat_ws
colcon build --packages-select pulsar_boat
source install/setup.bash
```
