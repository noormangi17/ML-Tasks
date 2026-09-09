import numpy as np
arr=np.random.rand(4,4)
diag=np.diag(arr)
diag_sum=np.sum(diag)
print(arr)
print(f"Diagonal elements: {diag}")
print(f"Sum of diagonals: {diag_sum}")