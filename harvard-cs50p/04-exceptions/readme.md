# Harvard CS50P – Exceptions in Python

Exceptions are errors that occur while a Python program is running. Python provides ways to handle these errors so that the program doesn't terminate unexpectedly. https://docs.python.org/3/tutorial/errors.html

## 1. SyntaxError

A `SyntaxError` occurs when Python cannot understand the code because it doesn't follow Python's syntax rules.

**Example:**

```python
print("Hello Python)
```

The closing double quote is missing.

**Explanation:**
- This is a coding mistake.
- The developer needs to fix the code.
- Python cannot execute the code until the syntax is corrected.

Corrected code:

```python
print("Hello Python")
```

## 2. Runtime Errors

Runtime errors occur while the program is executing.

For example, we may expect the user to enter a number, but the user enters text instead.

When Python tries to convert that text into an integer, it raises a `ValueError`.

**Example:**

```python
x = int(input("Enter a number: "))
print(f"The number is {x}")
```

If the user enters `hello`, Python raises:

```text
ValueError: invalid literal for int()
```

## 3. Handling Exceptions Using try and except

Python provides `try` and `except` blocks to handle exceptions.

- `try`: Contains the code that might cause an error.
- `except`: Contains the code that runs if a specified exception occurs.

**Example:**

```python
try:
    x = int(input("Enter a number: "))
    print(f"The number is {x}")

except ValueError:
    print("Please enter a valid number.")
```

**How it works:**

1. Python executes the code inside `try`.
2. If the user enters a valid number, the program prints the number.
3. If the user enters text that cannot be converted into an integer, Python raises a `ValueError`.
4. The `except` block catches the error and displays a friendly message instead of terminating with an unhandled exception.

## 4. Handling Multiple Exceptions

We can use multiple `except` blocks to handle different types of errors.

**Example:**

```python
try:
    x = int(input("Enter a number: "))
    result = 10 / x
    print(result)

except ValueError:
    print("Please enter a valid number.")

except ZeroDivisionError:
    print("You cannot divide by zero.")

print(x) 
```

**Explanation:**

- `ValueError`: Occurs when the input cannot be converted into an integer.
- `ZeroDivisionError`: Occurs when we try to divide a number by zero.
- `NameError`: Occurs when the variable or name is not defined..

## Key Takeaways

| Concept | Explanation |
|---|---|
| `SyntaxError` | Code does not follow Python syntax rules. |
| Runtime error | An error occurs while the program is running. |
| `ValueError` | A value is of the correct general type but is not acceptable for the operation. |
| `ZeroDivisionError` | Attempting to divide by zero. |
| `NameError` | Accessing x outside of scope. |
| `try` | Contains code that might raise an exception. |
| `except` | Handles a specified exception. |

**Important:** Exception handling helps make programs more reliable and user-friendly by allowing us to handle expected errors gracefully.