str=input("Enter a string: ")
freq={ch:str.count(ch) for ch in str}
print(freq)