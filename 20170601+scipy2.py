
# coding: utf-8

# In[ ]:

from scipy import integrate
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

y= lambda x:np.exp(-x**2)
integrate.quad(y,-np.inf,np.inf)


# In[ ]:

from scipy import interpolate
x=np.linspace(-18,18,36)
noise=.1*np.random.random(len(x))
signal=np.sinc(x)+noise

#插入一维插值
interpreted=interpolate.interp1d(x,signal)
x2=np.linspace(-18,18,180)
y=interpreted(x2)

#插入三维插值
cubic=interpolate.interp1d(x,signal,kind='cubic')
y2=cubic(x2)

plt.plot(x,signal,'o',label='data')
plt.plot(x2,y,':',label='liner')
plt.plot(x2,y2,'-',label='cubic')

plt.legend()
plt.show()


# In[ ]:

#ndimage&misc.lena
from scipy import misc,ndimage

image=misc.ascent().astype(np.float32)
plt.plot(221)
plt.title('original image')
img=plt.imshow(image,cmap=plt.cm.gray)
plt.axis('off')

plt.subplot(222)
plt.title('median filter')
filtered=ndimage.median_filter(image,size=(42,42))
plt.imshow(filtered,cmap=plt.cm.gray)

plt.subplot(223)
plt.title('rotated')
rotated=ndimage.rotate(image,90)
plt.imshow(rotated,cmap=plt.cm.gray)

plt.subplot(224)
plt.title('prewitt filter')
filtered=ndimage.prewitt(image)
plt.imshow(filtered,cmap=plt.cm.gray)

fig.tight_layout()
plt.show()


# In[ ]:

get_ipython().magic('pylab')

fig,axes=plt.subplots(4,5)
for i,ax in enumerate(axes.flat,start=1):
    ax.set_title('Test Axes{}'.format(i))
    ax.set_xlabel('X_axis')
    ax.set_ylabel('Y_axis')
    
fig.tight_layout()
plt.show()

