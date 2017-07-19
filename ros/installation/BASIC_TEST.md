Basic Testing
---


update the sources
```
source ~/.bashrc
```

if you have Nao, check Naoqi Driver providing the robot's IP
```
roslaunch naoqi_driver naoqi_driver.launch nao_ip:=169.254.199.42
```


output

```
$ roslaunch naoqi_driver naoqi_driver.launch nao_ip:=169.254.199.42
... logging to /home/map479/.ros/log/dafbd748-6619-11e7-b026-7071bc0c1eed/roslaunch-map479-DQ57TM-8780.log
Checking log directory for disk usage. This may take awhile.
Press Ctrl-C to interrupt
Done checking log file disk usage. Usage is <1GB.

started roslaunch server http://map479-DQ57TM:46026/

SUMMARY
========

PARAMETERS
 * /rosdistro: kinetic
 * /rosversion: 1.12.7

NODES
  /
    naoqi_driver (naoqi_driver/naoqi_driver_node)

auto-starting new master
process[master]: started with pid [8791]
ROS_MASTER_URI=http://localhost:11311

setting /run_id to dafbd748-6619-11e7-b026-7071bc0c1eed
process[rosout-1]: started with pid [8804]
started core service [/rosout]
process[naoqi_driver-2]: started with pid [8810]
Receiving information about robot model
set prefix successfully to
[I] 1499764690.011975 8810 qimessaging.session: Session listener created on tcp://0.0.0.0:0
[I] 1499764690.012262 8810 qimessaging.transportserver: TransportServer will listen on: tcp://169.254.164.69:36577
[I] 1499764690.012278 8810 qimessaging.transportserver: TransportServer will listen on: tcp://127.0.0.1:36577
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
using master ip: http://127.0.0.1:11311
NOT going to re-register the converters
camera/bottom/image_raw is resetting
camera/bottom/image_raw reset
/diagnostics is resetting
/diagnostics reset
camera/front/image_raw is resetting
camera/front/image_raw reset
imu/torso is resetting
imu/torso reset
info is resetting
load robot description from file
info reset
/joint_states is resetting
/joint_states reset
/rosout is resetting
/rosout reset
odom is resetting
odom reset
sonar is resetting
sonar reset
resetting subscriber teleop
teleop is resetting
teleop reset
resetting subscriber moveto
moveto is resetting
moveto reset
resetting subscriber speech
speech is resetting
speech reset
resetting service robot config service
robot config service is resetting
[ERROR] [1499764693.731811976]: Do not calculate NAO Footprint, no transform possible 1499764693.530578418
[ERROR] [1499764693.836380864]: Do not calculate NAO Footprint, no transform possible 1499764693.634981702
[ERROR] [1499764693.940377289]: Do not calculate NAO Footprint, no transform possible 1499764693.739158474
[ERROR] [1499764694.044089634]: Do not calculate NAO Footprint, no transform possible 1499764693.842849935

```

















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
