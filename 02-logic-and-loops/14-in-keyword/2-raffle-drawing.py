# Challenge: Raffle Drawing
# Build a feature that manages a charity raffle. The program picks a random winner but
# makes sure nobody wins twice. If the random winner has already won a prize, keep 
# drawing a random winner until you land on someone new.
# 1. Draw a random name from entrants.
# 2. If that name is already in winners, keep drawing until you get one
#    that isn't.
# 3. Add the new winner to winners and print: "Winner: <name>"

entrants = ["Amara", "Diego", "Priya", "Leo", "Sofia", "Kwame"]
winners = ["Diego", "Sofia"]

import random

# Draw a random winner
pick_winner = random.choice(entrants)
print(f"Initial pick: {pick_winner}")


# Keep drawing until we get a new winner
while pick_winner in winners:
    pick_winner = random.choice(entrants)

# Add the new winner to the list and print the result
winners.append(pick_winner)
print(f"Winner: {pick_winner}")

print(f"All winners: {winners}")