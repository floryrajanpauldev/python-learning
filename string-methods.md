# Python String Methods

## Overview

String methods are built-in Python tools that help us manipulate and clean strings.

They are useful when working with user input because the data entered by a user may contain unwanted spaces, inconsistent capitalization, or extra characters.

String methods help us clean and format that input to suit our code.

## 1. `upper()`

Converts all letters in a string to uppercase.

```python
recipe = "chicken tikka masala"
header = recipe.upper()

print(header)
```

**Output:**
```text
CHICKEN TIKKA MASALA
```

## 2. `lower()`

Converts all letters in a string to lowercase.

```python
search = "PASTA CARBONARA"
print(search.lower())
```

**Output:**
```text
pasta carbonara
```

This is useful when we want to compare text without worrying about capitalization.

For example, `"Pasta"` and `"PASTA"` have different capitalization, but converting both to lowercase makes them easier to compare.

## 3. `title()`

Converts the first letter of each word to uppercase.

```python
chef = "grace smith"
print(chef.title())
```

**Output:**
```text
Grace Smith
```

This is useful for formatting names and headings.

## 4. `strip()`

Removes whitespace from the beginning and end of a string.

```python
recipe = "     tiramisu    "
print(recipe.strip())
```

**Output:**
```text
tiramisu
```

Notice that `strip()` removes the extra spaces at both ends, not spaces between words.

### Removing a specific character

`strip()` can also remove a specified character from the beginning and end of a string.

```python
print("50%".strip('%'))
```

**Output:**
```text
50
```

Here, the `%` symbol is removed, leaving the string `"50"`.

In our PayUp app, we used this idea to clean a percentage entered as text before converting it into a number.

## 5. Chaining String Methods

We can call multiple string methods on the same string in a single expression. This is called **method chaining**.

```python
raw = "    CHiCKen TIKKA MasALA"
query = raw.strip().lower()

print(query)
```

**Output:**
```text
chicken tikka masala
```

### How does chaining work?

Python evaluates the methods from left to right:

1. `strip()` removes the extra spaces at the beginning and end.
2. `lower()` converts the remaining text to lowercase.
3. The cleaned string is assigned to `query`.

Instead of writing separate steps, we can combine them into one expression.

## 6. `join()`

The `join()` method combines multiple strings into one string, placing a specified separator between them.

```python
words = ["chicken", "tikka", "masala"]
recipe = " ".join(words)

print(recipe)
```

**Output:**
```text
chicken tikka masala
```

In this example, `" "` is the separator. Python inserts a space between each item in the list.

We can change the separator:

```python
words = ["Python", "String", "Methods"]

print("-".join(words))
```

**Output:**
```text
Python-String-Methods
```

Remember: `join()` is called on the separator string, and the items being joined must be strings.

## Summary

| Method | Purpose | Example result |
|---|---|---|
| `upper()` | Converts letters to uppercase | `"hello"` → `"HELLO"` |
| `lower()` | Converts letters to lowercase | `"HELLO"` → `"hello"` |
| `title()` | Capitalizes the beginning of each word | `"grace smith"` → `"Grace Smith"` |
| `strip()` | Removes whitespace or specified characters from both ends | `"  hello  "` → `"hello"` |
| `join()` | Combines strings using a separator | `" ".join(["Hello", "World"])` → `"Hello World"` |

## Key Takeaways

- String methods help us clean and format text.
- String methods return a result; they do not change the original string in place.
- `strip()` removes characters only from the beginning and end of a string.
- Method chaining lets us combine multiple operations.
- `join()` combines strings using a chosen separator.
- Cleaning user input helps make our programs more reliable.
