

def check_number(num):

    if num  % 2 == 0:
      return True
    else:
       return False
    
# call function
print(check_number(7))

def check_divisibility(num1,num2):
    if num1 % num2==0:
      return True
    else:
     return False
# call function
print(check_divisibility(12,5))

# local Variable in function
#  local variable is a variable that is declared inside a function and is not  accessible 
#out of that function

def akum():
    a=12
    print('this is a local variable')
def emma():
    b=10
    print("the value is" , b)
    
akum()
emma()

#Global Variables

y1 =600

def acha():
    print(y1)
    
acha()

def blaise():
    y2=y1+20
    print(y2-4)
    
blaise()

# Write a Python function called calculate_factorial 
# that takes a positive integer as input and calculates 
# its factorial using a loop. 

# The factorial of a number n 
# is the product of all positive integers from 1 to n.

def calculate_factorial(n):
    if n ==0:
        return 1
    else:
        return n * calculate_factorial (n-1)

print(calculate_factorial(0))

# ITERATION METHOD


def Calculate_factorial(x):
    if x==3:
        return 3
    else:
       # call to the function
       return (x*Calculate_factorial(x-3))
    print(calculate_factorial(3))
    

    
    
