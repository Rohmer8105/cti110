# Ryan
# March 9, 2024
# P2HW1
# Assignment assess student ability to edit and enhance exiting programs

budget = float(input("Enter your budget: $"))

destination = input("Enter your travel destination: ")

gas_expense = float(input("Enter the amount you will spend on gas: $"))

accommodation_expense = float(input("Enter the amount you will spend on accommodation: $"))

food_expense = float(input("Enter the amount you will spend on food: $"))

total_expenses = gas_expense + accommodation_expense + food_expense

remaining_budget = budget - total_expenses

print("\n------------Travel Expenses------------")
print("Location:", destination)
print("Initial Budget: ${:.2f}".format(budget))
print("Fuel:  ${:.2f}".format(gas_expense))
print("Accommodation: ${:.2f}".format(accommodation_expense))
print("Food: ${:.2f}".format(food_expense))
print("--------------------------------------------")
print("Remaining Balance: ${:.2f}".format(remaining_budget))
