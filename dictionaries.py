houses = {"Harry":"Griffindor", "Draco":"Slytherin"}
# dictionary houses is defined as above
# dictionaries can be used to map values to other values; so mapping values like user to info about them, people to houses they live in etc.
# then we can look up the key Harry to get the value Griffindor
print(houses["Harry"])

houses["Hermoine"] = "Griffindor"
# add values to the dictionary

print(houses["Hermoine"])

ages = {"Alice": 22, "Bob": 27}
# dictionary to keep track of ages of people.
# Dictionaries map keyes to values

ages ["Charlie"] = 30
# add name charlie to the dictionary and set the age
ages ["Alice"] += 1
# edit the age of Alice to be incremented by one
# the longer way to write: ages ["Alice"] = ages["Alice"] + 1
print(ages)
