a=eval(input("enter a number"))
flag=0
if a<=1:
    print("Not a prime Number")
else:
    for i in range(2,a):
        if (a%i)==0:
            flag=1
        break

if (flag==0):
    print("Prime Number")
else:
    print("Not Prime")
    