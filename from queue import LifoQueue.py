from queue import LifoQueue
stack=LifoQueue()
stack.put('A')
stack.put('B')
stack.put('c')
print(stack.get())