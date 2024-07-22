from threading import Thread
def fun():
    print("hello \n")

t1=Thread(target=fun)
print(t1.is_alive())
t1.start()
print(t1.is_alive())
    