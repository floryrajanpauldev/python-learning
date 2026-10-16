# Try and Except

## Converting a String to an Integer

We can use `int()` to convert a string containing a number into an integer. Python prints the number successfully.

```python
number = int("42")
print(number)

# Output:
42
```

However, if we try to convert a word into a number, Python raises an error.

```python
number = int("banana")
print(number)

# Output:
# Error
```

## Catching Exceptions

To catch these exceptions and give us an opportunity to address them, we can use `try` and `except`.

```python
try:
    number = int("banana")
except ValueError:
    print("Please enter a number.")
```

- `try` contains the code we want Python to attempt.
- `except ValueError` catches the error that occurs when a value cannot be converted to an integer.
- The `print()` statement displays a helpful message instead of allowing this exception to go unhandled.

## Using Try and Except with User Input

We can use `try` and `except` around user input when we expect the user to enter a number.

```python
try:
    age = int(input("How old are you? "))
    print(f"You'll be {age + 1} next year.")
except ValueError:
    print("Please enter a number.")
```

If the user enters a valid number, Python converts it to an integer and calculates their age next year.

If the user enters a word or another value that cannot be converted to an integer, Python catches the `ValueError` and prints:

```text
Please enter a number.
```
