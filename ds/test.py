from stack import Stack

s = Stack()
choice = 0
while choice<5:
    print('Stack operation')
    print('1.Push an element')
    print('2.pop an elements')
    print('3 peep element')
    print('4. search an element')
    print('5 exit')
    choice = int(input('enter ur choice:'))
    if choice ==1:
        element = int(input('enter an element:'))
        s.push(element)
    elif choice==2:
        element=s.pop()
        if element == -1:
            print('stack is empty')
        else:
            print('popped element is: ', element)
    elif choice == 3:
        element = s.pop()
        print('topmost elment is:', element)
    elif choice== 4:
        element = int(input('Enter the elment: '))
        pos = s.search(element)
        if pos == -1:
            print('stack is empty')
        elif pos == -2:
            print('element not found')
        else:
            print('element found at: ', pos)
    else:
        break

    print('the stack is:', s.display())
            
