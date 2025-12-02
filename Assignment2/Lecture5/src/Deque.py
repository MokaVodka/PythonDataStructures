# A head-and-tail implementation of a deque

# Each node is an instance of class Node
class Node:
    def __init__(self, value, next):
        self.value = value
        self.nxt = next


class DequeIter:
    def __init__(self, head):
        self.iterObj = head

    def __next__(self):
        if self.iterObj is None:
            raise StopIteration
        else:
            value = self.iterObj.value
            # Set next iter object to continue iterator
            self.iterObj = self.iterObj.nxt
            return value


class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # Add element n as last entry in deque
    def add_last(self, n):
        new = Node(n, None)
        if self.head is None:   # Empty queue
            self.head = new
            self.tail = new
        else:
            self.tail.nxt = new
            self.tail = new
        self.size += 1

    # Returns a string representation of the current deque content
    def __str__(self):
        s = "{ "
        node = self.head
        while node is not None:
            s += str(node.value) + " "
            node = node.nxt
        s += "}"
        return s

    # True if deque empty
    def is_empty(self):
        return self.size == 0

    # Add element n as first entry in deque
    def add_first(self, n):
        newNode = Node(n, self.head)
        self.head = newNode

        # Assign to tail if empty queue
        if self.tail is None:
            self.tail = newNode

        self.size += 1

    # Returns (without removing) the last entry in the deque.
    # Raises IndexError when accessing empty deque.
    def get_last(self):
        if self.size < 1:
            raise IndexError('Queue is empty, nothing to access')
        return self.tail.value

    # Returns (without removing) the first entry in the deque
    # Raises IndexError when accessing empty deque.
    def get_first(self):
        if self.size < 1:
            raise IndexError('Queue is empty, nothing to access')
        return self.head.value

    # Removes and returns the first entry in the deque.
    # Raises IndexError when accessing empty deque.
    # The case size = 1 requires speciall handling
    def remove_first(self):
        if self.size < 1:
            raise IndexError('Queue is empty, nothing to remove')

        headVal = self.head.value

        if self.size == 1:
            self.head = None
            self.tail = None

        else:
            self.head = self.head.nxt

        self.size -= 1
        return headVal

    # Removes and returns the last entry in the deque.
    # Raises IndexError when accessing empty deque.
    # The case size = 1 requires speciall handling
    def remove_last(self):
        if self.size < 1:
            raise IndexError('Queue is empty, nothing to remove')

        tailVal = self.tail.value

        if self.size == 1:
            self.head = None
            self.tail = None

        else:
            # Crawl to get previous Node of tail
            prevNode = self.head
            while prevNode.nxt != self.tail:
                prevNode = prevNode.nxt

            # Assign previous Node as tail
            self.tail = prevNode
            self.tail.nxt = None

        self.size -= 1
        return tailVal

    # Returns an iterator over the deque
    # allowing for simple iteration over all elements
    # Part of Lecture 6
    def __iter__(self):
        return DequeIter(self.head)
