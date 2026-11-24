#Without enumerate():

names = ["John", "Mary", "David"]

for index in range(len(names)):
    print(index, names[index])

#With enumerate():

names = ["John", "Mary", "David"]
for index, name in enumerate(names):
    print(index, name)

names = ["John", "Mary", "David"]
for index, name in enumerate(names, start=1):
    print(index, name)

tasks = ["Learn Python", "Practice SQL", "Build a project"]
for number, task in enumerate(tasks, start=1):
    print(f"{number}. {task}")

    