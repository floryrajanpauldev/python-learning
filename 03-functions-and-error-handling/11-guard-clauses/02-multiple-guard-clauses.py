
# Lesson: Multiple Guard Clauses
# Guard clauses check for conditions that prevent a function from continuing.
# return exits the function when a guard condition is met.

def fill_order(menu, order):
    if len(menu) == 0:
        print("Nothing available.")
        return

    if order not in menu:
        print(f"{order} isn't on the menu.")
        return

    menu.remove(order)
    print(f"Order placed: {order}")


# Example 1: The menu is empty
fill_order([], "Coffee")

# Example 2: The requested item isn't on the menu
fill_order(["Tea", "Juice"], "Coffee")

# Example 3: The requested item is available
fill_order(["Tea", "Coffee", "Juice"], "Coffee")
