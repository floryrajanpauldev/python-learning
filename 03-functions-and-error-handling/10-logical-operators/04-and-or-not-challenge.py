
# Challenge: Many Conditions
# Write one if statement for each situation, combining the values given with and, or, or not.

# 1. A houseplant only blooms if it got enough sun AND someone watered it. Print
#    "It bloomed!" when both are true.
got_enough_sun = True
was_watered = True
if got_enough_sun and was_watered:
    print("\nAnd-> It bloomed!\n")

# 2. You'll wear a ridiculous hat to the party if it's a costume party OR you don't know anyone there.
#    Print "Hat's going on." if either is true.
is_costume_party = False
knows_nobody = True
if is_costume_party or knows_nobody:
    print("\nOr-> Hat's going on.\n")

# 3. The cat lays across your keyboard on workdays, so it wins whenever it is NOT the
#    weekend. Print "Cat wins." when it isn't the weekend.
is_weekend = False

if not is_weekend:
    print("\nNot-> Cat wins.\n")