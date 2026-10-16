
# Lesson: Function Parameters and Arguments


# 1. A function with one parameter
def greet(name):
    print(f"Welcome, {name}!")


# Call the function with different arguments
greet("Jenny")
greet("Marcus")
greet("Mary")
greet("Sam")


# 2. A function with multiple parameters
def greet_with_messages(name, unread_messages):
    print(f"Welcome, {name}! You have {unread_messages} new messages.")


greet_with_messages("Jenny", 15)
greet_with_messages("Marcus", 8)


# 3. A variable in the global scope
shop_name = "The Coffee Shop"


def show_welcome():
    print(f"Welcome to {shop_name}")


show_welcome()


# 4. Parameters are local to their function
def greet_customer(name):
    print(f"Hello, {name}!")


greet_customer("Jenny")

# The variable name is only available inside greet_customer().
# Trying to use name here would raise a NameError:
# print(name)
