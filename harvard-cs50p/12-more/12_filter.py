numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda number: number % 2 == 0, numbers))
print(even_numbers)


employees = [
    {"name": "John", "age": 25},
    {"name": "Mary", "age": 17},
    {"name": "David", "age": 32}
]
adults = list(filter(lambda employee: employee["age"] >= 18, employees))
print(adults)

