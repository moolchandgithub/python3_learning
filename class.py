class Fruit(object):
    def __init__(self) -> None:
        super().__init__()
#        print("This is Fruit class")
    
    def nutrition(self, fruitname):
        d = {'Apple': 40, 'Orange': 30, 'Bananna': 25, 'Pear': 15}
        if fruitname in d:
            return(f"{fruitname} have {d[fruitname]} nutrition.")
        else:
            return(f"Fruit {fruitname} is not in nutrition list.")
    
    def fruit_shape(self, fruitname):
        d = {'Apple': 'Round', 'Orange': 'Round', 'Bananna': 'Oval', 'Pear': 'Round'}
        if fruitname in d:
            return(f"{fruitname} shape is {d[fruitname]}.")
        else:
            return(f"Fruit {fruitname} is not in shape list.")

class Apple(Fruit):
    def __init__(self) -> None:
        super().__init__()
#        print("This is Apple Fruit class")
    
    def color(self, fruitname):
        d = {'Apple': 'Red', 'Orange': 'Yellow', 'Bananna': 'Yellow', 'Pear': 'Green'}
        if fruitname in d:
            return(f"{fruitname} color is {d[fruitname]}.")
        else:
            return(f"Fruit {fruitname} is not in color list.")

    def nutrition(self, fruitname):
        super().nutrition(fruitname)
        d = {'Kiwi': 50, 'Watermelon': 60}
        if fruitname in d:
            return(f"{fruitname} have {d[fruitname]} nutrition.")
        else:
            return(f"Fruit {fruitname} is not in nutrition list.")

print('*'*20)
a = Fruit().fruit_shape('Apple')
print(a)
print('*'*20)
b = Fruit().nutrition('Pear')
print(b)
print('*'*20)
c = Apple().nutrition('Watermelon')
print(c)
print('*'*20)
d = Apple().color('Pear')
print(d)
