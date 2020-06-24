# logical operator
# and, or, not
x=100
y=200
print(x and y)
print(x or y)
print(not x)
# and ---  if x is false then it return x, otherwise return y
# or ----- if x is false then it return y, otherwise return x
m=bin(x)
n=bin(y)
print('m 100 : ',m)
print('n 200 : ',n)
print('and is: ',m and n)
print("or is : ",m or n)

# and
# -------
#  T T = T
#  T F = F
#  F T = F
#  F F = F

# or
# -------
#  T T = T
#  T F = T
#  F T = T
#  F F = F