# Python – Operator Overloading

## 1. What is Operator Overloading?

Operator overloading allows us to define how operators such as `+`, `-`, `*`, and `==` behave when used with objects created from our own classes.

Python uses special methods, also called magic methods or dunder methods, to implement operator overloading.

For example:
- `+` uses `__add__()`
- `-` uses `__sub__()`
- `*` uses `__mul__()`
- `==` uses `__eq__()`

## 2. Example using `__add__()`

```python
class Vault:
    def __init__(self, gold=0, silver=0):
        self.gold = gold
        self.silver = silver

    def __add__(self, other):
        gold = self.gold + other.gold
        silver = self.silver + other.silver
        return Vault(gold, silver)


v1 = Vault(100, 50)
v2 = Vault(200, 30)

total = v1 + v2

print(total.gold)
print(total.silver)
```

Output:

```text
300
80
```

## 3. How does `__add__()` work?

When Python sees:

```python
total = v1 + v2
```

It internally calls:

```python
total = v1.__add__(v2)
```

- `self` refers to the first object (`v1`).
- `other` refers to the second object (`v2`).
- The method adds the corresponding values.
- It returns a new `Vault` object containing the result.

## 4. Common Operator Overloading Methods

| Operator | Special Method | Purpose |
|---|---|---|
| `+` | `__add__()` | Addition |
| `-` | `__sub__()` | Subtraction |
| `*` | `__mul__()` | Multiplication |
| `/` | `__truediv__()` | Division |
| `==` | `__eq__()` | Equality comparison |
| `<` | `__lt__()` | Less than |
| `>` | `__gt__()` | Greater than |

## 5. Remember

- Operator overloading allows us to customize how operators work with our own objects.
- We use special methods such as `__add__()` to define the behavior.
- Python automatically calls the corresponding special method when the operator is used.