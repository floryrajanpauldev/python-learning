# Python REPL

**REPL** stands for:

> **R**ead → **E**valuate → **P**rint → **L**oop

The Python REPL lets us write Python code and see the result **immediately**, without creating or running a `.py` file.

It is useful for quickly testing Python expressions and experimenting with code.

## Start the Python REPL

Open the Terminal and type:

```bash
python
```

Press **Enter**.

Python will display a prompt like:

```text
>>>
```

The `>>>` means Python is ready for your input.

## Try an Expression

```python
5 + 5
```

Python immediately evaluates it and prints:

```text
10
```

## Try a Variable

```python
fruit = "apple"
```

Nothing is printed because we are assigning a value.

Now type:

```python
fruit and enter
```

Python displays:

```text
'apple'
```

## REPL and the Browser Console

The Python REPL is similar to using the **JavaScript console in a browser**.

In both cases, you can:

* Type code
* Execute it immediately
* See the result
* Experiment without creating a complete program

### JavaScript Console

```javascript
5 + 5
```

```text
10
```

### Python REPL

```python
5 + 5
```

```text
10
```

## Useful for Learning

The REPL is especially helpful when we want to quickly test something:

```python
"hello".upper()
```

```text
'HELLO'
```

Or:

```python
len("Python")
```

```text
6
```

Rather than creating a file just to test a small piece of Python code, we can use the REPL.

## Exiting the REPL

You can exit using:

```python
quit()
```

You can also use your terminal's end-of-input shortcut. On macOS/Linux, that is typically:

```text
Ctrl + D
```

On Windows, it is typically:

```text
Ctrl + Z
```

followed by **Enter**.

> **Note:** `Ctrl+C` interrupts the current command or input; it is not the standard way to exit the Python REPL.

## Quick Reference

| Action            | Example  |
| ----------------- | -------- |
| Start REPL        | `python` |
| Python prompt     | `>>>`    |
| Run an expression | `5 + 5`  |
| Check a variable  | `fruit`  |
| Exit              | `quit()` |

The REPL is a **general Python learning and testing tool**, so this file lives in the main section folder rather than inside a specific topic.
