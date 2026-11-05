
# ==========================================
# PYTHON PRINT() FUNCTION
# ==========================================
# print() displays output on the screen.
#
# Syntax:
# print(value1, value2, ..., sep=" ", end="\n")
#
# sep = Separator between multiple values.
# end = What to print at the end.
# By default, sep is a space and end is a newline.


# ------------------------------------------
# 1. BASIC PRINT
# ------------------------------------------
# Prints text on the screen.

print("Hello Python!")

# Output:
# Hello Python!


# ------------------------------------------
# 2. PRINT MULTIPLE VALUES
# ------------------------------------------
# Multiple values are separated by a space
# by default.

print("Hello", "Python", "World")

# Output:
# Hello Python World


# ------------------------------------------
# 3. SEP - SEPARATOR
# ------------------------------------------
# sep determines what goes BETWEEN values.
# Default value is a space (" ").

print("Hello", "Python", "World", sep="-")

# Output:
# Hello-Python-World

print("2026", "11", "03", sep="/")

# Output:
# 2026/11/03

print("React", "TypeScript", "Python", sep=" | ")

# Output:
# React | TypeScript | Python


# ------------------------------------------
# 4. END - ENDING CHARACTER
# ------------------------------------------
# end determines what is printed AFTER the values.
# Default value is a newline ("\n").

print("Hello")
print("Python")

# Output:
# Hello
# Python

# Change end to a space instead of a newline.

print("Hello", end=" ")
print("Python")

# Output:
# Hello Python

# Change end to three dots.

print("Loading", end="...")
print("Done!")

# Output:
# Loading...Done!


# ------------------------------------------
# 5. USING SEP AND END TOGETHER
# ------------------------------------------
# You can use both parameters in one print().

print("Python", "Java", "TypeScript",
      sep=" | ", end=" ---> ")

print("Programming Languages")

# Output:
# Python | Java | TypeScript ---> Programming Languages


# ------------------------------------------
# 6. PRINT VARIABLES
# ------------------------------------------
# print() can display variables and text together.

name = "Lori"
age = 30

print("Name:", name)
print("Age:", age)

# Output:
# Name: Lori
# Age: 30


# ------------------------------------------
# 7. F-STRINGS (FORMATTED STRINGS)
# ------------------------------------------
# f-strings allow variables inside strings.
# Put f before the opening quotation mark.

name = "Lori"
language = "Python"

print(f"My name is {name}.")
print(f"I am learning {language}.")

# Output:
# My name is Lori.
# I am learning Python.


# ------------------------------------------
# 8. PRINT NUMBERS AND CALCULATIONS
# ------------------------------------------

print(10 + 5)
print("Total:", 10 + 5)

# Output:
# 15
# Total: 15


# ------------------------------------------
# 9. PRINT SPECIAL CHARACTERS
# ------------------------------------------
# \n creates a new line.
# \t creates a tab space.

print("Hello\nPython")

# Output:
# Hello
# Python

print("Name:\tLori")

# Output:
# Name:   Lori


# ==========================================
# QUICK REFERENCE
# ==========================================
#
# print("Hello")
# Displays text.
#
# print("Hello", "Python")
# Separates values with a space by default.
#
# print("Hello", "Python", sep="-")
# Uses a hyphen between values.
#
# print("Hello", end=" ")
# Ends with a space instead of a newline.
#
# print("Hello", end="!")
# Ends with an exclamation mark.
#
# print("Hello", "Python", sep="-", end="!")
# Uses both sep and end.
#
# print(f"Hello {name}")
# Inserts a variable into a string.
#
# print("Hello\nPython")
# Prints on two lines.
#
# print("Name:\tLori")
# Adds a tab space.
#
# ==========================================
# END OF PRINT() EXAMPLES
# ==========================================
