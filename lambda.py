people = [
# define a people dictionary
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]

def f(person):
    return person["name"]

people.sort()
# people.sort() will give this error: TypeError: '<' not supported between instances of 'dict' and 'dict'
# that means python does not know how to sort these dictionaries be default
# 

print(people)
