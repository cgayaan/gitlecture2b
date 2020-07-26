# python decorators are a way to take a function and modify that function.
# a decorator takes a function as input and returns a modified version of that function as output
# this is possible because pyhton considers functions a just another value, this is called functional programmining paradigm
def announce(f):
# this announce function is going to take a function f as input
    def wrapper():
    # this function will take function f and wrap it up with some additional behavoir. Therefore thay are ususally called wrapper functions
        print("About to run the function...")
        # wrapper will print the above line
        f()
        # then actually run function f
        print("Done with the function")
        # then print something else
    return wrapper

@announce
# this adds the decorator to the hello world function
def hello():
    print("Hello, world!")

hello()
# we call hello and that will run the decorator as well
