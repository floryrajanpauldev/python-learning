"""
We use __str__() when we want to control what gets displayed when we print an object.
print(student) automatically calls student.__str__().
Without __str__(), Python displays a default representation of the object, rather than a meaningful description.

"""
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old."


student = Student("John", 20)

print(student)