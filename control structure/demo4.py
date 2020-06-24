# while loop
x=1
while x<=10:
    print(x)
    x+=1

print("end")

# using while loop display even numbers between 100 and 200
x=100
# while x>=100 and x<=200:
#     print(x)
#     x+=2

# how to take 2 variables as input at the same time and calculate even numbers

m,n = [int(x) for x in input("enter elements:").split(',')]

x=m
if x%2 !=0:
    x=x+1

while x>=m and x<=n:
    print(x)
    x+=2

