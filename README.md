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
