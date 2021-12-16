from abc import ABC, abstractclassmethod

class Shape(ABC):
    
    @abstractclassmethod
    def area():
        pass
    
    @abstractclassmethod
    def perimeter():
        pass
    
class Square(Shape):
    
    def __init__(self, side):
        self.__side = side
    
    def area(self):
        return self.__side * self.__side
    
    def perimeter(self):
        return 4 * self.__side
    
#a = Shape()
b = Square(10)
print(b.area())
print(b.perimeter())
