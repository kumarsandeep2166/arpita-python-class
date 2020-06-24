x=10
y=10.89
z=123456677.6785600
print("value of x :%i" %x)
print("value of y :%d" %y)
print("value of y :%f" %y)
print("value of y :%.2f" %y)
print("value of y :%.3f" %y)
print("value of z :%.3f" %z)
print("value of z :%5.5f" %z)

# print(string.format)
a,b,c=10,12,13
print("number={},{}".format(a,b))
print("number={0},number={1}".format(a,b))
print("number={0},number={1}, number={2}".format(b,a,c))
print("number={one},number={two}, number={three}".format(one=b,two=a,three=c))