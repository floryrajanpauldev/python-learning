# Jargon Jumble 🎮

# Challenge: Scramble a Word

#

# Steps:

# 1. Create a list of words.

# 2. Use random.choice() to pick a word.

# 3. Use list() to break the word into letters.

# 4. Use random.shuffle() to scramble the letters.

# 5. Use "".join() to turn the letters back

# into a string.

# 6. Print the scrambled word.

import random

# ----------------------------------------

# 1. Create a list of words

# ----------------------------------------

words = ["John", "Jani", "Janardhan"]

# ----------------------------------------

# 2. Pick a random word

# ----------------------------------------

pick_word = random.choice(words)

print(pick_word, "pick")

# ----------------------------------------

# 3. Break the word into individual letters

# ----------------------------------------

break_word = list(pick_word)

print(break_word, "break-word")

# ----------------------------------------

# 4. Shuffle the letters

# ----------------------------------------

#

# IMPORTANT:

# random.shuffle() changes the original list

# directly.

#

# It does NOT return the shuffled list.

#

# Therefore, we should NOT do:

#

# shuffle_word = random.shuffle(break_word)

#

# because shuffle_word would contain None.

#

# Instead, simply shuffle the original list.

random.shuffle(break_word)

print(break_word, "shuffle")

# ----------------------------------------

# 5. Join the letters back together

# ----------------------------------------

scramble_word = "".join(break_word)

print(scramble_word)
