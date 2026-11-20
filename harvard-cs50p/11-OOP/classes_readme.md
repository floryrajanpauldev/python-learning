# Classes in Python

## 1. What is a Class?

A **class** is a blueprint or template used to create objects.

An object is an instance of a class.

For example, if we have a `Student` class, we can create multiple student objects with different names and ages.

## 2. Creating a Class

Use the `class` keyword to define a class.

```python
class Student:
    pass
```

Here:
- `class` is the keyword used to create a class.
- `Student` is the class name.
- `pass` means do nothing for now. It is used as a placeholder when the class has no implementation yet.

## 3. Creating Objects

We can create objects from a class.

```python
class Student:
    pass

student1 = Student()
student2 = Student()
```

Here:
- `student1` and `student2` are objects.
- Both objects are instances of the `Student` class.

## 4. The `__init__()` Method

The `__init__()` method is a special method that runs automatically when an object is created.

It is commonly used to initialize the object's attributes.

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Smith", 25)

print(student1.name)
print(student1.age)
```

**Output:**

```text
Smith
25
```

Explanation:

- `__init__()` initializes the object.
- `self` refers to the current object.
- `self.name` and `self.age` are instance attributes.
- `"Smith"` and `25` are passed as arguments when creating the object.

## 5. What is `self`?

`self` refers to the current instance (object) of the class.

It allows us to access the object's attributes and methods.

For example:

```python
class Student:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"My name is {self.name}")

student1 = Student("Smith")

student1.introduce()
```

**Output:**

```text
My name is Smith
```

Note: `self` is not a Python keyword, but it is the standard naming convention.

## 6. Methods in a Class

A method is a function defined inside a class.

Methods describe the actions or behaviors an object can perform.

```python
class Student:
    def __init__(self, name):
        self.name = name

    def study(self):
        print(f"{self.name} is studying")

student1 = Student("Smith")

student1.study()
```

**Output:**

```text
Smith is studying
```

## 7. Instance Attributes

Instance attributes belong to individual objects.

Each object can have its own values.

```python
class Student:
    def __init__(self, name):
        self.name = name

student1 = Student("Smith")
student2 = Student("John")

print(student1.name)
print(student2.name)
```

**Output:**

```text
Smith
John
```

Each student object has its own `name`.

## 8. Summary

| Concept | Meaning |
|---|---|
| Class | Blueprint for creating objects |
| Object | An instance of a class |
| `__init__()` | Initializes an object |
| `self` | Refers to the current object |
| Attribute | Data associated with an object |
| Method | Function defined inside a class |

## 9. Practice Exercise

Create a `Student` class with the following:

1. An `__init__()` method that accepts `name` and `course`.
2. Store both values using `self`.
3. Create a method called `display()` that prints the student's name and course.
4. Create two student objects with different values.
5. Call the `display()` method for both objects.