from abc import ABC, abstractmethod

class abc(ABC):
    @abstractmethod
    def p(self):
        pass
        
class ab(abc):
    def p(self):
        print("hey")

# c=abc()
d=ab()
d.p()