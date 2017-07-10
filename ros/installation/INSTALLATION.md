Installation
---


# Setup ROS on your machine

Install ROS Kinetic for Ubuntu 16 http://wiki.ros.org/Installation


# 1.  Basic Configuration

```
sudo apt-get update
sudo apt-get install ros-kinetic-nao-robot ros-kinetic-nao-meshes
```

```
$ sudo apt-get install ros-kinetic-nao-robot ros-kinetic-nao-meshes
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following packages were automatically installed and are no longer required:
  libmircommon5 linux-headers-4.4.0-31 linux-headers-4.4.0-31-generic linux-headers-4.4.0-78 linux-headers-4.4.0-78-generic linux-headers-4.4.0-79 linux-headers-4.4.0-79-generic
  linux-image-4.4.0-31-generic linux-image-4.4.0-78-generic linux-image-4.4.0-79-generic linux-image-extra-4.4.0-31-generic linux-image-extra-4.4.0-78-generic linux-image-extra-4.4.0-79-generic
  ubuntu-core-launcher
Use 'sudo apt autoremove' to remove them.
The following additional packages will be installed:
  ros-kinetic-camera-info-manager-py ros-kinetic-humanoid-nav-msgs ros-kinetic-nao-apps ros-kinetic-nao-bringup ros-kinetic-nao-description ros-kinetic-naoqi-apps ros-kinetic-naoqi-bridge
  ros-kinetic-naoqi-bridge-msgs ros-kinetic-naoqi-driver ros-kinetic-naoqi-driver-py ros-kinetic-naoqi-libqi ros-kinetic-naoqi-libqicore ros-kinetic-naoqi-pose ros-kinetic-naoqi-sensors-py
  ros-kinetic-naoqi-tools
The following NEW packages will be installed
  ros-kinetic-camera-info-manager-py ros-kinetic-humanoid-nav-msgs ros-kinetic-nao-apps ros-kinetic-nao-bringup ros-kinetic-nao-description ros-kinetic-nao-meshes ros-kinetic-nao-robot
  ros-kinetic-naoqi-apps ros-kinetic-naoqi-bridge ros-kinetic-naoqi-bridge-msgs ros-kinetic-naoqi-driver ros-kinetic-naoqi-driver-py ros-kinetic-naoqi-libqi ros-kinetic-naoqi-libqicore
  ros-kinetic-naoqi-pose ros-kinetic-naoqi-sensors-py ros-kinetic-naoqi-tools
0 to upgrade, 17 to newly install, 0 to remove and 244 not to upgrade.
Need to get 4,783 kB of archives.
After this operation, 32.4 MB of additional disk space will be used.
Do you want to continue? [Y/n]

```

# MoveIt

install MoveIt!-specific packages, check https://github.com/ros-naoqi/nao_moveit_config

```
sudo apt-get install ros-kinetic-moveit ros-kinetic-moveit-visual-tools
```

