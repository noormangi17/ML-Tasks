import numpy as np
arr=np.random.randint(1,100,25)
arr_sum=np.sum(arr)
arr_mean=np.mean(arr)
arr_std=np.std(arr)
print(f"Sum: {arr_sum}")
print(f"Mean: {arr_mean}")
print(f"Standard Deviation: {arr_std}")