
# Lesson: The not Operator
# The not operator reverses a Boolean value.
# The not in operator checks whether a value is absent from a collection.

# Example 1: Checking login status
logged_in = False

if not logged_in:
    print("Please log in.")

# Example 2: Checking ticket availability
sold_out = ["Tuesday", "Saturday"]
day = "Wednesday"

if day not in sold_out:
    print("Tickets are available!")
