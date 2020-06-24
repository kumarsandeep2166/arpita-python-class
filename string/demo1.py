# indexing operation
str = 'core python'
#      012345678910
#       c o r e  p y t h o n
#    -11-10-9-8-7-6-5--4-3-2-1
for i in str:
    print(i, end='')

print()
# while loop in forward order
i=0
while(i<len(str)):
    print(str[i], end='')
    i+=1
print()

# while loop in backward order
i=-1
n=len(str)#11
while(i>=-n):
    print(str[i], end='')
    i-=1
print()

# another type of backwards traversing
str= 'core python'
i=1
n=len(str)
while(i<=n):
    print(str[-i], end='')
    i+=1
print()

# reverse order indexing using for loop
for i in str[::-1]:
    print(i, end='')
print()
# slicing operation
str = 'core python'
print('slicing operation')
print(str[::-1]) # shortcut of reversing a string
print(str[0:11])
print(str[1:10])
print(str[0:11:2])
print(str[:4:])

# repeating of strings
str = 'core python'
print(str*2)
print(str[5:7]*2)
print(str[5:7]*3)

# concatination of string
s1 = 'core '
s2 = 'python'
print(s1+s2)

# comparing of strings
s1='Bob'
s2 ='Box'
if(s1==s2):
    print('both are same')
else:
    print('not same')

s1='box'
s2='Box'
if(s1==s2):
    print('both are same')
else:
    print('not same')

# removing space from a string
str = '     Hrithik Roshan       '
print(str.strip()) # removes space from both sides of string
print(str.lstrip()) # removes space from left side of string
print(str.rstrip()) # removes space from right side of string
