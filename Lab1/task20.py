import numpy as np
arr=np.arange(1,17,1).reshape(4,4)
print(arr)
transpose=np.transpose(arr)
print(f"Transpose: {transpose}")
determinant=np.linalg.det(arr)
determinant=np.round(determinant,2)
print(f"Determinant: {determinant}")
if determinant!=0:
    inv=np.linalg.inv(arr)
    print("Inverse: ",inv)
else:
    print("Inverse does not exist")