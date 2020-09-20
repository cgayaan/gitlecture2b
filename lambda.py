people = [
# define a people List
# and inside the list we have 3 dictionaries
# python allows us to nest data structures inside other data structures
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]

def f(person):
# define a function that takes a person variable as input and then returns that persons name
    return person["name"]
    # this will help to sort persons by name
    # return person["house"] - can help to sort persons by their house
    # this function takes any variable passed and returns a dict object name
    # if we make it return person("name"), then we get error TypeError: 'dict' object is not callable
people.sort(key=f)
# people.sort() will give this error: TypeError: '<' not supported between instances of 'dict' and 'dict'
# that means python does not know how to sort these dictionaries by default
# so we need to tell the sort function how to sort these dictionaries by defining a function f defined above
# then we can sort by saying people.sort(key=f), i.e. by running the f function
# so we seem to be passing the people list to the function f as the person variable
# then function f will return the person variable (people list) name
# then the sort function will sort the people list+dictionary based on that returned name
people.sort(key=lambda person: person["name"])
# we can define the sort function like this as well
# a lambda is considered as a function
# so this lambda takes a person and returns a person's name
# person is the input of the function and person:["name"] is the output
# to get the above lambda to run, comment out the above f function and the people.sort(key=f)
print(people)
