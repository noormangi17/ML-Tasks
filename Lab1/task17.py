import numpy as np
arr=np.array([10,20,30,40,50])
minimum=np.min(arr)
maximum=np.max(arr)
normalized=(arr-minimum)/(maximum-minimum)
print(np.round(normalized,2))