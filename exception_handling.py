a = input("Enter your first number: ")
b = input("Enter your second number: ")
 
try:
    result = int(a) / int(b)
    print(f"Result is : {result}")
except ValueError as e:
    print("Please Provide integar number.")
except ZeroDivisionError as e:
    print("Please provide postive number.")
