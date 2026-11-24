# Python `enumerate()`

The `enumerate()` function lets you loop through an iterable and get both the index and the value at the same time.

## Syntax

```python
enumerate(iterable, start=0)
```

- `iterable`: A list, tuple, string, etc.
- `start`: The starting index. Default is `0`.

## Example 1: Loop through a list

```python
names = ["John", "Mary", "David"]

for index, name in enumerate(names):
    print(index, name)
```

**Output:**
```text
0 John
1 Mary
2 David
```

Explanation:
- `enumerate(names)` provides the index and the value.
- `index` receives the position.
- `name` receives the item.

## Example 2: Start indexing from 1

```python
names = ["John", "Mary", "David"]

for index, name in enumerate(names, start=1):
    print(index, name)
```

**Output:**
```text
1 John
2 Mary
3 David
```

## Example 3: Create a numbered list

```python
tasks = ["Learn Python", "Practice SQL", "Build a project"]

for number, task in enumerate(tasks, start=1):
    print(f"{number}. {task}")
```

**Output:**
```text
1. Learn Python
2. Practice SQL
3. Build a project
```

## Example 4: Convert enumerate into a list

```python
names = ["John", "Mary", "David"]

result = list(enumerate(names))

print(result)
```

**Output:**
```python
[(0, 'John'), (1, 'Mary'), (2, 'David')]
```

## `enumerate()` vs Regular Loop

Without `enumerate()`:

```python
names = ["John", "Mary", "David"]

for index in range(len(names)):
    print(index, names[index])
```

With `enumerate()`:

```python
for index, name in enumerate(names):
    print(index, name)
```

`enumerate()` is cleaner because you don't need to access each item using its index.

**Remember:** `enumerate()` gives you two things while looping:
- Index
- Value
