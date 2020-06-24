# processing the arrays
from array import *
arr = array('i', [10,20,30,23,24,56,67,10,23,56])
print('the original array is: ', arr)

# append 23 at last
arr.append(23)
arr.append(35)
print('the newly created array is: ', arr)

# remove the last element
arr.pop()
print('the newly created array is: ', arr)

# remove 6th index from arr
arr.pop(6)
print('the newly created array is: ', arr)

# remove 10 from array
arr.remove(10)
print('the newly created array is: ', arr)

# reverse the array
arr.reverse()
print('the newly created array is: ', arr)

# insert 90 at 5th position
arr.insert(5,90)
print('the newly created array is: ', arr)

# finding position of 23
i =arr.index(90)
print('the index is: ', i)

# convert array into list, bytes and string
lst = arr.tolist()
print('the list is: ',lst)
str = arr.tostring()
# for i in str:
#     print('the string is: ', i)

b= arr.tobytes()
# for i in b:
#     print('the bytes is: ', i)