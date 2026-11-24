double = lambda number: number * 2
print(double(6)) # 6 * 2 = 12

add = lambda a, b: a + b
print(add(10, 20)) #30


numbers = [1, 2, 3, 4, 5]
result = map(lambda number: number * 2, numbers)
print(list(result)) #[2, 4, 6, 8, 10]

numbers = [1, 2, 3, 4, 5, 6]
result = filter(lambda number: number % 2 == 0, numbers)
print(list(result)) #[2, 4, 6]

employees = [
    {"name": "John", "salary": 50000},
    {"name": "David", "salary": 70000},
    {"name": "Sarah", "salary": 60000}
]
result = sorted(employees, key=lambda employee: employee["salary"])
print(result)

#To sort in descending order:

resultDesc = sorted(
    employees,
    key=lambda employee: employee["salary"],
    reverse=True
)

print(resultDesc)