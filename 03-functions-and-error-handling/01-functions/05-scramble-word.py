# 2. You've scrambled a word before: turn it into a list of letters, shuffle them, and
#    join them back together. Let's make that reusable. Write scramble(word) so it takes
#    any word and prints a scrambled version of it.
#    Example output:
#    scramble("python") might print nohtyp



import random

def scramble(word):
    letters = list(word)
    random.shuffle(letters)
    new_word = "".join(letters)
    print(new_word)

scramble("python")