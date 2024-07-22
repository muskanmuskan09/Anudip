class abc:
    def __init__(self):
        self.__privatevar=45
    def __pmethod(self):
        print("private hello")

ob=abc()
print(ob._abc__privatevar)
ob._abc__pmethod()