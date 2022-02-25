stack = []

# append() function to push
# element in the stack
stack.append('a')
stack.append('b')
stack.append('c')
"""print(stack.top())"""
print('Initial stack')
print(stack)

# pop() function to pop
# element from stack in
# LIFO order
print('\nElements popped from stack:')

print(len(stack)-1)
print(stack.pop())
print(stack.pop())
print(stack.pop())

print('\nStack after elements are popped:')
print(stack)
