# argparse in Python

## What is argparse?

`argparse` is a built-in Python module used to handle command-line arguments.

It allows users to pass input values and options when running a Python program from the terminal.

Instead of hardcoding values in a program, users can provide them when executing the script.

## 1. Basic Example

```python
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("name")

args = parser.parse_args()

print(f"Hello, {args.name}!")
```

Run the program:

```bash
python main.py Flory
```

Output:

```text
Hello, Flory!
```

Here:
- `ArgumentParser()` creates an argument parser.
- `add_argument()` defines an argument.
- `parse_args()` reads the arguments provided by the user.
- `args.name` accesses the supplied value.

## 2. Positional Arguments

Positional arguments are required by default. Their values are provided in the order defined.

```python
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("name")
parser.add_argument("age", type=int)

args = parser.parse_args()

print(f"Name: {args.name}")
print(f"Age: {args.age}")
```

Run:

```bash
python main.py Flory 35
```

## 3. Optional Arguments

Optional arguments use a prefix such as `--`.

```python
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--city", default="Dayton")

args = parser.parse_args()

print(f"City: {args.city}")
```

Run:

```bash
python main.py --city Chicago
```

Output:

```text
City: Chicago
```

If no city is provided, the default value is `Dayton`.

## 4. Boolean Flags

Use `action="store_true"` to create a flag that becomes `True` when supplied.

```python
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--verbose", action="store_true")

args = parser.parse_args()

if args.verbose:
    print("Verbose mode enabled")
else:
    print("Verbose mode disabled")
```

Run:

```bash
python main.py --verbose
```

## 5. Adding Help and Descriptions

`argparse` automatically generates help information.

```python
import argparse

parser = argparse.ArgumentParser(
    description="Employee information program"
)

parser.add_argument("name", help="Employee name")
parser.add_argument("--age", type=int, help="Employee age")

args = parser.parse_args()

print(args.name)
print(args.age)
```

Run:

```bash
python main.py --help
```

The terminal displays the available arguments and their descriptions.

## 6. Common argparse Methods

| Method / Argument | Purpose |
|---|---|
| `ArgumentParser()` | Creates an argument parser |
| `add_argument()` | Defines an argument |
| `parse_args()` | Reads command-line arguments |
| `type=int` | Converts an argument to an integer |
| `default=value` | Sets a default value |
| `required=True` | Makes an optional argument required |
| `help=` | Provides an argument description |
| `action="store_true"` | Creates a Boolean flag |

## Benefits of argparse

- Accepts user input from the command line.
- Avoids hardcoding values.
- Supports required and optional arguments.
- Provides automatic help messages.
- Validates and converts argument types.
- Useful for building command-line applications and automation scripts.

## Summary

- `argparse` is part of Python's standard library.
- It is used to handle command-line arguments.
- Positional arguments are required by default.
- Optional arguments commonly use `--`.
- `parse_args()` processes the arguments.
- `--help` or `-h` displays usage instructions. 
#python3 harvard-cs50p/12-more/07_argparse_file.py -h

**Reference:** [Python Official Documentation – argparse](https://docs.python.org/3/library/argparse.html)