#! /usr/bin/env python
#-*- coding: utf-8 -*-
#https://github.com/SeanXP/Nao-Robot/blob/master/python/motion/joint/Arm/set_Arm.py
#################################################################
#   Copyright (C) 2015 Sean Guo. All rights reserved.
#
#	> File Name:        < set_Arm.py >
#	> Author:           < Sean Guo >
#	> Mail:             < iseanxp+code@gmail.com >
#	> Created Time:     < 2015/03/27 >
#	> Last Changed:
#	> Description:		Joint Control Robot Arm
#################################################################
#
# MACHINE: Ubuntu 16.04_x64 with Python 2.7.13
# MACHINE: Ubuntu 14.04_x64 with Python 2.7.6
# NAO VERSION: V4 T14
# NAOQI: naoqi 2.1.4.13 with python_naoqi-2.1.4.13-linux64

import argparse
from naoqi import ALProxy
import time

motion = None


def main(robot_IP, robot_PORT=9559):
    global motion
    # ----------> Connect to robot <----------
    tts = ALProxy("ALTextToSpeech", robot_IP, robot_PORT)
    motion = ALProxy("ALMotion", robot_IP, robot_PORT)



    motion.rest()



    # Wake up robot
    motion.wakeUp()


    time.sleep(1)

    #Testing Arm Movements definitions
    LArmInit()
    RArmInit()

    LArmUp()
    RArmUp()

    ArmUp2()
    LArmMoveInit()
    RArmMoveInit()



	
    # # Go to rest position
    motion.rest()


def LArmInit():
	motion.setAngles('LShoulderPitch', 0, 0.2)
	motion.setAngles('LShoulderRoll', 0, 0.2)
	motion.setAngles('LElbowYaw', 0, 0.2)
	motion.setAngles('LElbowRoll', 0, 0.2)
	motion.setAngles('LWristYaw', 0, 0.2)
	motion.setAngles('LHand', 0, 0.2)
def RArmInit():
 	motion.setAngles('RShoulderPitch', 0, 0.2)
 	motion.setAngles('RShoulderRoll', 0, 0.2)
 	motion.setAngles('RElbowYaw', 0, 0.2)
 	motion.setAngles('RElbowRoll', 0, 0.2)
 	motion.setAngles('RWristYaw', 0, 0.2)
 	motion.setAngles('RHand', 0, 0.2)
def LArmUp():
	motion.setAngles('LShoulderPitch', 0.7, 0.2)
	motion.setAngles('LShoulderRoll', 0.3, 0.2)
	motion.setAngles('LElbowYaw', -1.5, 0.2)
	motion.setAngles('LElbowRoll', -0.5, 0.2)
	motion.setAngles('LWristYaw', -1.7, 0.2)
	motion.setAngles('LHand', 0, 0.2)
def RArmUp():
	motion.setAngles('RShoulderPitch', 0.7, 0.2)
	motion.setAngles('RShoulderRoll', -0.3, 0.2)
	motion.setAngles('RElbowYaw', 1.5, 0.2)
	motion.setAngles('RElbowRoll', 0.5, 0.2)
	motion.setAngles('RWristYaw', 1.7, 0.2)
	motion.setAngles('RHand', 0, 0.2)
def ArmUp2():
	motion.rest()
	motion.wakeUp()
	motion.setAngles('RShoulderPitch', 0.7, 0.2)
	motion.setAngles('RWristYaw', 1.5, 0.2)
	motion.setAngles('LShoulderPitch', 0.7, 0.2)
	motion.setAngles('LWristYaw', -1.5, 0.2)

def LArmMoveInit():
    motion.setAngles('LShoulderPitch', 1, 0.2)
    motion.setAngles('LShoulderRoll', 0.3, 0.2)
    motion.setAngles('LElbowYaw', -1.3, 0.2)
    motion.setAngles('LElbowRoll', -0.5, 0.2)
    motion.setAngles('LWristYaw', 0, 0.2)
    motion.setAngles('LHand', 0, 0.2)
def RArmMoveInit():
 	motion.setAngles('RShoulderPitch', 1, 0.2)
 	motion.setAngles('RShoulderRoll', -0.3, 0.2)
 	motion.setAngles('RElbowYaw', 1.3, 0.2)
 	motion.setAngles('RElbowRoll', 0.5, 0.2)
 	motion.setAngles('RWristYaw', 0, 0.2)
	motion.setAngles('RHand', 0, 0.2)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="169.254.199.42", help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559, help="Robot port number")
    args = parser.parse_args()
    main(args.ip, args.port)
