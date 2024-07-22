# MULTIPLE INHERITANCE
class Dog():
    mothername=""
    def D(self):
        print(self.mothername)
class Cat():
    fathername=""
    def C(self):
        print(self.fathername)
class Animal(Dog,Cat):
    def G(self):
        print("Fathername=",self.fathername)
        print("Mothername=",self.mothername)
A=Animal()
A.fathername='kamal singh'
A.mothername='Bharti'
A.G()
# A.D()
# MULTI-LEVEL INHERITANCE
# class animal():
#     def __init__(self):
#         print("HEy")
        
# class Dog(animal):
#     def D(self):
#         print("Hi")
        
# class Cat(Dog):
#     def C(self):
#         print("Hello")
        
# A=Cat()
# A.C()
# A.D()

# SINGLE LEVEL INHERITANCE
#  class animal():
#     def __init__(self):
#         print("I am from animal")
# class dog(animal):
#     def A(self):
#         print("I am from Dog")
        
# D=dog()
# D.A()

# # Python program to demonstrate
# # multiple inheritance

# # Base class1
# class Mother:
# 	mothername = ""

# 	def mother(self):
# 		print(self.mothername)

# # Base class2


# class Father:
# 	fathername = ""

# 	def father(self):
# 		print(self.fathername)

# # Derived class


# class Son(Mother, Father):
# 	def parents(self):
# 		print("Father :", self.fathername)
# 		print("Mother :", self.mothername)


# # Driver's code
# s1 = Son()
# s1.fathername = "RAM"
# s1.mothername = "SITA"
# s1.parents()
