from threading import Thread ,current_thread
def A(n):
    print(current_thread())
    for i in range(n):
        print("I am from A function ")

def B(n,msg):
    for i in range(n):
        print(msg) 

#creating threads
t1=Thread(target=A,args=(2,))   
t2=Thread(target=B,kwargs={'n':3,'msg':'I am from B function'}) 

#start method
t1.start()
#join method
t1.join()
t2.start() 
t2.join()

#this is executed by main Thread
for i in range(2):
    print("i am from 'Main Thread'")

#is_alive() method    
print(t1.is_alive())

#getName method
print(t1.getName())

#name attriubute 
print(t2.name)

#setName method
t1.setName("multi")
print(t1.name)
