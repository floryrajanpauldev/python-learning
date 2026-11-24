# Python `filter()`

The `filter()` function is used to **select items from an iterable based on a condition**.

It keeps only the items for which the condition returns `True`.

## Syntax

```python
filter(function, iterable)
```

- `function`: A function that checks a condition.
- `iterable`: A collection such as a list or tuple.
- Returns a filter iterator, so use `list()` to convert it into a list.

## Example 1: Filter even numbers

```python
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = list(filter(lambda number: number % 2 == 0, numbers))

print(even_numbers)
```

**Output:**
```text
[2, 4, 6]
```

Explanation:
- `lambda number`: takes one number at a time.
- `number % 2 == 0`: checks whether the number is even.
- `filter()` keeps only numbers that satisfy the condition.

## Example 2: Filter employees by age

```python
employees = [
    {"name": "John", "age": 25},
    {"name": "Mary", "age": 17},
    {"name": "David", "age": 32}
]

adults = list(filter(lambda employee: employee["age"] >= 18, employees))

print(adults)
```

**Output:**
```python
[
    {"name": "John", "age": 25},
    {"name": "David", "age": 32}
]
```

## `filter()` vs `map()`

| Function | Purpose |
|---|---|
| `map()` | Performs an operation on every item |
| `filter()` | Selects items that satisfy a condition |

## `filter()` vs List Comprehension

Both can filter items.

Using `filter()`:
```python
even_numbers = list(filter(lambda n: n % 2 == 0, numbers))
```

Using list comprehension:
```python
even_numbers = [n for n in numbers if n % 2 == 0]
```

**Remember:**
- `map()` transforms items.
- `filter()` selects items.
- List comprehension can do both in a readable way.
