# Python Sets (`set`)

A **set** is a collection of unique values. It does not allow duplicate elements.

If we add the same value more than once, Python keeps only one copy.

## 1. Creating a Set

```python
names = {"Harry", "Hermione", "Ron", "Harry"}

print(names)
```

Output (the order may vary):

```text
{'Harry', 'Hermione', 'Ron'}
```

Notice that `"Harry"` appears only once.

**Important:**
- Sets do not maintain a guaranteed order.
- Sets are mutable, meaning we can add or remove elements.
- Sets do not support indexing.
- Set elements must be hashable (for example, strings and numbers).

To create an empty set, use `set()`.

```python
names = set()
```

`{}` creates an empty dictionary, not an empty set.

## 2. Adding Elements

Use `add()` to add an element.

```python
names = {"Harry", "Hermione"}

names.add("Ron")
names.add("Harry")

print(names)
```

Harry is not added again because sets do not allow duplicates.

## 3. Removing Elements

Python provides two common methods:

**remove()**

Removes an element. Raises a `KeyError` if the element does not exist.

```python
names.remove("Harry")
```

**discard()**

Removes an element if it exists. Does not raise an error if it is missing.

```python
names.discard("Draco")
```

## 4. Finding the Number of Elements

Use `len()` to get the number of unique elements.

```python
names = {"Harry", "Hermione", "Ron", "Harry"}

print(len(names))  # 3
```

## 5. Converting a List into a Set

We can convert a list into a set to eliminate duplicate values.

```python
names = ["Harry", "Ron", "Hermione", "Harry", "Ron"]

unique_names = set(names)

print(unique_names)
```

Output (the order may vary):

```text
{'Harry', 'Ron', 'Hermione'}
```

## 6. Set Operations

Sets support useful mathematical operations.

**Union (`|`)**

Combines elements from both sets without duplicates.

```python
set1 = {"Harry", "Ron"}
set2 = {"Hermione", "Ron"}

print(set1 | set2)
```

**Intersection (`&`)**

Returns elements that exist in both sets.

```python
print(set1 & set2)  # {'Ron'}
```

**Difference (`-`)**

Returns elements that exist in the first set but not the second.

```python
print(set1 - set2)  # {'Harry'}
```

## 7. Using a Set with a List of Dictionaries

We can use a list of dictionaries to store student information and a set to collect unique cities.

```python
students = [
    {"name": "Harry", "age": 20, "city": "London"},
    {"name": "Hermione", "age": 21, "city": "London"},
    {"name": "Ron", "age": 20, "city": "Manchester"},
    {"name": "Draco", "age": 21, "city": "London"},
    {"name": "Neville", "age": 20, "city": "Manchester"}
]

cities = set()

for student in students:
    cities.add(student["city"])

print(cities)
```

Output (the order may vary):

```text
{'London', 'Manchester'}
```

Even though multiple students live in the same city, the set stores each city only once.

We can also collect unique ages:

```python
ages = set()

for student in students:
    ages.add(student["age"])

print(ages)  # {20, 21}
```

## Key Takeaways

- A set stores unique values.
- Duplicate values are automatically eliminated.
- Use `add()` to add an element.
- Use `remove()` or `discard()` to remove an element.
- Use `len()` to count unique elements.
- Use `set(list_name)` to remove duplicates from a list.
- Sets are useful when we need to work with unique values, such as unique cities, names, or ages.