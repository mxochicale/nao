MoveIt  TEST
---

Check if you see a robot, [check the tutorial](https://github.com/ros-naoqi/nao_moveit_config)

```
roslaunch nao_moveit_config demo.launch
```


## MoveIt on a real robot

First, set NAO_IP environment variable to your robot's IP address:
```
export NAO_IP=169.254.199.42
```
Launch the DCM bringup:
```
roslaunch nao_dcm_bringup nao_dcm_H25_bringup_remote.launch
```
Wait until it is ready, then run:
```
roslaunch nao_moveit_config moveit_planner.launch
```


https://github.com/nlyubova/tutorials-for-Nao-Pepper-Romeo



## ERROR: cannot launch node of type [naoqi_dcm_driver/naoqi_dcm_driver]: naoqi_dcm_driver

```
$ roslaunch nao_dcm_bringup nao_dcm_H25_bringup_remote.launch
... logging to /home/map479/.ros/log/99086284-6619-11e7-b026-7071bc0c1eed/roslaunch-map479-DQ57TM-8118.log
Checking log directory for disk usage. This may take awhile.
Press Ctrl-C to interrupt
Done checking log file disk usage. Usage is <1GB.

xacro: Traditional processing is deprecated. Switch to --inorder processing!
To check for compatibility of your document, use option --check-order.
For more infos, see http://wiki.ros.org/xacro#Processing_Order
xacro.py is deprecated; please use xacro instead
started roslaunch server http://map479-DQ57TM:34156/

SUMMARY
========

PARAMETERS
 * /nao_dcm/Head_controller/joints: ['HeadYaw', 'Head...
 * /nao_dcm/Head_controller/type: position_controll...
 * /nao_dcm/LeftArm_controller/joints: ['LShoulderPitch'...
 * /nao_dcm/LeftArm_controller/type: position_controll...
 * /nao_dcm/LeftFoot_controller/joints: ['LAnklePitch', '...
 * /nao_dcm/LeftFoot_controller/type: position_controll...
 * /nao_dcm/LeftHand_controller/joints: ['LHand']
 * /nao_dcm/LeftHand_controller/type: position_controll...
 * /nao_dcm/LeftLeg_controller/joints: ['LHipRoll', 'LHi...
 * /nao_dcm/LeftLeg_controller/type: position_controll...
 * /nao_dcm/Pelvis_controller/joints: ['LHipYawPitch']
 * /nao_dcm/Pelvis_controller/type: position_controll...
 * /nao_dcm/RightArm_controller/joints: ['RShoulderPitch'...
 * /nao_dcm/RightArm_controller/type: position_controll...
 * /nao_dcm/RightFoot_controller/joints: ['RAnklePitch', '...
 * /nao_dcm/RightFoot_controller/type: position_controll...
 * /nao_dcm/RightHand_controller/joints: ['RHand']
 * /nao_dcm/RightHand_controller/type: position_controll...
 * /nao_dcm/RightLeg_controller/joints: ['RHipRoll', 'RHi...
 * /nao_dcm/RightLeg_controller/type: position_controll...
 * /nao_dcm/joint_state_controller/publish_rate: 50
 * /nao_dcm/joint_state_controller/type: joint_state_contr...
 * /naoqi_dcm_driver/BodyType: H25
 * /naoqi_dcm_driver/BottomCameraEnabled: True
 * /naoqi_dcm_driver/CameraBrokerIP: 0.0.0.0
 * /naoqi_dcm_driver/CameraBrokerPort: 54001
 * /naoqi_dcm_driver/CameraFrequency: 15
 * /naoqi_dcm_driver/ControllerFrequency: 10
 * /naoqi_dcm_driver/DriverBrokerIP: 127.0.0.1
 * /naoqi_dcm_driver/DriverBrokerPort: 54000
 * /naoqi_dcm_driver/JointPrecision: 0.00174532925
 * /naoqi_dcm_driver/OdomFrame: odom
 * /naoqi_dcm_driver/Prefix: nao_dcm
 * /naoqi_dcm_driver/RobotIP: 169.254.199.42
 * /naoqi_dcm_driver/RobotPort: 9559
 * /naoqi_dcm_driver/TopCameraEnabled: True
 * /naoqi_dcm_driver/TopicQueue: 10
 * /naoqi_dcm_driver/UseCamera: True
 * /naoqi_dcm_driver/Version: V4
 * /naoqi_dcm_driver/motor_groups: Body
 * /naoqi_dcm_driver/network_interface: eth0
 * /naoqi_dcm_driver/use_dcm: False
 * /robot_description: <?xml version="1....
 * /rosdistro: kinetic
 * /rosversion: 1.12.7

NODES
  /
    nao_trajectory_controller (controller_manager/spawner)
    naoqi_dcm_driver (naoqi_dcm_driver/naoqi_dcm_driver)

auto-starting new master
process[master]: started with pid [8132]
ROS_MASTER_URI=http://localhost:11311

setting /run_id to 99086284-6619-11e7-b026-7071bc0c1eed
process[rosout-1]: started with pid [8145]
started core service [/rosout]
process[nao_trajectory_controller-2]: started with pid [8162]
ERROR: cannot launch node of type [naoqi_dcm_driver/naoqi_dcm_driver]: naoqi_dcm_driver
ROS path [0]=/opt/ros/kinetic/share/ros
ROS path [1]=/home/map479/catkin_ws/src
ROS path [2]=/opt/ros/kinetic/share
[INFO] [1499764580.828330]: Controller Spawner: Waiting for service controller_manager/load_controller
```
