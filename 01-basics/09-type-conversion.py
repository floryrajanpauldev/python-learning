
# Type Conversion
#
# Type conversion allows us to change a value
# from one type to another.
#
# int()   → converts a value to an integer
# float() → converts a value to a floating-point number
# str()   → converts a value to a string
#
# input() returns a string by default.


# Convert a string to a float.

cost = float("300")

print(type(cost))
print(cost)


# Convert user input to a float.

budget = float(input("What is your budget for the project? "))

print(budget)

print(type(budget))


# Convert user input to an integer.

budget = int(input("What is your budget for the project? "))

print(budget)

print(type(budget))


# Without type conversion, input() returns a string.

budget = input("What is your budget for the project? ")

print(budget)

print(type(budget))


# Convert the input to an integer when arithmetic is needed.

budget = int(input("What is your budget for the project? "))

print(budget + 100)
