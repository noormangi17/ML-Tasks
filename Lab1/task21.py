import numpy as np
A=np.array([1,2,3])
B=np.array([4,5,6])
manual_dot=A*B
manual_dot=np.sum(manual_dot)
print("Manual Dot Product: ",manual_dot)
print("Dot product: ",np.dot(A,B))