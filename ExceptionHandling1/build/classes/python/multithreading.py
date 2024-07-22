from threading import Thread
import time


def func1(sec):
    print(f"sleeping for {sec} seconds")
    time.sleep(sec)
time1=time.perf_counter()

t1=Thread(target=func1,args=(4,))
t2=Thread(target=func1,args={2})

t1.start()
print(t1.is_alive())
# t1.join()
# print(t1.is_alive())
t2.start()
# t2.join()
print(t2.getName)
# print(t1.getName
t2.setName("multi")
print(t2.name)
time2=time.perf_counter()
print(time2-time1)
