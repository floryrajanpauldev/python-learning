name = input("What's your name? ")

with open("name-with.txt", "w") as file:
    file.write(name)    

# 'with' automatically closes the file after the block of code is executed, even if an error occurs.
#  This is a best practice for file handling in Python.
