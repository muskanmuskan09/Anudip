#Without Threading

"""import time
def sqr(n):
    for x in n:
        time.sleep(1)
        print(x%2)
def cube(n):
    for x in n:
        time.sleep(1)
        print(x%3)
n=[1,2,3,4,5]
s=time.time()
sqr(n)
cube(n)
e=time.time()
print("Time Taken : ",e-s)

"""
#With Threading

import threading
from threading import Thread
import time
def sqr(n):
    for x in n:
        time.sleep(1)
        print(x%2)
def cube(n):
    for x in n:
        time.sleep(1)
        print(x%3)
n=[1,2,3,4,5]
start=time.time()
t1=Thread(target=sqr,args=(n,))
t2=Thread(target=cube,args=(n,))
t1.start()
t1.join()
time.sleep(1)
t2.start()
t1.join()
t2.join()
end=time.time()
print("Time Taken : ",end-start)
