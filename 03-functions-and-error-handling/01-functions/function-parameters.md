# Python Function Parameters and Scope

## 1. Why use parameters?

Instead of writing a separate function for every person, we can write one reusable function that accepts a name.

```python
def greet(name):
    print(f"Welcome, {name}!")

greet("Jenny")
greet("Marcus")
```

The same function can greet many people.

## 2. Parameters vs. arguments

**Parameter:** The variable listed in the function definition.

```python
def greet(name):
    print(f"Welcome, {name}!")
```

Here, `name` is the parameter.

**Argument:** The actual value passed when the function is called.

```python
greet("Jenny")
```

Here, `"Jenny"` is the argument.

## 3. Multiple parameters

A function can accept more than one parameter.

```python
def greet(name, unread_messages):
    print(f"Welcome, {name}! You have {unread_messages} new messages.")

greet("Jenny", 15)
```

Output:

```text
Welcome, Jenny! You have 15 new messages.
```

Arguments are matched to parameters by position in this example:

- `"Jenny"` goes into `name`.
- `15` goes into `unread_messages`.

The order matters when using positional arguments.

## 4. Global scope

A variable defined outside a function is in the global scope.

```python
shop_name = "The Coffee Shop"

def show_welcome():
    print(f"Welcome to {shop_name}")

show_welcome()
```

Output:

```text
Welcome to The Coffee Shop
```

The function can read `shop_name` because it is defined outside the function.

## 5. Local scope

A parameter belongs to the function in which it is defined.

```python
def greet(name):
    print(f"Welcome, {name}!")

greet("Jenny")
```

The parameter `name` is local to `greet()`. You cannot use that local variable outside the function unless you return a value or otherwise make the value available.

## Key takeaways

- Parameters are named variables in a function definition.
- Arguments are the values passed into a function call.
- Functions can accept multiple parameters.
- Positional arguments match parameters in order.
- Global variables are defined outside functions.
- Parameters and local variables are available within their function's scope.
