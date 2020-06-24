from numpy import *

arr = array([12,34,54,65,67])
print(arr)

# creating array using array()
arr = array([12,34,54,65,67])
print(arr)

a = array(arr)
# assigning an array on a variable by calling array()

print(a)
b=a
print(b)

# creating arrays using linspace()
# linspace(start, stop, n) 
# start is a point from where iteration will start
# stop is where iteration stops
# n is the number that parts the element should be divided equally

x =  linspace(0,10,5)
print(x)

x = linspace(0,15,5)
print(x)

x= linspace(0,100, 5)
print(x)


# creating array using logspace()
# logspace(start, stop, n)
# start is the starting point where iteration will start to the power to 10
# stop is the ending point where iteration will stop to the power to 10
# n  is the divider

y = logspace(1, 5, 4)
n = len(y)
for i in range(n):
    print('%.1f'%y[i])

# creating arrays using arrange()
# arange() in numpy is same as range()
a = arange(5,12)
print(a)
b = arange(1,21,2)
print(b)