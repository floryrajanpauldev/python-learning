try:
    x = int(input("Enter a number: "))

except ValueError:
    print("Please enter a valid number.")

else:
    print(f"the number you entered is: {x}")