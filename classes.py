class Point():
# remember a class is a template for a type of object
    def __init__(self, input1, input2):
        # __init__ is called a magic method
        # it will be called each time we try to create a Point object
        # the very first argument self represents the object Point we try to create

        self.x = input1
        # we say self.x to say store the x and y values inside of itself
        self.y = input2
        # the 2 input values are going to be stored inside self in properties x and y

p = Point(2,8)
# create object p of type Point
# the self argument will be provided automatically, we dont need to specifically state it

print(p.x)
print(p.y)
# we say to prin the x and y values inside the self of the Point object
