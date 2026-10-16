
# Lesson: Python Functions
# A function is a reusable block of code.

import random


# 1. Define a function to roll a dice
def roll_dice():
    roll = random.randint(1, 6)
    print(f"You rolled a {roll}!")


# 2. Call the function three times
roll_dice()
roll_dice()
roll_dice()


# 3. Call one function inside another function
def throw_twice():
    roll_dice()
    roll_dice()


throw_twice()


# 4. Display the welcome screen
def show_welcome():
    print()
    print("Welcome to Dice Fight!")
    print()


# 5. Organize the game using functions
def play_game():
    show_welcome()
    throw_twice()


play_game()
