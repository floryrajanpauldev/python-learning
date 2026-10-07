
# Basic arithmetic operators

print(20 + 10)
print(20 - 10)
print(20 / 10)
print(20 * 10)


# Using variables with arithmetic

current_ties = 15
new_ties = 3

total_ties = current_ties + new_ties
print(total_ties)

total_cost = 5 * new_ties
print(total_cost)

remaining_ties = total_ties - 10
print(remaining_ties)

ties_per_friend = remaining_ties / 4
print(ties_per_friend)


# Calculations inside f-strings

print(f"I have {current_ties + new_ties} ties in my collection.")


# Challenge: Remaining songs
#
# You have 200 songs in your collection.
# You delete 47 songs.
# How many songs are remaining?

total_songs = 200
deleted_songs = 47

remaining_songs = total_songs - deleted_songs

print(remaining_songs)


# Challenge: Movie tickets
#
# A movie ticket costs $12.
# You are buying tickets for yourself and two friends.
# How much will the tickets cost altogether?

movie_ticket_cost = 12
num_of_tickets = 3

total_tickets = movie_ticket_cost * num_of_tickets

print(total_tickets)


# Challenge: Stickers
#
# You have 48 stickers.
# You want to divide them equally among 6 friends.
# How many stickers will each friend receive?

stickers = 48
friends = 6

stickers_per_friend = stickers / friends

print(stickers_per_friend)

