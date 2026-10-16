
"""
Python Day 1 - f-Strings

f-Strings provide an easy way to insert variables
and expressions directly into a string.

The string starts with the letter 'f' before the
opening quote.
"""

name = "Lori"
language = "Python"

message = f"My name is {name} and I am learning {language}."

print(message)


# Expressions can also be placed inside an f-String.

age = 25

print(f"I am {age} years old.")


# Expressions can be evaluated inside { }

a = 10
b = 5

print(f"The sum of {a} and {b} is {a + b}.")


# f-Strings are especially useful when combining
# multiple variables into a message.

first_name = "Lori"
last_name = "Paul"

print(f"My full name is {first_name} {last_name}.")
