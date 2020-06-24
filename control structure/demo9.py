# break statement
x=10
while x>=1:
    print(x)
    x-=1
    if x==5:
        break    
print("out of loop")

# continue statement
x=0
while x<10:
    x+=1
    if x>=5:
        # print(x)
        continue
    print(x)
print("out of loop")

# continue statement
# continue statement means loop will start from begining from the same line
# continue used to redirect the flow from begining 

x=10
while x>0:
    x-=1
    if x>=5:        
        continue
    print(x)
print("out of loop")