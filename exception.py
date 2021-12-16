"""
Exception Handling
"""
def car(carmake):
    car_dict = {'Make': 'Maruti', 'Model': '800', 'Year': 2001}

    try: 
        if carmake in car_dict:
#            print(f"{carmake}")
            print(f"Car model is {car_dict[carmake]}")
    except:
        print(f"Car is not in list")
        raise
    else:
        print(f"Car model ...")
    finally:
        print("This will always print")

car()