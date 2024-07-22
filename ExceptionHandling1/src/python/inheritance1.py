# multiple inheritance

class animal():
    def __init__(self):
        print("I AM FROM ANIMAL")
class dog():
    def D(self):
        print("I am from Dog")
class cat(animal,dog):
    def C(self):
        print("I am from cat")

d=cat()
d.D()
d.C()


# single inheritance
# class animal():
#     def __init__(self):
#         print("i am from animal")
# class dog(animal):
#     def D(self):
#         print("i am from dog")

# a=dog()
# a.D()


