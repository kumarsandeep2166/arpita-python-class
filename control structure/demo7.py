# how take multiple inputs in a single line and assign it on multiple variables

# a,b,c = [int(x) for x in input("enter nums: ").split(',')]
# print(a+b+c)

# for loop else suit

a = [12,23,45,65,76]
x = int(input("enter the the element you want to search: "))
for i in a:
    if x == i:
        print("yes it is present")
        break
    else:
        print("it is not present")



    
