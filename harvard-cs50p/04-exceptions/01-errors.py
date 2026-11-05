try:
    x = int(input("Enter a number: "))
    result = 10 / x
    print(result)

except ValueError:
    print("Please enter a valid number.")

except ZeroDivisionError:
    print("You cannot divide by zero.")

print(x)