```
$ sudo apt-get install ros-kinetic-moveit ros-kinetic-moveit-visual-tools
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following packages were automatically installed and are no longer required:
  libmircommon5 linux-headers-4.4.0-31 linux-headers-4.4.0-31-generic linux-headers-4.4.0-78 linux-headers-4.4.0-78-generic linux-headers-4.4.0-79 linux-headers-4.4.0-79-generic
  linux-image-4.4.0-31-generic linux-image-4.4.0-78-generic linux-image-4.4.0-79-generic linux-image-extra-4.4.0-31-generic linux-image-extra-4.4.0-78-generic linux-image-extra-4.4.0-79-generic
  ubuntu-core-launcher
Use 'sudo apt autoremove' to remove them.
The following additional packages will be installed:
  libccd-dev libccd2 libfcl-0.5-dev libfcl0.5 libglew-dev python-bs4 python-html5lib python-lxml python-pyassimp ros-kinetic-graph-msgs ros-kinetic-moveit-commander ros-kinetic-moveit-core
  ros-kinetic-moveit-fake-controller-manager ros-kinetic-moveit-kinematics ros-kinetic-moveit-msgs ros-kinetic-moveit-planners ros-kinetic-moveit-planners-ompl ros-kinetic-moveit-plugins
  ros-kinetic-moveit-ros ros-kinetic-moveit-ros-benchmarks ros-kinetic-moveit-ros-control-interface ros-kinetic-moveit-ros-manipulation ros-kinetic-moveit-ros-move-group
  ros-kinetic-moveit-ros-perception ros-kinetic-moveit-ros-planning ros-kinetic-moveit-ros-planning-interface ros-kinetic-moveit-ros-robot-interaction ros-kinetic-moveit-ros-visualization
  ros-kinetic-moveit-ros-warehouse ros-kinetic-moveit-setup-assistant ros-kinetic-moveit-simple-controller-manager ros-kinetic-object-recognition-msgs ros-kinetic-octomap-msgs ros-kinetic-ompl
  ros-kinetic-rviz-visual-tools ros-kinetic-srdfdom ros-kinetic-urdfdom-py ros-kinetic-warehouse-ros
Suggested packages:
  python-genshi python-lxml-dbg python-lxml-doc
The following NEW packages will be installed
  libccd-dev libccd2 libfcl-0.5-dev libfcl0.5 libglew-dev python-bs4 python-html5lib python-lxml python-pyassimp ros-kinetic-graph-msgs ros-kinetic-moveit ros-kinetic-moveit-commander
  ros-kinetic-moveit-core ros-kinetic-moveit-fake-controller-manager ros-kinetic-moveit-kinematics ros-kinetic-moveit-msgs ros-kinetic-moveit-planners ros-kinetic-moveit-planners-ompl
  ros-kinetic-moveit-plugins ros-kinetic-moveit-ros ros-kinetic-moveit-ros-benchmarks ros-kinetic-moveit-ros-control-interface ros-kinetic-moveit-ros-manipulation ros-kinetic-moveit-ros-move-group
  ros-kinetic-moveit-ros-perception ros-kinetic-moveit-ros-planning ros-kinetic-moveit-ros-planning-interface ros-kinetic-moveit-ros-robot-interaction ros-kinetic-moveit-ros-visualization
  ros-kinetic-moveit-ros-warehouse ros-kinetic-moveit-setup-assistant ros-kinetic-moveit-simple-controller-manager ros-kinetic-moveit-visual-tools ros-kinetic-object-recognition-msgs
  ros-kinetic-octomap-msgs ros-kinetic-ompl ros-kinetic-rviz-visual-tools ros-kinetic-srdfdom ros-kinetic-urdfdom-py ros-kinetic-warehouse-ros
0 to upgrade, 40 to newly install, 0 to remove and 244 not to upgrade.
Need to get 11.1 MB of archives.
After this operation, 75.4 MB of additional disk space will be used.
Do you want to continue? [Y/n]

```

compile the following packages from source

```
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/src
git clone https://github.com/ros-naoqi/nao_moveit_config
git clone https://github.com/ros-naoqi/nao_virtual
git clone https://github.com/ros-naoqi/nao_dcm_robot
cd .. && catkin_make
```


