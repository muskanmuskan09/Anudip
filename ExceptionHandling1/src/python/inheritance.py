# # hybird inheritance
# class school:
#     def Func1(self):
#         print("I am from School class")
# class student(school):
#     def Func2(self):
#         print("I am from student class")
# class student2(school):
#     def func3(self):
#         print("I am from student 2 class")
# class student3(student,school):
#     def func4(self):
#         print("I am from  student 3 class")

# obj=student3()
# obj.Func1()
# obj.Func2()

# Hierarchical inheritance
class parent:
    def FuncA(self):
        print("I am from parent class")
class childone(parent):
    def FuncB(self):
        print("I am from child one class")
class childtwo(parent):
    def funcC(self):
        print("I am from child two class")
a=parent ()
b=childone()
c=childtwo()
a.FuncA()
b.FuncB()
c.funcC()


# # multilevel inheritance
# class dogs():
#     def __init__(self):
#         self.a="Dogs"
# class cats():
#     def __init__(self):
#         self.b="Cats"  
# class Animal(dogs,cats):
#     def A(self):
#         print(f"I love {a} and {b}")
# x=dogs()
# y=cats()
# z=Animal()
# z.A()