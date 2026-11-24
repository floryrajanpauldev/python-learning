# Unpacking in Python

## What is Unpacking?

**Unpacking** in Python means extracting individual values from a collection (such as a list, tuple, or dictionary) and assigning them to separate variables.

Unpacking makes code cleaner and easier to read.

## 1. Unpacking a List

```python
student = ["Flory", 35, "Ohio"]

name, age, city = student

print(name)
print(age)
print(city)
```

**Output:**
```text
Flory
35
Ohio
```

Each variable receives the corresponding value from the list.

## 2. Unpacking a Tuple

Unpacking works the same way with tuples.

```python
employee = ("John", 5000, "Developer")

name, salary, role = employee

print(name, salary, role)
```

## 3. Extended Unpacking Using *

The `*` operator collects multiple remaining values into a list.

```python
numbers = [10, 20, 30, 40, 50]

first, *remaining = numbers

print(first)
print(remaining)
```

**Output:**
```text
10
[20, 30, 40, 50]
```

You can also collect values from the middle:

```python
first, *middle, last = numbers

print(first)   # 10
print(middle)  # [20, 30, 40]
print(last)    # 50
```

## 4. Dictionary Unpacking

Use `**` to unpack a dictionary into keyword arguments.

```python
def display_employee(name, age, city):
    print(name, age, city)

employee = {
    "name": "Flory",
    "age": 35,
    "city": "Ohio"
}

display_employee(**employee)
```

**Output:**
```text
Flory 35 Ohio
```

The dictionary keys must match the function parameter names.

## 5. Unpacking Function Arguments

Use `*` to unpack a list or tuple into positional function arguments.

```python
def add(a, b, c):
    return a + b + c

numbers = [10, 20, 30]

result = add(*numbers)

print(result)
```

**Output:**
```text
60
```

## 6. Swapping Variables

Python allows you to swap two variables without using a temporary variable.

```python
a = 10
b = 20

a, b = b, a

print(a)  # 20
print(b)  # 10
```

## 7. Common Unpacking Operators

| Operator | Purpose |
|---|---|
| `*` | Unpacks an iterable into positional values or collects remaining values |
| `**` | Unpacks a dictionary into keyword arguments |

## Important Notes

- The number of variables must match the number of values when using regular unpacking.
- Extended unpacking with `*` collects remaining values into a list.
- `*` is commonly used with lists, tuples, and function arguments.
- `**` is commonly used with dictionaries and keyword arguments.
- Dictionary keys must match the function parameter names when using `**` in a function call.

## Summary

Unpacking is useful for:
- Extracting values from lists and tuples.
- Assigning multiple variables in one statement.
- Collecting remaining values using `*`.
- Passing list values to functions using `*`.
- Passing dictionary values to functions using `**`.
- Swapping variable values.

**Reference:** [Python Tutorial – More on Lists and Unpacking](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)