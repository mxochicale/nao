#!/usr/bin/env python
#
# Reference:
# http://doc.aldebaran.com/2-1/naoqi/motion/control-cartesian.html#control-cartesian
#
# MACHINE: Ubuntu 16.04_x64 with Python 2.7.13
# MACHINE: Ubuntu 14.04_x64 with Python 2.7.6
# NAO VERSION: V4 T14
# NAOQI: naoqi 2.1.4.13 with python_naoqi-2.1.4.13-linux64


'''Cartesian control: Multiple Effector Trajectories'''
''' This example is only compatible with NAO '''

import argparse
import motion
import almath
from naoqi import ALProxy



def main(robotIP, PORT=9559):
    ''' Simultaneously control three effectors:
    the Torso, the Left Arm and the Right Arm
    Warning: Needs a PoseInit before executing
    '''

    motionProxy  = ALProxy("ALMotion", robotIP, PORT)
    postureProxy = ALProxy("ALRobotPosture", robotIP, PORT)


    # ttsProxy = ALProxy("ALTextToSpeech", robotIP, PORT)
    # ttsProxy.say("Hiya, I am ROCY")
    # ttsProxy.say("     ")
    # ttsProxy.say("You are going to imitate my arm movements")
    # ttsProxy.say("     ")
    # ttsProxy.say("Let's start")




    # Wake up robot
    motionProxy.wakeUp()

    # Send robot to Pose Init
    postureProxy.goToPosture("StandInit", 0.5)




    # Example showing how to use transformInterpolations
    frame        = motion.FRAME_ROBOT
    isAbsolute   = False
    useSensorValues = False

    coef       = 0.9                  # motion speed
    # Motion of Arms with block process
    effectorList = ["LArm", "RArm"]
    axisMaskList = [motion.AXIS_MASK_VEL, motion.AXIS_MASK_VEL]
    timeList     = [[1.0*coef], [1.0*coef]]         # seconds
    dy = -0.14

    pathList = []
    targetLArmTf = almath.Transform(motionProxy.getTransform("LArm", frame, useSensorValues))
    targetLArmTf.r2_c4 -= dy
    pathList.append(list(targetLArmTf.toVector()))

    targetRArmTf = almath.Transform(motionProxy.getTransform("RArm", frame, useSensorValues))
    targetRArmTf.r2_c4 += dy
    pathList.append(list(targetRArmTf.toVector()))

    motionProxy.transformInterpolations(effectorList, frame, pathList,axisMaskList, timeList)






    # Go to rest position
    motionProxy.rest()



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="169.254.199.42",
                        help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559,
                        help="Robot port number")

    args = parser.parse_args()
    main(args.ip, args.port)
