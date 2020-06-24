# mathematical operations on array
from numpy import *

arr1 = array([12,23,34,45,67,87])
arr2 = array([10,12,54,67,89,45])
arr3 = array([4,9,16,256,81,25,36,49])

print("sum of both arrays is: ",arr1+arr2)
print("substraction of both array is: ",arr1-arr2)

print("add 5: ",arr1+5)
print("minus 5: ",arr2-5)

print("sin value of arr1: ",sin(arr1))
print("cos value of arr1: ",cos(arr1))
print("tan value of arr1: ",tan(arr1))
print("arcsin value of arr1: ",arcsin(arr1))
print("arcos value of arr1: ",arccos(arr1))
print("arctan value of arr1: ",arctan(arr1))
print("absolute value of arr1: ", abs(arr1))
print("log 10 value of arr1: ", log10(arr1))
print("log value of arr1: ", log(arr1))
print("square value of arr1: ", pow(arr1, 2))
print("square root value of arr3: ", sqrt(arr3))
print("min  value of arr3: ", min(arr3))
print("max value of arr3: ", max(arr3))
print("median value of arr3: ", median(arr3))
print("mean value of arr3: ", mean(arr3))
print("sort  of arr3: ", sort(arr3))
