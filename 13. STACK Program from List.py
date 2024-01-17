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