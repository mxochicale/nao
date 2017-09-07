CHECKLIST FOR OPENDAY DEMO AT UNIVERSITY OF BIRMINGHAM
---

#TODO
* create an path that collect all the data from one participant
* define the times for the data collection, specifically for number_of_samples
at razor*.yaml

# NAO

turn on nao and wait till says unagmu
```
cd ~/mxochicale/github/nao/examples/exporting_animations_to_python/python_scripts
 ./TenUpperArmMovements_FRAME_SEP_30.py
```


# IMUS

1. Turn on sensors

2. bind bluetooth modules to rfcomm* ports [1]

```
cd ~/mxochicale/github/ros/bluetooth_dev_conf/automatic_connection && ./bind_four_automatic_connection_ubuntu1604.sh
```


# ROS

tune the following parameters for the ~/catkin_ws/razor_imu_9dof/config/razor*.yaml [2]
```
number_of_samples: 1000
main_data_stream_path: /home/map479/tmp/razor
```

```
cd && mkdir -p ~tmp/razor && cd ~/tmp/razor
```

Once the bluetooth modules have been binded, you can launch the app

```
roslaunch razor_imu_9dof razor-pub-four-imus.launch
```

Then press 'crtl-c' in the terminal


3. release bluetooth modules from  the rfcomm* ports
```
cd ~/mxochicale/github/ros/bluetooth_dev_conf/automatic_connection && ./release_four_automatic_connection_ubuntu1604.sh
```

4. Turn off sensors


# OPENFACE

[3]

```
cd ~/OpenFace/build/bin
```

```
cd ~/OpenFace/build/bin
mkdir openday && cd openday
.././Record   #[Q to exit]
.././FaceLandmarkVid -f ../openday/out.avi -ov "flvid.avi"
.././FeatureExtraction -rigid -verbose -f ../openday/out.avi -of "default.txt" -simalign ../openday/aligned
```

Play the FaceLandmarkVideo
```
cvlc --loop --fullscreen flvid.avi
```



#  REFERENCES


[1] [automatic_connection](https://github.com/mxochicale/ros/tree/master/bluetooth_dev_conf/automatic_connection)
[2] Further information about package configuration [mx_razor_imu_9dof/catkin_ws](https://github.com/mxochicale/ros/tree/master/mx_razor_imu_9dof/catkin_ws)
[3] https://github.com/mxochicale/openface
