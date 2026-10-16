# Importing Modules

#

# Python has many built-in functions that are

# available automatically, such as:

#

# print()

# list()

# sorted()

#

# Python also has many modules containing

# pre-written Python code that we can import

# and use in our own programs.

#

# A module is a file containing Python code

# that we can import and use.

#

# We use the `import` keyword to import a module.

# ----------------------------------------

# 1. Import the random module

# ----------------------------------------

import random

# ----------------------------------------

# 2. random.choice()

# ----------------------------------------

#

# choice() randomly picks ONE item from a list.

lunch_spots = ["Thai Palace", "Burrito Bar", "Noodle House"]

print(random.choice(lunch_spots))

# ----------------------------------------

# 3. random.shuffle()

# ----------------------------------------

#

# shuffle() takes a list and rearranges

# the items into a random order.

#

# Every time you run it, the order can change.

#

# IMPORTANT:

# shuffle() changes the ORIGINAL list directly.

# It does not create a new list for us.

random.shuffle(lunch_spots)

print(lunch_spots)

# ----------------------------------------

# 4. shuffle() changes the original list

# ----------------------------------------

random.shuffle(lunch_spots)

# The list is now in a new random order.

print(lunch_spots)

# ----------------------------------------

# 5. shuffle() and sorted()

# ----------------------------------------

#

# sorted() arranges the list in sorted order.

#

# sorted() returns a NEW sorted list.

# It does NOT change the original list.

print(sorted(lunch_spots))

# The original list is still shuffled.

print(lunch_spots)

# ========================================

# Challenge: Turn Order

# ========================================

#

# You're building a feature for a board game

# app that sets up each match.

#

# At the start of a game, you need to:

#

# 1. Shuffle the players into a random turn

# order, then print the list.

#

# 2. Randomly choose one player to be the

# dealer and print:

#

# <name> deals first

players = ["Mara", "Devon", "Priya", "Leo"]

random.shuffle(players)

print(players)

card_dealer = random.choice(players)

print(f"{card_dealer} deals first")

# ----------------------------------------

# 6. Important difference

# ----------------------------------------

#

# random.choice(list)

# -> randomly selects ONE item

#

# random.shuffle(list)

# -> randomly rearranges the entire list

# -> changes the original list directly

#

# sorted(list)

# -> returns a NEW sorted list

# -> does not change the original list

# ========================================

# 🎮 Jargon Jumble Connection

# ========================================

#

# To scramble a word, we will eventually:

#

# 1. Start with a word

# 2. Break it into individual letters

# 3. Shuffle the letters

# 4. Join the letters back into a string

#

# Example:

#

# word = "deploy"

#

# letters = list(word)

#

# ['d', 'e', 'p', 'l', 'o', 'y']

#

# random.shuffle(letters)

#

# Possible result:

#

# ['o', 'y', 'p', 'd', 'e', 'l']

#

# Later, we will join those letters back

# together to create:

#

# "oypdel"

#

# This will become the scrambled word

# shown to the player in Jargon Jumble.

# ----------------------------------------

# Key Takeaways

# ----------------------------------------

#

# import random

# -> imports the random module

#

# random.choice(my_list)

# -> randomly selects one item

#

# random.shuffle(my_list)

# -> randomly rearranges the list

# -> changes the original list directly

#

# sorted(my_list)

# -> creates and returns a new sorted list

# -> leaves the original list unchanged
