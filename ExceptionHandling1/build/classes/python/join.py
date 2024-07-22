from threading import Thread
def A():
    for i in range(3):
        print("hello")

def B():
    for i in range(2):
        print("hiiii")  

t1=Thread(target=A) 
t2=Thread(target=B) 

t1.start()
t1.join()
t2.start()
t2.join()


