from threading import Thread
def fun():
    print("Hello everyone")

t1= Thread(target=fun)
t2= Thread(target=fun)
print(t2.getName())   