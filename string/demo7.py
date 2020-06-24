# strings are immutable
str = 'core python'
print(str[0])
print(str[1])
# str[0]='x'
# print(str[0])
s1= 'core'
s2 = 'python'
print(id(s1))
print(id(s2))
s1=s2
print(id(s1))
# untill unless the value is assigned to another variable the string value 
# cannot be changes on a particular variable