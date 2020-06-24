# membership operator
# in, not in
lst= ['a','b','c','d']
for a in lst:
    print(a)

# identity operator
#  is, is not

a=23
b=23
print(id(a))
print(id(b))
if (a is b):
    print("same")
else:
    print("not same")

lst1 = ['a','b','c','d']
print(id(lst))
print(id(lst1))
if (lst is  lst1):
    print("same")
else:
    print("not same")