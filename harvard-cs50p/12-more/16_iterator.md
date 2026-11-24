# Python Iterators

An **iterator** is an object that allows you to access items one at a time from an iterable.

It remembers its current position and knows how to retrieve the next item.

## 1. Iterable vs Iterator

| Iterable | Iterator |
|---|---|
| An object you can loop over | An object that produces values one at a time |
| Can create an iterator | Keeps track of its current position |
| Examples: list, tuple, string | Created using `iter()` |

## 2. Using `iter()` and `next()`

```python
names = ["John", "Mary", "David"]

iterator = iter(names)

print(next(iterator))  # John
print(next(iterator))  # Mary
print(next(iterator))  # David
```

**Output:**
```text
John
Mary
David
```

- `iter()` creates an iterator from an iterable.
- `next()` retrieves the next item.
- Calling `next()` after all items are consumed raises `StopIteration`.

## 3. Using an Iterator with a For Loop

```python
numbers = [10, 20, 30]

iterator = iter(numbers)

for number in iterator:
    print(number)
```

A `for` loop automatically calls `next()` until there are no more items.

## 4. Creating a Custom Iterator

A custom iterator uses two special methods:

- `__iter__()` returns the iterator object.
- `__next__()` returns the next value or raises `StopIteration` when finished.

```python
class Count:
    def __init__(self, limit):
        self.limit = limit
        self.number = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.number < self.limit:
            self.number += 1
            return self.number

        raise StopIteration


counter = Count(3)

for number in counter:
    print(number)
```

**Output:**
```text
1
2
3
```

## 5. Iterator vs Generator

| Iterator | Generator |
|---|---|
| An object that follows the iterator protocol | A convenient way to create an iterator |
| Uses `__iter__()` and `__next__()` | Uses `yield` |
| Can be implemented using a class | Created using a generator function or expression |
| Produces values one at a time | Produces values one at a time |

**Important:** Every generator is an iterator, but not every iterator is a generator.

## 6. Real-World Uses

- Processing large collections one item at a time.
- Reading files line by line.
- Processing data without loading everything into memory.
- Working with generators and loops.

## Key Takeaways

- An iterable is something you can loop over.
- An iterator produces one value at a time.
- `iter()` creates an iterator.
- `next()` retrieves the next value.
- `StopIteration` indicates that there are no more values.
- Generators are a convenient way to create iterators.