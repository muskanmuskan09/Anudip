class animal():
    def __init__(self):
        print("Animal")

class dog(animal):
    def d(self):
        print("DOg")

class cat(animal):
    def c(self):
        print("cat")

class rat(animal):
    def r(self):
        print("Rat")

a=animal()
b=rat()
b.r()

