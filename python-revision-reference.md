# Python Revision Quick Reference

| Topic | Concepts / Syntax | Purpose |
|---|---|---|
| Variables | `name = "Alex"` | Store values |
| Data types | `str`, `int`, `float`, `bool` | Represent different kinds of data |
| Type conversion | `int()`, `str()`, `float()` | Convert values between types |
| Input and output | `input()`, `print()` | Receive user input and display output |
| F-strings | `f"Hello, {name}"` | Insert variables into strings |
| String methods | `.strip()`, `.title()` | Clean and format strings |
| Arithmetic operators | `+`, `-`, `*`, `/`, `//`, `%`, `**` | Perform calculations |
| Comparison operators | `==`, `!=`, `>`, `<`, `>=`, `<=` | Compare values |
| Conditional statements | `if`, `elif`, `else` | Make decisions |
| Boolean operators | `and`, `or`, `not` | Combine or reverse conditions |
| Membership operators | `in`, `not in` | Check whether a value exists in a collection |
| `while` loops | `while condition:` | Repeat while a condition is true |
| `for` loops | `for item in items:` | Iterate over items |
| Tuples | `("Annie", "Dancing Queen")` | Store multiple values together |
| Tuple unpacking | `name, song = singer` | Assign tuple values to separate variables |
| Lists | `items = ["Tea", "Coffee"]` | Store an ordered collection |
| `enumerate()` | `enumerate(items, start=1)` | Iterate with an index and item |
| `append()` | `items.append(value)` | Add an item to the end of a list |
| `pop()` | `items.pop(index)` | Remove and return an item by index |
| `remove()` | `items.remove(value)` | Remove an item by value |
| `insert()` | `items.insert(index, value)` | Insert an item at a specific position |
| Functions | `def greet():` | Create reusable blocks of code |
| Parameters | `def greet(name):` | Pass values into functions |
| Return values | `return result` | Send a value back from a function |
| Guard clauses | `if condition: ... return` | Exit a function early when a condition is met |
| Exception handling | `try`, `except` | Handle errors without an unhandled exception |
| `ValueError` | `except ValueError:` | Handle invalid value conversions, such as converting `"banana"` to an integer |
| Input validation | `if not name or not song:` | Reject missing or invalid required input |
| `len()` | `len(items)` | Get the number of items |
| List indexing | `items[0]` | Access an item by position |
| List mutation | `items.pop()`, `items.insert()` | Modify an existing list |

## Practice Project

**Sing Out: A Karaoke Queue Manager**

Use the concepts above to practise adding singers, displaying and numbering the queue, calling the next singer, moving a singer to the top, removing singers, validating input, and handling an empty queue.
