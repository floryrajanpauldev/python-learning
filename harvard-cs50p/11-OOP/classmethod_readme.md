# Python – Class Methods (`@classmethod`)

## 1. Instance Variable

- An instance variable belongs to an individual object.
- Each object can have its own value.
- It is usually defined using `self` inside the `__init__()` method.

```python
class Student:
    def __init__(self, name):
        self.name = name

student1 = Student("John")
student2 = Student("Mary")

print(student1.name)  # John
print(student2.name)  # Mary
```

## 2. Instance Method

- An instance method belongs to an object.
- It takes `self` as its first parameter.
- `self` refers to the current object.
- It can access instance variables.

```python
class Student:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"My name is {self.name}")

student = Student("John")
student.introduce()
```

Output:

```text
My name is John
```

## 3. Class Method (`@classmethod`)

- A class method belongs to the class rather than an individual object.
- It uses the `@classmethod` decorator.
- It takes `cls` as its first parameter.
- `cls` refers to the class itself.
- It can access class variables and other class methods.

### Example using random.choice()

```python
import random

class Student:
    students = ["John", "Mary", "David", "Sarah"]

    @classmethod
    def pick_student(cls):
        return random.choice(cls.students)

print(Student.pick_student())
```

Possible output:

```text
David
```

### Explanation

- `@classmethod` defines a class method.
- `cls` refers to the `Student` class.
- `cls.students` accesses the class variable.
- `random.choice()` randomly selects one student from the list.
- We can call the class method directly using `Student.pick_student()` without creating an object.

## 4. Difference Between Instance Method and Class Method

| Feature | Instance Method | Class Method |
|---|---|---|
| First parameter | `self` | `cls` |
| Belongs to | Object | Class |
| Decorator | Not required | `@classmethod` |
| Accesses | Instance variables | Class variables |
| Called using | Object or class (with explicit instance argument) | Class or object |

**Remember:**
- `self` refers to an individual object.
- `cls` refers to the class itself.
- `@classmethod` is useful when a method needs to work with class-level data rather than individual object data.