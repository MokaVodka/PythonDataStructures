class Heap:
    # Construct empty heap
    def __init__(self):
        self.array = []

    # String repr. of heap content
    def __str__(self):
        s = "{ "
        for node in self.array:
            if node is not None:
                s += str(node) + " "
        s += "}"
        return s

    # Current heap size
    def get_size(self):
        arraySize = len(self.array)

        # Array needs to be at least 2 to be valid
        # Because nodes start at i = 1, while None is in i = 0
        if arraySize > 1:
            return arraySize - 1
        else:
            return 0

    # True if heap empty, otherwise False
    def is_empty(self):
        return self.get_size() == 0

    # Return (without removing) top element
    def peek(self):
        # Empty heap
        if self.is_empty():
            raise IndexError('Heap is empty, nothing to peek')
        return self.array[1]

    # Add element to heap
    def add(self, elem):
        # Empty heap
        if self.is_empty():
            self.array.append(None)

        # Add element as last node
        self.array.append(elem)

        # Swap with smaller parent
        child = len(self.array) - 1  # Starts at last node
        parent = child // 2
        childVal = self.array[child]
        parentVal = self.array[parent]

        while parentVal is not None and childVal > parentVal:
            # Swap value
            self.array[parent] = childVal
            self.array[child] = parentVal

            # Set new comparison indexes
            child = parent
            parent = child // 2
            parentVal = self.array[parent]

    # Pull highest from heap
    def pull_high(self):
        # Empty heap
        if self.is_empty():
            raise IndexError('Heap is empty, nothing to pull')

        # Get highest value before removing
        topVal = self.array[1]

        # Move last node to root
        self.array[1] = self.array[-1]
        self.array.pop(-1)

        # When empty, Heap should not have None at i = 0
        # Thus, reset array
        if self.is_empty():
            self.array = []
            return topVal

        # Swap with highest child
        arraySize = len(self.array)
        parent, child = 1, 2  # Starts at root and left child
        parentVal = self.array[parent]

        # Stop swap process when:
        # a. child reaches end of array
        # b. child reaches end of current parent
        while child < arraySize and child <= ((parent * 2) + 1):
            childVal = self.array[child]

            if childVal > parentVal:
                # Swap value
                self.array[child] = parentVal
                self.array[parent] = childVal

                # Set new comparison indexes
                parent = child
                child = parent * 2
            else:
                child += 1

        return topVal

    # Support for iteration over all elements
    def __iter__(self):
        self._iterIndex = 1
        return self

    def __next__(self):
        if self.is_empty() or self._iterIndex > self.get_size():
            raise StopIteration
        value = self.array[self._iterIndex]
        self._iterIndex += 1
        return value
