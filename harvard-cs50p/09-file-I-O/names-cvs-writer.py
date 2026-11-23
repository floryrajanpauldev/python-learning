import csv

name = input("What's your name? ")
address = input("What's your address? ")

with open("names-cvs-writer.csv", "a") as file:
    writer = csv.writer(file)
    if file.tell() == 0:
        writer.writerow(["name", "address"])
    writer.writerow([name, address])  # Write the name and address as a new row in the CSV file     