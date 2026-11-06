from pathlib import Path

names = []  # Initialize an empty list to store names
with open(Path(__file__).with_name("name-a.txt"), "r") as file:
    for line in file:
        names.append(line.strip())  # Read each line from the file, strip whitespace, and add to the list   

print("\n\n**** Sorting in ascending order ****")  # Print a blank line for better readability
for name in sorted(names):  # Sort the names alphabetically and iterate over them
    print(f"Hello names list, {name}!")  # Print a greeting for each name in the list

print("\n\n**** Sorting in reverse order ****")  # Print a blank line for better readability
for name in sorted(names, reverse=True):  # Sort the names alphabetically in reverse order and iterate over them
    print(f"Hello names list, {name}!")  # Print a greeting for each name in the list

