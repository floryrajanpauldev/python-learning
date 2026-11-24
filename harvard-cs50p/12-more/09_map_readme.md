# map() in Python

## What is map()?

`map()` is a built-in Python function that applies a specified function to every item in an iterable (such as a list or tuple).

It returns a **map object (iterator)**, which can be converted into a list, tuple, or another iterable.

### Syntax

```python
map(function, iterable)
```

- `function`: The function to apply to each item.
- `iterable`: The collection of items to process.

## 1. Basic Example

Use `map()` to double every number in a list.

```python
numbers = [1, 2, 3, 4, 5]

def double(number):
    return number * 2

result = map(double, numbers)

print(list(result))
```

**Output:**
```text
[2, 4, 6, 8, 10]
```

## 2. Using lambda with map()

You can use a lambda function instead of defining a separate function.

```python
numbers = [1, 2, 3, 4, 5]

result = map(lambda number: number * 2, numbers)

print(list(result))
```

**Output:**
```text
[2, 4, 6, 8, 10]
```

## 3. Converting Strings to Integers

A common use of `map()` is converting values from one data type to another.

```python
numbers = ["10", "20", "30", "40"]

result = map(int, numbers)

print(list(result))
```

**Output:**
```text
[10, 20, 30, 40]
```

## 4. Using map() with Multiple Iterables

`map()` can accept multiple iterables. The function receives corresponding values from each iterable.

```python
numbers1 = [1, 2, 3]
numbers2 = [10, 20, 30]

result = map(lambda a, b: a + b, numbers1, numbers2)

print(list(result))
```

**Output:**
```text
[11, 22, 33]
```

Note: When multiple iterables are provided, `map()` stops when the shortest iterable is exhausted.

## 5. map() with a List of Dictionaries

Imagine you have employee records and want to extract employee names.

```python
employees = [
    {"name": "John", "age": 30},
    {"name": "David", "age": 35},
    {"name": "Sarah", "age": 28}
]

names = map(lambda employee: employee["name"], employees)

print(list(names))
```

**Output:**
```text
['John', 'David', 'Sarah']
```

## 6. map() vs. List Comprehension

Both can transform items in a collection.

**Using map():**

```python
numbers = [1, 2, 3, 4]

result = list(map(lambda x: x * 2, numbers))
```

**Using list comprehension:**

```python
numbers = [1, 2, 3, 4]

result = [x * 2 for x in numbers]
```

Both produce:

```text
[2, 4, 6, 8]
```

| map() | List Comprehension |
|---|---|
| Applies a function to each item | Creates a new list using an expression |
| Returns a map iterator | Returns a list |
| Often used with existing functions | Often easier for simple transformations |

## 7. Important Notes

- `map()` is a built-in Python function.
- It does not modify the original iterable.
- It returns an iterator, not a list.
- Convert the result using `list()` or `tuple()` when needed.
- Its iterator is consumed as you iterate over it.

## Summary

`map()` is useful when you want to apply the same operation to every item in a collection.

Common use cases:
- Converting data types.
- Transforming lists of values.
- Extracting fields from records.
- Applying calculations to collections.
- Processing multiple iterables together.

**Reference:** [Python Official Documentation – map()](https://docs.python.org/3/library/functions.html#map)