# Lesson: Try and Except

number = int("42")
print(number)

try:
    number = int("banana")
except ValueError:
    print("Please enter a number.")
