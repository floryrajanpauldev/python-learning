numbers = [1, 2, 3, 4, 5, 6]

even_numbers = {
    number: number * number
    for number in numbers
    if number % 2 == 0
}

print(even_numbers)


names = ["John", "Mary", "David"]
ages = [25, 28, 32]

employees = {
    name: age
    for name, age in zip(names, ages)
}

print(employees)