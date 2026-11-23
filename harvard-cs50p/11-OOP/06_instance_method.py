class Student:
    def __init__(self, name):
        self.name = name

    def introduce(self): #instance method with self as first parameter
        print(f"My name is {self.name}")

student = Student("John")
student.introduce()