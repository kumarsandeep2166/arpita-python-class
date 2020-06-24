# using index method
str = input('Enter a string:    ')
sub = input("enter the string to check: ")

# index() ---  mainstring.index(substring, begining, ending)
try:
    n = str.index(sub, 0, len(str))
except:
    print('sub string not found')
else:
    print('found at: ', n+1)