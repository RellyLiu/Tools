#!/usr/bin/python
#coding=utf-8

import math
import sys

def getDistance(pointX, pointY, line1X, line1Y, line2X, line2Y):
    
    vector1X = pointX - line1X
    vector1Y = pointY - line1Y

    vector2X = line2X - line1X
    vector2Y = line2Y - line1Y

    area = math.fabs(vector1X * vector2Y - vector1Y * vector2X)
    length = math.sqrt(vector2X * vector2X + vector2Y * vector2Y)
    dis = area / length
    return dis

if sys.argv[1] == "-h":
    print "获取点到直线的距离，后面的两个点为直线"
    print "useage: ./getDistance.py p1x p1y p2x p2y p3x p3y"
    sys.exit(0)

ret = getDistance(float(sys.argv[1]), float(sys.argv[2]), \
    float(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5]), float(sys.argv[6]))
print "distance: ",ret
