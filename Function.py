# function without a parameter
# example 1
def my_name():
    print('Welcome to Compudemy Happiness')

print(my_name())
# example 2
def my_profession():
    print("my name is Happiness ,am a DevOP ENGINEER" )
print(my_profession())

#function with parameter

#example 1
def course_func(name, age):
    print('my name is',name,'I am',age,'yrs old')

course_func("happiness",5)
# function with parameter
# example 2

def my_credentials(name,address,birthdate):
    print("hello",name,"Welcome to Compudemy")
    print("i live in",address)
    print("i was born on",birthdate)

my_credentials("Happiness","cooper line","june 1994")  

# example 3

def check_if_odd_or_even(number):
    if number % 2==0:
        print(number,"is even number")
    else:
        print(number,"is odd number")
    check_if_odd_or_even(40)