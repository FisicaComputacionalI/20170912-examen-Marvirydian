import numpy as np
import matplotlib.pyplot as plt
#Grafica un vector para valores de x
x=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
plt.xlabel('Edad')
#Grafica un vector y para cada valor de x
y=[1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017]
plt.ylabel('Anios')
plt.title('Marlene')
#Usa matplotlib para graficar x y y
plt.plot(x,y,'cs')
plt.savefig('recta.png')
plt.show()