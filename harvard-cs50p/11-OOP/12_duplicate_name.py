class Student:
    def __init__(self, name, age):
        if not name:
            raise ValueError("Missing name")
        self.name = name
        self.age = age

    ...


class Professor:
    def __init__(self, name, subject):
        if not name:
            raise ValueError("Missing name")
        self.name = name
        self.subject = subject

    