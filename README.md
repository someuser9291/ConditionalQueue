# ConditionalQueue
A re-implementation of the classic thread-safe Queue, where the get function accepts a lambda expression as an argument to set a condition on what items can be returned.

```python
>>> from ConditionalQueue import ConditionalQueue
>>> q = ConditionalQueue()
>>> for i in xrange(10):
...     q.put(i)
...
>>> q.get(condition_lambda=lambda item: item >= 9)
9
>>> q.get(block=False, condition_lambda=lambda item: item == 9)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "ConditionalQueue.py", line 43, in get
    raise Empty()
Queue.Empty
>>> q.get(timeout=1, condition_lambda=lambda item: item == 9)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "ConditionalQueue.py", line 52, in get
    raise Empty()
Queue.Empty
```

The behavior of the ConditionalQueue is rather predictable, except for the next case:
No item matched the given condition and 'block' is True; then, get() hangs until a new item is placed in the queue.

If you didn't get the drawback; if your condition is complex, e.g a time condition, it will only be tested against Queue items once someone puts a new item into the Queue and not instantly when one of the items meets the condition.

To overcome this, never use a complex lambda with indefinite blocking; define a timeout, or use non-blocking. Thus, implement the complex condition polling in the code that contains the Queue.


# LinkedList
The ConditionalQueue uses a (singly) LinkedList to hold its items, because all usages of the items collection are more efficient under a linkd list rather than the builtin list, which is implemented as an array.

The beauty of this LinkedList class, which for some reason does not exist in the collections module (I couldn't even find a good implementation anywhere around the Internet), is that it has the same interface as the built-in python list.

```python
>>> from LinkedList import LinkedList
>>> l = LinkedList()
>>> l.append(1)
>>> l.extend([1, 2, 3])
>>> print l
[1, 1, 2, 3]
>>> l.reverse()
>>> print l
[3, 2, 1, 1]
>>> l.sort()
>>> print l
[1, 1, 2, 3]
>>> for item in l:
...     print item
...
1
1
2
3
>>> l[-1]
3
```

If efficiency is compared to an array-based list, the array list only beats the linked list when accessing it with an index
```python
l[1]
```
