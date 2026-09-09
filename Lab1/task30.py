import numpy as np
import matplotlib.pyplot as plt
x=np.random.randint(1,100,10)
y=x**2
fig, ax=plt.subplots(2,2)
ax[0,0].plot(x,y,color='pink')
ax[0,0].set_title("Line Plot")
ax[0,0].set_xlabel('x')
ax[0,0].set_ylabel('y')
ax[0,1].bar(x,y,color='blue')
ax[0,1].set_title("Bar Chart")
ax[0,1].set_xlabel('x')
ax[0,1].set_ylabel('y')
ax[1,0].scatter(x,y,color='purple')
ax[1,0].set_title("Scatter Plot")
ax[1,0].set_xlabel('x')
ax[1,0].set_ylabel('y')
ax[1,1].hist(x,bins=5,color='green')
ax[1,1].set_title("Histogram")
ax[1,1].set_xlabel('Value')
ax[1,1].set_ylabel('Frequency')
plt.tight_layout
plt.show()