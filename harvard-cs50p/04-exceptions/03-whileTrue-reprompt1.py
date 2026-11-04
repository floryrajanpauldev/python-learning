"""while True
while True: creates a loop that continues running indefinitely because the condition True is always true.
1. You usually use break to stop the loop when a particular condition is met or 
2. return the value if using a function."""

while True:
    answer = input("Do you want to continue? (yes/no): ")

    if answer == "no":
        break

    print("Continuing...")

print("Loop stopped!")