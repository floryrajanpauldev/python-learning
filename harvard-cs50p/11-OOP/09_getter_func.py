#A property allows us to access a method like an instance variable.
class Student:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name #The underscore indicates that _name is intended for internal use. It is a Python naming convention, not strict privacy.


student = Student("John")

print(student.name)