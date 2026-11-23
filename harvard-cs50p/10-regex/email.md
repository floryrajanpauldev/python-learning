## 5. Alternation and Grouping

Regular expressions support alternation and grouping to create more complex search patterns.

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

## 6. Email Validation Using Regular Expressions

We can combine different RegEx symbols to validate an email address.

**Example 1: Basic email validation**

```python
import re

email = input("Enter your email: ")

if re.search(r"^\w+@\w+\.edu$", email):
    print("Valid")
else:
    print("Invalid")
```

### Understanding the pattern

```python
r"^\w+@\w+\.edu$"
```

| Pattern | Meaning |
|---|---|
| `^` | Start of string |
| `\w+` | One or more word characters |
| `@` | Matches the @ symbol |
| `\w+` | One or more word characters |
| `\.` | Matches an actual dot |
| `edu` | Matches the text edu |
| `$` | End of string |

### Example 2: Using Character Sets

```python
if re.search(r"^[a-zA-Z0-9_ ]+@\w+\.edu$", email):
    print("Valid")
else:
    print("Invalid")
```

We can replace `[a-zA-Z0-9_]` with `\w` because `\w` matches letters, digits, and underscores.

Note: `\w` does not match spaces.

### Example 3: Optional Groups in Email Validation

We can use optional groups to allow additional parts of an email address.

```python
if re.search(r"^\w+(\.+\w)?@\w+\.\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")
```

**Understanding the pattern:**

| Pattern | Meaning |
|---|---|
| `^` | Start of string |
| `\w+` | One or more word characters |
| `(\.+\w)?` | Optional capturing group: one or more dots followed by a word character |
| `@` | Matches the @ symbol |
| `\w+\.` | One or more word characters followed by a dot |
| `\w+` | One or more word characters |
| `\.edu` | Matches the literal `.edu` |
| `$` | End of string |

**Important:** `?` makes the preceding group optional, meaning it can appear zero or one time.

## 7. Regular Expression Flags

Flags are optional parameters that modify how regular expressions behave.

The default value is `0`, meaning no special flags are applied.

| Flag | Meaning |
|---|---|
| `re.IGNORECASE` | Ignores uppercase and lowercase differences |
| `re.MULTILINE` | Makes `^` and `$` match the beginning and end of each line |
| `re.DOTALL` | Makes `.` match newline characters as well |

### 1. `re.IGNORECASE`

Ignores case sensitivity when matching text.

```python
import re

email = "USER@EXAMPLE.EDU"

if re.search(r"^\w+@\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")
```

We can also convert the email to lowercase using:

```python
email = email.lower()
```

### 2. `re.MULTILINE`

By default, `^` and `$` match the beginning and end of the entire string.

With `re.MULTILINE`:
- `^` matches the beginning of each line.
- `$` matches the end of each line.

### 3. `re.DOTALL`

By default, `.` does not match newline characters.

With `re.DOTALL`, `.` also matches newline characters.

## 8. Raw Strings (`r`)

In Python, `r` before a string indicates that it is a raw string.

Raw strings are useful when writing regular expressions because they prevent Python from interpreting backslashes as escape sequences.

**Example:**

```python
pattern = r"\d+"
```

Here:
- `r` indicates a raw string.
- `\d` represents a decimal digit.
- `+` means one or more occurrences.

**Without a raw string:**

```python
pattern = "\\d+"
```

We need to escape the backslash ourselves.

**Important:** Raw strings are particularly useful when working with RegEx because patterns frequently contain backslashes such as `\d`, `\w`, `\s`, and `\.`.


## 9. `re.match()`

The `re.match()` function checks for a match **only at the beginning of the string**.

**Syntax:**

```python
re.match(pattern, string, flags=0)
```

**Important:**
- `re.match()` always starts matching at the beginning of the string.
- Therefore, we do not need to use `^` in the pattern.
- It does not require the entire string to match.

**Example:**

```python
import re

text = "Python is easy to learn"

result = re.match(r"Python", text)

if result:
    print("Match found")
else:
    print("No match found")
```

**Output:**

```text
Match found
```

## 10. `re.fullmatch()`

The `re.fullmatch()` function checks whether the **entire string matches the given pattern**.

**Syntax:**

```python
re.fullmatch(pattern, string, flags=0)
```

**Important:**
- The entire string must match the pattern.
- We do not need to use `^` or `$` in the pattern.
- If any part of the string does not match, it returns `None`.

**Example:**

```python
import re

text = "Python"

result = re.fullmatch(r"\w+", text)

if result:
    print("Full match found")
else:
    print("No full match found")
```

**Output:**

```text
Full match found
```

## 11. Difference Between `search()`, `match()`, and `fullmatch()`

| Function | Behavior |
|---|---|
| `re.search()` | Searches anywhere in the string |
| `re.match()` | Checks only at the beginning of the string |
| `re.fullmatch()` | Checks whether the entire string matches |

**Example using all three:**

```python
import re

text = "Hello Python"

print(re.search(r"Python", text))
print(re.match(r"Python", text))
print(re.fullmatch(r"Hello", text))
```

**Result:**
- `re.search()` – Match found because Python appears in the string.
- `re.match()` – Returns `None` because Python is not at the beginning.
- `re.fullmatch()` – Returns `None` because the entire string is not just Hello.