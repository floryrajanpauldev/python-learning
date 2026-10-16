
# Lesson: Using insert()
# insert() adds an item at a specific index in a list.
# It takes two arguments: the index and the value to insert.

tasks = ["do laundry", "call mom"]
tasks.insert(0, "pay rent")
print(tasks)


todo = tasks.pop(2)
tasks.insert(0, todo)
print(tasks)