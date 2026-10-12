# Python List append()
# append() adds one item to the end of a list.

# 1. Adding items to an empty list
tasks = []

tasks.append("Send invoices")
tasks.append("Book the venue")
tasks.append("Reply to emails")

print(tasks)


# 2. Adding an item from user input
tasks = []

tasks.append("Send invoices")
tasks.append("Book the venue")
tasks.append("Reply to emails")

task_item = input("Add an item: ")

tasks.append(task_item)

print(tasks)


# 3. append() modifies the existing list directly.
# It returns None, so don't assign its result back to tasks.

# Correct:
# tasks.append("Prepare presentation")

# Incorrect:
# tasks = tasks.append("Prepare presentation")