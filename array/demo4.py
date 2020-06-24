# sorting of elements in an array using bubble sort technique
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

# bubble sort technique
# 23 34 45 32 10 12 34 30
# 23 34 32 10 12 34 30 45
# 23 32 10 12 30 34 34 45
# 23 10 12 30 32 34 34 45
# 10 12 23 30 32 34 34 45
flag = False
for i in range(x-1): # 0 to n-1
    for j in range(x-1-i): # is from 0 to 1 element lesser than i
        if arr[j] > arr[j+1]: # 
            # swapping done here
            t = arr[j] # j=2 t=45
            arr[j] = arr[j+1] # 45 = 32  32 will be at 2nd place
            arr[j+1] = t #  45 will be at 3rd place
            flag = True
    if flag == False:
        break
    else:
        flag = False

print('the sorted array is: ', arr) 

# 1st case i=0 j=0
# 2nd case i=0 j=1
# 3rd case 1=0 j=2
# 4th i=0 j=3
# 5th i=0 j=4

# 6th i=1 j=0
# 7th i=1 j=1
# 8th i=1 j=2
# if arr[0] > arr[1]