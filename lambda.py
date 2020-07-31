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
    # return person["house"] can help to sort persons by their house
people.sort(key=f)
# people.sort() will give this error: TypeError: '<' not supported between instances of 'dict' and 'dict'
# that means python does not know how to sort these dictionaries by default
# so we need to tell the sort function how to sort these dictionaries by defining a function f defined above
# then we can sort by saying people.sort(key=f), i.e. by running the f function

print(people)
