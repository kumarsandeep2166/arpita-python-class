# use of pass statement
# pass statement does nothing
# in python a function, class and a loop can't left with empty codes. 
# so pass is used to do nothing
a = [2,4,-1,7,8,-3,-4,-5,9,6,-9]
for i in a:
    if i>0:
        pass
    else:
        print(i)

print("another way")
for i in a:
    if i<0:
        print(i)
    else:
        pass

def myfunction():
    pass

class X:
    pass

x=0
while x<10:
    x+=1
    if x<5:
        pass
    print(x)
print("out of loop")