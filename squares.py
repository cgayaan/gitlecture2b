from functions import square
# import functions
# we can import just functions and the call functions.square

# from functions.py file import the square function

for i in range(10):
    print(f"The square of {i} is {square(i)}")
    #print(f"The square of {i} is {functions.square(i)}")
    # need to call functions.square if we only import functions
# run loop 10 times with a different sqaure value of i using the defined square function
