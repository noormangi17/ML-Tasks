import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,2*np.pi,100)
y_sin=np.sin(x)
y_cos=np.cos(x)
plt.plot(x,y_sin,label='sin(x)')
plt.plot(x,y_cos,label='cos(x)',color="red")
plt.legend()
plt.title("cos(x) and sin(x) graph")
plt.xlabel('x')
plt.ylabel('y')
plt.show()