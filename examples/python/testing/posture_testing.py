#!/usr/bin/env python2.7
#
#
#
# Tested with python 2.7.13 on ubuntu 16.04 on  Wed 10 May 23:52:06 BST 2017 @bhamuk
#
#
# This program test the following predefined postures:
# Crouch, SitRelax, Stand, StandInit, StandZero.
# A posture for NAO is a unique configuration for its joints [1]
# [1] http://doc.aldebaran.com/2-1/naoqi/motion/alrobotposture.html
#
#
# HARDWARE: NAO V4 T14
# SOFTWARE: naoqi 2.1.4.13 with python_naoqi-2.1.4.13-linux64
#
# Miguel P. Xochicale [http://mxochicale.github.io]
# Doctoral Researcher in Human-Robot Interaction
# University of Birmingham, U.K. (2014-2018)

import sys
from naoqi import ALProxy

IP = "169.254.199.42"
PORT = 9559


try:
    postureProxy = ALProxy("ALRobotPosture", IP, PORT)
except Exception,e:
    print "Could not create proxy to ALRobotPosture"
    print "Error was: ",e
    sys.exit(1)


try:
    proxy = ALProxy("ALMotion",IP,PORT)
except Exception,e:
    print "Could not create proxy to ALTextToSpeech"
    print "Error was: ",e
    sys.exit(1)


def StiffnessOff(proxy):
  pNames = 'Body'
  pStiffnessLists = 0.0
  pTimeLists = 1.0
  proxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)





postureProxy.goToPosture("StandInit", 1.0)
postureProxy.goToPosture("SitRelax", 1.0)
postureProxy.goToPosture("StandZero", 1.0)
postureProxy.goToPosture("Stand", 1.0)
postureProxy.goToPosture("Crouch", 1.0)
print postureProxy.getPostureFamily()


# postureProxy.goToPosture("Sit", 1.0)
# postureProxy.goToPosture("LyingBelly", 1.0)
# postureProxy.goToPosture("LyingBack", 1.0)


StiffnessOff(proxy)
