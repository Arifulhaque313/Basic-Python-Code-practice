n=int(input("Enter the number ="))
flag=0
for i in range (2,n//2):
    if(n%i==0):
        flag=1
        break
if(flag==0):
    print("Prime")

else :
    print("not prime")