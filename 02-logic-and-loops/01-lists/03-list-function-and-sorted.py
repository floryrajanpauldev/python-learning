# Python Lists — list() and sorted()

#

# Jargon Jumble will eventually need to:

#

# 1. Break a word into individual letters

# 2. Randomize/shuffle those letters

# 3. Join the letters back together

#

# The list() function helps us with step 1.

# ----------------------------------------

# 1. Accessing a character in a string

# ----------------------------------------

print("listen"[3])

# Output:

# t

# ----------------------------------------

# 2. Using list() with a string

# ----------------------------------------

#

# list() breaks a string into individual

# characters and creates a list.

letters = list("listen")

print(letters)

# Output:

# ['l', 'i', 's', 't', 'e', 'n']

# ----------------------------------------

# 3. sorted()

# ----------------------------------------

#

# sorted() arranges the items in a list

# in alphabetical order.

#

# Important:

# sorted() returns a new sorted list.

print(sorted(letters))

# Output:

# ['e', 'i', 'l', 'n', 's', 't']

# ========================================

# Anagrams

# ========================================

#

# Anagrams are words made from the exact

# same letters rearranged.

#

# Example:

#

# listen

# silent

#

# When we sort the letters of both words,

# the results should be identical.

first_word = list("listen")
second_word = list("silent")

print(sorted(first_word))
print(sorted(second_word))

# Output:

# ['e', 'i', 'l', 'n', 's', 't']

# ['e', 'i', 'l', 'n', 's', 't']

# ========================================

# Challenge: Anagram Check

# ========================================

#

# Anagrams are two words made from the exact

# same letters rearranged.

#

# For each pair:

# 1. Split both words into lists

# 2. Sort the lists

# 3. Print the results

#

# If the two sorted lists match, the words

# are anagrams.

# ----------------------------------------

# 1. earth and heart

# ----------------------------------------

earth = list("earth")
heart = list("heart")

print(sorted(earth))
print(sorted(heart))

# ----------------------------------------

# 2. below and elbow

# ----------------------------------------

below = list("below")
elbow = list("elbow")

print(sorted(below))
print(sorted(elbow))

# ----------------------------------------

# 3. night and tight

# ----------------------------------------

night = list("night")
tight = list("tight")

print(sorted(night))
print(sorted(tight))

# ----------------------------------------

# Key Takeaways

# ----------------------------------------

#

# list("word")

# -> breaks a string into individual characters

#

# sorted(my_list)

# -> returns a new list with items sorted

#

# These ideas are useful for:

# - working with individual characters

# - comparing words

# - solving anagram problems

# - preparing words to be scrambled

#

# Later, Jargon Jumble will use a similar

# process to scramble its words.
