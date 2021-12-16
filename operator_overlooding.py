class Books():
    
    def __init__(self, pages):
        self.__pages = pages
        
    def __add__(self, other):
        return self.__pages + other.__pages
    
class Python():
    
    def __init__(self, pages):
        self.pages = pages
    
    def __add__(self, other):
        return self.pages + other.pages
    
    def __gt__(self, other):
        return self.pages > other.pages
    
    def __sub__(self, other):
        return self.pages - other.pages
    
class Java():
    
    def __init__(self, pages):
        self.pages = pages
        
a = Books(100)
b = Books(150)

c = a + b
print (c)

d = "Name :" + " Moolchand"
print(d)

b1 = Python(300)
b2 = Java(237)

print (b1 + b2)
print (b1 > b2)
print (b1 - b2)
