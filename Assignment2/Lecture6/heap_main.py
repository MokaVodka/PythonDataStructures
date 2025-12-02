import Heap as hp

# Program starts
print("Heap demo starts\n")
heap = hp.Heap()

# Add 10 integers using add_last and print list content
for i in range(1, 11):
    heap.add_last(i)
print(heap)
print("Size:", heap.size)

# Add 10 integers using add_first and print list content
for i in range(11, 21):
    heap.add_first(i)
print(heap)
print("Size:", heap.size)

# Demo get_last, get_first, remove_first, remove_last
print("\nget_last():", heap.get_last())
print("get_first():", heap.get_first())
print("remove_first():", heap.remove_first())
print("remove_last():", heap.remove_last())
print(heap)
print("Size:", heap.size)
print("is_empty():", heap.is_empty())


# Test add and remove all
print("\nTest to remove all elements")
heap = hp.Heap()   # A new empty heap
for i in range(100, 106):
    heap.add_first(i)
print("After adding elements:", heap)

while not heap.is_empty():
    heap.remove_last()
print("After removing all elements:", heap)
print("Size:", heap.size)
print("is_empty():", heap.is_empty())

# Demo iterator  (Part of Lecture 6)
print("\nIterator test")
heap = hp.Heap()   # A new empty heap
for i in range(1, 11):  # ==> 1,2,3,...,9,10
    heap.add_last(i)
for n in heap:
    print(n, end=" ")
print()

# Demo exceptions
print("\nAccessing an empty heap")
empty = hp.Heap()     # An empty heap
try:
    empty.get_last()
except IndexError as exc:
    print("get_last:", exc)

try:
    empty.get_first()
except IndexError as exc:
    print("get_first:", exc)

try:
    empty.remove_first()
except IndexError as exc:
    print("remove_first:", exc)

try:
    empty.remove_last()
except IndexError as exc:
    print("remove_last:", exc)
