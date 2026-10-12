# Challenge: Returning functions 
# For each function, save the result to a variable, then use the result to print an f string.

# 1. Write room_area(length, width) that returns the area of a room. Get the area of a
#    12 by 10 room.
#    Example output:
#    The room is 120 square feet.

def room_area(length, width):
    return length * width

room = room_area(12, 10)
print(f"The room is {room} square feet.")

# 2. Write add_tax(price) that returns a price with 8% tax added (multiply by 1.08). Get
#    the total for a $50 item.
#    Example output:
#    With tax, that comes to $54.0.

def add_tax(price): 
    return price * 1.08

taxed_price = add_tax(50)
print(f"With tax, that comes to ${taxed_price}")

# 3. Write full_name(first, last) that returns a first and last name joined with a space.
#    Use it to build a name, then print a greeting with it.
#    Example output:
#    Welcome, Mike Reed!

def full_name(first, last):
    return first + ' ' + last

name = full_name("John", "Smith")
print(f"Welcome, {name}!")