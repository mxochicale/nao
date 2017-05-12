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


    # Send robot to Stand Init
    postureProxy.goToPosture("StandInit", 0.5)



    coef       = 1.2                   # motion speed
    useSensorValues = False

    # Motion of Arms with block process
    frame     = motion.FRAME_TORSO
    axisMask  = almath.AXIS_MASK_VEL  # control just the position
    times     = [1.0*coef, 2.0*coef]  # seconds


    # Motion of Right Arm during the first half of the Torso motion
    effector  = "RArm"

    path = []
    currentTf = motionProxy.getTransform(effector, frame, useSensorValues)
    targetTf  = almath.Transform(currentTf)
    #targetTf.r2_c4 -= 0.14 # y
    ## targetTf.r3_c4 -= 0.08 # z

    targetTf.r1_c4 += 0.01 # x ?
    targetTf.r2_c4 -= 0.08 # y

    path.append(list(targetTf.toVector()))
    path.append(currentTf)

    motionProxy.transformInterpolations(effector, frame, path, axisMask, times)


    #
    # # Motion of Left Arm during the last half of the Torso motion
    # effector   = "LArm"
    #
    # path = []
    # currentTf = motionProxy.getTransform(effector, frame, useSensorValues)
    # targetTf  = almath.Transform(currentTf)
    # targetTf.r2_c4 += 0.14 # y
    # path.append(list(targetTf.toVector()))
    # path.append(currentTf)
    #
    # motionProxy.transformInterpolations(effector, frame, path, axisMask, times)
    #



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
