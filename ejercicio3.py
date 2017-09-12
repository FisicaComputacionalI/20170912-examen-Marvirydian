import numpy as np
import matplotlib.pyplot as plt
def f(x):
  return (2*np.sin(x))+2015
def h(x):
  return (x+1997)
x1=np.arange(0.0,20.0,0.1)
plt.figure(1)
plt.subplot(211)
plt.plot(x1,f(x1),'c',x1,h(x1),'r')
plt.title('GRAFICA 3')
plt.subplot(212)
plt.plot(x1,f(x1),'m')
plt.savefig('Grafica3.png')
plt.show()

