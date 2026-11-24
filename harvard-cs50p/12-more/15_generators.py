from pathlib import Path


def get_numbers():
    yield 1
    yield 2
    yield 3

numbers = get_numbers()

print(next(numbers))  # 1
print(next(numbers))  # 2
print(next(numbers))  # 3



def read_file(filename):
    with open(filename) as file:
        for line in file:
            yield line

for line in read_file(Path(__file__).with_name("data.txt")):
    print(line)