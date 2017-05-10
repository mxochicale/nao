#!/usr/bin/env python2.7
#
#
# Tested with python 2.7.13 on ubuntu 16.04 on  Wed 10 May 23:52:06 BST 2017 @bhamuk
#
# This program reproduce audio files using loadFile
#
#
# HARDWARE: NAO V4 T14
# SOFTWARE: naoqi 2.1.4.13 with python_naoqi-2.1.4.13-linux64
#
# Miguel P. Xochicale [http://mxochicale.github.io]
# Doctoral Researcher in Human-Robot Interaction
# University of Birmingham, U.K. (2014-2018)

import sys
import time
from naoqi import ALProxy


IP = "169.254.199.42"
# IP = "169.254.225.141"
PORT = 9559


try:
    aup = ALProxy("ALAudioPlayer", IP, PORT)
except Exception,e:
    print "Could not create proxy to ALTextToSpeech"
    print "Error was: ",e
    sys.exit(1)

#
## fileId = aup.post.playFile("/usr/share/naoqi/wav/*.wav")
#
fileId = aup.loadFile("/usr/share/naoqi/wav/0.wav")
time.sleep(0.5)
aup.play(fileId)

fileId = aup.loadFile("/usr/share/naoqi/wav/body_not_found.wav")
time.sleep(0.5)
aup.play(fileId)

fileId = aup.loadFile("/usr/share/naoqi/wav/random.wav")
time.sleep(0.5)
aup.play(fileId)

fileId = aup.loadFile("/usr/share/naoqi/wav/outch.wav")
time.sleep(0.5)
aup.play(fileId)


#
# #Loads a file and launchs the playing 1 seconds later

time.sleep(1)
aup.playSine(1000,20,0,0.5)
time.sleep(1)
aup.playSine(500,20,0,0.5)
# time.sleep(.1)
# aup.playSine(500,20,0,1.0)
