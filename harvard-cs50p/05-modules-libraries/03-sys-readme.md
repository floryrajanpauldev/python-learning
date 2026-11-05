# Python sys Module

## 1. What is sys?

`sys` is a built-in Python module that provides access to system-specific functionality and information about the Python environment.

It allows Python programs to interact with the Python interpreter and its execution environment.

**Important:**
- `sys` is a built-in Python module.
- Import it using `import sys`.

```python
import sys
```

## 2. Common Uses of the sys Module

| Function / Attribute | Purpose |
|---|---|
| `sys.argv` | Access command-line arguments passed to a Python program |
| `sys.exit()` | Exit a Python program |
| `sys.version` | Get the Python version |
| `sys.platform` | Identify the operating system platform |
| `sys.path` | See where Python looks for modules to import |
| `sys.stdin` | Access standard input |
| `sys.stdout` | Access standard output |
| `sys.stderr` | Access standard error output |

## 3. Examples

### Example 1: Check Python Version

```python
import sys

print(sys.version)
```

Displays the Python version currently running.

### Example 2: Exit a Program

```python
import sys

age = int(input("Enter your age: "))

if age < 0:
    sys.exit("Age cannot be negative!")

print("Your age is:", age)
```

If the age is negative, `sys.exit()` terminates the program.

### Example 3: Command-Line Arguments

```python
import sys

print(sys.argv)
```

`sys.argv` contains the arguments passed to your Python program when you run it from the terminal.

For example, run:

```bash
python3 app.py hello
```

Output:

```text
['app.py', 'hello']
```

- `sys.argv[0]` contains the script name (`app.py`).
- `sys.argv[1]` contains the first argument (`hello`).

## 4. Why is sys Useful in Real-World Applications?

Developers use `sys` when they need to:

- Read arguments provided through the terminal.
- Exit a program when something goes wrong.
- Check Python or operating system information.
- Control or inspect how Python runs a program.

## 5. Key Takeaways

- `sys` is a built-in Python module.
- Use `import sys` to access it.
- It helps Python programs interact with the interpreter and execution environment.

### Difference Between sys and Third-Party Packages

| Module / Package | Type | Installation |
|---|---|---|
| `sys` | Built-in Python module | No installation required |

