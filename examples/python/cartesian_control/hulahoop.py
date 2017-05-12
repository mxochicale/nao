#!/usr/bin/env python
#
# Reference:
# https://github.com/mikemcfarlane/Code_sprints/blob/master/Kivy/Introduction_to_Kivy.ipynb
#
#
# MACHINE: Ubuntu 16.04_x64 with Python 2.7.13
# MACHINE: Ubuntu 14.04_x64 with Python 2.7.6
# NAO VERSION: V4 T14
# NAOQI: naoqi 2.1.4.13 with python_naoqi-2.1.4.13-linux64
#


######
###### BECAREFUL WITH THIS ONE, THE MOVEMETNS ARE NOT SMOOTH AT ALL.
######


'''Motion: Hula Hoop ***'''

import argparse
import motion
import almath
from naoqi import ALProxy



def main(robotIP, PORT=9559):
    '''
        Example of a whole body multiple effectors control "LArm", "RArm" and "Torso"
        Warning: Needs a PoseInit before executing
                 Whole body balancer must be inactivated at the end of the script
    '''

    motionProxy  = ALProxy("ALMotion", robotIP, PORT)
    postureProxy = ALProxy("ALRobotPosture", robotIP, PORT)

    # end initialize proxy, begin go to Stand Init

    # Wake up robot
    motionProxy.wakeUp()


    # Send robot to Stand Init
    postureProxy.goToPosture("StandInit", 0.5)

    isAbsolute   = True
    useSensorValues = False

    # Arms motion
    effectorList = ["LArm", "RArm"]

    frame        = motion.FRAME_ROBOT

    # pathLArm
    pathLArm = []
    currentTf = motionProxy.getTransform("LArm", frame, useSensorValues)
    # 1
    target1Tf  = almath.Transform(currentTf)
    target1Tf.r1_c4 += 0.00 # x?
    target1Tf.r2_c4 += 0.00 # y
    target1Tf.r3_c4 += 0.00 # z

    # 2
    target2Tf  = almath.Transform(currentTf)
    target2Tf.r1_c4 += 0.20 # x?
    target2Tf.r2_c4 -= 0.00 # y
    target2Tf.r3_c4 += 0.20 # z

    pathLArm.append(list(target1Tf.toVector()))
    pathLArm.append(list(target2Tf.toVector()))
    pathLArm.append(list(target1Tf.toVector()))
    pathLArm.append(list(target2Tf.toVector()))
    pathLArm.append(list(target1Tf.toVector()))

    # pathRArm
    pathRArm = []
    currentTf = motionProxy.getTransform("RArm", frame, useSensorValues)
    # 1
    target1Tf  = almath.Transform(currentTf)
    target1Tf.r1_c4 += 0.00 # x?
    target1Tf.r2_c4 += 0.00 # y
    target1Tf.r3_c4 += 0.00 # z

    # 2
    target2Tf  = almath.Transform(currentTf)
    target2Tf.r1_c4 += 0.00 # x?
    target2Tf.r2_c4 -= 0.20 # y
    target2Tf.r3_c4 += 0.20 # z

    pathRArm.append(list(target1Tf.toVector()))
    pathRArm.append(list(target2Tf.toVector()))
    pathRArm.append(list(target1Tf.toVector()))
    pathRArm.append(list(target2Tf.toVector()))
    pathRArm.append(list(target1Tf.toVector()))
    pathRArm.append(list(target2Tf.toVector()))

    pathList = [pathLArm, pathRArm]

    axisMaskList = [almath.AXIS_MASK_VEL, # for "LArm"
                    almath.AXIS_MASK_VEL] # for "RArm"

    coef       = 1.6
    timesList  = [ [coef*(i+1) for i in range(5)],  # for "LArm" in seconds
                   [coef*(i+1) for i in range(6)] ] # for "RArm" in seconds

    # called cartesian interpolation
    motionProxy.transformInterpolations(effectorList, frame, pathList, axisMaskList, timesList)


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
