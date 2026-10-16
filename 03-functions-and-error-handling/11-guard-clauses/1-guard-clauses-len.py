
# Lesson: Guard Clauses
# A guard clause checks whether a function should stop early.
# return exits the function when the guard condition is met. 
# IndexError fix is check witn len if it's 0 

def serve_order(orders):
    if len(orders) == 0:
        print("Nothing left to serve.")
        return

    item = orders.pop(0)
    print(f"Serving: {item}")


serve_order([])
serve_order(["apple"])
