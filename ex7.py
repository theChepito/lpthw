# define the number of total cars
cars = 100

# quantify the space in each car
space_in_a_car = 4.0

# quantify the number of drivers
drivers = 30

# quantify the number of passengers
passengers = 90

# calculate the number of cars not being driven
cars_not_driven = cars - drivers

# quantify the number of cars as equal to # of drivers
cars_driven = drivers

# calculate the number of available spots for passengers
carpool_capacity = cars_driven * space_in_a_car

# calculate the average pax per car
average_passengers_per_car = passengers / cars_driven


# print statements to summarize the results of carpool analysis
print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
