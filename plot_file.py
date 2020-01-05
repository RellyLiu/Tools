#!/usr/bin/python
# coding=utf-8

import numpy as np
from matplotlib.pyplot import *
#from pylab import *

(x,y) = np.loadtxt('data.txt',dtype=float,skiprows=1,comments='#',delimiter=' ',usecols=(0,1),unpack=True)
plot(x,y,'y')
show()
