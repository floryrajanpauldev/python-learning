class Student:
    def __init__(self, name, house):
        self.name = name
        self.age = house

    def __str__(self):
        return f"{self.name} is {self.age}"

    @classmethod
    def get(cls):
        name = input("Enter your name: ")
        age = input("Enter your age: ")
        return cls(name, age)


def main():
    student = Student.get()
    print(student)

if __name__ == "__main__":
    main()

"""
What happens here?
1. get() asks the user for their name.
2. It asks for their age.
3. cls refers to the Student class.
4. cls(name, age) creates a new Student object.
5. That object is returned. - It is equivalent to: return Student(name, age)
    
"""