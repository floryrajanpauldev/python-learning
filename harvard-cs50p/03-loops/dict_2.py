students = [
    {"name": "Lori", "age": 30, "major": "Computer Science"},
    {"name": "John", "age": 25, "major": "Mathematics"},
    {"name": "Alice", "age": 28, "major": "Physics "}
]

for student in students:
    print(f"{student['name']}, is of age {student['age']}, and her major is in {student['major']}")