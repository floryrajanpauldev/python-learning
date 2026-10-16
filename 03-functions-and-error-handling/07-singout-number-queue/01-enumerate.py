
# Lesson: Using enumerate()
# enumerate() lets us loop through a list and get both
# the index (position) and the item at that position.

contacts = ["Freda", "Homer", "Chance"]

for i, contact in enumerate(contacts):
    print(i, contact)


#output 
#0 Freda
#1 Homer
#2 Chance