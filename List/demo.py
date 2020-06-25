lst = [12,23,34,45, 'python', 'arpita',12.45,10+6j]
# extract all elements from list
for i in lst:
    print(i)

# extract each element using while loop
i=0
n= len(lst)
while i<n:
    print(lst[i])
    i+=1

# slicing

print(lst[::-1]) #reverse the list elements