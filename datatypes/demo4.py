r = range(10)
for i in r:
    if i == 4:        
        continue
    if i==8:
        break
    print(i)


# find out odd numbers within 50
print("odd numbers list")
r = range(1,50,2)
for i in r:
    print(i)
print("------------------")
# find out even numbers within 50
print("even numbers")
r = range(0,50,2)
for i in r:
    print(i)
print("-----------------------")

# find out odd and even numbers within 30 without using range.
print("even numbers")
i=0
while(i<=30):
    if i%2 == 0:
        print(i)
    i+=1   
print("-----------")

print("odd numbers")
i=0
while(i<=30):
    if i%2 == 1:
        print(i)
    i+=1   
print("-----------")