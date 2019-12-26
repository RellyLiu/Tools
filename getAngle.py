#!/usr/bin/python
#coding=utf-8

import math
import sys

def getAngle(point1X, point1Y, point2X, point2Y, point3X, point3Y):
    
    vector1X = point1X - point2X
    vector1Y = point1Y - point2Y

    vector2X = point3X - point2X
    vector2Y = point3Y - point2Y

    product = vector1X * vector2X + vector1Y * vector2Y
    vector1Lenght = math.sqrt(vector1X * vector1X + vector1Y * vector1Y)
    vector2Lenght = math.sqrt(vector2X * vector2X + vector2Y * vector2Y)

    rad = math.acos(product/(vector1Lenght * vector2Lenght))
    angle = rad / 3.1415926 * 180
    return angle

if sys.argv[1] == "-h":
    print "获取三个点组成向量的夹角，第二个点是顶点"
    print "useage: ./getAngle.py p1x p1y p2x p2y p3x p3y"
    sys.exit(0)

ret = getAngle(float(sys.argv[1]), float(sys.argv[2]), \
    float(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5]), float(sys.argv[6]))
print "angle: ",ret
