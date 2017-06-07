
# coding: utf-8

# In[ ]:

import pandas as pd
import numpy as np

data=pd.read_excel(r'C:\Users\gcwee\Desktop\eg.xlsx',sheetname='Sheet1')
data1=pd.read_excel(r'C:\Users\gcwee\Desktop\eg.xlsx',sheetname='Sheet2')

data=data[-252:-2]
data1=data1[-252:-2]

o=data.open
h=data.high
l=data.low
c=data.close
v=data.value

o1=data1.open1
h1=data1.high1
l1=data1.low1
c1=data1.close1
v1=data1.value1

returns0=np.diff(c)/c[:-1]
returns1=np.diff(c1)/c1[:-1]

covrances=np.cov(returns0,returns1)
covrances


# In[ ]:

import pandas as pd
import numpy as np
from matplotlib.pyplot import plot
from matplotlib.pyplot import show

data=pd.read_excel(r'C:\Users\gcwee\Desktop\eg.xlsx',sheetname='Sheet1')
data1=pd.read_excel(r'C:\Users\gcwee\Desktop\eg.xlsx',sheetname='Sheet2')

data=data[-252:-2]
data1=data1[-252:-2]

o=data.open
h=data.high
l=data.low
c=data.close
v=data.value

o1=data1.open1
h1=data1.high1
l1=data1.low1
c1=data1.close1
v1=data1.value1

returns0=np.diff(c)/c[:-1]
returns1=np.diff(c1)/c1[:-1]

c=np.array(c)
c1=np.array(c1)

difference=c-c1
difference

avg=np.mean(difference)
dev=np.std(difference)
print('out of sync',np.abs(difference[-1]-avg)>2*dev)

t=np.arange(len(np.array(returns0)))
plot(t,returns0)
plot(t,returns1)
show()

