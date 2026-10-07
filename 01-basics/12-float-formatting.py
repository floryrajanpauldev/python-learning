
# Formatting Floats in f-Strings
#
# Use :.2f to display a float with exactly
# two digits after the decimal point.
#
# :
#     Starts the formatting instruction.
#
# .2
#     Displays exactly two decimal places.
#
# f
#     Formats the value as a floating-point number.


funds_remaining = 230.83838833333

print(
    f"This month, I have ${funds_remaining:.2f} "
    f"after I pay all of my bills."
)

