
#finally block illustrated

import sys
while True:
    print("Hello")
    a=eval(input("enter a:"))
    b=eval(input("enter b:"))
    try:
        c=a/b
        print("c is: ",c)
        print("Hello")
        break
    
    except:
            print("Failed coz b was:",b)
            print("Error class was:",sys.exc_info()[0])
    finally:
            print("a was:",a)
            print("b was:",b)
    

