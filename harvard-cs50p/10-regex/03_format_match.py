import re

name = input("What is your name? ").strip()

matches = re.search(r"^(.+),\s*(.+)$", name)

if matches:
    last = matches.group(1)
    first = matches.group(2)
    name = f"{first} {last}"

print(f"Hello, {name}")


#v2

import re

name = input("What is your name? ")

if matches := re.search(r"^(.+), *(.+)$", name):
    name = matches.group(2) + " " + matches.group(1)

print(f"hello, {name}")