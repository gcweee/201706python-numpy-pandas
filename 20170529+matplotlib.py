
# coding: utf-8

# In[ ]:

#matplotlib
#http://www.labri.fr/perso/nrougier/teaching/matplotlib/


# In[ ]:

import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
C,S = np.cos(X), np.sin(X)

import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C,S = np.cos(X), np.sin(X)

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
       [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])

plt.yticks([-1, 0, +1],
       [r'$-1$', r'$0$', r'$+1$'])

for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(16)
    label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.65 ))

t = 2*np.pi/3
plt.plot([t,t],[0,np.cos(t)], color ='blue', linewidth=1.5, linestyle="--")
plt.scatter([t,],[np.cos(t),], 50, color ='blue')

plt.annotate(r'$\sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
             xy=(t, np.sin(t)), xycoords='data',
             xytext=(+10, +30), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

plt.plot([t,t],[0,np.sin(t)], color ='red', linewidth=1.5, linestyle="--")
plt.scatter([t,],[np.sin(t),], 50, color ='red')

plt.annotate(r'$\cos(\frac{2\pi}{3})=-\frac{1}{2}$',
             xy=(t, np.cos(t)), xycoords='data',
             xytext=(-90, -50), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

plt.plot(X,C)
plt.plot(X,S)

plt.show()


# In[8]:

#frip drop
# New figure with white background
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

fig = plt.figure(figsize=(6,6), facecolor='white')

# New axis over the whole figure, no frame and a 1:1 aspect ratio
ax = fig.add_axes([0,0,1,1], frameon=False, aspect=1)

# Number of ring
n = 50
size_min = 50
size_max = 50*50

# Ring position
P = np.random.uniform(0,1,(n,2))

# Ring colors
C = np.ones((n,4)) * (0,0,0,1)
# Alpha color channel goes from 0 (transparent) to 1 (opaque)
C[:,3] = np.linspace(0,1,n)

# Ring sizes
S = np.linspace(size_min, size_max, n)

# Scatter plot
scat = ax.scatter(P[:,0], P[:,1], s=S, lw = 0.5,
                  edgecolors = C, facecolors='None')

# Ensure limits are [0,1] and remove ticks
ax.set_xlim(0,1), ax.set_xticks([])
ax.set_ylim(0,1), ax.set_yticks([])

def update(frame):
    global P, C, S

    # Every ring is made more transparent
    C[:,3] = np.maximum(0, C[:,3] - 1.0/n)

    # Each ring is made larger
    S += (size_max - size_min) / n

    # Reset ring specific ring (relative to frame number)
    i = frame % 50
    P[i] = np.random.uniform(0,1,2)
    S[i] = size_min
    C[i,3] = 1

    # Update scatter object
    scat.set_edgecolors(C)
    scat.set_sizes(S)
    scat.set_offsets(P)

    # Return the modified object
    return scat,

animation=animation.FuncAnimation(fig, update, interval=10, blit=True, frames=200)
#animation.save('rain.gif', writer='imagemagick', fps=30, dpi=40)
plt.show()


# In[ ]:

import numpy as np
import matplotlib.pyplot as plt

plt.subplot(2,3,1)
plt.subplot(2,3,2)
plt.subplot(2,3,3)
plt.subplot(2,2,4)
plt.subplot(2,2,5)
plt.show()


# In[ ]:

plt.subplot(3,3,1)
plt.subplot(3,3,2)
plt.subplot(3,3,3)
plt.subplot(3,4,5)
plt.subplot(3,4,6)
plt.subplot(3,4,7)
plt.subplot(3,4,8)
plt.subplot(3,5,11)
plt.subplot(3,5,12)
plt.subplot(3,5,13)
plt.subplot(3,5,14)
plt.subplot(3,5,15)
plt.show()


# In[ ]:

x=np.arange(1,19,.4)

y1=np.log10(x)
y2=.01*x**2
y3=np.sin(x)

plt.plot(x,y1,'r-',label='y1')
plt.plot(x,y2,'b^',label='y2')
plt.plot(x,y3,'mo',label='$y3$')

plt.legend(loc=2)

plt.show()


# In[ ]:

import numpy as np
import matplotlib.pyplot as plt
def func(x):
return np.sin(2*np.pi*x)
x1 = np.arange(0.0,4.0,0.1)
x2 = np.arange(0.0,4.0,0.01)
y1 = func(x1)
y2 = func(x2)
y1n = y1 + 0.1*np.random.randn(len(x1))
plt.figure()
plt.subplot(211)
plt.plot(x1,y1,'bo',x2,y2,'r:')
plt.subplot(212)
plt.plot(x1,y1n,'bo',x2,y2,'r:')
plt.show()


# In[ ]:

x1=np.arange(.0,4.0,.1)
x2=np.arange(.0,4.0,.001)
def func(x):
    return 2*np.sin(2*np.pi*x)

y1=func(x1)
y2=func(x2)

plt.figure()
plt.subplot(211)
plt.plot(x1,y1,'r*',x2,y2,'b:')
plt.subplot(212)
plt.axis([-1.0,5.0,-3.2,3.2])
plt.plot(x1,y1,'mo',x2,y2,'g:')
plt.show()




# In[ ]:

#3D plot
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib.cm as cm

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
n = 200
xs = np.random.rand(n)
ys = np.random.rand(n)
zs = np.random.rand(n)
rs = np.sqrt(xs*xs + ys*ys + zs*zs)

ax.scatter(xs,ys,zs,c=rs,marker='o')
ax.set_xlabel('x label')
ax.set_ylabel('y label')
ax.set_zlabel('z label')

plt.show()


# In[ ]:

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = np.linspace(0, 1 *np.pi, 100)
y = np.linspace(0, 2 *np.pi, 100)
x, y = np.meshgrid(x,y)
z = -np.sin(x)*np.sin(y)
ax.plot_wireframe(x, y, z, rstride=5, cstride=5)
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

surf = ax.plot_surface(x, y, z, rstride=4, cstride=4,
cmap=cm.coolwarm,alpha=0.7)
fig.colorbar(surf,shrink=0.5)
cset = ax.contourf(x, y, z, zdir='z',cmap=cm.coolwarm,offset=-1)
cset=ax.contourf(x,y,z,zdir='z',cmap=cm.summer,offset=-1)

plt.show()


