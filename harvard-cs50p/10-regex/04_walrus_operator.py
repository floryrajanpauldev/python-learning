#Example 1 – Without Walrus Operator
numbers = [1, 2, 3, 4, 5]

count = len(numbers)

if count > 3:
    print(f"There are {count} numbers")


#Example 2 – With Walrus Operator
numbers = [1, 2, 3, 4, 5]

if (count := len(numbers)) > 3:
    print(f"There are {count} numbers")

#Example 3 – Using while
while (name := input("Enter your name: ")) != "quit":
    print(f"Hello, {name}")



