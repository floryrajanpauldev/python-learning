#Use * to unpack a list or tuple into positional function arguments.

def add(a, b, c):
    return a + b + c

numbers = [10, 20, 30]

result = add(*numbers)

print(result)# 60