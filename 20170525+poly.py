
# coding: utf-8

# In[ ]:

import numpy as np
import pandas as pd
from matplotlib.pyplot import plot
from matplotlib.pyplot import show
import random

data1=pd.read_excel(r'G:\201705python\numpy&pandas\eg2\eg2.xlsx',sheetname='Sheet1')
data2=pd.read_excel(r'G:\201705python\numpy&pandas\eg2\eg2.xlsx',sheetname='Sheet2')

data1=data1[-50:-2]
data2=data2[-50:-2]

c_601288=data2
c_601398=data1

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

def calc_profits(op,hi,lo,cl):
    buy=op
    if lo<buy<cl:
        return (cl-buy)/buy
    else:
        return 0
    
func=np.vectorize(calc_profits)
profits1=func(o1,h1,l1,c1)
profits2=func(o2,h2,l2,c2)

weights=np.hanning(10)
r1=np.diff(c1)/c1[:-1]
r2=np.diff(c2)/c2[:-1]
smooth_r1=np.convolve(weights/weights.sum(),r1)
smooth_r2=np.convolve(weights/weights.sum(),r2)

t1=np.arange(len(r1))
t2=np.arange(len(r2))
s_t1=np.arange(len(smooth_r1))
s_t2=np.arange(len(smooth_r2))

plot(t1,r1)
plot(s_t1,smooth_r1)
show()

plot(t2,r2)
plot(s_t2,smooth_r2)
show()

poly_1=np.polyfit(s_t1,smooth_r1,3)
poly_2=np.polyfit(s_t2,smooth_r2,3)
poly_sub=np.polysub(poly_1,poly_2)
xpoints=np.roots(poly_sub)

reals=np.isreal(xpoints)
xpoints=np.select([reals],[xpoints])
real_xpoints=xpoints.real
real_xpoints_without0=np.trim_zeros(real_xpoints)

print('real intersection point',xpoints)
print('sans 0s',real_xpoints_without0)



