try:
    a=10
    b=0
    assert b!=0,"invalid operation"
except AssertionError as ae:
    print(ae)