# Python — join() Function

#

# The join() function takes the items in a list

# and joins them together into a single string.

#

# It is called `join()` because it joins list items

# using a separator.

#

# The separator goes BEFORE `.join()`.

# ----------------------------------------

# 1. Joining words with a comma and space

# ----------------------------------------

result = ", ".join(["peace", "love", "happiness"])

print(result)

# Output:

# peace, love, happiness

# ----------------------------------------

# 2. The separator can be anything

# ----------------------------------------

#

# We can use:

# - a comma

# - a dash

# - a space

# - a word

# - an emoji

# - an empty string

# - or any other string

print("-".join(["peace", "love", "happiness"]))

print(" ".join(["peace", "love", "happiness"]))

print(" ❤️ ".join(["peace", "love", "happiness"]))

print(" and ".join(["peace", "love", "happiness"]))

# ----------------------------------------

# 3. Joining with no separator

# ----------------------------------------

#

# An empty string "" means that nothing

# will be placed between the items.

#

# This is what we will need when we

# turn scrambled letters back into a word.

letters = ["p", "y", "t", "h", "o", "n"]

word = "".join(letters)

print(word)

# Output:

# python

# ========================================

# Challenge: Four Joiners

# ========================================

#

# 1. Join ["mysite.com", "products", "sale"]

# with "/" to build a URL path.

#

# 2. Join ["2026", "05", "29"] with "-"

# to format a date.

#

# 3. Join ["hip", "hip", "hooray"] with " "

# for the crowd.

#

# 4. Join `letters` into a single word

# with no separator.

# ----------------------------------------

# 1. Build a URL path

# ----------------------------------------

url_path = "/".join(["mysite.com", "products", "sale"])

print(url_path)

# Output:

# mysite.com/products/sale

# ----------------------------------------

# 2. Format a date

# ----------------------------------------

format_date = "-".join(["2026", "05", "29"])

print(format_date)

# Output:

# 2026-05-29

# ----------------------------------------

# 3. Create a crowd chant

# ----------------------------------------

crowd = " ".join(["hip", "hip", "hooray"])

print(crowd)

# Output:

# hip hip hooray

# ----------------------------------------

# 4. Join letters into a word

# ----------------------------------------

letters = ["p", "y", "t", "h", "o", "n"]

word = "".join(letters)

print(word)

# Output:

# python

# ----------------------------------------

# Key Takeaways

# ----------------------------------------

#

# separator.join(list)

#

# The separator determines what goes

# between each item.

#

# Examples:

#

# ", ".join(["a", "b", "c"])

# -> "a, b, c"

#

# "-".join(["a", "b", "c"])

# -> "a-b-c"

#

# " ".join(["a", "b", "c"])

# -> "a b c"

#

# "".join(["a", "b", "c"])

# -> "abc"

#

#

# IMPORTANT:

# join() creates a STRING from the list items.

#

# Jargon Jumble connection 🎮

#

# We will eventually:

#

# 1. Take a word

# 2. Break it into letters using list()

# 3. Shuffle the letters using random.shuffle()

# 4. Join the letters back together using join()

#

# Example:

#

# letters = ["d", "e", "p", "l", "o", "y"]

#

# random.shuffle(letters)

#

# scrambled_word = "".join(letters)

#

# This gives us the scrambled word

# that we can show to the player.
