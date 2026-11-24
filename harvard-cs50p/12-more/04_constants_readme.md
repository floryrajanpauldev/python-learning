# Constants in Python

## What are Constants?

A **constant** is a variable whose value is intended to remain unchanged throughout a program.

Python does not have a built-in keyword to declare constants. Instead, we use **uppercase names** by convention.

## 1. Creating Constants

```python
PI = 3.14159
MAX_USERS = 100
COMPANY_NAME = "ABC Company"
```

## 2. Using Constants

```python
TAX_RATE = 0.08

salary = 5000
tax = salary * TAX_RATE

print(tax)
```

**Output:**
```text
400.0
```

## 3. Can Constants Be Changed?

Python allows constants to be reassigned because it does not enforce constant values.

```python
MAX_USERS = 100
MAX_USERS = 200  # Python allows this
```

However, uppercase naming indicates that the value should not be changed.

## 4. Constants vs Variables

| Constants | Variables |
|---|---|
| Use uppercase names | Usually use lowercase names |
| Intended to remain unchanged | Can change |
| `MAX_USERS = 100` | `user_count = 10` |

## Summary

- Python does not enforce constants.
- Use uppercase names to identify constants.
- Constants should not be reassigned.
- Constants make code easier to read and maintain.

**Reference:** [PEP 8 – Naming Conventions](https://peps.python.org/pep-0008/)