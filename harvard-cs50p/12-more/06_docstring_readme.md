# Docstrings in Python

## What are Docstrings?

A **docstring** (documentation string) is a string used to describe the purpose and functionality of a Python module, class, or function.

Docstrings help developers understand what the code does and how to use it.

They are written using triple quotes (`""" """`).

## 1. Function Docstring

A function docstring describes what a function does.

```python
def greet(name: str) -> str:
    """Return a greeting message."""
    return f"Hello, {name}!"
```

## 2. Class Docstring

A class docstring describes the purpose of a class.

```python
class Student:
    """Represent a student with a name and age."""

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
```

## 3. Multi-line Docstring

For more detailed documentation, use multiple lines.

```python
def calculate_total(price: float, quantity: int) -> float:
    """
    Calculate the total price.

    Args:
        price: Price of one item.
        quantity: Number of items.

    Returns:
        The total price.
    """
    return price * quantity
```

### Common Sections

- **Description:** Explains what the function does.
- **Args:** Describes the function parameters.
- **Returns:** Describes the returned value.
- **Raises:** Describes exceptions the function may raise.

## 4. Accessing Docstrings

Use the `__doc__` attribute to access a docstring.

```python
def greet(name: str) -> str:
    """Return a greeting message."""
    return f"Hello, {name}!"

print(greet.__doc__)
```

**Output:**

```text
Return a greeting message.
```

You can also use Python's built-in `help()` function.

```python
help(greet)
```

## 5. Comments vs. Docstrings

| Comments | Docstrings |
|---|---|
| Explain code or logic | Document modules, classes, and functions |
| Start with `#` | Use triple quotes |
| Not accessible through `__doc__` | Accessible through `__doc__` |
| Explain implementation details | Explain purpose and usage |

## Benefits of Docstrings

- Improve code readability.
- Explain the purpose of functions and classes.
- Make code easier to maintain.
- Help developers understand how to use existing code.
- Support automatic documentation tools.

## Summary

- Docstrings document Python modules, classes, and functions.
- Use triple double quotes (`""" """`).
- Place the docstring immediately after the definition.
- Use `__doc__` or `help()` to access documentation.
- Follow consistent documentation conventions.

**Reference:** [PEP 257 – Docstring Conventions](https://peps.python.org/pep-0257/)