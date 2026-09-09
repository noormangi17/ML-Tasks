str=input("Enter a string: ")
str=str.replace(" ","")
rev=str[::-1]
if rev== str:
    print(f"{str} is a Palindrome")
else:
    print(f"{str} is not a Palindrome")