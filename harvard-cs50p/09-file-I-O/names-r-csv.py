from pathlib import Path

with open(Path(__file__).with_name("names-a-csv.csv"), "r") as file:
    for line in file:
       name, address = line.rstrip().split(",")
       print(f"Hello, {name}! Your address is {address}.")

