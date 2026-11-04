# The pass statement is a placeholder. It tells Python to do nothing.

def main():
    x = get_int()
    print(f"You entered: {x}")

def get_int():
    while True:
        try:
            return int(input("Enter a number: ")) # here we use return to exit the function and return the value, no break needed
        except ValueError:
            pass  # Do nothing and prompt again 

main()