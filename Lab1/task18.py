import numpy as np
marks=np.random.randint(1,100,(5,3))
total=np.sum(marks,axis=1)
mean=np.mean(marks,axis=1)
print("Marks: ",marks)
print("Total: ",total)
print("Mean: ",np.round(mean,2))
