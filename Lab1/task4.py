def removeDuplicates(*nums):
     res=[]
     for i in nums:
         if i not in res:
            res.append(i)
     return res
a = removeDuplicates(10, 20, 30, 10, 40)

print(a)