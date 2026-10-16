
# Challenge: Excuse Generator
#
# Create an excuse generator that asks the user for:
# - A name
# - An event
# - A number
# - A plural noun
# - A verb
#
# Then use the user's answers to create and print
# a funny excuse using an f-string.


name = input("Who is the excuse for? ")
event = input("What's the event? ")
number = input("Enter a number: ")
noun = input("Enter a plural noun: ")
verb = input("Enter a verb: ")

excuse = f"Sorry {name}, I can't go to {event} — I have {number} {noun} to {verb} and honestly it's taking longer than expected."

print(excuse)
