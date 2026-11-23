## Walrus Operator (`:=`)

The **Walrus Operator**, also called the **Assignment Expression**, was introduced in Python 3.8.

It allows us to **assign a value to a variable and use that value in the same expression**.

### Example 1: Using `:=` with an `if` statement

```python
numbers = [1, 2, 3, 4, 5]

if (count := len(numbers)) > 3:
    print(f"There are {count} numbers")
```

**Output:**
```text
There are 5 numbers
```

Explanation:
- `len(numbers)` calculates the number of items.
- `count := len(numbers)` assigns that result to `count`.
- We can immediately use `count` in the condition and inside the `if` block.

### Example 2: Using `:=` with a `while` loop

```python
while (name := input("Enter your name: ")) != "quit":
    print(f"Hello, {name}")
```

Explanation:
- `input()` asks the user to enter a name.
- `:=` assigns the entered value to `name`.
- The loop continues until the user enters `"quit"`.

### Difference between `=` and `:=`

| Operator | Purpose |
|---|---|
| `=` | Regular assignment statement |
| `:=` | Assignment expression — assigns a value and uses it within an expression |

**Remember:** `:=` is useful when you want to assign a value and use it immediately in a condition or expression. It does not replace regular `=` assignments.