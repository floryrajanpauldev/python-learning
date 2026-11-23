# Python – Special Methods and Properties

## 1. `__str__()`

- A special method that controls the string representation of an object.
- Automatically called when we use `print()` on an object.
- Should return a string.

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old."

student = Student("John", 20)
print(student)
```

Output:

```text
John is 20 years old.
```

## 2. `@property` – Getter

- A property allows us to access a method like an instance variable.
- A getter retrieves the value of an attribute.
- We use `@property` to define a getter.

```python
class Student:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

student = Student("John")
print(student.name)
```

Output:

```text
John
```

Notice that we use `student.name`, not `student.name()`.

## 3. `@name.setter` – Setter

- A setter allows us to update a property's value.
- We can validate the value before updating it.
- We use `@property_name.setter` to define a setter.

```python
class Student:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")

        self._age = value

student = Student(20)

print(student.age)

student.age = 21
print(student.age)
```

Output:

```text
20
21
```

If we assign a negative age, the setter raises a `ValueError`.

## 4. Getter vs Setter

| Getter | Setter |
|---|---|
| Retrieves a value | Updates a value |
| Uses `@property` | Uses `@property_name.setter` |
| `student.age` | `student.age = 21` |

**Remember:**
- `__str__()` controls how an object is displayed.
- `@property` is used to retrieve a value.
- `@property_name.setter` is used to update and validate a value.