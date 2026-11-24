#Syntax for using map is - map(function, iterable)

numbers = [1, 2, 3, 4, 5]

def double(number):
    return number * 2

result = map(double, numbers)

print(list(result)) #[2, 4, 6, 8, 10]

