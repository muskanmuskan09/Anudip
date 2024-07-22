import threading
#import time
# Indicates some task being done
def func(seconds):
    print(f"Sleeping for {seconds}seconds")
    #time.sleep(seconds)
func(4)
func(2)
func(1)