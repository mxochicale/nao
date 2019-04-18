Installation
---


# Setup ROS on your machine

Install ROS Kinetic for Ubuntu 16 http://wiki.ros.org/Installation


# 1.  Basic Configuration

```
sudo apt-get update
sudo apt-get install ros-kinetic-nao-robot ros-kinetic-nao-meshes  ros-kinetic-nao-description ros-kinetic-naoqi-driver

```

# MoveIt

install MoveIt!-specific packages, check https://github.com/ros-naoqi/nao_moveit_config

```
sudo apt-get install ros-kinetic-moveit ros-kinetic-moveit-visual-tools
```

# compile the following packages from source

```
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/src
git clone https://github.com/ros-naoqi/nao_moveit_config
git clone https://github.com/ros-naoqi/nao_virtual
git clone https://github.com/ros-naoqi/nao_dcm_robot
git clone https://github.com/ros-naoqi/naoqi_driver
cd ~/catkin_ws/ && catkin_make
```

# test

source ~/.bashrc

```
roslaunch naoqi_driver naoqi_driver.launch nao_ip:=169.254.199.42
```



# issue

* [ ] no launch

	cannot find any roslaunch file for nao*

	
	Sun 24 Feb 06:48:25 GMT 2019

