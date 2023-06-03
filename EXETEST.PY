from calculate_cost import calculate_total_cost
product_cost = float(input("What is the product cost: "))
location = input(("Enter your location (US, Europe, Canada, others): "))
total_cost = calculate_total_cost(location, product_cost)
print("You have to pay $", total_cost)