#import math

from math import remainder, lcm
#from mool_modules import car
import mool_modules.car as car_details

def num_remainder(x, y):
    z = remainder(x, y)
    a = lcm(x, y)
    print (f"Remainder is : {z}")
    print (f"LCM is : {a}")

b = car_details.info('Maruti', 'Alto')
print(b)

num_remainder(8, 2)

