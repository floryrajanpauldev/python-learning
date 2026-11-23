from pathlib import Path
import csv

students = []
with open(Path(__file__).with_name("names-dict.csv")) as file:
    reader = csv.DictReader(file, skipinitialspace=True)
    for row in reader:
            student = {"name": row["name"], "address": row["address"]}
            students.append(student)

#DictReader reads the CSV file and returns each row as a dictionary, allowing us to access the values by their column names. This makes the code more readable and less error-prone, especially if the order of columns changes in the CSV file.
for student in sorted(students, key=lambda student: student["name"]): 
    print(f"Hello, {student['name']}! Your address is {student['address']}.")