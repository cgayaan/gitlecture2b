import sys
# import the sys library to use the exit method

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
# this is to handle ValueError: invalid literal for int() with base 10, non numeric values
    print("Error: Invalid input")
    sys.exit(1)

try:
    result = x / y
except ZeroDivisionError:
# this is to handle ZeroDivisionError: division by zero
# if we divide a value by zero then we get the above exception
# we will handle this sxception and then print a message and exit
# to exit we use a method from the sys library in python called sys.exit
    print("Error: Cannot divide by 0.")
    sys.exit(1)
    # exit the program with a status code of 1
    # status code 1 means something went wrong

print(f"{x} / {y} = {result}")
