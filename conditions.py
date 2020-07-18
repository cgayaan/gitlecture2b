n = int(input("Number: "))
# input by default will return a string, so n = input("Number: ") wont work
# we need to use int function and have the input inside it
if n > 0:
    print("n is positive")
# python requires indentation to say its inside the if statement block
elif n < 0:
    print("n is negative")
# python uses elif instead of saying elseif
else:
    print("n is zero")
