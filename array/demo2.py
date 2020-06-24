# indexing operation
from array import *

b = array('u',['a','b','c','d','e','f','g','h'])
# calculate the total size of array 'b' by calling len()
n = len(b)
print("using for loop")
for i in range(n):
    print(b[i], end=' ')


print('using while loop')
i=0
while i<n:
    print(b[i], end=' ')
    i+=1

print('slicing operation')
print('-----------------------')

print(b[0:6]) #prints values from index 0 to 6
print(b[1:])  # prints values from index 1
print(b[:7])  # prints values from index 0 to 7
print(b[0:7:2]) # prints skipping 1 element from index 0 to 7
print(b[3::2]) #prints values from index 3 to last index skipping 1 element

# python supports backward indexing but restricts backward traversing
print(b[-6:-1])
print(b[-7:])
print(b[-7::2])

for i in b[-7::2]:
    print(i)
