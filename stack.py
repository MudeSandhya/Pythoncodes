#implement stack by using list
"""stack=[]
stack.append(3)
stack.append(5)
print(stack)
stack.pop()
print(stack)
stack.append(4)
stack.pop()
print(stack)
#implement stack by using collection deque
from collections import deque
stack=deque()
stack.append(3)
stack.append(4)
print(stack)
stack.pop()
print(stack)
stack.append(9)
stack.append(7)
stack.append(5)
print(stack.pop())
print(stack.pop())
print(stack)
"""
from queue import LifoQueue
stack=LifoQueue(maxsize=4)
stack.put(5)
print(list(stack))
stack.put(7)
stack.put(5)
print(stack)
stack.put(6)
print(stack)
stack.put(9)
print(stack)
print(stack.full())


'''for ele in stack:
    print(ele)'''
