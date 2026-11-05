# sending the user a prompt to enter a number, and if they enter something that can't be converted to an integer, 
# we catch the ValueError and print an error message, then prompt again.

def main():
    x = get_int("Enter a number: ")
    print(f"You entered: {x}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt)) # here we use return to exit the function and return the value, no break needed
        except ValueError:
            print("Please enter a valid number.")  # Print an error message and prompt again

main()