# Python List append()

## 1. What is append()?

`append()` is a list method that adds one item to the end of an existing list.

## 2. Adding items to a list

```python
tasks = []

tasks.append("Send invoices")
tasks.append("Book the venue")
tasks.append("Reply to emails")

print(tasks)
```

Output:

```text
['Send invoices', 'Book the venue', 'Reply to emails']
```

## 3. Adding user input

```python
tasks = []

task_item = input("Add an item: ")
tasks.append(task_item)

print(tasks)
```

The user's input is stored in `task_item` and then added to the list.

## 4. Important points

- `[]` creates an empty list.
- `append()` adds one item at a time.
- New items are added to the end of the list.
- `append()` modifies the existing list directly.
- `append()` returns `None`; it does not return the updated list.

## 5. Common mistake

Incorrect:

```python
tasks = tasks.append("Send invoices")
```

This assigns `None` to `tasks`, because `append()` returns `None`.

Correct:

```python
tasks.append("Send invoices")
```

## Key Takeaway

Use `list.append(item)` when you want to add one item to the end of a list.