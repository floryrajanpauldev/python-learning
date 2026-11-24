 #Creating a Set

names = {"Harry", "Hermione", "Ron", "Harry"}

print(names)

#Output (the order may vary):  {'Harry', 'Hermione', 'Ron'}

namesNew = set() # empty set
namesNew = {"Harry", "Hermione"}
namesNew.add("Ron") #Adding Elements
namesNew.add("Harry")
print(namesNew)


namesNew.remove("Ron") # removing elements
print(namesNew)


namesLen = {"Harry", "Hermione", "Ron", "Harry"}
print(len(namesLen))  # 3


namesList = ["Harry", "Ron", "Hermione", "Harry", "Ron"]
unique_names = set(names)
print(unique_names)


students = [
    {"name": "Harry", "age": 20, "city": "London"},
    {"name": "Hermione", "age": 21, "city": "London"},
    {"name": "Ron", "age": 20, "city": "Manchester"},
    {"name": "Draco", "age": 21, "city": "London"},
    {"name": "Neville", "age": 20, "city": "Manchester"}
]

cities = set()

for student in students:
    cities.add(student["city"])

print(cities) #{'London', 'Manchester'}
