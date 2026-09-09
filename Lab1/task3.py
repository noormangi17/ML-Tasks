n=int(input("Enter \'n\' to generate fibonacii \'n\' terms: "))
first=0
second=1
print(first)
print(second)
for i in range(0,n-2):
    sum=first+second
    print(sum)
    first=second
    second=sum
    
