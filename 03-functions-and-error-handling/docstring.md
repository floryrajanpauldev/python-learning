# Python Docstrings

## What is a docstring?

A **docstring** is a string written inside triple quotes (`""" ... """`) that describes what a function, class, or module does.

It helps us understand the purpose of a piece of code.

## Example from the Sing Out app

```python
def show_queue(queue):
    """Print everyone currently in the queue."""
    print("[the queue goes here]")
```

In this example:

- `def show_queue(queue):` defines a function named `show_queue` with a parameter named `queue`.
- `"""Print everyone currently in the queue."""` is the docstring. It describes what the function should do.
- `print("[the queue goes here]")` is the current placeholder output.

## Why use triple quotes?

Triple quotes allow us to write documentation as a string. They can also contain longer descriptions spanning multiple lines.

A docstring is normally placed immediately after the function definition line, inside the function body.

## Docstrings vs. comments

A docstring and a comment can both help explain code, but they are different.

**Docstring:**

```python
def add_singer(queue):
    """Add a singer to the queue."""
    print("[add a singer]")
```

**Comment:**

```python
# TODO: Replace this placeholder with the actual implementation.
print("[add a singer]")
```

- A docstring documents the purpose of a function, class, or module.
- A comment, which starts with `#`, explains code or leaves a reminder.
- A docstring is stored by Python as documentation; a comment is not.

## Accessing a docstring

Python lets us access a function's docstring using its `__doc__` attribute.

```python
def show_queue(queue):
    """Print everyone currently in the queue."""
    print("[the queue goes here]")

print(show_queue.__doc__)
```

Output:

```text
Print everyone currently in the queue.
```

## Key takeaway

A docstring uses triple quotes and describes what a function does. In our Sing Out app, we'll use docstrings to explain the purpose of functions such as `show_queue()`, `add_singer()`, and `remove_singer()`.
