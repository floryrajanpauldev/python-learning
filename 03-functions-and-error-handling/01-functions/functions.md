# Python Functions

## What is a function?

A **function** is a reusable block of code that performs a specific task. Functions help us organize our programs and avoid repeating code.

## Defining a function

Use the `def` keyword to define a function.

```python
def roll_dice():
    roll = random.randint(1, 6)
    print(f"You rolled a {roll}!")
```

The parts of a function definition:

- `def` — tells Python that we are defining a function.
- `roll_dice` — the function name.
- `()` — parentheses, which can hold parameters.
- `:` — marks the beginning of the function body.
- Indentation — identifies the statements that belong to the function.

Because this example uses `random.randint()`, we also need `import random` at the beginning of the Python file.

## Calling a function

Defining a function does not execute its body. We execute it by calling the function:

```python
roll_dice()
```

We can call the same function multiple times:

```python
roll_dice()
roll_dice()
roll_dice()
```

Each call rolls the dice once.

## Calling a function inside another function

A function can call another function.

```python
def throw_twice():
    roll_dice()
    roll_dice()

throw_twice()
```

Calling `throw_twice()` calls `roll_dice()` twice.

## Organizing a program with functions

We can create separate functions for different tasks.

```python
def show_welcome():
    print()
    print("Welcome to Dice Fight!")
    print()

def play_game():
    show_welcome()
    throw_twice()

play_game()
```

Here, `play_game()` calls `show_welcome()` and `throw_twice()`.

## Key takeaways

- Use `def` to define a function.
- Indentation matters.
- A function runs when it is called.
- A function can be called multiple times.
- One function can call another function.
- Use meaningful names, such as `roll_dice()` and `show_welcome()`.
