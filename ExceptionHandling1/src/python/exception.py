class Error(Exception):
   """Base class for other exceptions"""
   pass

class ValueTooSmallError(Error):
   """Raised when the input value is too small"""
   pass

class ValueTooLargeError(Error):
   """Raised when the input value is too large"""
   pass

import sys
from random import randint
l=randint(1,100)
count=0
while True:
    try:
        randomlist=int(input("enter number btw 1 and 100 :"))
        count+=1
        if randomlist<l:
            raise ValueTooSmallError
        elif randomlist>l:
            raise ValueTooLargeError
        break
    except ValueTooLargeError:
        print("value large")
    except ValueTooSmallError:
        print("small")

print("great")
print("u took",count,"chances")