class check():
    def area(self,x=None,y=None):
        if x!=None and y!=None:
           return x*y
        elif x!=None:
           return x*x
        else:
            return 0
        
a=check()
print(a.area())
print(a.area(3))
print(a.area(2,4))