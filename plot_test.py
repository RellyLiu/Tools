#!/usr/bin/python
#coding=utf-8

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-1 * np.pi, np.pi, 0.01)
y = np.sin(x)
z = np.cos(x)

#画一个具有2行2列的子图，此图为第1行第1列
#plt.subplot(221)
#plt.plot(x,y)
#plt.plot(x,z, color='r')
#横轴参考线
#plt.axhline(y=0, linewidth=4, color='r')
#plt.axhline(y=0.5, xmin=0.25, xmax=0.75, color='b')
#纵轴参考线
#plt.axvline(x=0, linewidth=4, color='b', linestyle='--')
#画区域
#plt.axhspan(0.25, 0.75, facecolor='0.5', alpha=0.5)
#plt.axvspan(0.75, 1.0, facecolor='g', alpha=0.5)
#横纵坐标的显示范围
#plt.axis([-1 * np.pi, np.pi, -1, 1])

#更改线的颜色
#plt.subplot(222)
plot1 = plt.plot(x,z, color='b')
plot2 = plt.plot(x,z, 'r')
plt.ylim(-1,1)
plt.legend([plot1,plot2], ['sin','cos'], loc = 'upper right')

#画离散的点
#plt.subplot(223)
#a = np.arange(0, 10, 0.5)
#b = a
#plt.plot(a,b,'o')

#更改线的风格
#plt.subplot(224)
#plt.title('change line style')
#plt.xlabel('x')
#plt.ylabel('y')
#plt.plot(a,b,'--')
plt.show()


