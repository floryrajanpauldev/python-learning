# Equality Operators

#

# Equality operators compare two values and

# return a Boolean value: True or False.

# ----------------------------------------

# 1. Equal to ==

# ----------------------------------------

#

# The double equal sign `==` is used to

# compare two values.

print("apple" == "apple")

# Output:

# True

print("apple" == "orange")

# Output:

# False

# ----------------------------------------

# 2. Boolean values

# ----------------------------------------

#

# True and False are Boolean values in Python.

#

# Notice that they start with a capital letter:

#

# True

# False

#

# Python treats lowercase `true` and `false`

# as variable names, so they will cause an error

# if they have not been defined.

# ----------------------------------------

# 3. Equality is case-sensitive

# ----------------------------------------

print("apple" == "Apple")

# Output:

# False

#

# "apple" and "Apple" are different strings.

# ----------------------------------------

# 4. Not equal to !=

# ----------------------------------------

#

# The `!=` operator checks whether two values

# are different.

print("cat" != "dog")

# Output:

# True

# ----------------------------------------

# 5. Working with numbers

# ----------------------------------------

print(5 == 5)

# Output:

# True

print(5 != 5)

# Output:

# False

# ========================================

# Example: Password Check

# ========================================

#

# We can store a password and compare it

# with the password entered by the user.

password = "SECRET"

user_password = input("Enter your password: ")

print(password == user_password)

print(password != user_password)

# Example:

#

# Enter your password: PASSWORD

#

# False

# True

#

# The entered password "PASSWORD" does not

# match "SECRET".

#

# Therefore:

#

# password == user_password

# -> False

#

# password != user_password

# -> True

# ----------------------------------------

# Key Takeaways

# ----------------------------------------

#

# ==  -> equal to

# !=  -> not equal to

#

# Both operators return a Boolean value:

#

# True

# False

#

# String comparisons are case-sensitive.

#

# "apple" == "Apple"

# -> False

#

# Python Boolean values use capital letters:

#

# True

# False
