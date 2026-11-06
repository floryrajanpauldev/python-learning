import csv
from operator import add

name = input("What's your name? ")
address = input("What's your address? ")

with open("names-dict-writer.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "address"])
    if file.tell() == 0:
        writer.writeheader()  # Write the header row if the file is empty   
    writer.writerow({"name":name, "address":address})  # Write the name and address as a new row in the CSV file     