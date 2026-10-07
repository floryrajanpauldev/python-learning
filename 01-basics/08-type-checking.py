
# Type Checking
#
# Python values have different types.
#
# Some basic types we have learned:
# - str   → string
# - int   → integer
# - float → decimal number
#
# Use type() to check the type of a value.


cost = 300

print(type(cost))
print(cost)


# A number inside quotes is a string.

service_charge = "30"

print(type(service_charge))
print(service_charge)


# input() returns a string by default.

budget = input("What is your budget for the project? ")

print(budget)

print(type(budget))


# Because budget is a string, it cannot be added
# directly to an integer.

# print(budget + 100)
