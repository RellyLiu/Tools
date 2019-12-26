#!/usr/bin/python
#coding=utf-8

import pylab as pl
import numpy as np

data = np.loadtxt('/home/dahua/log/odom_data', unpack=False);

x = data[:, 0]
y = data[:, 1]

print x
print y

pl.xlabel(u"x轴")
pl.ylabel(u"y轴")
pl.xlim(-10,10)
pl.ylim(-10,10)
pl.title(u"测试")

pl.plot(x, y, 'ob-', label=u"路径")
pl.legend()
pl.show()
