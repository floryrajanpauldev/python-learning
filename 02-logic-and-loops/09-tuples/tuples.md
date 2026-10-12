# Python Tuples

## Overview

A **tuple** is a Python data type used to store multiple values together in a single variable.

Tuples are useful when we want to group related values that belong together and should not be changed.

For example, a color on a website can be represented using three RGB values:

- **R** — Red
- **G** — Green
- **B** — Blue

Steel Blue has the RGB values `(70, 130, 180)`.

```python
steel_blue = (70, 130, 180)
print(steel_blue)
```

**Output:**

```text
(70, 130, 180)
```

The parentheses `()` are commonly used to create a tuple.

## 1. Accessing Tuple Values Using Indexes

Just like lists, tuples use zero-based indexing.

```python
steel_blue = (70, 130, 180)

print(steel_blue[0])
print(steel_blue[1])
print(steel_blue[2])
```

**Output:**

```text
70
130
180
```

| Index | Value | Color component |
|---:|---:|---|
| `0` | `70` | Red |
| `1` | `130` | Green |
| `2` | `180` | Blue |

Remember that indexing starts at `0`, not `1`.

## 2. Tuples Are Immutable

The main difference between a tuple and a list is that **tuples are immutable**.

Immutable means that the values in a tuple cannot be reassigned using an index after the tuple has been created.

```python
steel_blue = (70, 130, 180)

steel_blue[0] = 300

print(steel_blue[0])
```

**Output:**

```text
TypeError: 'tuple' object does not support item assignment
```

Python raises a `TypeError` because we are trying to change the value at index `0`.

### Tuple vs. List

```python
# List: mutable
rgb_list = [70, 130, 180]
rgb_list[0] = 300

# Tuple: immutable
rgb_tuple = (70, 130, 180)
# rgb_tuple[0] = 300  # This raises a TypeError
```

Lists are appropriate when the collection needs to change. Tuples are appropriate when the collection of values should remain fixed.

**Important:** You can assign a completely new tuple to the variable, but you cannot modify an individual element of the existing tuple.

## 3. Tuple Unpacking

**Unpacking** means assigning the individual values of a tuple to separate variables in one statement.

Instead of accessing every value using its index, we can write:

```python
steel_blue = (70, 130, 180)

red, green, blue = steel_blue

print(red)
print(green)
print(blue)
```

**Output:**

```text
70
130
180
```

Python assigns the values in order:

- `red` receives `70`.
- `green` receives `130`.
- `blue` receives `180`.

The number of variables on the left must match the number of values in the tuple.

This is similar to destructuring in JavaScript.

## 4. Using Indexing and Unpacking Together

We can store multiple RGB tuples inside a list called `color_palette`.

```python
color_palette = [
    (70, 130, 180),
    (240, 128, 128),
    (60, 179, 113)
]

red, green, blue = color_palette[0]
print(f"RGB: {red}, {green}, {blue}")

red, green, blue = color_palette[1]
print(f"RGB: {red}, {green}, {blue}")
```

**Output:**

```text
RGB: 70, 130, 180
RGB: 240, 128, 128
```

### How does this work?

1. `color_palette[0]` accesses the first tuple in the list.
2. `red, green, blue = color_palette[0]` unpacks its three values.
3. The second assignment reuses the same variable names for the second tuple.

We can reuse `red`, `green`, and `blue` because each assignment gives those variables new values.

This example combines two data types:

- **List:** stores multiple colors and allows items to be added, removed, or replaced.
- **Tuple:** stores the three RGB values for each color.

The list is mutable, but each tuple's individual values are immutable.

## 5. Key Takeaways

- A tuple stores multiple values together.
- Tuples are commonly written using parentheses `()`.
- Tuple indexing starts at `0`, just like list indexing.
- Tuples are immutable: their individual elements cannot be reassigned.
- Unpacking assigns tuple values to separate variables.
- A list can contain tuples, making it useful for storing collections of related data.
- Tuples are a good choice when values belong together and should remain fixed.

