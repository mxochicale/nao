[NAO Examples](https://github.com/FelipMarti/nao_examples) in ROS by FelipMarti
---


```
cd ~/catkin_ws/src/ && git clone https://github.com/FelipMarti/nao_examples
cd ~/catkin_ws/ && catkin_make
source ~/.bashrc
```




## ISSUES

in ~/catkin_ws/src
 rm -rf nao_leds_effects/ nao_tactile_detection nao_tactile_detection_class/ nao_tactile_interface/

in  ~/catkin_ws/devel/share
rm -rf nao_leds_effects/ nao_tactile_detection nao_tactile_detection_class/ nao_tactile_interface/

```
/home/map479/catkin_ws/src/nao_examples/nao_leds_effects/include/nao_leds_effects_node.h:16:40: fatal error: nao_leds_effects/LedEffect.h: No such file or directory

/home/map479/catkin_ws/src/nao_examples/nao_tactile_interface/include/nao_tactile_interface_node.h:22:44: fatal error: naoqi_bridge_msgs/TactileTouch.h: No such file or directory
```

## [nao_leds_effects/LedEffect.h: and naoqi_bridge_msgs/TactileTouch.h: No such file or directory](https://github.com/FelipMarti/nao_examples/issues/1)


I have tried to build the nao_examples package on a machine with Ubuntu 16.05 with ROS kinetic and NAOqi 2.14.13.
However, I am not entirely sure how to solve this issue with the following header dependencies.
```
~/catkin_ws/src/nao_examples/nao_leds_effects/include/nao_leds_effects_node.h:16:40: fatal error: nao_leds_effects/LedEffect.h: No such file or directory
~/catkin_ws/src/nao_examples/nao_tactile_interface/include/nao_tactile_interface_node.h:22:44: fatal error: naoqi_bridge_msgs/TactileTouch.h: No such file or directory
```
Any suggestion?
