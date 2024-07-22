f=open("random.text","r")
even=0
s = f.readline().split()
for i in s:
    if int(i)%2==0:
        print(i)
        even+=1

print(even)
f.close()





# from random import randint
# f=open("random.text","w")
# for i in range(1,16):
#     x=randint(500,1000)
#     f.write(str(x)+ " ")
# f.close()
