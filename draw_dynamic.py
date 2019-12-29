#!/usr/bin/python
#coding=utf-8

import numpy as np
import matplotlib.pyplot as plt
import sys

pause = False
x_scale = 100
data_file = sys.argv[1]

def onClick(event):
    global pause
    if pause:
        pause = False
    else:
        pause = True

def plot_vehicle(x, y, theta):
    global x_scale

    p1_i = np.array([0.01 * x_scale, 0, 1]).T
    p2_i = np.array([-0.01 * x_scale, 0.005 * x_scale, 1]).T
    p3_i = np.array([-0.01 * x_scale, -0.005 * x_scale, 1]).T

    T = transformation_matrix(x, y, theta)
    p1 = np.matmul(T, p1_i)
    p2 = np.matmul(T, p2_i)
    p3 = np.matmul(T, p3_i)

    plt.plot([p1[0], p2[0]], [p1[1], p2[1]], 'k-')
    plt.plot([p2[0], p3[0]], [p2[1], p3[1]], 'k-')
    plt.plot([p3[0], p1[0]], [p3[1], p1[1]], 'k-')

def transformation_matrix(x, y, theta):

    return np.array([
        [np.cos(theta), -np.sin(theta), x],
        [np.sin(theta), np.cos(theta), y],
        [0, 0, 1]
    ])

f = open(data_file)
x = []
y = []
a = []

fig = plt.figure(1)
fig.canvas.mpl_connect('button_press_event', onClick)
ax = fig.add_subplot(1,1,1)

count = 0
cache = 0

for line in f:

  cache = cache + 1
  if cache < 20:
     continue
  cache = 0

  if  pause: 
    plt.pause(1)

  if not pause:
    data = line.split()
    x.append( float(data[0] ) )
    y.append( float(data[1] ) ) 
    a.append( float(data[2] ) )

    plt.clf()
    plot_vehicle(x[-1], y[-1], a[-1])
    plt.plot(x, y, 'b--')
    plt.axis('equal')
    plt.draw()

    plt.pause(0.001)

  if count > 20000:
    x = []
    y = []
    a = []
    plt.clf()
    count = 0

  count = count + 1
  x_scale = plt.axis()[1] - plt.axis()[0]

plt.show()
