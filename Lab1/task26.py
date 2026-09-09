import matplotlib.pyplot as plt
import numpy as np
x=np.arange(1,31,1)
print(x)
y=np.random.randint(-10,40,30)
plt.plot(x,y)
plt.title("Line Chart")
plt.xlabel("Day")
plt.ylabel("Temperaure")
plt.show()