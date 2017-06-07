
# coding: utf-8

# In[ ]:

#fash fourier transform
import numpy as np
from matplotlib.pyplot import plot
from matplotlib.pyplot import show

x=np.linspace(0,2*np.pi,30)
wave=np.cos(x)
transformed=np.fft.fft(wave)

fftshift=np.fft.fftshift(transformed)

plot(transformed)
plot(fftshift)
show()


# In[ ]:

#random walk

cash=np.zeros(10000)
cash[0]=1000
outcome=np.random.binomial(9,.5,size=len(cash))

for i in range(1,len(cash)):
    if outcome[i]<5:
        cash[i]=cash[i-1]-1
    elif outcome[i]<10:
        cash[i]=cash[i-1]+1
    else:
        raise AssertionError('Unexpected outcome',outcome)

plot(outcome)
show()

plot(np.arange(len(cash)),cash)
show()


# In[ ]:

#hypergeometric distribution
points=np.zeros(100)
outcomes=np.random.hypergeometric(25,1,3,size=len(points))

for i in range(len(points)):
    if outcomes[i]==3:
        points[i]=points[i-1]+1
    elif outcomes[i]==2:
        points[i]=points[i-1]-6
    else:
        points[i]
    print (outcomes[i],points[i])
    
plot(np.arange(len(points)),points)
show()

