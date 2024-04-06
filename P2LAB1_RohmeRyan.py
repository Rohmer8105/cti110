# Ryan Rohme
# March 3, 2024
# P2LAB1
# Write a program with a car's gas mileage (miles/gallon) and the cost of gas (dollars/gallon) as floating-point input
mileage = float(input())
gas_cost = float(input())

gas_cost_20 = 20 / mileage * gas_cost
gas_cost_75 = 75 / mileage * gas_cost
gas_cost_500 = 500 / mileage * gas_cost

print(f'{gas_cost_20:.2f} {gas_cost_75:.2f} {gas_cost_500:.2f}')
