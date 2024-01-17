def push_greater_75(key):
    if dict[key] > 75:
            stack.append(key)

def pop():
    if len(stack) > 0:
        return stack.pop()
    else:
        print('Stack is underflow')

stack = []
dict = {"OM": 76, "JAI": 45, "BABITA": 89, "ARUN": 65, "ANUJ": 90, "TARUN": 82}

for name in dict.keys():
    push_greater_75(name)

print ("Pushed names into the stack where marks > 75:")
while stack:
    print(pop())