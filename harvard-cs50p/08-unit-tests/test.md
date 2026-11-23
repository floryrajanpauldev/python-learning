# Python Unit Testing

## 1. What is Unit Testing?

Unit testing is the process of testing individual parts (units) of a program to make sure they work as expected.

For example, if we write a function to calculate the square of a number, we can write tests to verify that the function returns the correct result for different inputs.

## 2. Using `assert`

Python provides the `assert` statement to test whether a condition is true.

- If the condition is `True`, the test passes.
- If the condition is `False`, Python raises an `AssertionError`.

### Example

```python
def square(n):
    return n * n

assert square(2) == 4
assert square(3) == 9
assert square(4) == 16
```

If all assertions are true, the program finishes without an error.

## 3. Organizing Test Files

A common naming convention is to name test files:

```text
test_filename.py
```

For example, if our main Python file is named `calculator.py`, its test file can be named:

```text
test_calculator.py
```

Inside the test file, import the function we want to test:

```python
from calculator import square
```

Then write assertions to test the function:

```python
from calculator import square

def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(4) == 16
```

## 4. Using pytest
https://docs.pytest.org/en/stable/ 

**pytest** is a popular third-party Python testing framework.

It makes writing and running tests easier and provides detailed information when a test fails.

### Installation

Run the following command in your terminal:

```bash
python3 -m pip install pytest
```

### Running Tests

From your project directory, run:

```bash
python3 -m pytest

or

pytest filename.py
```

Pytest automatically discovers files named `test_*.py` or `*_test.py` and runs the test functions inside them that start with `test_`.

## 5. Key Takeaways

- **Unit Testing:** Tests individual functions or components of a program.
- **`assert`:** Checks whether a condition is true.
- **Test file:** Commonly named `test_filename.py`.
- **Import:** Use `from filename import function_name` to import the function being tested.
- **pytest:** A third-party Python testing framework.
- **Installation:** Use `python3 -m pip install pytest`.

**Remember:** Writing a function is only part of the job. Unit tests help verify that the function produces the expected results.


## Using `raise`

The `raise` keyword is used to intentionally generate an exception when something goes wrong or when a condition is not met.

It allows developers to control when an error should occur.

### Example

```python
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")

    return age
```

In this example, if the age is negative, Python raises a `ValueError` with a custom error message.

**Remember:**
- `raise` intentionally generates an exception.
- `try` contains code that might cause an exception.
- `except` catches and handles the exception.