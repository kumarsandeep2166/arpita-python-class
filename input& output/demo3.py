var1, var2, var3 = [int(x) for x in input("enter 3 nums: ").split(",")]
print("sum is: ", var1+var2+var3)

# take two inputs from key board and find sum , multiplication of those numbers
x = int(input("enter 1st num: "))
y = int(input("enter 2nd num: "))
print("sum of {0}, {1} is :{2}".format(x,y, x+y))
print("prod of {0}, {1} is :{2}".format(x,y, x*y))