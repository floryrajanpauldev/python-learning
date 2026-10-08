# Challenge: Comparison Checks

#

# Apps often compare numbers to decide what to show a user.

# Use comparison operators inside f-strings to print

# a labeled result for each check.

unread_messages = 0

age = 25

cart_total = 45

tickets_left = 8

# Check whether there are more than 0 unread messages.

print(f"Has unread messages (more than 0): {unread_messages > 0}")

# Check whether the user is 25 or older.

print(f"Old enough to rent a car (25 or older): {age >= 25}")

# Check whether the cart total is under $50.

print(f"Under the $50 free-shipping minimum: {cart_total < 50}")

# Check whether there are 0 or fewer tickets left.

print(f"Sold out (0 or fewer tickets left): {tickets_left <= 0}")

# Expected output:

#

# Has unread messages (more than 0): False

# Old enough to rent a car (25 or older): True

# Under the $50 free-shipping minimum: True

# Sold out (0 or fewer tickets left): False

#One thing worth noticing here: you're putting the comparison expression directly inside { }:
#{age >= 25}
#Python evaluates age >= 25 first → True, and then the f-string puts that result into the text.