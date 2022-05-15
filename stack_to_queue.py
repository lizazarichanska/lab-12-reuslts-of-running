>>> stack = ArrayStack()
>>> stack.add(10)
>>> stack.add(100)
>>> stack.add(1000)
>>> stack.add(10000)
>>> queue = stack_to_queue(stack)
>>> print(queue)
[10000, 1000, 100, 10]
>>> print(stack)
[10, 100, 1000, 10000]
>>> print(stack.pop())
10000
>>> print(queue.pop())
10000
>>> stack.add(11)
>>> queue.add(11)
>>> print(queue)
[1000, 100, 10, 11]
>>> print(stack)
[10, 100, 1000, 11]
