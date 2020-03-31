#!/usr/bin/python
#coding=utf-8

import math
import sys

def getY(p1X, p1Y, p2X, p2Y, x):
    
	if p1X == p2X:
		return -9999
	
	p = (p1Y - p2Y) / (p1X - p2X)
	return p * (x - p2X) + p2Y

if sys.argv[1] == "-h":
    print "已知直线上的两个点p1 p2 和x，求y值，使其在线上"
    print "useage: ./getY.py p1x p1y p2x p2y x"
    sys.exit(0)

ret = getY(float(sys.argv[1]), float(sys.argv[2]), \
    float(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5]))
print "value: ",ret
