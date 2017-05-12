#! /usr/bin/env python
# -*- encoding: UTF-8 -*-
# http://doc.aldebaran.com/2-1/naoqi/audio/alanimatedspeech-api.html#ALAnimatedSpeechProxy::declareAnimationsPackage__ssCR

# MACHINE: Ubuntu 16.04x64 with python 2.7.13 
# NAO V4. Body Type: T14
# SOFTWARE: naoqi 2.1.4.13 with python_naoqi-2.1.4.13-linux64
#
# Miguel P. Xochicale [http://mxochicale.github.io]
# Doctoral Researcher in Human-Robot Interaction
# University of Birmingham, U.K. (2014-2018)
#
#

'''Say a text with a local configuration'''

import argparse
from naoqi import ALProxy

def main(robotIP, PORT=9559):

    animatedSpeechProxy = ALProxy("ALAnimatedSpeech", robotIP, PORT)

    # set the local configuration
    configuration = {"bodyLanguageMode":"contextual"}
    animatedSpeechProxy.say("Hello, I am Nao", configuration)




if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="169.254.199.42",
                        help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559,
                        help="Robot port number")

    args = parser.parse_args()
    main(args.ip, args.port)
