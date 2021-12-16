def car():
    car_dict = {'Make': 'Maruti', 'Model': '800', 'Year': 2001}
    a = car_dict['xyz']
    return a

try: 
    car()
except:
    print("Not in Dictonary")
    raise
else:
    print(f"Car Make is {car()}")
finally:
    print("This will always print")
