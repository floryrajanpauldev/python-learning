# Challenge: Discount Code

#

# Build a promo code checker for an online shop.

# The shopper enters a promo code and the program

# checks whether it matches the flash sale code.

promo_code = "FLASH50"

user_code = input("Enter your promo code: ")

# Check whether the user's code is equal to the promo code.

is_equal = user_code == promo_code

print(f"The user entered code is equal to the promo code - {is_equal}")

# Check whether the user's code is NOT equal to the promo code.

is_not_equal = user_code != promo_code

print(f"The user entered code is not equal to the promo code - {is_not_equal}")

# Try entering:

#

# FLASH50

#

# Output:

# The user entered code is equal to the promo code - True

# The user entered code is not equal to the promo code - False

#

#

# Now try:

#

# flash50

#

# Output:

# The user entered code is equal to the promo code - False

# The user entered code is not equal to the promo code - True

#

# This happens because Python string comparisons

# are case-sensitive.

