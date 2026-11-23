from pathlib import Path


#Sort by name and print the names and addresses in sorted order
students = []
with open(Path(__file__).with_name("names-a-csv.csv"), "r") as file:
     for line in file:
           name, address = line.rstrip().split(",")
           student = {"name": name, "address": address}
           students.append(student) 
def get_name(student):
    return student["name"] 


print("\n\n**** Sorting by name in ascending order ****")
for student in sorted(students, key=get_name): 
    #here python allows to pass a function as an argument to another function, in this case we are passing the get_name function to the sorted function, which will use the return value of the get_name function to sort the students list
    print(f"Hello, {student['name']}! Your address is {student['address']}.")

def get_address(student):
    return student["address"] 

# we can also sort by address, by passing student["address"] instead of student["name"] in the return statement
print("\n\n**** Sorting by address in ascending order ****")
for student in sorted(students, key=get_address):
    print(f" {student['address']} - {student['name']}.")

print("\n\n**** Sorting by address in reverse order ****")
for student in sorted(students, key=get_address, reverse=True):
    print(f" {student['address']} - {student['name']}.")

