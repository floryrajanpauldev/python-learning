# Python – Inheritance

## 1. What is Inheritance?

Inheritance allows one class to reuse the attributes and methods of another class.

Instead of writing the same code in multiple classes, we can create a common parent class and let other classes inherit from it.

### Problem: Duplicate code

Both `Student` and `Professor` classes have a common attribute called `name`.

Both classes also perform the same validation to check whether the name is empty.

```python
class Student:
    def __init__(self, name, age):
        if not name:
            raise ValueError("Missing name")

        self.name = name
        self.age = age


class Professor:
    def __init__(self, name, subject):
        if not name:
            raise ValueError("Missing name")

        self.name = name
        self.subject = subject
```

Notice that we are repeating the same validation and assignment for `name`.

**Solution: Inheritance**

We can move the common functionality into a parent class called `Name`.

## 2. Parent Class

A parent class is also called a base class or superclass.

It contains common attributes and methods that other classes can inherit.

```python
class Name:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")

        self.name = name
```

Here:
- `Name` is the parent class.
- It accepts a name.
- It checks whether the name is empty.
- It stores the name using `self.name`.

## 3. Child Classes

A child class is also called a derived class or subclass.

A child class inherits from its parent class.

We specify the parent class inside parentheses.

### Student class

```python
class Student(Name):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
```

### Professor class

```python
class Professor(Name):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
```

Here:
- `Student(Name)` means Student inherits from Name.
- `Professor(Name)` means Professor inherits from Name.
- Both child classes inherit the `name` attribute and its validation from the parent class.

## 4. What is `super()`?

`super()` allows a child class to call methods from its parent class.

For example:

```python
super().__init__(name)
```

This calls the `__init__()` method of the parent class (`Name`).

It passes the name to the parent class, where the name is validated and assigned to `self.name`.

We don't need to repeat the validation in Student and Professor.

## 5. Complete Example

```python
class Name:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")

        self.name = name


class Student(Name):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age


class Professor(Name):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject


name = Name("Jaz")
student = Student("Harry", "20")
professor = Professor("Severus", "Science")
```

## 6. Benefits of Inheritance

- **Code reusability:** We can reuse common code from the parent class.
- **Avoid duplication:** We don't need to repeat the same validation in multiple classes.
- **Maintainability:** If we need to change the name validation, we only need to update the parent class.
- **Extensibility:** Child classes can have their own additional attributes and methods.

## 7. Important Terms

| Term | Meaning |
|---|---|
| Parent class | The class whose attributes and methods are inherited |
| Child class | The class that inherits from another class |
| Inheritance | Reusing functionality from another class |
| `super()` | Used to access parent class methods |
| `super().__init__(name)` | Calls the parent class constructor |

**Remember:** Inheritance helps us avoid duplicate code by placing common functionality in a parent class and allowing child classes to reuse it.