stack = []
size = 5
def PUSH():
    if len(stack) < size:
        roll = int(input('Enter the roll number of students to push: '))
        name = input('Enter the name of the student to push: ')
        L = [roll, name]
        stack.append(L)
        print('successfully pushed!')
    else:
        print('Stack overflow')

def POP():
    if len(stack) > 0:
        print(stack.pop(),'popped successfully!')
    else:
        print('Stack underflow')


def TRAVERSE():
    if len(stack) > 0:
        print('Elements of stack:')
        for node in stack:
            print(node)
    else:
        print('Stack underflow')

while True:
    print('1. Push')
    print('2. Pop')
    print('3. Traverse')
    print('4. Exit')
    ch = int(input('Enter your choice: '))
    if ch == 1:
        PUSH()
    elif ch == 2:
        POP()
    elif ch == 3:
        TRAVERSE()
    elif ch == 4:
        break
    else:
        print('Invalid choice!')