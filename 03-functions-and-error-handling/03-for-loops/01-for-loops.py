
# Lesson: For Loops
# A for loop runs a block of code once for every item in a list.

guests = ["Marcus", "Lena", "Sarah", "Priya"]

for guest in guests:
    print(f"Welcome, {guest}!")

print("That's everyone!")


#guests is the list containing four names.
#for guest in guests: loops through the list one item at a time.
#guest is the loop variable. It holds the current name during each iteration.
#The indented print() statement runs once for each guest.
#print("That's everyone!") is outside the loop, so it runs once after all four guests have been welcomed.