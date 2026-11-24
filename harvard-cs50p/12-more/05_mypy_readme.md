# mypy in Python

## What is mypy?

**mypy** is a static type checker for Python. It checks whether your code follows the type hints you have defined, helping identify potential type errors before running the program.

Python does not enforce type hints at runtime. mypy provides an additional layer of type checking during development.

## 1. Install mypy

Install mypy using pip:

```bash
pip install mypy
```

## 2. Example: Type Checking

Consider the following function:

```python
def add(a: int, b: int) -> int:
    return a + b

result = add(10, "20")
print(result)
```
#mypy harvard-cs50p/12-more/05_add_mypy.py

Here, the function expects two integers, but the second argument is a string.

Python does not check this type mismatch before execution.

## 3. Run mypy

Save the code in a file named `main.py`.

Run the following command:

```bash
mypy main.py
```

mypy identifies the type mismatch and reports an error.

## 4. Correct the Type Error

Pass an integer instead of a string:

```python
def add(a: int, b: int) -> int:
    return a + b

result = add(10, 20)
print(result)
```

Run mypy again:

```bash
mypy main.py
```

Expected output:

```text
Success: no issues found in 1 source file
```

## 5. Common mypy Commands

| Command | Purpose |
|---|---|
| `mypy main.py` | Checks a specific Python file |
| `mypy .` | Checks Python files in the current directory |
| `mypy --strict main.py` | Enables stricter type checking |

## 6. Benefits of mypy

- Detects potential type errors early.
- Helps maintain clean and reliable code.
- Improves code readability and maintainability.
- Useful for large Python applications.
- Supports better development practices when working with teams.

## Type Hints vs. mypy

| Type Hints | mypy |
|---|---|
| Define expected data types | Checks the use of those types |
| Written in Python code | Runs as a separate tool |
| Not enforced at runtime | Performs static type checking |

## Summary

- Type hints describe the expected types of variables, parameters, and return values.
- mypy checks whether the code follows those type hints.
- mypy does not execute the Python program.
- It helps identify potential errors before runtime.

**Reference:** [Official mypy documentation](https://mypy.readthedocs.io/en/stable/)