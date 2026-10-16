# Python `enumerate()`

## What does `enumerate()` do?

The built-in `enumerate()` function lets us loop through an iterable, such as a list, and get two values during each iteration:

- **Index:** The position of the item.
- **Item:** The actual value at that position.

Without `enumerate()`, a `for` loop gives us the items. With `enumerate()`, we can get both the index and the item.

## Example

```python
contacts = ["Freda", "Homer", "Chance"]

for i, contact in enumerate(contacts):
    print(i, contact)
```

### Output

```text
0 Freda
1 Homer
2 Chance
```

## How does it work?

1. `enumerate(contacts)` provides the index and item for each contact.
2. `i` receives the index.
3. `contact` receives the contact's name.
4. `print(i, contact)` displays both values.

By default, `enumerate()` starts the index at `0`.

## Start numbering at 1

We can use the optional `start` argument to begin counting at `1`:

```python
for i, contact in enumerate(contacts, start=1):
    print(i, contact)
```

Output:

```text
1 Freda
2 Homer
3 Chance
```

## Key takeaway

Use `enumerate()` when you need both the position and the value of each item in a loop.

**Remember:** The default starting index is `0`, but you can change it with `start=1` or another starting number.
