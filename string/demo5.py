str = input("enter a string: ")
sub = input('Enter a sub string: ')

flag = False
n = len(str)
pos = -1
while True:
    pos = str.find(sub, pos+1, n)
    if pos == -1:
        break
    print('found at ', pos+1)
    flag = True

if flag == False:
    print('sub string not found')

