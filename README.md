# 🚁 ROS2 Swarm Drone Project

A ROS 2 Humble based Leader-Follower Swarm Drone Simulation developed using Python and ROS2 communication mechanisms.

## 📖 Overview

This project demonstrates a basic swarm drone system where:

- One drone acts as the Leader.
- Multiple drones act as Followers.
- Followers continuously receive the leader's position.
- Followers maintain formation using configurable offsets.
- Communication is achieved through ROS2 Topics.

This project serves as a foundation for future development of:

- Autonomous Drone Swarms
- Formation Flying
- Multi-Agent Systems
- PX4 Integration
- Gazebo Simulation
- Real Drone Deployment

---

## 🏗️ Project Architecture

```text
                     +----------------+
                     | Leader Drone   |
                     | /leader_pose   |
                     +--------+-------+
                              |
          ------------------------------------------
          |                    |                  |
          |                    |                  |
          ▼                    ▼                  ▼

 +----------------+  +----------------+  +----------------+
 | Follower #1    |  | Follower #2    |  | Follower #3    |
 | /follower1_pose|  | /follower2_pose|  | /follower3_pose|
 +----------------+  +----------------+  +----------------+
```

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
│       ├── package.xml
│       ├── setup.py
│       ├── setup.cfg
│       └── resource
│
├── build
├── install
├── log
└── README.md
```

---

## 🚀 Features

- ROS2 Humble Compatible
- Python-Based Nodes
- Publisher-Subscriber Communication
- Leader-Follower Formation Control
- Real-Time Position Updates
- Configurable Formation Offsets
- Lightweight Architecture
- Easily Extendable

---

## 🔧 Requirements

### Software

- Ubuntu 22.04
- ROS2 Humble
- Python 3.10+
- Colcon
- Git

### ROS2 Packages

```bash
sudo apt update
sudo apt install -y \
python3-colcon-common-extensions \
ros-humble-geometry-msgs
```

---

## ⚙️ Build Instructions

### Clone Repository

```bash
git clone https://github.com/Sumitb09/swarm-drone-ros2.git
cd swarm-drone-ros2
```

### Source ROS2

```bash
source /opt/ros/humble/setup.bash
```

### Build Workspace

```bash
colcon build
```

### Source Workspace

```bash
source install/setup.bash
```

---

## ▶️ Running the Swarm

### Terminal 1 — Leader Drone

```bash
source /opt/ros/humble/setup.bash
source install/setup.bash

ros2 run leader_follower leader_node
```

---

### Terminal 2 — Follower 1

```bash
source /opt/ros/humble/setup.bash
source install/setup.bash

ros2 run leader_follower follower_node \
--ros-args \
-p follower_id:=1 \
-p x_offset:=-2.0 \
-p y_offset:=-2.0
```

---

### Terminal 3 — Follower 2

```bash
source /opt/ros/humble/setup.bash
source install/setup.bash

ros2 run leader_follower follower_node \
--ros-args \
-p follower_id:=2 \
-p x_offset:=-2.0 \
-p y_offset:=2.0
```

---

### Terminal 4 — Follower 3

```bash
source /opt/ros/humble/setup.bash
source install/setup.bash

ros2 run leader_follower follower_node \
--ros-args \
-p follower_id:=3 \
-p x_offset:=-4.0 \
-p y_offset:=0.0
```

---

## 📡 ROS2 Topics

### List Topics

```bash
ros2 topic list
```

Expected Output:

```text
/leader_pose
/follower1_pose
/follower2_pose
/follower3_pose
```

---

### View Leader Position

```bash
ros2 topic echo /leader_pose
```

---

### View Follower Position

```bash
ros2 topic echo /follower1_pose
```

```bash
ros2 topic echo /follower2_pose
```

```bash
ros2 topic echo /follower3_pose
```

---

## 📊 Example Output

Leader:

```text
Publishing Leader Position
X = 100
Y = 50
Z = 10
```

Follower 1:

```text
Following Leader
X = 98
Y = 48
```

Follower 2:

```text
Following Leader
X = 98
Y = 52
```

Follower 3:

```text
Following Leader
X = 96
Y = 50
```

---

## 🛠 Technologies Used

- ROS2 Humble
- Python
- rclpy
- geometry_msgs
- Colcon
- Git
- Linux

---

## 🔮 Future Improvements

- Gazebo Integration
- RViz Visualization
- PX4 SITL Integration
- MAVROS Support
- Drone Formation Control
- Obstacle Avoidance
- Path Planning
- Multi-Agent Coordination
- Real Drone Deployment

---

## 👨‍💻 Author

### Sumit Bharti

- Electronics, Communication & IoT Engineer
- Robotics Developer
- ROS2 Enthusiast
- Open Source Contributor

GitHub:
https://github.com/Sumitb09

---

## 📜 License

MIT License

Copyright (c) 2026 Sumit Bharti

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files to deal in the Software without restriction.
