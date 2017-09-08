CHECKLIST FOR THE OPENDAY DEMO AT UNIVERSITY OF BIRMINGHAM
---


# Setting Up


1. Create path to save data

```
mkdir -p ~/tmp/openday_v##
```
where "v##" is the number of open day. For this case the tag, it is used
v02 since it is the second time that the data is collected from the openday
visitors. NB. Data will be deleted or anonimalised by blurring faces in
the videos.

2. tune the following parameters for the ~/catkin_ws/razor_imu_9dof/config/razor*.yaml [2]
```
number_of_samples: 2000
main_data_stream_path: /home/map479/tmp/openday_v02
```
1000 samples ~ 20 seconds;   
2000 samples ~ 40 seconds;   
3000 samples ~ 60 seconds  


# NAO

The boot process is completed when NAO says “OGNAK GNOUK” and it takes around
2minutes 13 seconds, then you can establish the network connection with NAO
and open a terminal to execute nao's movements with the python script.

T1
```
cd ~/mxochicale/github/nao/examples/exporting_animations_to_python/python_scripts
 ./TenUpperArmMovements_FRAME_SEP_30.py
```
The execution time for "./TenUpperArmMovements_FRAME_SEP_30.py" is 34 seconds.


# IMUS and ROS
1. Turn on Razor sensors
2. bind bluetooth modules to rfcomm* ports [1]
T2
```
cd ~/mxochicale/github/ros/bluetooth_dev_conf/automatic_connection && ./bind_four_automatic_connection_ubuntu1604.sh && sleep 15
```
and wait around 15 seconds


Once the bluetooth modules have been binded, you can launch the app

```
roslaunch razor_imu_9dof razor-pub-four-imus.launch
```
booting sensors takes around 15 to 20 seconds


Then press 'crtl-c' in the terminal


3. release bluetooth modules from  the rfcomm* ports
```
cd ~/mxochicale/github/ros/bluetooth_dev_conf/automatic_connection && ./release_four_automatic_connection_ubuntu1604.sh
```

4. Turn off sensors

# OPENFACE

[3]

T4

```
cd ~/mxochicale/github/nao/openday-uob
sleep 10 && ./openface_pNN.sh pNNgXXaNN
```
sleep 10 seconds to wait for the 15 seconds for the imus to boot

ctr-q to exit


#  REFERENCES

[1] [automatic_connection](https://github.com/mxochicale/ros/tree/master/bluetooth_dev_conf/automatic_connection)  
[2] Further information about package configuration [mx_razor_imu_9dof/catkin_ws](https://github.com/mxochicale/ros/tree/master/mx_razor_imu_9dof/catkin_ws)  
[3] https://github.com/mxochicale/openface  



## TODO
- [ ] create general checklist 
- [ ] change the variable /home/map479/tmp/openday_v02 for another version of the openday
- [x] ~~create an path that collect all the data from one participant~~
- [x] ~~define the times for the data collection, specifically for number_of_samples at razor*.yaml~~
- [x] ~~underline todo list~~


## OBSERVATIONS for /openday_v02


*
