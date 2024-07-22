from array import *
a=[3,1,1,2]
b=[4,3,3,2,1]
a.sort()
b.sort()
# print("hello")
# print(a,b)
for i in range(len(a)):
        if a[i]!=a[i+1]:
            continue
        else:
            a.pop(i)
print(a)