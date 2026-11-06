from pathlib import Path


#Sort by name and print the names and addresses in sorted order
students = []
with open(Path(__file__).with_name("names-a-csv.csv"), "r") as file:
     for line in file:
           name, address = line.rstrip().split(",")
           student = {"name": name, "address": address}
           students.append(student) 

#lamda is an anonymous function, which means it doesn't have a name.
#we did not have to create a get_name function to sort the students list by name, 
# we can use a lamda function instead, which is a more concise way to write a function that takes one argument and returns a value.
print("\n\n**** Sorting by name in ascending order ****")

for student in sorted(students, key=lambda student: student["name"]): 
    print(f"Hello, {student['name']}! Your address is {student['address']}.")


