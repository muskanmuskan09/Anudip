class abc():
    def __init__(self,x):
        self.x=x
    def __lt__(self,other):
        print("1 :",self.x)
        print("2 :",other.x)
        print("comparison",end='')
        return self.x<other.x
    
a=abc(12)
b=abc(3)
c=a<b
print(c)



# class abc():
#     def __init__(self,x):
#         self.x=x
#     def __add__(self,other):
#         print("first :",self.x)
#         print("sec:",other.x)
#         print("addition:",end='')
#         return self.x+other.x
#     def __sub__(self,other):
#         print("first :",self.x)
#         print("sec:",other.x)
#         print("addition:",end='')
#         return self.x-other.x
    
# a=abc(20)
# b=abc(10)
# c=a+b
# print(c)
# d=a-b
# print(d)
