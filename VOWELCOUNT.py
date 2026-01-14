x=input("Enter a string: ")
c=0
for i in x:
    if i in  'AEIOUaeiou':
        c+=1
print("Number of vowels:",c)