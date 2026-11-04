def main():
    hello("Harry")
    goodbye("Harry")

def hello(name):
    print(f"hello, {name}")

def goodbye(name):
    print(f"goodbye, {name}")

# here we will not call main() because we want to use this file as a module in another file, 
# so we will not call main() here - else Hello Harry and Goodbye Harry will be printed when we import this file in another file

if __name__ == "__main__":
    main()  # this will only run if we run this file directly, not when we import it in another file 
