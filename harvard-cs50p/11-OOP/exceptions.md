# Python – Exceptions

## 1. What are Exceptions?

An exception is an error that occurs while a Python program is running.

Exceptions can occur due to different reasons, such as:
- User entering an invalid value.
- Dividing a number by zero.
- Trying to open a file that does not exist.
- Trying to convert an invalid string into an integer.

Examples:

```python
x = int(input("Enter a number: "))
```

If the user enters `hello`, Python raises a `ValueError` because it cannot convert the string into an integer.

```python
x = 10 / 0
```

This raises a `ZeroDivisionError` because we cannot divide a number by zero.

## 2. Common Python Exceptions

| Exception | When does it occur? |
|---|---|
| `ValueError` | When a value is invalid |
| `TypeError` | When an operation is performed on an inappropriate data type |
| `NameError` | When a variable is not defined |
| `ZeroDivisionError` | When dividing by zero |
| `IndexError` | When accessing an invalid list index |
| `KeyError` | When accessing a dictionary key that does not exist |
| `FileNotFoundError` | When trying to open a file that does not exist |
| `AttributeError` | When accessing an attribute that an object does not have |

## 3. try and except

We use `try` and `except` to handle exceptions so that the program can respond to errors instead of terminating unexpectedly.

- `try`: Contains the code that might cause an exception.
- `except`: Handles the exception if it occurs.

Example:

```python
try:
    x = int(input("Enter a number: "))
    print(x)

except ValueError:
    print("Please enter a valid number.")
```

If the user enters a valid number, the `try` block executes successfully.

If the user enters an invalid value, the `except` block handles the `ValueError`.

## 4. Handling Multiple Exceptions

We can use multiple `except` blocks to handle different types of exceptions.

```python
try:
    x = int(input("Enter a number: "))
    result = 10 / x
    print(result)

except ValueError:
    print("Please enter a valid number.")

except ZeroDivisionError:
    print("Cannot divide by zero.")
```

Each `except` block handles a specific type of exception.

## 5. else

The `else` block executes only when no exception occurs in the `try` block.

```python
try:
    x = int(input("Enter a number: "))

except ValueError:
    print("Invalid input.")

else:
    print(f"You entered {x}.")
```

If the user enters a valid number, the `else` block executes.

If a `ValueError` occurs, the `except` block executes instead.

## 6. finally

The `finally` block executes whether an exception occurs or not.

It is commonly used for cleanup operations, such as closing files or releasing resources.

```python
try:
    x = int(input("Enter a number: "))

except ValueError:
    print("Invalid input.")

finally:
    print("Program finished.")
```

The message `Program finished.` is printed in both cases.

## 7. raise

We use `raise` when we want to generate an exception ourselves.

For example, if the user enters a negative age, we can raise a `ValueError`.

```python
age = int(input("Enter your age: "))

if age < 0:
    raise ValueError("Age cannot be negative.")

print(age)
```

If the age is negative, Python raises a `ValueError`.

We can also use `raise` inside a class to validate values.

```python
class Student:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")

        self.name = name
```

## 8. Summary

| Keyword | Purpose |
|---|---|
| `try` | Executes code that might cause an exception |
| `except` | Handles an exception |
| `else` | Executes when no exception occurs |
| `finally` | Executes whether an exception occurs or not |
| `raise` | Generates an exception manually |

## Remember

- Exceptions are errors that occur while a program is running.
- `try` and `except` help us handle exceptions.
- `else` executes when there is no exception.
- `finally` executes regardless of whether an exception occurs.
- `raise` allows us to generate an exception when a condition is not met.