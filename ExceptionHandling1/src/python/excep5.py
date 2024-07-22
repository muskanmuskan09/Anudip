# handling multiple exceptions

import sys
try:
    a=0
    x=input("enter an integer:")
    b=1/int(x)
    c=1/b
    
except (TypeError, ZeroDivisionError):
    print("Exception caught:",sys.exc_info()[0])
finally:
    print("b= ",b,"c= ",c)
    
