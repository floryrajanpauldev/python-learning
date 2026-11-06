def main():
    x = int(input("Enter a number to get its square? "))
    print(f"The square of {x} is {square(x)}")

def square(n):
    return n * n

if __name__ == "__main__":
    main()