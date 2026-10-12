# Python `in` Keyword

## 1. What does `in` do?

The `in` keyword checks whether an item exists in a collection, such as a list.

```python
already_called = ["B-7", "I-22", "G-51"]

print("B-7" in already_called)   # True
print("O-68" in already_called)  # False
```

- `True`: The item exists in the list.
- `False`: The item does not exist in the list.

## 2. Using `in` with a while loop

```python
while pick in already_called:
    pick = random.choice(bingo_numbers)
```

The loop continues while `pick` is already in `already_called`.

When the condition becomes `False`, the loop stops.

## 3. Combining `while`, `in`, and `append()`

In the Bingo example:

1. `random.choice()` selects a random number.
2. `in` checks whether the number has already been called.
3. `while` keeps selecting another number if it has already been called.
4. `append()` adds the new number to the list.

## 4. Important consideration

If every number in `bingo_numbers` has already been called, the loop can continue indefinitely because every random selection will be a duplicate.

The example assumes that at least one uncalled number remains.

## Key Takeaways

- `in` checks membership in a collection.
- `while` repeats as long as its condition is `True`.
- `random.choice()` selects a random item from a list.
- `append()` adds an item to the end of a list.