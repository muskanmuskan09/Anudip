# overloading comparison operators

class abc:
    def __init__(self,x):
        self.x=x
    def __lt__(self,other):
        print("The value of ob1 is:",self.x)
        print("The value of ob2 is:",other.x)
        print("ob1<ob2 is :",end=' ')
        return self.x < other.x
    def __gt__(self,other):
        print("The value of ob1 is:",self.x)
        print("The value of ob2 is:",other.x)
        print("ob1>ob2 is :",end=' ')
        return self.x > other.x
    def __ne__(self,other):
        print("The value of ob1 is:",self.x)
        print("The value of ob2 is:",other.x)
        print("ob1!=ob2 is :",end=' ')
        return self.x != other.x

ob1=abc(30)
ob2=abc(20)
ob3=ob1!=ob2     # ob3= ob1.__ne__(ob2)
print(ob3)
ob3=ob1>ob2     # ob3= ob1.__gt__(ob2)
print(ob3)
ob3=ob1<ob2     # ob3= ob1.__lt__(ob2)
print(ob3)
