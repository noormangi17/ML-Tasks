import numpy as np
arr=np.random.randint(1,12,(3,4))
print(arr)
rows=[0,2]
columns=[1,3]
arr2=arr[np.ix_(rows,columns)]
print(arr2)
