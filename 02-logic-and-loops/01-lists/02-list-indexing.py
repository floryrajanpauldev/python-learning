# Python Lists — Accessing Individual Values

#

# Each item in a list has an index (position).

# Python uses ZERO-based indexing:

#

# First item  -> index 0

# Second item -> index 1

# Third item  -> index 2

# ----------------------------------------

# 1. Accessing items using positive indexes

# ----------------------------------------

playlist = ["Bohemian Rhapsody", "Hey Jude", "Dancing Queen"]

print(playlist[0])  # First item
print(playlist[1])  # Second item
print(playlist[2])  # Third item

# ----------------------------------------

# 2. Accessing items using negative indexes

# ----------------------------------------

#

# Negative indexes let us work backward

# through the list.

#

# -1 -> Last item

# -2 -> Second-to-last item

# -3 -> Third-to-last item

print(playlist[-1])  # Last item
print(playlist[-2])  # Second-to-last item
print(playlist[-3])  # Third-to-last item

# ----------------------------------------

# 3. Index that does not exist

# ----------------------------------------

#

# playlist has indexes 0, 1, and 2.

# Trying to access index 10 will cause:

#

# IndexError: list index out of range

#

# print(playlist[10])

# ----------------------------------------

# 4. Using a list value with an f-string

# ----------------------------------------

top_song = playlist[0]

print(f"Now playing: {top_song}")

# ========================================

# Challenge: Build a Support Queue

# ========================================

#

# You're building a help desk feature that

# shows who's waiting in line for support.

#

# Use indexing to create a status display:

#

# Now helping: Ada

# Next in line: Grace

# Just added: Alan

#

# "Now helping" is the first person in line.

# "Next in line" is the second person.

# "Just added" is the last person.

tickets = ["Ada", "Grace", "Linus", "Margaret", "Alan"]

now_helping = tickets[0]

next_in_line = tickets[1]

just_added = tickets[-1]

print(f"Now helping: {now_helping}")
print(f"Next in line: {next_in_line}")
print(f"Just added: {just_added}")

# ----------------------------------------

# Key Takeaways

# ----------------------------------------

#

# Indexes start at 0.

#

# list[0]  -> first item

# list[1]  -> second item

# list[-1] -> last item

# list[-2] -> second-to-last item

#

# Trying to access an index that does not exist produces an IndexError.
