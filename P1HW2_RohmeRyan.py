# Ryan
# February 25, 2024
# P1HW2
# You will create a program that does some basic math on numbers that are entered.


budget = float(input("Enter your budget: $"))

destination = input("Enter your travel destination: ")

gas_expense = float(input("Enter the amount you will spend on gas: $"))

accommodation_expense = float(input("Enter the amount you will spend on accommodation: $"))

food_expense = float(input("Enter the amount you will spend on food: $"))

total_expenses = gas_expense + accommodation_expense + food_expense

remaining_budget = budget - total_expenses

print("\nYour travel details:")
print("Destination:", destination)
print("Budget: $", budget)
print("Gas expense: $", gas_expense)
print("Accommodation expense: $", accommodation_expense)
print("Food expense: $", food_expense)
print("Total expenses: $", total_expenses)
print("Remaining budget: $", remaining_budget)
