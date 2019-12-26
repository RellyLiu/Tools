#!/usr/bin/python
#coding=utf-8

import numpy as np
import math

def multiply(matrix1, matrix2):
    ret = np.dot(matrix1, matrix2)
    return ret

angle = -45 / 180.0 * 3.14159
matrix1 = np.array([[math.cos(angle),math.sin(angle)],[-1 * math.sin(angle), math.cos(angle)]])
matrix2 = np.array([1, 1])
ret = multiply(matrix1, matrix2)
print "ret: %s", ret
