# wap to display all positions of a sub string in a given string
str = input("enter a string: ")
sub = input('Enter a sub string: ')

i=0
flag = False
while i<len(str):
    pos = str.find(sub, 0, len(str))
    if pos!=-1:
        print('the sub string found at: ', pos+1)
        i=pos+1
        flag = True
        break
    else:
        i = i+1 #search next character onwards
if flag == False:
    print('sub string not found')