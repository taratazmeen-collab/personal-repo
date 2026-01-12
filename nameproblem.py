name=input("Enter a name here =")
i=len(name)
print ("The length of the name is:",i)
#this section is to print the name in vertical order
k=int(input("Enter the number u want to print  ="))
if k==0:
    print("You have entered 0, hence vertical order will be printed")
    for i in range(i) :
        print(name[i])
#this section is to print the name in vertical reverse order
else:
    print("You have entered",k,"hence vertical reverse order will be printed")
    for j in range(i-1,-1,-1) :
        print(name[j])  