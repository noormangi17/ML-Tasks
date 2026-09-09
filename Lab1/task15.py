import numpy as np
arr1=np.random.randint(1,10,(3,3))
arr2=np.random.randint(1,10,(3,3))
print(f"Matrxi 1: {arr1}")
print(f"Matrxi 2: {arr2}")
print(f"Element-wise Multiplication: {arr1*arr2}")
print(f"Matrix Multiplication: {arr1@arr2}")

