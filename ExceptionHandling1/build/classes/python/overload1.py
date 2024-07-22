class abc:
    def __init__(self,x):
        self.x=x
    def __add__(self,other):
        print("The value of ob1 is:",self.x)
        print("The value of ob2 is:",other.x)
        print("The addition of two objects is:",end=' ')
        return self.x + other.x
    def __sub__(self,other):
        print("The value of ob1 is:",self.x)
        print("The value of ob2 is:",other.x)
        print("The subtraction of two objects is:",end=' ')
        return self.x - other.x
ob1=abc(10)
ob2=abc(20)
ob3=ob1+ob2     # ob3= ob1.__sub__(ob2)
print(ob3)
ob3=ob1-ob2
print(ob3)
