budget = 150
count = 0
total_cost = 0

while count < 3:
   enter_grocery = input("Enter the grocery item: such as milk, eggs, bread, and vegetables: ")
   enter_cost = float(input(f"Enter the cost of the {enter_grocery}: "))
   print(f"Your grocery item is {enter_grocery}, costing: ${enter_cost:.2f}")
   print(f"Your budget is ${budget}")

   total_cost += enter_cost
   remaining_budget = budget - total_cost
   count += 1

   if(total_cost > budget):
       print("You have exceeded your budget.")
   elif(total_cost == budget):
       print("You have exactly met your budget.")
   else:
       print("\nYou are within your budget.")

print(f"Your total cost is ${total_cost:.2f}")  
print(f"Your remaining budget is ${remaining_budget:.2f}")  

