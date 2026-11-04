#https://docs.python.org/3/library/random.html
#random — Generate pseudo-random numbers¶

import random
#CHOICE - random.choice() will give you a random item from a list
coin = random.choice(["heads", "tails"]) # this will give you either heads or tails
print(coin) 

# we can use "from" keyword to import not just random.choice but all the functions in the random module. 
# This way we can use the functions without having to prefix them with "random."

from random import choice, random, shuffle, randint
print(random()) # this will give you a random float between 0 and 1
coin = choice(["heads", "tails"])
print(coin)

#SHUFFLE - random.shuffle() will shuffle the items in a list
items = [1, 2, 3, 4, 5]
shuffle(items) # this will shuffle the items in the list
for item in items:
    print(item) # this will print the items in the list in a random order   
print("Shuffle", items)


# RANDINT - random.randint(a, b) will give you a random integer between a and b (inclusive)
print(randint(1, 10)) # this will give you a random integer between 1 and 10