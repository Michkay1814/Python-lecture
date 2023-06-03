#Create two variables x and y, 
# and initially set them each to a different number. Write a python script that swaps both values.

# Example: x = 10, y = 20
# Output: x = 20, y = 10

# method 1: using swap variable as temporary variable
x = int(input("enter the value x:"))
y = int(input("enter the value of y:"))
print("the value of x and y before swapping is:", x ,y)

swap = x
x = y
y =swap
print("the value of x is:", x)
print("the value of y is:", y)


# method 2: without using swap variable
x = int(input("enter the value of x for method 2:"))
y = int(input("enter the value of y for method 2:"))

x, y =y,x

print("the value of x is:",x)
print("the value of y is :",y)

# method 3: using a function
#swap=0

def swap_value(x,y):
    swap = x
    x = y
    y = swap
    numbers =(swap_value)
    int(input("enter the value of x for method  3:"))
    int(input("enter the value of y for method 3:"))
    
    
    print(numbers)












    


y=45
print(45) 


