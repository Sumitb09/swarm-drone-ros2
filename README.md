# 🚁 SWARN: ROS 2 + PX4 Leader-Follower Swarm Drone System

A ROS 2 Humble and PX4-based swarm drone framework implementing leader-follower formation control using real PX4 SITL telemetry through Micro XRCE-DDS.

---

## 📖 Overview

SWARN is a multi-drone swarm simulation framework developed using:

- ROS 2 Humble
- PX4 Autopilot
- PX4 SITL
- Micro XRCE-DDS
- Python (rclpy)
- Docker

The system demonstrates a leader-follower architecture where:

- A PX4-controlled leader drone publishes real-time position data.
- ROS 2 nodes subscribe to PX4 telemetry.
- Follower drones compute formation positions relative to the leader.
- Formation targets are continuously updated in real time.

---

## 🏗 System Architecture

```text
                   PX4 SITL Leader
                          │
                          ▼
         /fmu/out/vehicle_local_position_v1
                          │
                          ▼
                    leader_node.py
                          │
                          ▼
                     /leader_pose
                          │
                          ▼
                   follower_node.py
                          │
          ┌───────────────┼───────────────┐
          ▼               ▼               ▼

   /follower1_pose  /follower2_pose  /follower3_pose
```

---

## 🚀 Features

### ROS 2 Integration

- ROS 2 Humble Compatible
- Python-Based Nodes
- DDS Communication
- Publisher-Subscriber Architecture

### PX4 Integration

- PX4 SITL Support
- Micro XRCE-DDS Bridge
- Real-Time Vehicle Telemetry
- Vehicle Local Position Streaming

### Swarm Features

- Leader-Follower Architecture
- Formation Control
- Configurable Formation Offsets
- Multi-Agent Coordination
- Real-Time Target Generation

### Development Environment

- Docker-Based Deployment
- Ubuntu 22.04
- Git Version Control
- Modular ROS 2 Package Structure

---

## 📂 Project Structure

```text
swarm_ws
│
├── src
│   └── leader_follower
│       ├── leader_follower
│       │   ├── __init__.py
│       │   ├── leader_node.py
│       │   └── follower_node.py
│       │
│       ├── scripts
│       │   └── swarm_dashboard.py
│       │
│       ├── package.xml
│       ├── setup.py
│       ├── setup.cfg
│       ├── resource
│       └── test
│
├── build
├── install
├── log
└── README.md
```

---

## 🔧 Requirements

### Operating System

- Ubuntu 22.04 LTS

### ROS

- ROS 2 Humble

### PX4

- PX4 Autopilot
- PX4 SITL
- px4_msgs
- Micro XRCE-DDS Agent

### Dependencies

```bash
sudo apt update

sudo apt install -y \
python3-colcon-common-extensions \
python3-pip \
git
```

---

## ⚙️ Build Instructions

### Clone Repository

```bash
git clone https://github.com/Sumitb09/swarm-drone-ros2.git

cd swarm-drone-ros2
```

### Source ROS 2

```bash
source /opt/ros/humble/setup.bash
```

### Build Workspace

```bash
colcon build --symlink-install
```

### Source Workspace

```bash
source install/setup.bash
```

---

## 🚁 Running the Swarm

### Terminal 1 – Start Micro XRCE Agent

```bash
MicroXRCEAgent udp4 -p 8888
```

### Terminal 2 – Start PX4 SITL

```bash
cd PX4-Autopilot

./build/px4_sitl_default/bin/px4 \
./build/px4_sitl_default/etc
```

### Terminal 3 – Start Leader Node

```bash
source /opt/ros/humble/setup.bash
source install/setup.bash

ros2 run leader_follower leader_node
```

### Terminal 4 – Start Follower Node

```bash
source /opt/ros/humble/setup.bash
source install/setup.bash

ros2 run leader_follower follower_node
```

---

## 📡 ROS Topics

### PX4 Topics

```text
/fmu/out/vehicle_local_position_v1
/fmu/out/vehicle_attitude
/fmu/out/vehicle_odometry
```

### Leader Topic

```text
/leader_pose
```

### Formation Topics

```text
/follower1_pose
/follower2_pose
/follower3_pose
```

---

## 🧪 Validation Results

Successfully verified:

### PX4 → ROS2 Communication

```bash
ros2 topic echo /fmu/out/vehicle_local_position_v1 --once
```

### Leader Position Publishing

```bash
ros2 topic echo /leader_pose --once
```

### Formation Target Generation

```bash
ros2 topic echo /follower1_pose --once
ros2 topic echo /follower2_pose --once
ros2 topic echo /follower3_pose --once
```

All topics publish valid real-time position data.

---

## 🛠 Technologies Used

- ROS 2 Humble
- PX4 Autopilot
- PX4 SITL
- Micro XRCE-DDS
- Python
- rclpy
- geometry_msgs
- Docker
- Git
- Linux

---

## 🔮 Future Work

- Multi-PX4 Swarm Deployment
- Offboard Control
- Autonomous Formation Flight
- Gazebo Harmonic Visualization
- Obstacle Avoidance
- Path Planning
- Mission Coordination
- MAVLink Integration
- Real Hardware Deployment

---

## 👨‍💻 Author

### Sumit Bharti

- Electronics, Communication & IoT Engineer
- Robotics Developer
- ROS 2 Developer
- PX4 Enthusiast
- Open Source Contributor

GitHub: https://github.com/Sumitb09

---

## 📜 License

MIT License

Copyright (c) 2026 Sumit Bharti

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files to deal in the Software without restriction.
