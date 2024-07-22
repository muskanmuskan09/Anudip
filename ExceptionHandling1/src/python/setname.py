from threading import Thread

def fun(n):
    print("Hello")

t1=Thread(target=fun,args=(3,))

t1.start()

#using getName and setName
print(t1.getName())   
t1.setName("multi")
print(t1.name) 