# Challenge: BINGO!
# Use a while loop and the "in" keyword to avoid
# calling a Bingo number that was already called.

import random

bingo_numbers = [
    "B-7",
    "I-22",
    "N-33",
    "G-51",
    "O-68",
    "B-3",
    "I-19",
    "O-72",
]

already_called = ["B-7", "I-22", "G-51"]

# Check whether a number exists in the list.
print("B-7" in already_called)   # True
print("O-68" in already_called)  # False

# Pick a random Bingo number.
pick = random.choice(bingo_numbers)

# Keep picking while the number was already called.
while pick in already_called:
    pick = random.choice(bingo_numbers)

# Display and record the new number.
print(f"Next call: {pick}")

already_called.append(pick)

print(already_called)