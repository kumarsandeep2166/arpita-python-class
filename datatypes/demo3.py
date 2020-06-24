lst = [45,78,12.36, 'python', 'java', 'a', 10-6j, 'php', 'dotnet', 12,35,76]
tup = tuple(lst)
print(tup)
# tup[0]=32
# print(tup)
# TypeError: 'tuple' object does not support item assignment
print(tup[0:6])
print(tup[0:10:2])
print(tup[0::3])
print(tup*2)
print(tup[-2])
print(tup[-8:-1])
print(tup[-10:-1:2])