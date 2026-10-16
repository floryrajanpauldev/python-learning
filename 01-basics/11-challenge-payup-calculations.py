
# Challenge: PayUp - Type Conversion and Calculate the Split
#
# Apply type conversion to the PayUp app.
#
# - Convert cost to a float.
# - Convert service_charge to an integer.
# - Convert group_size to an integer.
#
# Then calculate:
# - The total service charge.
# - The grand total.
# - The amount each person must pay.


event = input("What was the event or occasion? ")

cost = float(input("How much was it? "))

service_charge = int(
    input(
        "Was there a tip or a service charge? "
        "Enter a whole number (e.g. 20 for 20%): "
    )
)

group_size = int(input("How many people were in your group? "))


print(type(cost))
print(type(service_charge))
print(type(group_size))

# Calculate the service charge amount.
#
# The user enters a whole-number percentage,
# so divide by 100 to convert it to a decimal.

service_charge_total = cost * service_charge / 100


# Calculate the grand total.

grand_total = cost + service_charge_total


# Calculate the amount each person must pay.

total_per_person = grand_total / group_size


print("Welcome to PayUp!")

print()

print(f"Here's the breakdown for {event}:")

print()

print(f"Cost: ${cost}")

print(f"Service charges: ${service_charge_total}")

print(f"Group size: {group_size}")

print(f"Grand total: ${grand_total}")

print()

print(f"Each person must PayUp: ${total_per_person}")
