class Name:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name
    ...

class Student(Name):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    ...


class Professor(Name):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    ...
name = Name("Jaz")
student = Student("Harry", "20")
professor = Professor("Severus", "Science")