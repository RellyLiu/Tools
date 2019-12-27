import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d
import time
import pdb
pause = False
def onClick(event):
    global pause
    pause = True

def plot_vehicle(x, y, theta, x_traj, y_traj):
    p1_i = np.array([0.5, 0, 1]).T
    p2_i = np.array([-0.5, 0.25, 1]).T
    p3_i = np.array([-0.5, -0.25, 1]).T

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

plt.ion()
fig = plt.figure(1)
t = [0]
t_now = 0
f = open("/home/dahua/workspace/script/pose_data")
x = []
y = []
a = []
fig.canvas.mpl_connect('button_press_event', onClick)

count=0
for line in f:
  count = count + 1
  if count < 20:
     continue
  count = 0

  if  pause: 
    plt.pause(1)

  if not pause:
    data = line.split()
    plt.clf()
    x.append( float(data[0] ) )
    y.append( float(data[1] ) ) 
    a.append( float(data[2] ) ) 
    plot_vehicle(x[-1], y[-1], a[-1], x, y)
    plt.plot(x, y, 'b--')
    ax = fig.add_subplot( 111)
    ax.axis('equal')
    plt.legend(loc='lower left')
    plt.text(-3, 20, "b",size = 15 ,alpha = 0.2)
    plt.draw()
    plt.pause(0.000000001)
plt.ioff()
plt.show()


