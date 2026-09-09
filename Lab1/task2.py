def is_prime(n):
    count =0
    for i in range(1,n+1):
        if((n%i)==0):
            count+=1
    if(count>2):
        return False
    else:
        return True
n=int(input("Enter a number to check if it is prime or not: "))
if(is_prime(n)):
    print(n," is prime")
else:
    print(n," is not prime")
