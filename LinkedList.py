from collections import MutableSequence


class Node(object):
    """
    A node that holds a value and possibly connects to a next node.
    """
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class LinkedList(MutableSequence):
    """
    A list where items are linked to each other.
    """
    def __init__(self, head=None):
        self.head = head
        self.__length = 0

    def append(self, value):
        self.insert(self.__length, value)

    def insert(self, index, value):
        if index == 0:
            self.head = Node(value, next_node=self.head)            
        else:
            current_node = self.__get_node_at(index - 1)

            new_node = Node(value)
            if current_node.next is not None:
                new_node.next = current_node.next.next

            current_node.next = new_node
        self.__length += 1

    def remove(self, value):
        current_node = self.head
        previous = None

        while current_node is not None:
            if current_node.value == value:
                break

            previous = current_node
            current_node = current_node.next

        if previous == None:
            self.head = current_node.next
        else:
            previous.next = current_node.next

        self.__length -= 1

    def pop(self, index):
        popped_node = None

        if index == 0:
            popped_node = self.head
            self.head = self.head.next
        else:
            current_node = self.__get_node_at(index - 1)

            popped_node = current_node.next
            current_node.next = current_node.next

        self.__length -= 1

        return popped_node.value

    # =========================
    # Emulating container type
    # =========================
    def __contains__(self, value):
        current_node = self.head
        found = False
        while current_node is not None and not found:
            if current_node.value == value:
                found = True
            else:
                current_node = current_node.next

        return found

    def __len__(self):
        return self.__length

    def __iter__(self):
        current_node = self.head

        while current_node is not None:
            yield current_node.value
            current_node = current_node.next

    def __getitem__(self, index):
        current_node = self.__get_node_at(index)
        return current_node.value

    def __setitem__(self, index, value):
        self.insert(index, value)
        self.pop(index + 1)

    def __delitem__(self, index):
        self.pop(index)

    # =========================
    # Internal functions
    # =========================
    def __get_node_at(self, index):
        if index > self.__length > 0 or (index < 0 and abs(index) > (self.__length + 1)):
            raise IndexError(index)

        current_node = self.head

        # Support for negative indexes as indexes from end-to-start
        if index < 0:
            index = self.__length - abs(index)

        for _ in xrange(index):
            current_node = current_node.next

        return current_node
