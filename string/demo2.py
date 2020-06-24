# checking membership
# to check 1 string is present inside another or not
str = input('Enter a string:    ')
sub = input("enter the string to check: ")
# if sub in str:
#     print("yes it is present")
# else:
#     print('not present')

# in this case the entire second string is checked
# finding substrings
# logic
# find position of sub in str
# search from 0 to last character in str
# mainstring.find(substring, begining, ending)
n= str.find(sub, 0, len(str))
# find() return -1 if substring is not found 
if n==-1:
    print("the specified string is not found")
else:
    print("it is found at:", n+1)

