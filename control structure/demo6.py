# wap to display the sum of elements present in a list
a = [10,23,12,34,56,78]
sum = 0
# use of for loop
for i in a:
    # print(i)
    sum+=i
print('sum is: ', sum)
print('------------------------------')

# use of while loop
i=0
sum=0
while i<len(a):
    sum+=a[i]
    i+=1
print('sum is: ', sum)
