class TeaException(Exception):
    def __init__(self, args):
        self.msg = args

class Tea():
    def __init__(self, temp):
        self.__temp = temp
    
    def tea_state(self):
        if self.__temp > 80:
            raise TeaException("Tea is Too Hot")
        elif self.__temp < 50:
            raise TeaException("Tea is Too Cold")
        else:
            return ("Tea is Good. Please have it.")            

tea = Tea(40)
print(tea.tea_state())