#!/usr/bin/env python
#
#
#
#
# This program move the Left Arm of Nao in Horizontal Movement "LShoulderRoll"
# from =90 to 0 degrees. It also plays a sound in each of the repetitions
# to let the person know about the #REPETITIONS = 1
#
#
# [1] http://doc.aldebaran.com/1-14/naoqi/motion/control-joint-api.html?highlight=angleinterpolation#ALMotionProxy::angleInterpolation
#
# MACHINE: Ubuntu 14.04_x64 with Python 2.7.6
# NAO VERSION: V4 T14
# NAOQI: naoqi 2.1.4.13 with python_naoqi-2.1.4.13-linux64
#
# Miguel P. Xochicale [http://mxochicale.github.io]
# Doctoral Researcher in Human-Robot Interaction
# University of Birmingham, U.K. (2014-2018)


# Call library
import sys
import math
import almath
import time
import naoqi
from naoqi import ALProxy


IP = "169.254.199.42"
PORT = 9559


try:
    proxy = ALProxy("ALMotion",IP,PORT)
except Exception,e:
    print "Could not create proxy to ALTextToSpeech"
    print "Error was: ",e
    sys.exit(1)


try:
    postureProxy = ALProxy("ALRobotPosture", IP, PORT)
except Exception, e:
    print "Could not create proxy to ALRobotPosture"
    print "Error was: ", e
    sys.exit(1)

try:
    aup = ALProxy("ALAudioPlayer", IP, PORT)
except Exception,e:
    print "Could not create proxy to ALTextToSpeech"
    print "Error was: ",e
    sys.exit(1)


try:
    tts = ALProxy("ALTextToSpeech", IP, PORT)
except Exception,e:
    print "Could not create proxy to ALTextToSpeech"
    print "Error was: ",e
    sys.exit(1)


#We use the "Body" name to signify the collection of all joints
def StiffnessOn(proxy):
  pNames = 'Body'
  pStiffnessLists = 1.0
  pTimeLists = 1.0
  proxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)


def StiffnessOff(proxy):
  pNames = 'Body'
  pStiffnessLists = 0.0
  pTimeLists = 1.0
  proxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)


###### Voice Parameters
tts.setVolume(1.0) #Changes the volume



###### Voice Parameters
tts.setVolume(1.0) #Changes the volume


StiffnessOn(proxy)
print proxy.getSummary() # print motion state


postureProxy.goToPosture("Crouch", 1.0)
postureProxy.goToPosture("StandZero", 0.5)



maxSpeedFraction = 0.05 # Using 5% of maximum joint speed
names = "LShoulderPitch"
targetAngles = [25.0*almath.TO_RAD]
proxy.angleInterpolationWithSpeed(names, targetAngles, maxSpeedFraction)


time.sleep(3)
aup.playSine(1000,20,0,0.2)
time.sleep(0.3)
aup.playSine(1000,20,0,0.2)
time.sleep(0.3)
aup.playSine(1000,20,0,0.2)
time.sleep(0.3)
tts.say("Start")




REPETITIONS = 2

maxSpeedFraction = 0.1 # Using 25% of maximum joint speed
count = 0
while (count < REPETITIONS):
    count = count + 1
    print 'Repetition:', count

    names = "LShoulderRoll"
    targetAngles = [60.0*almath.TO_RAD]
    proxy.angleInterpolationWithSpeed(names, targetAngles, maxSpeedFraction)
    aup.playSine(1000,20,0,0.1)
    names = "LShoulderRoll"
    targetAngles = [0.0*almath.TO_RAD]
    proxy.angleInterpolationWithSpeed(names, targetAngles, maxSpeedFraction)
    aup.playSine(1000,20,0,0.2)




time.sleep(0.3)
aup.playSine(1000,20,0,0.2)
time.sleep(0.3)
aup.playSine(1000,20,0,0.2)
time.sleep(0.3)
tts.say("Stop")



postureProxy.goToPosture("Crouch", 0.5)
StiffnessOff(proxy)
