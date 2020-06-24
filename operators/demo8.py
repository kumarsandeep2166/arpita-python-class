# bitwise operator
# there are following types
# bitwise complement operator(~)
# bitwise and operator (&)
# bitwise or operator (|)
# bitwise xor operator (^)
# bitwise left shift operator (<<)
# bitwise right shift opeartor (>>)

# here all the operations takes through 8 bit arrangement
x = 45
y = bin(x)
print('binary of x is : ', y)
x=45
y=25
print(x & y)
print(x | y)
print(x ^ y)
print(~x)
print(~y)
print(x<<2)
print(x>>2)