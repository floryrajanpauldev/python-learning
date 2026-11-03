""" It is best to think of a dictionary as a set of key: value pairs, with the requirement that 
the keys are unique (within one dictionary). A pair of braces creates an empty dictionary: {}. 
Placing a comma-separated list of key:value pairs within the braces adds initial key:value pairs to the dictionary; 
this is also the way dictionaries are written on output."""

student = {"Health": "A", "Math": "B+", "History": "B", "English": "A+"}

for key in student:
    print(key, student[key])