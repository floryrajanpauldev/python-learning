# Python Generators

A **generator** is a special type of function that produces values one at a time instead of creating and returning all values at once.

Generators use the `yield` keyword instead of `return`.

## 1. Generator Function

```python
def get_numbers():
    yield 1
    yield 2
    yield 3

numbers = get_numbers()

print(next(numbers))  # 1
print(next(numbers))  # 2
print(next(numbers))  # 3
```

**Output:**
```text
1
2
3
```

- `yield` produces a value and pauses the function.
- `next()` requests the next value.
- The function remembers where it stopped and resumes from there.

## 2. Using a Generator with a For Loop

```python
def get_numbers():
    yield 1
    yield 2
    yield 3

for number in get_numbers():
    print(number)
```

**Output:**
```text
1
2
3
```

A `for` loop automatically requests the next value until the generator is exhausted.

## 3. Generator vs Regular Function

Regular function using `return`:

```python
def get_numbers():
    return [1, 2, 3]
```

Generator using `yield`:

```python
def get_numbers():
    yield 1
    yield 2
    yield 3
```

| `return` | `yield` |
|---|---|
| Returns a result | Produces a value |
| Ends the function | Pauses the function |
| Can return a list of values | Produces values one at a time |

## 4. Generator Expression

A generator expression is similar to list comprehension, but uses parentheses `()` instead of square brackets `[]`.

```python
numbers = (number * 2 for number in range(5))

for number in numbers:
    print(number)
```

**Output:**
```text
0
2
4
6
8
```

## 5. List Comprehension vs Generator Expression

List comprehension:

```python
numbers = [number * 2 for number in range(5)]
```

Generator expression:

```python
numbers = (number * 2 for number in range(5))
```

| List comprehension | Generator expression |
|---|---|
| Creates a list | Creates a generator |
| Stores all results in memory | Produces results when requested |
| Uses `[]` | Uses `()` |

## 6. Why Use Generators?

- **Memory efficient:** Does not need to store all results at once.
- **Lazy evaluation:** Produces values only when needed.
- **Large datasets:** Useful for processing large files or streams of data.

## 7. Real-World Example: Reading a File

A generator can read a large file one line at a time instead of loading the entire file into memory.

```python
def read_file(filename):
    with open(filename) as file:
        for line in file:
            yield line

for line in read_file("data.txt"):
    print(line)
```

The accompanying `15_generator.py` example reads the `data.txt` file beside the script, regardless of the current working directory.

## Key Takeaways

- `yield` is used to create generator functions.
- `next()` retrieves the next value.
- Generators remember their execution state.
- Generator expressions use parentheses `()`.
- Generators are useful for memory-efficient processing of large amounts of data.