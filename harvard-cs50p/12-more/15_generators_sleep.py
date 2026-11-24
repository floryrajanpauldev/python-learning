# Counting the sheeps to fall a sleep
#if the count - n is massive then the fucntion will not work but generator solves this problem
#Let's say n = 1,000,000.


#Regular function

def count_sheep(n):
    for i in range(n):
        print("🐑" * (i + 1))

count_sheep(5)


#Generator version
def count_sheep(n):
    for i in range(n):
        yield "🐑" * (i + 1) #(one value at a time)

for sheep in count_sheep(5):
    print(sheep)

"""
The output looks exactly the same, but the generator produces each line one at a time.

The important difference:
- print() displays the result immediately.
- yield produces a value and pauses the function.
- The for loop requests the next value and resumes the generator.

A regular function can still work with a large count if it doesn't store all results.
 The main advantage is that a generator lets you process values one at a time.
"""