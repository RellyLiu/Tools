#!/usr/bin/python
#coding=utf-8

import numpy as np
import math
import sys

def matrixDot(matrix1, matrix2):
    ret = np.dot(matrix1, matrix2)
    return ret

if sys.argv[1] == "-h":
    print "获取两个点组成的向量在第一个点的方向上的分量"
    print "useage: ./getCoordCompent.py p1x p1y p1theta p2x p2y"
    sys.exit(0)

pointAx = float(sys.argv[1])
pointAy = float(sys.argv[2])
pointAtheta = float(sys.argv[3])

pointBx = float(sys.argv[4])
pointBy = float(sys.argv[5])


angle = pointAtheta / 180.0 * 3.14159
matrix1 = np.array([[math.cos(angle),math.sin(angle)],[-1 * math.sin(angle), math.cos(angle)]])
matrix2 = np.array([pointBx - pointAx, pointBy - pointAy])
ret = matrixDot(matrix1, matrix2)

print "result:", ret
