#!/usr/bin/python
#coding=utf-8

import math
import sys

def getDistance(point1X, point1Y, point2X, point2Y,):
    
    length = math.sqrt((point1X - point2X) * (point1X - point2X) + (point1Y - point2Y) * (point1Y- point2Y))
    return length

if sys.argv[1] == "-h":
    print "获取两点之间的距离"
    print "useage: ./calDistance.py p1x p1y p2x p2y"
    sys.exit(0)

ret = getDistance(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]))
print "distance: ",ret
