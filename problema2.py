import numpy as np
import matplotlib.pyplot as plt
def f(x):
  return (2*np.sin(x))+2015
x1=np.arange(0.0,10.0,0.5)
plt.title('UNIVERSIDAD')
plt.plot(x1,f(x1),'cs',x1,f(x1),'g')
plt.savefig('Universidad.png')
plt.show()

