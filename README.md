# Stark's Assembly Bay

A ROS 2 Humble project implementing robot telemetry and a simple robotic arm model.

## Q1: Robot Telemetry

* Publishes commands for three robot joints.
* Monitors joint positions.
* Checks whether each joint is within its allowed range.
* Publishes overall robot status on `robot_status`.

### Topics

| Topic             | Type    |
| ----------------- | ------- |
| `/joint1_command` | Float32 |
| `/joint2_command` | Float32 |
| `/joint3_command` | Float32 |
| `/robot_status`   | String  |

### Nodes

* `robot_controller`
* `robot_monitor`
* `robot_status`

### How did we build

```bash
cd ~/starks_assembly_bay
colcon build
source install/setup.bash
```

### Run

```bash
ros2 launch robot_telemetry telemetry.launch.py
```

### Example Output(attached screenshot)

```text
Joint 1: 160.9° -> SAFE
Joint 2: 163.7° -> SAFE
Joint 3: -8.8 cm -> LIMIT EXCEEDED
```

## Q2

Contains the URDF/Xacro model and RViz visualization of Stark's robotic arm.

### Run 

```bash
ros2 launch starks_arm_description display.launch.py
```
