#Newton Raphson Method
import numpy as np
import matplotlib.pyplot as plt
def f(x):
	y=(x**2)-11
	return y
	
def deri(x):
	d=2*x
	return d
	
xi=0
xf=10
n=100

xx=np.linspace(xi,xf,n)
yy=xx*xx-11
plt.plot(xx,yy)
plt.axhline()
plt.axvline()
plt.show()
	
err=1
eps=0.01
x=8
u=0

while err>eps:
	x= x-(f(x)/deri(x))
	err=abs(x-u)
	u=x
print("the equation is x^2-11")	
print('the root is',x)
print("error=",err)