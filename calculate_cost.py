def calculate_total_cost(location, product_cost):
    if location.upper() == "US":
        shipping_cost = 5
    elif location.upper() == "Europe":
        shipping_cost = 7
    elif location.upper() == "Canada":
        shipping_cost = 3
    else:
        shipping_cost = 9
    total_cost = shipping_cost + product_cost
    return total_cost