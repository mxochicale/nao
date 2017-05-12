#!/usr/bin/env python
#
#
# MACHINE: Ubuntu 16.04_x64 with Python 2.7.13
# MACHINE: Ubuntu 14.04_x64 with Python 2.7.6
# NAO VERSION: V4 T14
# NAOQI: naoqi 2.1.4.13 with python_naoqi-2.1.4.13-linux64
#
# Miguel P. Xochicale [http://mxochicale.github.io]
# Doctoral Researcher in Human-Robot Interaction
# University of Birmingham, U.K. (2014-2018)

# Call library
import argparse
import sys
import math
import almath
import time
import naoqi
from naoqi import ALProxy


def main(robotIP, PORT=9559):
    ''' Create N repetitions of horizontal arm movements
    controlling LShoulderPitch
    '''
    # the following varialbles should be global
    # in order to be recognised by the defined functions
    global motionProxy
    global aupProxy

    motionProxy  = ALProxy("ALMotion", robotIP, PORT)
    postureProxy = ALProxy("ALRobotPosture", robotIP, PORT)
    ttsProxy = ALProxy("ALTextToSpeech", robotIP, PORT)
    aupProxy = ALProxy("ALAudioPlayer", robotIP, PORT)



    # Wake up robot
    motionProxy.wakeUp()

    ##### Send robot to:
    postureProxy.goToPosture("StandZero", 0.5)

    # postureProxy.goToPosture("StandInit", 0.5)

    # postureProxy.goToPosture("Crouch", 0.5)

    # postureProxy.goToPosture("Stand", 0.5)
    # postureProxy.goToPosture("Sit", 0.5)
    # postureProxy.goToPosture("SitRelax", 0.5)
    # postureProxy.goToPosture("LyingBack", 0.5)
    # postureProxy.goToPosture("LyingBelly", 0.5)


    maxSpeedFraction = 0.05 # Using 5% of maximum joint speed
    names = "LShoulderPitch"
    targetAngles = [0.0*almath.TO_RAD]
    motionProxy.angleInterpolationWithSpeed(names, targetAngles, maxSpeedFraction)

    time.sleep(1)
    aupProxy.playSine(1000,20,0,0.2)


    ttsProxy.setVolume(0.2)  ##Volume set to 0.6 = 60%


    for i in range(11):
        if i == 0:
            ttsProxy.say("Zero")
            print 'Repetition:', i
            HorizontalMovement()
        elif i == 1:
            ttsProxy.say("One")
            print 'Repetition:', i
            HorizontalMovement()
        elif i == 2:
            ttsProxy.say("Two")
            print 'Repetition:', i
            HorizontalMovement()
        elif i == 3:
            ttsProxy.say("Three")
            print 'Repetition:', i
            HorizontalMovement()
        elif i == 4:
            ttsProxy.say("Four")
            print 'Repetition:', i
            HorizontalMovement()
        elif i == 5:
            ttsProxy.say("Five")
            print 'Repetition:', i
            HorizontalMovement()
        elif i == 6:
            ttsProxy.say("Six")
            print 'Repetition:', i
            HorizontalMovement()
        elif i == 7:
            ttsProxy.say("Seven")
            print 'Repetition:', i
            HorizontalMovement()
        elif i == 8:
            ttsProxy.say("Eight")
            print 'Repetition:', i
            HorizontalMovement()
        elif i == 9:
            ttsProxy.say("Nine")
            print 'Repetition:', i
            HorizontalMovement()
        elif i == 10:
            ttsProxy.say("Ten")
            print 'Repetition:', i
            HorizontalMovement()
        else:
            ttsProxy.say("Stop")

    ttsProxy.say("Stop")

    # Go to rest position
    motionProxy.rest()



def HorizontalMovement():
    maxSpeedFraction = 0.2 # Using 25% of maximum joint speed
    names = "LShoulderRoll"
    targetAngles = [60.0*almath.TO_RAD]
    motionProxy.angleInterpolationWithSpeed(names, targetAngles, maxSpeedFraction)
    aupProxy.playSine(1000,20,0,0.05)

    names = "LShoulderRoll"
    targetAngles = [0.0*almath.TO_RAD]
    motionProxy.angleInterpolationWithSpeed(names, targetAngles, maxSpeedFraction)
    aupProxy.playSine(1000,20,0,0.05)



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="169.254.199.42",
                        help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559,
                        help="Robot port number")

    args = parser.parse_args()
    main(args.ip, args.port)
