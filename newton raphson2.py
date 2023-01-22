import matplotlib.pyplot as plt
import numpy as np
def f(x):
	return np.sin(x)-x/10
def deri(x):
	return np.cos(x)-1/10
xx=np.linspace(-4,4,100)
yy=f(xx)
plt.plot(xx,yy)
plt.axhline()
plt.axvline()
plt.show()
eps=0.001
err=1
x1=3
x2=0.3
u1=0
u2=0
while err>=eps:
	x1=x1-f(x1)/deri(x1)
	err=abs(x1-u1)
	u1=x1
	x2=x2-f(x2)/deri(x2)
	err=abs(x2-u2)
	u2=x2
print(x1)
print(x2)