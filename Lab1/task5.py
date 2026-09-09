str=input("Enter any string: ")
vowel=0
consonant=0
digit=0
space=0
for i in str:
    if i.lower() in "aeiou":
        vowel+=1
    elif i.isalpha():
        consonant+=1
    elif i.isdigit():
        digit+=1
    elif i==" ":
        space+=1
print(f"String has: \n1.Vowels: {vowel}\n2.Consonants: {consonant}\n3.Digits: {digit}\n4.Spaces: {space}")

