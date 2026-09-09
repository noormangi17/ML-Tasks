import numpy as np
temp=np.random.randint(-10,60,12)
print(temp)
mask=temp>35
print("Number of months having temperature greater than 35: ",len(temp[mask]))