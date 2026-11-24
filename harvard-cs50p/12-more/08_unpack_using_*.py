#The * operator collects multiple remaining values into a list.

numbers = [10, 20, 30, 40, 50]

first, *remaining = numbers

print("First number", first)
print("Remaining numbers using *", remaining)
"""
Output:

10
[20, 30, 40, 50]
"""


#You can also collect values from the middle:

first, *middle, last = numbers

print(first)   # 10
print(middle)  # [20, 30, 40]
print(last)    # 50