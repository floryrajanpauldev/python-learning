# Type Hints in Python

## What are Type Hints?

Type hints specify the expected data types of variables, function parameters, and return values.

They improve code readability, maintainability, and help IDEs identify potential type-related errors.

Python does not enforce type hints at runtime.

## 1. Variable Type Hints

Use `:` to specify the expected data type.

```python
name: str = "Flory"
age: int = 30
salary: float = 85000.50
is_active: bool = True
```

## 2. Function Parameter Type Hints

Specify the expected types of function parameters.

```python
def greet(name: str, age: int):
    print(f"Hello {name}, you are {age} years old.")

greet("Flory", 30)
```

## 3. Return Type Hints

Use `->` to specify the expected return type.

```python
def add(a: int, b: int) -> int:
    return a + b

result = add(10, 20)
print(result)
```

**Output:**
```text
30
```

For functions that do not return a value, use `None`.

```python
def display_message(message: str) -> None:
    print(message)
```

## 4. Type Hints with Multiple Types

Use the `|` operator when a value can have more than one type.

```python
def get_id(user_id: int | str) -> str:
    return str(user_id)
```

## 5. Type Hints with Collections

```python
names: list[str] = ["Smith", "John", "David"]

ages: list[int] = [25, 30, 35]

employee: dict[str, int] = {"age": 30}
```

## 6. Type Hints in Classes

Type hints can be used for class attributes, instance attributes, and methods.

```python
class Student:
    SCHOOL_NAME: str = "ABC School"

    def __init__(self, name: str, age: int):
        self.name: str = name
        self.age: int = age

    def display(self) -> None:
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"School: {Student.SCHOOL_NAME}")


student = Student("Flory", 25)
student.display()
```

## 7. Common Type Hints

| Type Hint | Description |
|---|---|
| `str` | String |
| `int` | Integer |
| `float` | Decimal number |
| `bool` | Boolean |
| `list[str]` | List of strings |
| `dict[str, int]` | Dictionary with string keys and integer values |
| `tuple[int, str]` | Tuple containing an integer and a string |
| `None` | No return value |

## Summary

- Type hints describe expected data types.
- Use `:` for variable and parameter annotations.
- Use `->` for function return types.
- Type hints improve readability and IDE support.
- Python does not enforce type hints at runtime.

**Reference:** [Python – typing module](https://docs.python.org/3/library/typing.html)