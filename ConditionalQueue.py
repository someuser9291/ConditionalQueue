from Queue import Queue, Empty
from time import time as _time

from LinkedList import LinkedList


class ConditionalQueue(Queue):
    """
    Create a queue capable of limiting its get function to a condition.
    """
    def __init__(self, maxsize=0):
        Queue.__init__(self, maxsize=maxsize)
        # We use a linked list to maximize efficiency when removing items
        self.__items = LinkedList()

    def get(self, block=True, timeout=None, condition_lambda=None):
        """Remove and return an item from the queue.

        If optional args 'block' is true and 'timeout' is None (the default),
        block if necessary until an item is available. If 'timeout' is
        a non-negative number, it blocks at most 'timeout' seconds and raises
        the Empty exception if no item was available within that time.
        Otherwise ('block' is false), return an item if one is immediately
        available, else raise the Empty exception ('timeout' is ignored
        in that case).

        If condition_lambda is specified, only an item matching the given condition_lambda can ever be returned 
        from this function. 
        The condition_lambda is called with a queue item each time. If it returns True, the item is returned.
        WARNING: If no item matched the condition and 'block' is True, the function will hang at least until a new item
                 is placed in the queue.
        """
        with self.not_empty:
            endtime = None
            if timeout is not None:
                endtime = _time() + timeout

            while True:
                for potential_item in self.__items:
                    if condition_lambda is None or condition_lambda(potential_item):
                        self.__items.remove(potential_item)
                        self.not_full.notify()
                        return potential_item

                if not block:
                    raise Empty()
                elif timeout is None:
                    self.not_empty.wait()
                elif timeout < 0:
                    raise ValueError("'timeout' must be a non-negative number")
                # If blocking with a timeout
                else:
                    remaining = endtime - _time()
                    if remaining <= 0.0:
                        raise Empty()
                    self.not_empty.wait(remaining)


    # Override these methods to implement other queue organizations
    # (e.g. stack or priority queue).
    # These will only be called with appropriate locks held

    # Initialize the queue representation
    def _init(self, maxsize):
        pass

    def _qsize(self, len=len):
        return len(self.__items)

    # Put a new item in the queue
    def _put(self, item, index=-1):
        if index >= 0:
            self.__items.insert(index, item)
        else:
            self.__items.append(item)

    # Get an item from the queue
    def _get(self, index=0):
        return self.__items.pop(index)
