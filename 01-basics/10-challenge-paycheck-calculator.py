
# Challenge: Paycheck Calculator
#
# Build a simple paycheck calculator.
#
# 1. Instead of hard-coded values, prompt the user
#    for their hourly rate and hours worked.
#
# 2. Convert hourly_rate to a float and
#    hours_worked to an integer.
#
# 3. Type check both variables.
#
# 4. Multiply them together and print the total pay.


hourly_rate = float(input("What is your hourly rate? "))

hours_worked = int(input("How many hours did you work? "))


# Type check both variables.

print(type(hourly_rate))

print(type(hours_worked))


# Calculate total pay.

total_pay = hourly_rate * hours_worked

print(total_pay)
