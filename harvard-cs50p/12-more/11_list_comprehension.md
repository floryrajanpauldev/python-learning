# List Comprehension in Python

## What is List Comprehension?

**List comprehension** is a concise way to create a new list from an existing iterable (such as a list, tuple, or range).

It provides a shorter alternative to using a `for` loop when creating a list.

## Syntax

```python
[expression for item in iterable]
```

- `expression`: Operation performed on each item.
- `item`: Variable representing each item.
- `iterable`: Collection being iterated over.

## 1. Without List Comprehension

Using a regular `for` loop:

```python
numbers = [1, 2, 3, 4, 5]

result = []

for number in numbers:
    result.append(number * 2)

print(result)
```

**Output:**

```text
[2, 4, 6, 8, 10]
```

## 2. With List Comprehension

The same operation can be written in one line:

```python
numbers = [1, 2, 3, 4, 5]

result = [number * 2 for number in numbers]
#"experssion is - Perform an operation (number * 2) on each item in the iterable and collect the results into a new list."

print(result)
```

**Output:**

```text
[2, 4, 6, 8, 10]
```

## 3. List Comprehension with Conditions

Use `if` to filter items based on a condition.

Example: Get only even numbers.

```python
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = [
    number for number in numbers
    if number % 2 == 0
]

print(even_numbers)
```

**Output:**

```text
[2, 4, 6]
```

## 4. List Comprehension with Strings

Example: Convert employee names to uppercase.

```python
employees = ["John", "David", "Sarah"]

names = [name.upper() for name in employees]

print(names)
```

**Output:**

```text
['JOHN', 'DAVID', 'SARAH']
```

## 5. List Comprehension with Dictionaries

Example: Extract employee names from a list of dictionaries.

```python
employees = [
    {"name": "John", "age": 30},
    {"name": "David", "age": 35},
    {"name": "Sarah", "age": 28}
]

names = [employee["name"] for employee in employees]

print(names)
```

**Output:**

```text
['John', 'David', 'Sarah']
```

## 6. List Comprehension vs. map()

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

| List Comprehension | map() |
|---|---|
| Creates a new list | Returns a map iterator |
| Uses `for` inside brackets | Uses a function and iterable |
| Supports conditions directly | Often combined with `filter()` for filtering |
| Often easier to read for simple transformations | Useful when applying an existing function |

## 7. List Comprehension vs. React map()

In React, JavaScript's `.map()` method is commonly used to transform arrays and render lists of JSX elements.

**Python:**

```python
numbers = [1, 2, 3]

result = [number * 2 for number in numbers]
```

**React / TypeScript:**

```tsx
const numbers = [1, 2, 3];

const result = numbers.map((number) => number * 2);
```

Both transform each item and produce a new collection.

## Important Notes

- List comprehension creates a new list.
- It does not modify the original iterable.
- It can include conditions using `if`.
- It can perform transformations and filtering.
- Avoid complicated expressions that make the code difficult to read.

## Summary

List comprehension is useful for:

- Creating new lists.
- Transforming existing values.
- Filtering items based on conditions.
- Extracting values from dictionaries.
- Replacing simple loops with shorter, readable code.

**Reference:** [Python Official Documentation – List Comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)