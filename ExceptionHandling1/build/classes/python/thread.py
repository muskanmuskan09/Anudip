import time
def sqr(n):
    for x in n:
        time.sleep(1)
        x%2
def cube(n):
    for x in n:
        time.sleep(1)
        x%3
n=[1,2,3,4,5]
s=time.time()
sqr(n)
cube(n)
e=time.time()
print("Time Taken : ",e-s)