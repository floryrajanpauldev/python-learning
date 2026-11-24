# Python Dictionary Comprehension

Dictionary comprehension is used to create a new dictionary in a concise way using a loop.

## Syntax

```python
{key: value for item in iterable}
```

- `key`: The dictionary key.
- `value`: The value associated with the key.
- `item`: Each item from the iterable.

## Example 1: Create a dictionary from a list

```python
names = ["John", "Mary", "David"]

name_lengths = {
    name: len(name)
    for name in names
}

print(name_lengths)
```

**Output:**
```python
{
    "John": 4,
    "Mary": 4,
    "David": 5
}
```

Explanation:
- Loop through each name.
- Use the name as the dictionary key.
- Use the length of the name as the value.

## Example 2: Create a dictionary with a condition

```python
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = {
    number: number * number
    for number in numbers
    if number % 2 == 0
}

print(even_numbers)
```

**Output:**
```python
{
    2: 4,
    4: 16,
    6: 36
}
```

Only even numbers are included, and their squares become the values.

## Example 3: Convert two lists into a dictionary

```python
names = ["John", "Mary", "David"]
ages = [25, 28, 32]

employees = {
    name: age
    for name, age in zip(names, ages)
}

print(employees)
```

**Output:**
```python
{
    "John": 25,
    "Mary": 28,
    "David": 32
}
```

## Dictionary Comprehension vs List Comprehension

| List comprehension | Dictionary comprehension |
|---|---|
| `[expression for item in iterable]` | `{key: value for item in iterable}` |
| Creates a list | Creates a dictionary |
| Uses square brackets `[]` | Uses curly braces `{}` |

**Remember:**
- List comprehension creates a list.
- Dictionary comprehension creates key-value pairs.
- You can add an `if` condition to filter items.
