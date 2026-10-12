# While Loops
# A while loop repeats as long as its condition is True.

# 1. Basic while loop
count = 1

while count <= 5:
    print(count) #indentation matters 
    count += 1


# 2. Using break to exit a loop
count = 1

while count <= 5:
    if count == 3:
        break

    print(count)
    count += 1