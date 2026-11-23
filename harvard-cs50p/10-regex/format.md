## 12. Formatting User Input – Name

Sometimes users enter their names in different formats.

For example:
- `Flory Rajan`
- `Rajan, Flory`

We can use Python string methods or Regular Expressions to format the name consistently.

### V1 – Using String Methods (`split()`)

We can use `split()` to separate the last name and first name when a comma is present.

```python
name = input("What is your name? ").strip()

if "," in name:
    lastname, firstname = name.split(",", maxsplit=1)
    name = f"{firstname.strip()} {lastname.strip()}"

print(f"Hello, {name}")
```

**Example 1:**

Input:
```text
Rajan, Flory
```

Output:
```text
Hello, Flory Rajan
```

**Example 2:**

Input:
```text
Flory
```

Output:
```text
Hello, Flory
```

**Important points:**
- `strip()` removes leading and trailing whitespace.
- `split()` separates a string based on a delimiter.
- `maxsplit=1` limits splitting to one occurrence.
- `split()` does not support Regular Expression patterns.

If we want to split using a RegEx pattern, we can use `re.split()`.

```python
lastname, firstname = re.split(r",\s*", name, maxsplit=1)
```

Here, `\s*` means zero or more whitespace characters after the comma.

### V2 – Using Regular Expressions (`re.search()`)

We can use `re.search()` with capturing groups to separate the last name and first name.

```python
import re

name = input("What is your name? ").strip()

matches = re.search(r"^(.+),\s*(.+)$", name)

if matches:
    lastname = matches.group(1)
    firstname = matches.group(2)

    name = f"{firstname} {lastname}"

print(f"Hello, {name}")
```

**Example 1:**

Input:
```text
Rajan, Flory
```

Output:
```text
Hello, Flory Rajan
```

**Example 2:**

Input:
```text
Smith, John
```

Output:
```text
Hello, John Smith
```

**Example 3:**

Input:
```text
Paul,David
```

Output:
```text
Hello, David Paul
```

### Understanding the RegEx Pattern

```python
r"^(.+),\s*(.+)$"
```

| Pattern | Meaning |
|---|---|
| `^` | Start of string |
| `(.+)` | Captures the last name |
| `,` | Matches the comma |
| `\s*` | Zero or more whitespace characters |
| `(.+)` | Captures the first name |
| `$` | End of string |

### Understanding `group()`

When we use parentheses `( )`, they create capturing groups.

We can retrieve the matched values using `group()`.

```python
import re

name = "Rajan, Flory"

matches = re.search(r"^(.+),\s*(.+)$", name)

print(matches.group(0))
print(matches.group(1))
print(matches.group(2))
```

**Output:**

```text
Rajan, Flory
Rajan
Flory
```

- `group(0)` – Returns the entire matched string.
- `group(1)` – Returns the first captured group (last name).
- `group(2)` – Returns the second captured group (first name).

### V1 vs V2

| V1 – String Methods | V2 – Regular Expressions |
|---|---|
| Uses `split()` | Uses `re.search()` |
| Simple and readable | More flexible pattern matching |
| No capturing groups | Uses capturing groups |
| Good for basic string formatting | Good for learning pattern matching |

**Key takeaway:** Both approaches can format user input. Use string methods for simple splitting and Regular Expressions when you need more flexible pattern matching.