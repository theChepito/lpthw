cars = 100 # number of cars available
space_in_a_car = 4 # total seats in each car
drivers = 30 # total number of drivers in current day
passengers = 90 # total passengers riding in cars in current day
cars_not_driven = cars - drivers # total cars not in service
cars_driven = drivers # total cars in service
carpool_capacity = cars_driven * space_in_a_car # total seats in current day
average_passengers_per_car = passengers / cars_driven # average pax in each car

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
