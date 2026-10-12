# While Loops

## 1. What is a while loop?

A `while` loop repeats a block of code as long as its condition is `True`.

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

Output: `1, 2, 3, 4, 5`

## 2. How it works

- Initialize the counter before the loop.
- Check the condition.
- Execute the indented statements while the condition is `True`.
- Update the counter so the loop can eventually stop.

## 3. Incrementing a counter

These statements do the same thing:

```python
count = count + 1
```

```python
count += 1
```

The second statement is shorthand for the first.

## 4. Infinite loops

If the condition never becomes `False`, the loop may continue indefinitely.

Remember to update the counter or change the condition when needed.

Press `Ctrl + C` in the terminal to interrupt a running loop.

## 5. The break statement

The `break` statement immediately exits the loop.

```python
count = 1

while count <= 5:
    if count == 3:
        break

    print(count)
    count += 1
```

Output:

```text
1
2
```

The number `3` is not printed because `break` runs first.

## 6. Constants by convention

Uppercase variable names indicate values intended to remain unchanged.

```python
TOTAL_LAPS = 10
```

Python does not enforce constants; uppercase naming is a convention.

## 7. Using a constant in a while loop

```python
TOTAL_LAPS = 10
lap = 1

while lap <= TOTAL_LAPS:
    print(f"Lap: {lap}")
    lap += 1
```

The loop prints laps 1 through 10.

## Key Takeaways

- `while` repeats while a condition is `True`.
- Indentation determines which statements belong to the loop.
- Update counters to avoid unintended infinite loops.
- `break` exits a loop immediately.
- Uppercase names represent constants by convention.