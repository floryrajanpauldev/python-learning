# Here we are trying to format user input - name

name = input("What is your name?  ").strip()

if ',' in name:
    lastname, firstname = name.split(", ?") # ? means it may or maynot have a space after the comma
    name = f"{firstname} {lastname}"

    print(f"hello, {name}")