
# coding: utf-8

# In[3]:

from matplotlib.pyplot import plot
from matplotlib.pyplot import show
import pandas as pd
import numpy as np

def fit_line(t,y):
    A=np.vstack([t,np.ones_like(t)]).T
    return np.linalg.lstsq(A,y)[0]
    print(A)

data=pd.read_excel(r'G:\新建文件夹\eg.\eg1.xls')
data=data[-200:-1]
h=data.high
l=data.low
c=data.close

pivots=(h+l+c)/3

t=np.arange(len(c))
sa,sb=fit_line(t,pivots-h+l)
ra,rb=fit_line(t,pivots+h-l)

support=sa*t+sb
resistance=ra*t+rb

plot(t,c)
plot(t,support)
plot(t,resistance)
show()

