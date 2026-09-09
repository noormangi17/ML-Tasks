def multiply(*args):
    args=list(args)
    prod=1
    for i in args:
        prod=prod*i
    return prod
print("Product: ",multiply(1,2,3))