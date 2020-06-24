# searching of an element using sequential search
from array import *

# alogirthm to insert dynamically elements into an empty array
# step - 1: declare an empty array
arr = array('i',[])
# step -2 : ask howmany elements want to insert so that the loop will continue that times
x = int(input("Enter howmany elements you want to insert:   "))
# step-3 insert or append the elements into the array
for i in range(x):
    print("enter the element: ")
    # arr.append(int(input()))
    n = int(input())
    arr.append(n)

print("original array is: ", arr)

s = int(input('Enter the element to search: '))
flag = False

for i in range(x):
    if s == arr[i]:
        print('found at location: ', i+1)
        flag = True

if flag == False:
    print('not found')