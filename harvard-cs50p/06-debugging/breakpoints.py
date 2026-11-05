n = 5
for i in range(n):
    print("#" * i) # will print only 4 times because i is 0

print("\nPrinting 5 times")
for j in range(n):
    print("#" * (j+1)) # will print 5 times because j is 1, 2, 3, 4, 5
