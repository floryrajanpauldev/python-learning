balance = 0

def main():
    print("First Balance:", balance)
    deposit(100)
    withdraw(50)
    print("Final Balance", balance)

def deposit(n):
    global balance # refer the global balance variable
    balance += n

def withdraw(n):
    global balance # refer the global balance variable
    balance -= n

main()