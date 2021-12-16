class Polygon:
    __width = None
    __height = None
    
    def get_values(self, w, h):
        self.__width = w
        self.__height = h
    
    def set_width(self):
        return self.__width
    
    def set_heigth(self):
        return self.__height
    
class Square(Polygon):
    def area(self):
        return self.set_width() * self.set_heigth()
    
class Tringle(Polygon):
    def area(self):
        return self.set_heigth() * self.set_width() * 1/2

s1 = Square()
s1.get_values(5, 5)
print(s1.area())

t1 = Tringle()
t1.get_values(10, 5)
print(t1.area())