>>> queue = ArrayQueue()
>>> queue.add(10)
>>> queue.add(100)
>>> queue.add(1000)
>>> queue.add(10000)
>>> stack = queue_to_stack(queue)
>>> print(queue)
[10, 100, 1000, 10000]
>>> print(stack)
[10000, 1000, 100, 10]
>>> print(stack.pop())
10
>>> print(queue.pop())
10
>>> stack.add(11)
>>> queue.add(11)
>>> print(queue)
[100, 1000, 10000, 11]
>>> print(stack)
[10000, 1000, 100, 11]
