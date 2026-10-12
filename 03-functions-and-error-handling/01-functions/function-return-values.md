# Python Function Return Values

## What does `return` do?

The `return` keyword sends a value back from a function to the code that called it.

Unlike `print()`, which displays something on the screen, `return` lets us store and reuse the result.

## Example 1: Calculate slices

```python
def slices_needed(guests):
    return guests * 2

slices = slices_needed(10)
print(slices)
```

Step by step:

1. `slices_needed(10)` calls the function with `guests = 10`.
2. `guests * 2` calculates `10 * 2`, which is `20`.
3. `return` sends `20` back to the caller.
4. `slices = slices_needed(10)` stores `20` in the variable `slices`.

## Example 2: Calculate pizzas

```python
import math

def pizzas_needed(slices):
    return math.ceil(slices / 8)

pizzas = pizzas_needed(20)
print(pizzas)
```

Each pizza has 8 slices. We need `20 / 8 = 2.5` pizzas, so `math.ceil()` rounds up to `3`.

The `ceil()` function rounds a number **up to the next integer** when needed.

## Connecting the functions

```python
slices = slices_needed(10)
pizzas = pizzas_needed(slices)

print(pizzas)
```

The first function calculates the number of slices. Its result becomes the argument for the second function, which calculates how many pizzas are needed.

Output:

```text
3
```

## Key difference: `print()` vs. `return`

- `print()` displays a value.
- `return` sends a value back so it can be stored, passed to another function, or used in a calculation.

A function can return a result without printing anything itself.
