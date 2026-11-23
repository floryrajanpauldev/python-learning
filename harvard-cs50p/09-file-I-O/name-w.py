name = input("What is your name? ")

file = open("name-w.txt", "w")
file.write(name)
file.close()

""" running name.py will create a file called name.txt and write the name entered by the user into that file.
The file is opened in write mode ("w"), which means that if the file already exists, its contents will be overwritten. 
After writing the name to the file, the file is closed to ensure that all data is properly saved and resources are released.

"""