#!/usr/bin/env python
#
#
# MACHINE: Ubuntu 14.04_x64 with Python 2.7.6
# NAO VERSION: V4 T14
# NAOQI: naoqi 2.1.4.13 with python_naoqi-2.1.4.13-linux64
#
# Miguel P. Xochicale [http://mxochicale.github.io]
# Doctoral Researcher in Human-Robot Interaction
# University of Birmingham, U.K. (2014-2018)
#
# Reference:
# http://doc.aldebaran.com/2-1/naoqi/motion/tools-general-api.html#ALMotionProxy::getBodyNames__ssCR


import time
import almath
import argparse
from naoqi import ALProxy


def main(robotIP, PORT=9559):
    motionProxy = ALProxy("ALMotion", robotIP, PORT)

    motionProxy.setStiffnesses("Head", 1.0)

    # Two trajectories in one command. Each trajectory must have a
    # corresponding number of times
    names      = ["HeadYaw", "HeadPitch"]
    angleLists = [[1.0, -1.0], [-0.5]]
    times      = [[2.0,  4.0], [ 4.5]]
    isAbsolute = True
    motionProxy.angleInterpolation(names, angleLists, times, isAbsolute)

    time.sleep(1.0)
    motionProxy.setStiffnesses("Head", 0.0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="169.254.199.42",
                        help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559,
                        help="Robot port number")

    args = parser.parse_args()
    main(args.ip, args.port)
