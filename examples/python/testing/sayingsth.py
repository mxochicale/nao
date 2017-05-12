#!/usr/bin/env python
#
#
#
# This program use ALTextToSpeech proxy defined as tts in order to say
# whatever is in between the quotes tts.say("?????????")
#
# MACHINE: Ubuntu 16.04x64 with python 2.7.13 
# NAO V4. Body Type: T14
# SOFTWARE: naoqi 2.1.4.13 with python_naoqi-2.1.4.13-linux64
#
# Miguel P. Xochicale [http://mxochicale.github.io]
# Doctoral Researcher in Human-Robot Interaction
# University of Birmingham, U.K. (2014-2018)
#
#

import sys
from naoqi import ALProxy

IP = "169.254.199.42"
PORT = 9559

try:
    tts = ALProxy("ALTextToSpeech", IP, PORT)
except Exception,e:
    print "Could not create proxy to ALTextToSpeech"
    print "Error was: ",e
    sys.exit(1)


print sys.version_info


tts.setVolume(0.9)  ##Volume set to 90%
tts.setParameter("pitchShift", 1.2) #Applies a pitch shifting to the voice
tts.setParameter("doubleVoice", 0.0) #Deactivates double voice

tts.say("Hiya. My name is NAO")
tts.say("Bye-bye")
