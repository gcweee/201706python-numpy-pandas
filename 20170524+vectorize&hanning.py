# http://blog.csdn.net/jairuschan/article/details/7517773
# coding: utf-8

# In[1]:

import sys
print ("脚本名：", sys.argv[0])
for i in range(1, len(sys.argv)):
  print ("参数", i, sys.argv[i])


# In[ ]:

import numpy as np
import pandas as pd

data=pd.read_excel(r'C:\Users\Administrator\Desktop\eg1.xls')

o=data.open
h=data.high
l=data.low
c=data.close
v=data.value

def calc_profit(opens,high,low,close):
    buy=opens
    if low<buy<high:
        return (close-buy)/buy
    else:
        return 0

func=np.vectorize(calc_profit)
profits=func(o,h,l,c)
print ('Profits:',profits)


# In[ ]:

r=(c-o)/o
for i in range(len(c)):
    if np.sum(r[i:i+252]<0):
        print('sum of r is negative')
    i=+252


# In[ ]:

import pandas as pd
import numpy as np
from matplotlib.pyplot import plot
from matplotlib.pyplot import show

data1=pd.read_excel(r'C:\Users\Administrator\Desktop\eg2\000001.xls')
data2=pd.read_excel(r'C:\Users\Administrator\Desktop\eg2\000002.xls')

o1=data1.open
h1=data1.high
l1=data1.low
c1=data1.close
v1=data1.volumes
o2=data2.open
h2=data2.high
l2=data2.low
c2=data2.close
v2=data2.volumes

c1=c1[-252:-1]
c2=c2[-252:-1]

weights=np.hanning(8)
returns1=np.diff(c1)/c1[:-1]
returns2=np.diff(c2)/c2[:-1]
smooth1=np.convolve(weights/weights.sum(),returns1)
smooth2=np.convolve(weights/weights.sum(),returns2)
t=np.arange(252)
t1=np.arange(len(c1)-1)
t2=np.arange(len(c2)-1)

smooth1=smooth1[:252]
smooth2=smooth2[:252]

plot(t1,returns1)
plot(t,smooth1)
show()

plot(t2,returns2)
plot(t,smooth2)
show()


# In[ ]:

import pandas as pd
import numpy as np
from matplotlib.pyplot import plot
from matplotlib.pyplot import show

data1=pd.read_excel(r'C:\Users\Administrator\Desktop\eg2\000001.xls')
data2=pd.read_excel(r'C:\Users\Administrator\Desktop\eg2\000002.xls')

o1=data1.open
h1=data1.high
l1=data1.low
c1=data1.close
v1=data1.volumes
o2=data2.open
h2=data2.high
l2=data2.low
c2=data2.close
v2=data2.volumes

c1=c1[-252:-1]
c2=c2[-252:-1]

weights=np.hanning(5) #平滑股票收益率hanning
returns1=np.diff(c1)/c1[:-1]
returns2=np.diff(c2)/c2[:-1]
smooth1=np.convolve(weights/weights.sum(),returns1)
smooth2=np.convolve(weights/weights.sum(),returns2)
t=np.arange(252)
t1=np.arange(len(c1)-1)
t2=np.arange(len(c2)-1)

smooth1=smooth1[:252]
smooth2=smooth2[:252]

plot(t1,returns1)
plot(t,smooth1)
show()

plot(t2,returns2)
plot(t,smooth2)
show()

