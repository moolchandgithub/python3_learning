## Author : Moolchand
## Triangle Shape class as part of assignment
from math import sqrt
from shapes.shape import Shape

class Triangle(Shape):
    
    decimal_places = 2
    
    def __init__(self, sd1, sd2, sd3):
        self.side1 = sd1
        self.side2 = sd2
        self.side3 = sd3
    
    def area(self):
        semiparam = (self.side1 + self.side2 + self.side3) * 1/2
        return round(sqrt(semiparam * (semiparam - self.side1)*(semiparam - self.side2)*(semiparam - self.side3)) , self.decimal_places)
    
    def perimeter(self):
        return self.side1 + self.side2 + self.side3
    
    def isIsosceles(self):
        if self.side1 == self.side2:
            return True
        elif self.side1 == self.side3:
            return True
        elif self.side2 == self.side3:
            return True
        else:
            return False
    
    def isEquilateral(self):
        if self.side1 == self.side2 == self.side3:
            return True
        else:
            return False
