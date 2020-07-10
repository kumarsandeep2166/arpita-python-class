# linkedlist program
# take an empty list
ll = []
# append some elements into the list
ll.append("America")
ll.append("Russia")
ll.append("India")
ll.append("Brazil")
ll.append("England")

print('the new list is:', ll)
choice =0
while choice<6:
    print('LinkedList operation')
    print('1.Append an element')
    print('2.insert an elements')
    print('3 remove element')
    print('4.replace element ')
    print('5. search an element')
    print('6 exit')
    choice=int(input("enter the choice: "))
    if choice==1:
        element = input('enter the element:')
        ll.append(element)
        print('the new list is:',ll)
    elif choice==2:
        element = input('enter the element:')
        pos = int(input('at what pposition:'))
        ll.insert(pos, element)
        print('the new list is:',ll)
    elif choice==3:
        try:
            element = input('enter the element:')
            ll.remove(element)
            print('the new list is:',ll)
        except ValueError:
            print('element not found')
    elif choice==4:
        element = input('enter the element:')
        pos = int(input('at what pposition:'))
        ll.pop(pos)
        ll.insert(pos, element)
        print('the new list is:',ll)
    elif choice==5:
        element = input('enter the element:')
        try:
            pos = ll.index(element)
            print('the element found at:', pos, 'position')
        except ValueError:
            print('element not found')
    else:
        break
print('list = ',ll)

        


