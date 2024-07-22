#without threads
#perf_counter is used to find execution time of a program

import time
def func1(seconds):
    print("sleeping for",seconds,"seconds")
    time.sleep(seconds)

time1=time.perf_counter()

func1(3)
func1(2)
func1(1)

time2=time.perf_counter()
print(time2-time1)

