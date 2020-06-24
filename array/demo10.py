# comparing array
from numpy import *
a = array([1,2,3,4,5])
b = array([1,3,6,5,3])

# manual comparing
c = a==b
print("result of c: ", c)
c = a>=b
print("result of c: ", c)
c = a<=b
print("result of c: ", c)


# use of any() and all()
c = a>b
print("result of c: ", any(c))
print("result of c: ", all(c))

c = a==b
print("result of c: ", any(c))
print("result of c: ", all(c))