```
Base path: /home/map479/catkin_ws
Source space: /home/map479/catkin_ws/src
Build space: /home/map479/catkin_ws/build
Devel space: /home/map479/catkin_ws/devel
Install space: /home/map479/catkin_ws/install
####
#### Running command: "cmake /home/map479/catkin_ws/src -DCATKIN_DEVEL_PREFIX=/home/map479/catkin_ws/devel -DCMAKE_INSTALL_PREFIX=/home/map479/catkin_ws/install -G Unix Makefiles" in "/home/map479/catkin_ws/build"
####
-- Using CATKIN_DEVEL_PREFIX: /home/map479/catkin_ws/devel
-- Using CMAKE_PREFIX_PATH: /home/map479/catkin_ws/devel;/opt/ros/kinetic
-- This workspace overlays: /home/map479/catkin_ws/devel;/opt/ros/kinetic
-- Using PYTHON_EXECUTABLE: /usr/bin/python
-- Using Debian Python package layout
-- Using empy: /usr/bin/empy
-- Using CATKIN_ENABLE_TESTING: ON
-- Call enable_testing()
-- Using CATKIN_TEST_RESULTS_DIR: /home/map479/catkin_ws/build/test_results
-- Found gtest sources under '/usr/src/gtest': gtests will be built
-- Using Python nosetests: /usr/bin/nosetests-2.7
-- catkin 0.7.6
-- BUILD_SHARED_LIBS is on
-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-- ~~  traversing 14 packages in topological order:
-- ~~  - image_pipeline (metapackage)
-- ~~  - nao_control
-- ~~  - nao_dcm_bringup
-- ~~  - camera_calibration
-- ~~  - image_publisher
-- ~~  - image_view
-- ~~  - image_proc
-- ~~  - razor_imu_9dof
-- ~~  - stereo_image_proc
-- ~~  - depth_image_proc
-- ~~  - image_rotate
-- ~~  - usb_cam
-- ~~  - nao_gazebo_plugin
-- ~~  - nao_moveit_config
-- ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
-- +++ processing catkin metapackage: 'image_pipeline'
-- ==> add_subdirectory(image_pipeline/image_pipeline)
-- +++ processing catkin package: 'nao_control'
-- ==> add_subdirectory(nao_virtual/nao_control)
-- +++ processing catkin package: 'nao_dcm_bringup'
-- ==> add_subdirectory(nao_dcm_robot/nao_dcm_bringup)
-- Boost version: 1.58.0
-- +++ processing catkin package: 'camera_calibration'
-- ==> add_subdirectory(image_pipeline/camera_calibration)
-- +++ processing catkin package: 'image_publisher'
-- ==> add_subdirectory(image_pipeline/image_publisher)
-- +++ processing catkin package: 'image_view'
-- ==> add_subdirectory(image_pipeline/image_view)
-- Using these message generators: gencpp;geneus;genlisp;gennodejs;genpy
-- Boost version: 1.58.0
-- Found the following Boost libraries:
--   signals
--   thread
--   chrono
--   system
--   date_time
--   atomic
-- Found OpenCV: /opt/ros/kinetic (found version "3.2.0")
-- +++ processing catkin package: 'image_proc'
-- ==> add_subdirectory(image_pipeline/image_proc)
-- Boost version: 1.58.0
-- Found the following Boost libraries:
--   thread
--   chrono
--   system
--   date_time
--   atomic
-- +++ processing catkin package: 'razor_imu_9dof'
-- ==> add_subdirectory(razor_imu_9dof)
CMake Warning at /opt/ros/kinetic/share/catkin/cmake/catkin_package.cmake:166 (message):
  catkin_package() DEPENDS on 'CATKIN' but neither 'CATKIN_INCLUDE_DIRS' nor
  'CATKIN_LIBRARIES' is defined.
Call Stack (most recent call first):
  /opt/ros/kinetic/share/catkin/cmake/catkin_package.cmake:102 (_catkin_package)
  razor_imu_9dof/CMakeLists.txt:8 (catkin_package)


-- +++ processing catkin package: 'stereo_image_proc'
-- ==> add_subdirectory(image_pipeline/stereo_image_proc)
-- Boost version: 1.58.0
-- Found the following Boost libraries:
--   thread
--   chrono
--   system
--   date_time
--   atomic
-- +++ processing catkin package: 'depth_image_proc'
-- ==> add_subdirectory(image_pipeline/depth_image_proc)
-- Using these message generators: gencpp;geneus;genlisp;gennodejs;genpy
-- Boost version: 1.58.0
-- +++ processing catkin package: 'image_rotate'
-- ==> add_subdirectory(image_pipeline/image_rotate)
-- Using these message generators: gencpp;geneus;genlisp;gennodejs;genpy
-- Found OpenCV: /opt/ros/kinetic (found version "3.2.0") found components:  core imgproc
-- +++ processing catkin package: 'usb_cam'
-- ==> add_subdirectory(usb_cam)
-- +++ processing catkin package: 'nao_gazebo_plugin'
-- ==> add_subdirectory(nao_virtual/nao_gazebo_plugin)
-- +++ processing catkin package: 'nao_moveit_config'
-- ==> add_subdirectory(nao_moveit_config)
-- Configuring done
-- Generating done
-- Build files have been written to: /home/map479/catkin_ws/build
####
#### Running command: "make -j4 -l4" in "/home/map479/catkin_ws/build"
####
[  1%] Built target image_publisher_gencfg
[  3%] Built target image_view_gencfg
[  6%] Built target video_recorder
[  9%] Built target image_publisher_exe
[ 12%] Built target extract_images
[ 18%] Built target image_view_exe
[ 18%] Built target image_saver
[ 21%] Built target disparity_view
[ 28%] Built target image_proc_gencfg
[ 29%] Built target razor_imu_9dof_gencfg
[ 31%] Built target stereo_image_proc_gencfg
[ 32%] Built target image_rotate_gencfg
[ 35%] Built target image_rotate_exe
[ 43%] Built target image_view
[ 45%] Built target stereo_view
[ 60%] Built target depth_image_proc
[ 64%] Built target image_publisher
[ 78%] Built target image_proc
[ 81%] Built target image_rotate
[ 84%] Built target image_proc_exe
[ 90%] Built target stereo_image_proc
[ 93%] Built target usb_cam
[ 96%] Built target stereoimageproc_exe
[100%] Built target usb_cam_node

```



