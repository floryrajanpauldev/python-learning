from pathlib import Path

with open(Path(__file__).with_name("name-a.txt"), "r") as file:
    lines = file.readlines()  # Read all lines from the file
for line in lines:
    print(f"Hello, {line.rstrip()}!")  # Print a greeting for each name in the file, removing any leading/trailing whitespace

print()  # Print a blank line for better readability
with open(Path(__file__).with_name("name-a.txt"), "r") as file:
    name = file.read().strip()  # Read the name from the file and remove any leading/trailing whitespace
print(f"Hello, {name}!")  # Print a greeting using the name read from the file

