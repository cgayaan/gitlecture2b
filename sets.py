# Create an empty set
# A set is a collection where no item appears twice
s = set()

#Add elements to the set
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(3)

print(s)
# even though 3 is added twice, the output is always {1,2,3,4}
# no element can appear twice in a set - mathematical definition

s.remove(2)
#remove an element from a set

print(s)

print(f"The set as {len(s)} elements")
#calculate the length of the set called s
