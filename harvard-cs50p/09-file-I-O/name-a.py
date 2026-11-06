name = input("What is your name? ")

file = open("name-a.txt", "a") 
file.write(name + "\n")
file.close()

# 'a' will append to the file if it already exists, or create a new file if it doesn't exist
# '\n' is a newline character that will ensure each name is written on a new line in the file