class Flight ():
    def __init__(self, capacity):
        self.capacity = capacity
        # we say self.capacity will store the capacity variable value
        self.passengers = []
        # we say self.passengers will store the list of passengers. The List is empty curently
    def add_passenger(self,name):
    # we define a new method under the Flight class to add passengers. Note the indentation.
        if not self.open_seats():
        # if there are no open seats. Its the same as if self.open_seats()==0:
            return False
            # return false if there are no open seats.
        self.passengers.append(name)
        # self.passengers has the empty passenger list. We append the value in name variable to that list.
        return True
        # retuen true if there are open seats.
    def open_seats(self):
    # we define a new method under Flight class to count open seats. It does not need arguments, so only self is there
        return self.capacity-len(self.passengers)
        # we subtract the length of the passengers list from the capacity value

flight = Flight(3)
# object flight of type Flight has a capacity of 3

people = ["Harry", "Ron", "Hermoine", "Ginny"]
for person in people:
    # loop over every person or x in that people list
    success = flight.add_passenger(person)
    # for each person do flight.add_passenger(person) and save the result (True/False) in the variable called success
    if success:
    # this one not sure...?
    # apparently it means if success = True
    # I think its because True is returned only if self.passengers.append(name) is run
    # also we can remove the line success = flight.add_passenger(person)
    # and we can just say if flight.add_passenger(person) to make the code optimized
        print(f"Added {person} to flight successfully.")
    else:
    # apparently this means if success = False
    # because False is returned only if not self.open_seats() is run
        print(f"No available seats for {person}.")
