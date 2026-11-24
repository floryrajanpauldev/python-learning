# Lambda Functions in Python

## What is a Lambda Function?

A **lambda function** is a small, anonymous function in Python that can contain a single expression.

Anonymous means the function does not have a name.

Lambda functions are useful when you need a simple function for a short period without defining it using `def`.

### Syntax

```python
lambda arguments: expression
```

- `lambda` – keyword used to create the function.
- `arguments` – input parameters.
- `expression` – operation performed and returned automatically.

## 1. Regular Function vs. Lambda

**Using a regular function:**

```python
def double(number):
    return number * 2

print(double(5))
```

**Output:**
```text
10
```

**Using lambda:**

```python
double = lambda number: number * 2

print(double(5))
```

**Output:**
```text
10
```

Both examples perform the same operation.

## 2. Lambda with Multiple Parameters

A lambda function can accept multiple arguments.

```python
add = lambda a, b: a + b

print(add(10, 20))
```

**Output:**
```text
30
```

## 3. Lambda with map()

`map()` applies a function to every item in an iterable.

Lambda is commonly used with `map()` when you need a small transformation.

```python
numbers = [1, 2, 3, 4, 5]

result = map(lambda number: number * 2, numbers)

print(list(result))
```

**Output:**
```text
[2, 4, 6, 8, 10]
```

Here, `lambda number: number * 2` doubles each number.

## 4. Lambda with filter()

`filter()` selects items that satisfy a condition.

```python
numbers = [1, 2, 3, 4, 5, 6]

result = filter(lambda number: number % 2 == 0, numbers)

print(list(result))
```

**Output:**
```text
[2, 4, 6]
```

Here, the lambda function checks whether each number is even.

## 5. Lambda with sorted()

Lambda can be used to customize how items are sorted.

```python
employees = [
    {"name": "John", "salary": 50000},
    {"name": "David", "salary": 70000},
    {"name": "Sarah", "salary": 60000}
]

result = sorted(employees, key=lambda employee: employee["salary"])

print(result)
```

The employees are sorted by salary in ascending order.

To sort in descending order:

```python
result = sorted(
    employees,
    key=lambda employee: employee["salary"],
    reverse=True
)
```

## 6. Lambda vs. Regular Functions

| Lambda | Regular Function |
|---|---|
| Uses the `lambda` keyword | Uses the `def` keyword |
| Anonymous by default | Has a function name |
| Contains one expression | Can contain multiple statements |
| Returns the expression result automatically | Uses `return` to return a value |
| Useful for short operations | Better for complex logic and reusable functionality |

## Important Notes

- Lambda functions can accept multiple parameters.
- A lambda function contains only one expression.
- The expression result is returned automatically.
- Lambda functions cannot contain statements such as `return`, `for`, or `while`.
- Commonly used with `map()`, `filter()`, and `sorted()`.

## Summary

Lambda functions are useful for writing short, simple functions without defining a separate function using `def`.

Common use cases:
- Transforming values with `map()`.
- Filtering values with `filter()`.
- Customizing sorting with `sorted()`.
- Performing simple calculations.

**Reference:** [Python Official Documentation – Lambda Expressions](https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions)