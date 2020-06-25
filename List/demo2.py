num = [1,2,3,4,5]
n = len(num)
print('length of list is: ', n)

num.append(6)
print('after appending the list is: ', num)

num.insert(3,7)
print('after inserting the list is: ', num)

num1= num.copy()
print('after copying  the new list is: ', num1)

i = num.count(1)
print('no of times: ', i)

num.extend(num1)
print('after extending the list is: ', num)

num.remove(7)
print('after removing the list is: ', num)

num.pop()
print('after poping the list is: ', num)

num.reverse()
print('after reversing the list is: ', num)

num.sort()
print('after sorting the list is: ', num)

num.clear()
print('after clearing the list is: ', num)