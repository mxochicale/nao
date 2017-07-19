References
---



# ROS basics for Aldebaran/SoftBank robots.
By Natalia Lyubova June 2016



### Setup your system

install ROS (Indigo is recommended), check http://wiki.ros.org/Installation
```
sudo apt-get install ros-indigo-desktop
source /opt/ros/indigo/setup.bash
```


if you use Nao (recommended), check http://wiki.ros.org/nao
```
sudo apt-get install ros-indigo-nao-robot ros-indigo-nao-meshes
```


### 1.  Basic Configuration

* [nao_robot](https://github.com/ros-naoqi/nao_robot)  package is a meta-package that includes
  * Robot model (URDF): nao_description
  * Robot-specific Startup: nao_bringup
  * Applications: nao_apps
* install:
```
sudo apt-get install ros-indigo-nao-robot
```



* [nao_robot/nao_description](http://wiki.ros.org/nao_description) includes:
* URDF (Universal Robot  Description Format): XML  describing the rigid kinematics
* meshes
* basis for
  * low level: kinematics, actuators/sensors
  * high level: planning, navigation, grasping
  * GUIs
* install:
```
sudo apt-get install ros-indigo-nao-description
```


## 2. NAOqi Driver


[naoqi_driver](http://ros-naoqi.github.io/naoqi_driver) includes

* Driver module between NAOqi OS and ROS
* Common for all Aldebaran robots
* Gets data from NAOqi hence ensuring low latency and CPU usage
  * actuator data
  * sensor data
  * basic diagnostic for battery, temperature
* Allows to control:
  * /cmd_vel
  * /move_base_simple/goal
  * /joint_angles
* You can run it locally on a robot or remotely on PC







### References
* [Slides](http://www.tech.plym.ac.uk/SoCCE/CRNS/APRIL/cefalu-event/APRIL_Cefalu_Lyubova-1.pdf)
* [Source Code](https://github.com/nlyubova/tutorials-for-Nao-Pepper-Romeo)



# ROS NAO Tutorial
By Lagrand et al. 2016


ROS packages for the Nao robot.
```
sudo apt-get install ros-<distro>-nao-robot
sudo apt-get install ros-<distro>-nao-bringup
sudo apt-get install ros-<distro>-naoqi-bridge
sudo apt-get install ros-<distro>-naoqi-extras
```

Correct working of the naoqi_driver can be verified by:
```
ROS_IP= roscore
rosrun naoqi_driver naoqi_driver_node --qi-url=tcp://:9559 --roscore_ip --network_interface
rosnode info /nao_robot
kill driver
```

Correct working of the full nao_bringup can be verified by:
```
Download world.stl
roslaunch nao_bringup nao_full_py.launch nao_ip:= roscore_ip:=
rosrun rviz rviz
add the MoveIt as MotionPlanner. add world.stl as Scene Object:
```

References
* [RosNaoTutorial](https://staff.fnwi.uva.nl/a.visser/activities/FutureOfRescue/day5.php)
* [Slides](https://staff.fnwi.uva.nl/a.visser/activities/FutureOfRescue/RosNaoTutorial.pdf)
