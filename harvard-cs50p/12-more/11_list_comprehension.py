#Without list comprehension

numbers = [1, 2, 3, 4, 5]

result = []

for number in numbers:
    result.append(number * 2)

print(result)

#with list comprehension
#Syntax [expression for item in iterable]
#"experssion is - Perform an operation (number * 2) on each item in the iterable and collect the results into a new list."

numbers = [1, 2, 3, 4, 5]

result = [number * 2 for number in numbers]

print(result)