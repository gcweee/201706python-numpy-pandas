import numpy as np
def ultimate_answer(a):
    result=np.zeros_like(a)
	#创建一个与a相同的元素皆为0的矩阵
    result.flat=42
	#最终结果为42
    return result

ufunc=np.frompyfunc(ultimate_answer,1,1)
#使用frompyfunc方法
ufunc(np.arange(4))
ufunc(np.arange(6).reshape(3,2))
#注意：reshape为方法，要用"."
 
#Fibonacci&rint
from matplotlib.pyplot import show
from matplotlib.pyplot import plot
 
F=np.matrix([[1,1],[1,0]])

n=np.arange(1,9)
sqrt5=np.sqrt(5)
phi=(1+sqrt5)/2
fibonacci=np.rint(phi**n-(-1/phi)**n)/sqrt5
#注意：此处rint方法可以不用，仍可得出结果
plot(n,fibonacci)
show()

#Lissajous curve
from matplotlib.pyplot import show
from matplotlib.pyplot import plot

t=np.linspace(-np.pi,np.pi,500)
x=np.sin(9*t+np.pi/4)
y=np.sin(8*t)
plot(x,y)
show()

#Fourier series
t=np.linspace(-np.pi,np.pi,201)
k=np.arange(1,199)
k=2*k-1
f=np.zeros_like(t)

for i in range(len(t)):
    f[i]=np.sum(np.sin(k*t[i])/k)
f=(4/np.pi)*f

plot(t,f)
show()

#避免使用循环
t=np.linspace(-np.pi,np.pi,199)
k=np.arange(1,200)
k=2*k-1

def fourier_series(k1,t1):
    k1=2*k1-1
    return np.sum((4*np.sin(k1*t1))/(k1*np.pi))

ufunc=np.vectorize(fourier_series)

fourier_series=ufunc(t,k)
plot(t,fourier_series)
show()

