# Python Global Variables

A **global variable** is a variable declared outside a function. It can be accessed by functions within the same module.

## 1. Accessing a Global Variable

```python
name = "Harry"  # Global variable

def display():
    print(name)

display()  # Harry
```

We can read a global variable inside a function without using the `global` keyword.

## 2. Modifying a Global Variable

To modify a global variable inside a function, use the `global` keyword.

```python
count = 10

def update():
    global count
    count = 20

update()

print(count)  # 20
```

Without `global`, assigning a value to `count` inside the function creates a local variable instead.

## Key Points

- Global variables are declared outside functions.
- They can be accessed inside functions.
- Use `global` when you need to modify a global variable inside a function.
- Avoid unnecessary global variables because they can make code harder to maintain.