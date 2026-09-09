import numpy as np
def isSymmetric(arr):
    arr=np.array(arr)
    trans=np.transpose(arr)
    return np.all(trans==arr)
arr2=[[1,1],[1,1]]
if(isSymmetric(arr2)):
    print("Symmetric")
else:
    print("Not Symmetric")
arr3=[[1,2],[3,4]]
if(isSymmetric(arr3)):
    print("Symmetric")
else:
    print("Not Symmetric")

