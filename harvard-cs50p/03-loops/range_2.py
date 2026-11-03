"""We are trying to print a block of wall 
3 bricks on each line and 3 rows
###
###
###
"""
# we can use a nested for loop to print the wall of bricks
print("\nUsing 2 dimentional for loop\n")

for i in range(3):  # outer loop for rows
    for j in range(3):  # inner loop for columns
        print("#", end="")  # print a brick without a newline
    print()  # print a newline after each row

# another way to print the wall of bricks is to use a single for loop and string multiplication    print("\nNew way to do it")
print("\nNew way to do it\n")

for i in range(3):
    print("#" * 3)  # print 3 bricks in a row   