# Testing

update the sources
```
source ~/.bashrc
```

if you have Nao, check Naoqi Driver providing the robot's IP
```
roslaunch naoqi_driver naoqi_driver.launch nao_ip:=169.254.199.42
```


test MoveIt! and check if you see a robot, [check the tutorial](https://github.com/ros-naoqi/nao_moveit_config)

```
roslaunch nao_moveit_config demo.launch
```




https://github.com/nlyubova/tutorials-for-Nao-Pepper-Romeo


# ISSUES


### Could not find network interface named eth0, possible interfaces are ... eno1 lo
```
$ roslaunch naoqi_driver naoqi_driver.launch nao_ip:=169.254.199.42
... logging to /home/map479/.ros/log/fdc53fce-65a8-11e7-8e3b-7071bc0c1eed/roslaunch-map479-DQ57TM-17622.log
Checking log directory for disk usage. This may take awhile.
Press Ctrl-C to interrupt
Done checking log file disk usage. Usage is <1GB.

started roslaunch server http://map479-DQ57TM:46743/

SUMMARY
========

PARAMETERS
 * /rosdistro: kinetic
 * /rosversion: 1.12.7

NODES
  /
    naoqi_driver (naoqi_driver/naoqi_driver_node)

auto-starting new master
process[master]: started with pid [17633]
ROS_MASTER_URI=http://localhost:11311

setting /run_id to fdc53fce-65a8-11e7-8e3b-7071bc0c1eed
process[rosout-1]: started with pid [17646]
started core service [/rosout]
process[naoqi_driver-2]: started with pid [17652]
Receiving information about robot model
set prefix successfully to
[I] 1499716215.251739 17652 qimessaging.session: Session listener created on tcp://0.0.0.0:0
[I] 1499716215.252039 17652 qimessaging.transportserver: TransportServer will listen on: tcp://169.254.164.69:37321
[I] 1499716215.252056 17652 qimessaging.transportserver: TransportServer will listen on: tcp://127.0.0.1:37321
using ip address: 127.0.0.1 @ eth0
found a catkin prefix /opt/ros/kinetic/share/naoqi_driver/share/boot_config.json
load boot config from /opt/ros/kinetic/share/naoqi_driver/share/boot_config.json
found a catkin URDF /opt/ros/kinetic/share/naoqi_driver/share/urdf/nao.urdf
Audio Extractor: Start
RightBumperPressed
LeftBumperPressed
ROS-Driver-RightBumperPressed : Start
HandRightBackTouched
HandRightLeftTouched
HandRightRightTouched
HandLeftBackTouched
HandLeftLeftTouched
HandLeftRightTouched
ROS-Driver-HandRightBackTouched : Start
FrontTactilTouched
MiddleTactilTouched
RearTactilTouched
ROS-Driver-FrontTactilTouched : Start
registered subscriber:	teleop
registered subscriber:	moveto
registered subscriber:	speech
nodehandle reset
Could not find network interface named eth0, possible interfaces are ... eno1 lo
================================================================================REQUIRED process [naoqi_driver-2] has died!
process has died [pid 17652, exit code 1, cmd /opt/ros/kinetic/lib/naoqi_driver/naoqi_driver_node --qi-url=tcp://169.254.199.42:9559 --roscore_ip=127.0.0.1 --network_interface=eth0 __name:=naoqi_driver __log:=/home/map479/.ros/log/fdc53fce-65a8-11e7-8e3b-7071bc0c1eed/naoqi_driver-2.log].
log file: /home/map479/.ros/log/fdc53fce-65a8-11e7-8e3b-7071bc0c1eed/naoqi_driver-2*.log
Initiating shutdown!
================================================================================
[naoqi_driver-2] killing on exit
[rosout-1] killing on exit
[master] killing on exit
shutting down processing monitor...
... shutting down processing monitor complete
done
map479@map479-DQ57TM:~$

```

solution


Changing Network Interfaces name Ubuntu 16.04
https://askubuntu.com/questions/767786/changing-network-interfaces-name-ubuntu-16-04


Edit your /etc/default/grub changing the line from
```
GRUB_CMDLINE_LINUX=""
```
to
```
GRUB_CMDLINE_LINUX="net.ifnames=0 biosdevname=0"
```
and, finally run as root:
```
$ sudo update-grub
```
and reboot your system.
```
$ sudo reboot
```
