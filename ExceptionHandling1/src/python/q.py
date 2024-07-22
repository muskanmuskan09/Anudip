# n=[33,55,33,56,44,66]
# n.sort()
# print(int(n))

l=[]
# n=int(input())
for i in range(0,10):
    a=int(input())
    l.append(a)
    
s=set(l)
S=list(s)
S.sort()
print(S)