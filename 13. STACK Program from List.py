'''
Write a program to create a list containing 10 integers with separate user
defined functions to perform the following operations based on this list.
    ● Push odd numbers of list into a stack, which will receive as argument.
    ● Pop the content of the stack.

Write the main program to create and traverse the list to integrate created functions, and to
display the content of stack by using second function.
    
For Example:
    If the Content of the list is as follows:
    [12, 13, 34, 56, 21, 79, 98, 22, 35, 38]
    Then Output of the code should be: 35 79 21 13
'''
#############################################################################

def pushodd(L):
    for ele in L:
        if ele % 2 != 0:
            stack.append(ele)

def pop(L):
    if len(stack) > 0:
        return stack.pop()
    else:
        print('Stack is underflow')

stack = []
integers = []

for i in range(10):
    num = int(input('Enter an integer: '))
    integers.append(num)

pushodd(integers)

print("List of Numbers:", integers)
print("Stack Contents (odd numbers):", end=" ")


while stack:
    print(pop(integers), end=' ')