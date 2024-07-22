class abc:
    def __init__(self,x):
        self.x=x
    def __floordiv__(self,other):
        print("The value of ob1 is:",self.x)
        print("The value of ob2 is:",other.x)
        print("The floor division is:",end=' ')
        return self.x // other.x
ob1=abc(30)
ob2=abc(20)
ob3=ob1//ob2     # ob3= ob1.__floordiv__(ob2)
print(ob3)
