# Python `insert()`

## What does `insert()` do?

The `insert()` method adds an item to a list at a specified position.

It takes two arguments:

1. **Index:** The position where you want to insert the item.
2. **Value:** The item you want to insert.

## Example

```python
tasks = ["do laundry", "call mom"]

tasks.insert(0, "pay rent")

print(tasks)
```

Output:

```text
['pay rent', 'do laundry', 'call mom']
```

### How it works

- `insert(0, "pay rent")` inserts `"pay rent"` at index `0`.
- The existing items shift to the right.
- The original list is updated.

## Key points

- List indexes start at `0`.
- `insert(index, value)` inserts an item at the specified position.
- Unlike `append()`, which adds an item to the end, `insert()` lets you choose the position.
- `insert()` modifies the original list and returns `None`.
