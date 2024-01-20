'''
Write a menu-based program to implement stack to show
PUSH, POP and TRAVERSE operation, where each node of stack will
contain, Roll of student and name of student, as information.
'''
#############################################################################

stack = []

def PUSH():
    roll = int(input('Enter the roll number of students to push: '))
    name = input('Enter the name of the student to push: ')
    L = [roll, name]
    stack.append(L)
    print('successfully pushed!')

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
    msg = '''1. Push
2. Pop
3. Traverse
0. Exit'''
    ch = int(input(f'{msg}\nEnter your choice: '))
    if ch == 1:
        PUSH()
    elif ch == 2:
        POP()
    elif ch == 3:
        TRAVERSE()
    elif ch == 0:
        break
    else:
        print('Invalid choice!')