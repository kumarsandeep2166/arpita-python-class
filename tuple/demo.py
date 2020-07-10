# list comprehension
# use of matrix
mat = [[1,2,3],[3,4,5],[4,5,6]]
print(mat)
# display elements row by row
print('row by row')
for i in mat:
    print(i)

print('elements in 1st row')
for i in mat[0]:
    print(i)
print('elements in 2nd row')
for i in mat[1]:
    print(i)
print('elements in 3rd row')
for i in mat[2]:
    print(i)

# list comprehension
square=[]
for i in range(1,11):
    square.append(i**2)
print(square)

# add each element of 1 list with another
l1= [1,2,3]
l2= [2,3,4]
l3=[]
for i in l1:
    for j in l2:
        l3.append(i+j)
print(l3)
l1= [1,2,3]
l2= [2,3,4]
l3 = l1+l2
print(l3)