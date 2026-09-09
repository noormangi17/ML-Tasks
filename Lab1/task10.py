nums=[1,2,3,4,5,6,7,8,9,10]
odd=lambda x:x%2==1
odd_nums=filter(odd,nums)
print(list(odd_nums))