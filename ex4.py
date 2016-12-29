cars = 100 #integer
space_in_a_car = 4.0 #floating point
drivers = 30 #integer
passengers = 90 #integer
cars_not_driven = cars - drivers #integer
cars_driven = drivers #integer
carpool_capacity = cars_driven * space_in_a_car #floating point
average_passengers_per_car = passengers / cars_driven #integer

print "There are", cars, "cars available." #There are 100 cars available."
print "There are only", drivers, "drivers available." #There are only 30 drivers available.
print "There will be", cars_not_driven, "empty cars today." #There will be 70 empty cars today.
print "We can transport", carpool_capacity, "people today." #We can transport 120.0 people today.
print "We have", passengers, "to carpool today." #We have 90 to carpool today
print "We need to put about", average_passengers_per_car, "in each car." #We need to put about 3 in each car."

#LPTHW Exercise answer: Line 7 defines the variable "carpool_capacity". On line 8, the author performed operations on an unknown variable "car_pool_capacity"

#LPTHW Extra Credit:
# 1 Using 4.0 caused the floating point to be carried over to the "carpool_capacity" variable. That is why the ".0" is included on the output for line 13.
# 2 A floating point number is a non-integer variable
# 3 Comments on each variable type
# 4 The initial '=' can be considered part of the assignment statement. Comparing two values would require the use of '==' for a boolean return
# 5 _ is an underscore character
# 6 In shell: test = 1; test2 = 2; added = test1 + test2; print added