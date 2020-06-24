a=b=12
print("sum is:", (a+b))

# this is an example of single line comment
# example on how to take an input from keyboard
# x = input("Enter your name::  ")
# print('you have entered: ',x)

# program on multi line comments
def example():
    """
    this fucntion will return 1 after calling
    when we call this fucntion  this will automatically return 1
    """
    '''
    this is also a type of multi line comment
    by this example we are now cleared what single and mutiple line comment is.
    '''
    return 1
print("the returned value from fucntion is: ",example())

def add(x,y):
    """
    this function will add two numbers
    """
    print("sum is:  ",(x+y))

add(10,25)