class Compute:
    def area(self, x=None, y=None):
          if x!=None and y !=None:
              return x*y
          elif x!=None:
              return x*x
          else:
              return 0
obj = Compute()
print(obj.area())
print(obj.area(6))
print(obj.area(2,8))