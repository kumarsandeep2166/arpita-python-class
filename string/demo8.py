# replacing string with another string
# stringname.replace(old, new)
str = 'core java'
s2 = str.replace('java', 'python')
print(s2)

# splitting and joining
str = 'book,cat,dog,earphone,flower,goat,horse'
# incase of using split() on a string the value comes with a list
print(type(str))
str1 = str.split(',')
print(str1)
print(type(str1))
# incase of calling join() on a list we have specify the separator
str2 = ' '.join(str1)
print(str2)
print(type(str2))
# split() converts a string into a list and join() converts a list into a string