# Python `pop()` and `remove()`

## What does `pop()` do?

The `pop()` method removes an item from a list using its index and **returns the removed item**.

### Example

```python
tasks = ["email Sam", "book the venue", "pay the band"]

first = tasks.pop(0)

print(first)
print(tasks)
```

Output:

```text
email Sam
['book the venue', 'pay the band']
```

- `pop(0)` removes the item at index `0`.
- The removed item is returned and stored in `first`.
- The original list is updated.

If you call `pop()` without an index, it removes and returns the last item in the list.

## `pop()` versus `remove()`

| `pop()` | `remove()` |
|---|---|
| Removes an item using its index | Removes an item using its value |
| Returns the removed item | Returns `None` |
| Can be used when you need the removed value | Useful when you know the value to remove |

### Example: `pop()`

```python
tasks = ["email Sam", "book the venue", "pay the band"]

removed_task = tasks.pop(0)
print(removed_task)
```

Output:

```text
email Sam
```

### Example: `remove()`

```python
tasks = ["email Sam", "book the venue", "pay the band"]

result = tasks.remove("email Sam")
print(result)
```

Output:

```text
None
```

The task is removed, but `remove()` does not return the removed task.

## How we use `pop()` in Sing Out

In our karaoke queue, we can use `pop()` to remove the first singer and announce whose turn it is.

For example:

```python
singer, song = queue.pop(0)
print(f"It's {singer}'s turn to sing {song}!")
```

Here, `pop(0)` removes the first tuple from the queue and returns it. Tuple unpacking assigns the singer's name to `singer` and the song title to `song`.

**Key takeaway:** Use `pop()` when you need to remove an item by position and use the removed value afterward.
