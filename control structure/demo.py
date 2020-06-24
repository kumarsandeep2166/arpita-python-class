num=1
if num == 1:
    print("yes")

num = 10
if(num%2 == 0):
    print("yes")
else:
    print("NO")

# how to check a number is even or odd

num = int(input("Enter a num: "))
if(num%2 == 0):
    print(num, " is an even number")
else:
    print(num, " is an not even number")

# to test if a number is in between two numbers

a = int(input("Enter 1st number :"))
b = int(input("Enter 2nd number :"))
c = int(input("Enter 3rd number :"))
if (c>=a and c<=b):
    print(c," lies between ", a, " and ", b)
else:
    print(c," doesnt lies between ", a, " and ", b)