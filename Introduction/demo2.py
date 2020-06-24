a=None 
print(a)
# when an object is assigned to None then, the value become None Object

# NUmeric datatype
# 3 types
# int
a=12
print(a)
print(type(a))
# float
x=12.34
print(x)
print(type(x))
# complex
c1 = 10+34j
c2= -5+4j
c3=c1+c2
print("complex addition is: ", (c1+c2))
print(type(c3))

# representing binary, hexa, octa numbers
# binary -- bin()
# hex--- hex()
# octa --- oct()

# conversion of datatypes explicitly
x=12.78
print('int of x is:', int(x))
print('complex of x is:', complex(x))
print('float of x is:', float(x))
f=10
print("float of f is: ",float(f))
a,b=10,-8
print("complex of a,b is:", complex(a,b))

a=123
print("binary of a is: ", bin(a))
print("hexa deciaml of a is: ", hex(a))
print("octa decimal of a is: ", oct(a))

# boolean datatype
a=10>5
print(a)
b=5>10
print(b)

