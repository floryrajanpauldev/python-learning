# Python File I/O (File Input and Output)

File I/O allows Python programs to read data from files and write data to files.

Python provides the built-in `open()` function to work with files.

## 1. open()

The `open()` function is used to open a file.

### Syntax

```python
file = open("filename.txt", "mode")
```

Common file modes:

| Mode | Purpose |
|---|---|
| `"r"` | Read an existing file |
| `"w"` | Write to a file (creates a new file or overwrites existing content) |
| `"a"` | Append content to the end of a file |
| `"x"` | Create a new file; raises an error if it already exists |

## 2. read()

The `read()` method is used to read the contents of a file.

### Example

```python
file = open("hello.txt", "r")

content = file.read()

print(content)

file.close()
```

- `open()` opens the file in read mode.
- `read()` reads the file contents.
- `close()` closes the file.

## 3. write()

The `write()` method is used to write content into a file.

### Example

```python
file = open("hello.txt", "w")

file.write("Hello, Python!")

file.close()
```

**Important:** When using `"w"` mode, existing content in the file is overwritten.

## 4. close()

The `close()` method closes an opened file.

It is important to close files after working with them to release system resources.

```python
file = open("hello.txt", "r")

content = file.read()

file.close()
```

## 5. Key Takeaways

- `open()` opens a file.
- `read()` reads the contents of a file.
- `write()` writes content into a file.
- `close()` closes the file.
- File modes determine whether we read, write, append, or create a file.

**Remember:** Python also provides a `with open()` statement, which automatically closes the file when the block finishes. We will explore this as another way to work with files.