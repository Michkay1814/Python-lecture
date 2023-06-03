
#You want to buy something from Amazon. 
# The seller charges different prices for shipping cost
#based on location. For US it's 5$ for Europe it's 7$ for Canada 
# it's 3$ for other places it's 9$
#Create a program that:
#● Reads the cost of the product
#● Reads your location
#● Print the amount of money you have to pay
#Ouput: "You have to pay 23$, 20$ for the product
# and 3$ for shipping cos

 def calculate_total_cost(product_cost,location):
        if location == "US":
            shipping_cost = 5
        elif location == "EUROPE":
            shipping_cost = 7
        elif location == "CANADA":
            shipping_cost = 3
        else:
            shipping_cost = 9
        total_cost = product_cost + shipping_cost
        return total_cost
    

