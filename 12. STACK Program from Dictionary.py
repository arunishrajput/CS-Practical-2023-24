'''
Consider the following dictionary containing names and marks as key value
pairs of 6 students.
{"OM":76, "JAI":45, "BABITA":89, "ARUN":65, "ANUJ":90, "TARUN":82}
Write a program, with separate user defined functions to perform the following operations:
● Push the keys (name of the student) of the dictionary into a stack, where the corresponding
value (marks) is greater than 75. Function will receive key as argument.
● Pop the content of the stack and return it.
Write the main program to integrate created functions to display the content of stack.
'''
#############################################################################

def push_greater_75(key):
    if dict[key] > 75:
            stack.append(key)

def pop():
    if len(stack) > 0:
        return stack.pop()
    else:
        print('Stack is underflow')

stack = []
stack, dict = {"OM": 76, "JAI": 45, "BABITA": 89, "ARUN": 65, "ANUJ": 90, "TARUN": 82}

for name in dict.keys():
    push_greater_75(name)

print ("Pushed names into the stack where marks > 75:")
while stack:
    print(pop())