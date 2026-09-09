import numpy as np
import matplotlib.pyplot as plt
x=np.random.randn(500)
mean_val=np.mean(x)
plt.hist(x,bins=30,color='pink',alpha=0.7)
plt.axvline(mean_val,color='blue',linestyle='--',label=f'Mean: {mean_val:.2f}')
plt.title("Histogram")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.legend()
plt.show()