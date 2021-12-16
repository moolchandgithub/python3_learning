class Speed():
    def __init__(self) -> None:
        self.speed = 10
        self.__new_speed = 80
    
    def get_new_speed(self):
        return self.__new_speed
    
    def set_new_speed(self, newspeed):
        self.__new_speed = newspeed
        

car = Speed()
print(car.speed)
print(car.get_new_speed())
car.set_new_speed(100)
print(car.get_new_speed())