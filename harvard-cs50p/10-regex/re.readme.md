# Regular Expressions (RegEx) – Python
https://docs.python.org/3/library/re.html



## 1. Importing the `re` Library

Python provides a built-in library called `re` to work with Regular Expressions (RegEx).

Regular Expressions are patterns used to search, match, and manipulate strings.

```python
import re
```

**Note:**
- `re` is a built-in Python library.
- No additional installation is required.

## 2. `re.search()`

The `re.search()` function searches for a pattern anywhere in a given string.

**Syntax:**

```python
re.search(pattern, string, flags=0)
```

**Parameters:**

1. `pattern`: The pattern we want to search for in the string.
2. `string`: The actual string in which we want to search.
3. `flags`: An optional parameter used to modify the behavior of the regular expression. Default value is `0`.

**Example:**

```python
import re

text = "I am learning Python"

result = re.search("Python", text)

if result:
    print("Pattern found")
else:
    print("Pattern not found")
```

**Output:**

```text
Pattern found
```

**Important points:**
- `re.search()` returns a match object if the pattern is found.
- It returns `None` if no match is found.
- It searches throughout the entire string, not just at the beginning.

## 3. Special Characters in Regular Expressions

Regular expressions use a whole bunch of special symbols to define search patterns.

These symbols help us specify how many times a character or group of characters should appear and which characters we want to match.

| Symbol | Meaning |
|---|---|
| `.` | Any character except a newline |
| `*` | Zero or more repetitions |
| `+` | One or more repetitions |
| `?` | Zero or one repetition (optional) |
| `{m}` | Exactly m repetitions |
| `{m,n}` | Between m and n repetitions |
| `^` | Matches the start of the string |
| `$` | Matches the end of the string |
| `[ ]` | Matches any one character from the specified set |
| `[^ ]` | Matches any character NOT in the specified set |

**Examples:**

- `a*` – Zero or more occurrences of `a`.
- `a+` – One or more occurrences of `a`.
- `a?` – Zero or one occurrence of `a`.
- `a{3}` – Exactly three occurrences of `a`.
- `a{2,4}` – Between two and four occurrences of `a`.
- `^Hello` – Matches `Hello` at the beginning of the string.
- `world$` – Matches `world` at the end of the string.
- `[abc]` – Matches either `a`, `b`, or `c`.
- `[^abc]` – Matches any character except `a`, `b`, or `c`.

**Important:**
- `[abc]` is a character set.
- `[^abc]` is the complement of that set.
- Inside square brackets, `^` means NOT when it appears first.
- Outside square brackets, `^` represents the beginning of a string.

## 4. Shorthand Character Classes

Regular expressions provide shorthand characters to search for commonly used character types.

| Pattern | Meaning |
|---|---|
| `\d` | Matches a decimal digit (0–9) |
| `\D` | Matches anything that is NOT a decimal digit |
| `\s` | Matches whitespace characters (spaces, tabs, newlines) |
| `\S` | Matches anything that is NOT a whitespace character |
| `\w` | Matches word characters (letters, digits, and underscore `_`) |
| `\W` | Matches anything that is NOT a word character |

**Examples:**

- `\d` – Matches a digit.
- `\D` – Matches a non-digit character.
- `\s` – Matches whitespace.
- `\S` – Matches a non-whitespace character.
- `\w` – Matches letters, numbers, or underscores.
- `\W` – Matches special characters such as `@`, `#`, and `!`.

**Example:**

```python
import re

text = "My phone number is 12345"

result = re.findall(r"\d", text)

print(result)
```

**Output:**

```text
['1', '2', '3', '4', '5']
```

## 5. Alternation and Grouping

Regular expressions also support alternation and grouping.

| Pattern | Meaning |
|---|---|
| `A\|B` | Matches either A or B |
| `(…)` | Creates a capturing group |
| `(?:…)` | Creates a non-capturing group |

### 1. Alternation (`|`)

The pipe symbol (`|`) works like an OR operator. It matches either the expression before or after it.

**Example:**

```python
import re

text = "I like Python"

result = re.search(r"Python|Java", text)

if result:
    print("Match found:", result.group())
```

**Output:**

```text
Match found: Python
```

### 2. Capturing Group (`(...)`)

Parentheses create a group that captures the matched portion of the string.

We can retrieve the captured value using `group()`.

**Example:**

```python
import re

text = "My phone number is 12345"

result = re.search(r"(\d+)", text)

if result:
    print(result.group(1))
```

**Output:**

```text
12345
```

### 3. Non-Capturing Group (`(?:...)`)

A non-capturing group groups expressions together but does not capture the matched value separately.

**Example:**

```python
import re

text = "I like Python"

result = re.search(r"(?:Python|Java)", text)

if result:
    print(result.group())
```

**Output:**

```text
Python
```

**Important difference:**

- `(…)` – Groups and captures the matched expression.
- `(?:…)` – Groups the expression without capturing it.

```
import re

text = "cat dog rat"

result = re.findall("[^abc]", text)

print(result)

# This finds individual characters that are not a, b, or c.

```