for i in range(5):
    print(i)

#we are not printing i so we can add the underscore to indicate that we are not using the variable i
#but printing _ will still give you the value of i in the range 0, 1, 2.
for _ in range(3):
    print("Hello, world!") 


#To iterate over the indices of a sequence, you can combine range() and len() as follows:
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])
