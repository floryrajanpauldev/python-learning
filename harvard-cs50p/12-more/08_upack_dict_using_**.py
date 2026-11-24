#Use ** to unpack a dictionary into keyword arguments.

def display_employee(name, age, city):
    print(name, age, city)

employee = {
    "name": "Smith",
    "age": 35,
    "city": "Ohio"
}

display_employee(**employee)
"""
Output:

Smith 35 Ohio

"""