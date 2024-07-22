import sys


try:
    a=2
    b=0
    if a>b:
        raise NameError
except:
    print("error occured")