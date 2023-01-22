import matplotlib.pyplot as plt
import numpy as np
def f(x):
	return x*x-5*x+6
x=np.linspace(1,6,100)
y=f(x)
plt.plot(x,y)
plt.axhline()
plt.axvline()
plt.show()
a=1
b=2.5
el=0.01
e=(b-a)
while e>el:
	c=(a+b)/2
	if f(a)*f(b)>=0:
		print("not")
	elif f(c)*f(a)<0:
		b=c
		e=(b-a)
	elif f(c)*f(a)>0:
		a=c
		e=(b-a)
print(c)

a=2.5
b=4
el=0.01
e=(b-a)
while e>el:
	c=(a+b)/2
	if f(a)*f(b)>=0:
		print("not")
	elif f(c)*f(a)<0:
		b=c
		e=(b-a)
	elif f(c)*f(a)>0:
		a=c
		e=(b-a)
print(c)