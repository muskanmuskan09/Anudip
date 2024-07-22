#using threads

#importing threading library
import threading
import time

#creating function for threads
def func1(sec):
    print(f"sleeping for {sec} seconds")
    time.sleep(sec)

time1=time.perf_counter() #It will print the time

#creating threads
t1=threading.Thread(target=func1, args=(3,))
t2=threading.Thread(target=func1, args=(2,))
t3=threading.Thread(target=func1, args=(1,))

#we have to manually start the threads
t1.start()
#t1.join()
t2.start()
#t2.join()
t3.start()
#t3.join()
time2=time.perf_counter()
print(time2-time1)











