import numpy as np
n=10
nums=[]
for i in range(n):
    num=int(input("Entter a number to add to list: "))
    nums.append(num)
print(nums)
arr=np.array(nums)
arr=np.sort(arr)
print(arr)
med=np.median(arr)
print(f"Median: {med}")