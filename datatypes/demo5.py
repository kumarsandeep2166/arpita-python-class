x = [10,20,25,36,65,10,25]
s = set(x)
print(s)

b = {10,20,12,20,10,15,14,18}
print(b)

s.update([23])
print(s)

s.remove(25)
print(s)

ch = set("Welcome to Core Python")
print(ch)
# we cannot retrieve the elements from set 
# print(ch[0:13])
# TypeError: 'set' object is not subscriptable
