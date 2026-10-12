
# Python String Methods
# String methods help us clean and format text.

# 1. upper() - converts all letters to uppercase
recipe = "chicken tikka masala"
header = recipe.upper()
print(header)

# 2. lower() - converts all letters to lowercase
search = "PASTA CARBONARA"
print(search.lower())

# 3. title() - capitalizes the first letter of each word
chef = "grace smith"
print(chef.title())

# 4. strip() - removes whitespace from both ends
recipe = "     tiramisu    "
print(recipe.strip())

# 5. strip('%') - removes the specified character from both ends
print("50%".strip('%'))

# 6. Method chaining - combines multiple string methods
raw = "    CHiCKen TIKKA MasALA"
query = raw.strip().lower()
print(query)

# 7. join() - combines strings using a separator
words = ["chicken", "tikka", "masala"]
recipe = "-".join(words)
print(recipe)
