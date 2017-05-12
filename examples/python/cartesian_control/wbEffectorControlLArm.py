#!/usr/bin/env python
# http://doc.aldebaran.com/2-1/dev/python/examples/motion/whole_body.html#arms
#
# MACHINE: Ubuntu 16.04_x64 with Python 2.7.13
# MACHINE: Ubuntu 14.04_x64 with Python 2.7.6
# NAO VERSION: V4 T14
# NAOQI: naoqi 2.1.4.13 with python_naoqi-2.1.4.13-linux64


# -*- encoding: UTF-8 -*-


### VERY SLOW MOTION
''' Whole Body Motion: Left or Right Arm position control '''
''' This example is only compatible with NAO '''

import argparse
import motion
import time
from naoqi import ALProxy

def main(robotIP, PORT, chainName):
    ''' Example of a whole body Left or Right Arm position control
        Warning: Needs a PoseInit before executing
                 Whole body balancer must be inactivated at the end of the script
    '''

    motionProxy  = ALProxy("ALMotion", robotIP, PORT)
    postureProxy = ALProxy("ALRobotPosture", robotIP, PORT)

    # Wake up robot
    motionProxy.wakeUp()

    # Send robot to Stand Init
    #postureProxy.goToPosture("StandInit", 0.5)

    frame     = motion.FRAME_ROBOT
    useSensor = False

    effectorInit = motionProxy.getPosition(chainName, frame, useSensor)

    # Active LArm tracking
    isEnabled = True
    motionProxy.wbEnableEffectorControl(chainName, isEnabled)

    # Example showing how to set position target for LArm
    # The 3 coordinates are absolute LArm position in FRAME_ROBOT
    # Position in meter in x, y and z axis.

    # X Axis LArm Position feasible movement = [ +0.00, +0.12] meter
    # Y Axis LArm Position feasible movement = [ -0.05, +0.10] meter
    # Y Axis RArm Position feasible movement = [ -0.10, +0.05] meter
    # Z Axis LArm Position feasible movement = [ -0.10, +0.10] meter




    coef = 1.0
    if chainName == "LArm":
        coef = +1.0
    elif chainName == "RArm":
        coef = -1.0

    targetCoordinateList = [
    [ +0.12, +0.00*coef, +0.00], # target 0
    [ +0.12, +0.00*coef, -0.10], # target 1
    [ +0.12, +0.05*coef, -0.10], # target 1
    [ +0.12, +0.05*coef, +0.10], # target 2
    [ +0.12, -0.10*coef, +0.10], # target 3
    [ +0.12, -0.10*coef, -0.10], # target 4
    [ +0.12, +0.00*coef, -0.10], # target 5
    [ +0.12, +0.00*coef, +0.00], # target 6
    [ +0.00, +0.00*coef, +0.00], # target 7
    ]


    # wbSetEffectorControl is a non blocking function
    # time.sleep allow head go to his target
    # The recommended minimum period between two successives set commands is
    # 0.2 s.
    for targetCoordinate in targetCoordinateList:
        targetCoordinate = [targetCoordinate[i] + effectorInit[i] for i in range(3)]
        motionProxy.wbSetEffectorControl(chainName, targetCoordinate)
        time.sleep(4.0)

    # Deactivate Head tracking
    isEnabled    = False
    motionProxy.wbEnableEffectorControl(chainName, isEnabled)

    # Go to rest position
    motionProxy.rest()



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="169.254.199.42",
                        help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559,
                        help="Robot port number")
    parser.add_argument("--chain", type=str, default="LArm",
                        choices=["LArm", "RArm"], help="Chain name")

    args = parser.parse_args()
    main(args.ip, args.port, args.chain)
