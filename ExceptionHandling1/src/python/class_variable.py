class MyClass:
    class_variable = "Hello, I'm a class variable!"

    def __init__(self):
        # You can access the class variable inside the instance methods.
        print(self.class_variable)

# Creating instances of MyClass
obj1 = MyClass()  # Output: Hello, I'm a class variable!
obj2 = MyClass()  # Output: Hello, I'm a class variable!