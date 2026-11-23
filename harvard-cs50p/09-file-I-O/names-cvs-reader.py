from pathlib import Path
import csv

students = []
with open(Path(__file__).with_name("names-error.csv")) as file:
    reader = csv.reader(file)
    for row in reader:
            name, address = row
            student = {"name": name, "address": address}
            students.append(student)

for student in sorted(students, key=lambda student: student["name"]): 
    print(f"Hello, {student['name']}! Your address is {student['address']}.")