Usage
---


1. Turn on NAO!
and wait until it says


2. Open an terminal  and
```
roslaunch naoqi_driver naoqi_driver.launch nao_ip:=169.254.199.42
```


3. Other terminal

```
$ rosnode info /naoqi_driver_node
--------------------------------------------------------------------------------
Node [/naoqi_driver_node]
Publications:
 * /naoqi_driver_node/camera/front/image_raw [sensor_msgs/Image]
 * /naoqi_driver_node/camera/front/image_raw/compressed/parameter_descriptions [dynamic_reconfigure/ConfigDescription]
 * /naoqi_driver_node/camera/bottom/image_raw/theora/parameter_descriptions [dynamic_reconfigure/ConfigDescription]
 * /naoqi_driver_node/camera/bottom/image_raw/compressed/parameter_descriptions [dynamic_reconfigure/ConfigDescription]
 * /naoqi_driver_node/sonar/right [sensor_msgs/Range]
 * /naoqi_driver_node/camera/bottom/image_raw [sensor_msgs/Image]
 * /naoqi_driver_node/head_touch [naoqi_bridge_msgs/HeadTouch]
 * /naoqi_driver_node/imu/torso [sensor_msgs/Imu]
 * /naoqi_driver_node/camera/bottom/image_raw/theora/parameter_updates [dynamic_reconfigure/Config]
 * /naoqi_driver_node/camera/front/camera_info [sensor_msgs/CameraInfo]
 * /naoqi_driver_node/bumper [naoqi_bridge_msgs/Bumper]
 * /naoqi_driver_node/camera/front/image_raw/theora/parameter_updates [dynamic_reconfigure/Config]
 * /naoqi_driver_node/hand_touch [naoqi_bridge_msgs/HandTouch]
 * /diagnostics [diagnostic_msgs/DiagnosticArray]
 * /naoqi_driver_node/sonar/left [sensor_msgs/Range]
 * /naoqi_driver_node/audio [naoqi_bridge_msgs/AudioBuffer]
 * /naoqi_driver_node/camera/front/image_raw/theora/parameter_descriptions [dynamic_reconfigure/ConfigDescription]
 * /naoqi_driver_node/odom [nav_msgs/Odometry]
 * /joint_states [sensor_msgs/JointState]
 * /rosout [rosgraph_msgs/Log]
 * /tf [tf2_msgs/TFMessage]
 * /naoqi_driver_node/camera/bottom/image_raw/compressed/parameter_updates [dynamic_reconfigure/Config]
 * /naoqi_driver_node/camera/bottom/image_raw/compressed [sensor_msgs/CompressedImage]
 * /naoqi_driver_node/camera/bottom/camera_info [sensor_msgs/CameraInfo]
 * /naoqi_driver_node/camera/front/image_raw/compressed/parameter_updates [dynamic_reconfigure/Config]
 * /naoqi_driver_node/camera/front/image_raw/theora [theora_image_transport/Packet]
 * /naoqi_driver_node/camera/bottom/image_raw/theora [theora_image_transport/Packet]
 * /naoqi_driver_node/camera/front/image_raw/compressed [sensor_msgs/CompressedImage]
 * /naoqi_driver_node/info [naoqi_bridge_msgs/StringStamped]

Subscriptions:
 * /speech [unknown type]
 * /move_base_simple/goal [unknown type]
 * /cmd_vel [unknown type]
 * /joint_angles [unknown type]

Services:
 * /naoqi_driver_node/get_loggers
 * /naoqi_driver/get_robot_config
 * /naoqi_driver_node/camera/front/image_raw/compressed/set_parameters
 * /naoqi_driver_node/camera/bottom/image_raw/compressedDepth/set_parameters
 * /naoqi_driver_node/camera/front/image_raw/compressedDepth/set_parameters
 * /naoqi_driver_node/camera/bottom/image_raw/theora/set_parameters
 * /naoqi_driver_node/camera/bottom/image_raw/compressed/set_parameters
 * /naoqi_driver_node/set_logger_level
 * /naoqi_driver_node/camera/front/image_raw/theora/set_parameters


contacting node http://169.254.164.69:46829/ ...
Pid: 5868
Connections:
 * topic: /rosout
    * to: /rosout
    * direction: outbound
    * transport: TCPROS
```



3. Open a new terminal and check the nodes

```
$ rostopic list
/cmd_vel
/diagnostics
/joint_angles
/joint_states
/move_base_simple/goal
/naoqi_driver_node/audio
/naoqi_driver_node/bumper
/naoqi_driver_node/camera/bottom/camera_info
/naoqi_driver_node/camera/bottom/image_raw
/naoqi_driver_node/camera/bottom/image_raw/compressed
/naoqi_driver_node/camera/bottom/image_raw/compressed/parameter_descriptions
/naoqi_driver_node/camera/bottom/image_raw/compressed/parameter_updates
/naoqi_driver_node/camera/bottom/image_raw/theora
/naoqi_driver_node/camera/bottom/image_raw/theora/parameter_descriptions
/naoqi_driver_node/camera/bottom/image_raw/theora/parameter_updates
/naoqi_driver_node/camera/front/camera_info
/naoqi_driver_node/camera/front/image_raw
/naoqi_driver_node/camera/front/image_raw/compressed
/naoqi_driver_node/camera/front/image_raw/compressed/parameter_descriptions
/naoqi_driver_node/camera/front/image_raw/compressed/parameter_updates
/naoqi_driver_node/camera/front/image_raw/theora
/naoqi_driver_node/camera/front/image_raw/theora/parameter_descriptions
/naoqi_driver_node/camera/front/image_raw/theora/parameter_updates
/naoqi_driver_node/hand_touch
/naoqi_driver_node/head_touch
/naoqi_driver_node/imu/torso
/naoqi_driver_node/info
/naoqi_driver_node/odom
/naoqi_driver_node/sonar/left
/naoqi_driver_node/sonar/right
/rosout
/rosout_agg
/speech
/tf
```


## Cameras

```
rostopic echo /naoqi_driver_node/camera/bottom/camera_info
rostopic echo /naoqi_driver_node/camera/front/camera_info

```


```
rqt_image_view /naoqi_driver_node/camera/bottom/image_raw
rqt_image_view /naoqi_driver_node/camera/front/image_raw
```

## joint angle states
```
rostopic echo /joint_states
```


/cmd_vel
/diagnostics
/joint_angles

/move_base_simple/goal
/naoqi_driver_node/audio
/naoqi_driver_node/bumper


/naoqi_driver_node/hand_touch
/naoqi_driver_node/head_touch
/naoqi_driver_node/imu/torso
/naoqi_driver_node/info
/naoqi_driver_node/odom
/naoqi_driver_node/sonar/left
/naoqi_driver_node/sonar/right
/rosout
/rosout_agg
/speech
/tf




## rviz

T1 roslaunch naoqi_driver naoqi_driver.launch nao_ip:=169.254.199.42
T2 rosrun rviz rviz

on rviz
```
Global Status: Error
TF
  Status Warn
  CameraBottom_frame No transform form
```
