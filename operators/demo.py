# arithmetic operator

a=20
b=10

print("addition is:", (a+b))
print("substraction is:", (a-b))
print("multiplication is:", (a*b))
print("division is:", (a/b))
print("modulus is:", (a%b))
print("exponentian is:", (a**b))
print("floor division is:", (a//b))
# floor division means it performs divsion and gives the quotient as outout
# modulus gives remainder 

# rules
# first paranthesis are evaluated
# second exponentian are evaluated
# third multiplication, division, modulus, floor division are evaluated and given equal priority
# fourth addition and substraction  are evaluated
# last assignment are done

d= 1+(20-4)-2*10+20/5-(90//6)%4
print(d)
