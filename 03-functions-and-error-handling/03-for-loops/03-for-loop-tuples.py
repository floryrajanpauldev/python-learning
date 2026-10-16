
# Lesson: Using For Loops with Tuples
# A for loop can process a list of tuples one tuple at a time.
# Tuple unpacking assigns each value to its own variable.

guests = [
    ("Marcus", "lasagna"),
    ("Lena", "salad"),
    ("Sarah", "brownies")
]

for guest in guests:
   # print(f"Guest has both name and dish : {guest}")
    name, dish = guest
    print(f"{name} is bringing {dish}")
