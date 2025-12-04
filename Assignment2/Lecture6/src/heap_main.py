import Heap as hp


# Start demo
print('Heap demo starts')
heap = hp.Heap()
print('')


# Add int with add() and print heap content
for i in range(1, 11):
    heap.add(i)
print(heap)
print(f'get_size(): {heap.get_size()}')

for i in range(11, 21):
    heap.add(i)
print(heap)
print(f'get_size(): {heap.get_size()}')
print('')


# Demo peek(), pull_high()
print(f'peek(): {heap.peek()}')
print(f'pull_high(): {heap.pull_high()}')
print(heap)
print(f'get_size(): {heap.get_size()}')
print(f'is_empty(): {heap.is_empty()}')
print('')


# Test add and remove all
print('Test to remove all elements')
heap = hp.Heap()
for i in range(0, 21, 2):
    heap.add(i)
print(f'After adding elements: {heap}')

while not heap.is_empty():
    removed = heap.pull_high()
    print(f'Removed: {removed}')
print(f'After removing all elements: {heap}')
print(f'get_size(): {heap.get_size()}')
print(f'is_empty(): {heap.is_empty()}')
print('')


# Demo iterator
print('Iterator test')
heap = hp.Heap()
for i in range(1, 11):  # ==> 1,2,3,...,9,10
    heap.add(i)
for n in heap:
    print(n, end=' ')
print('')
print('')


# Demo exceptions
print('Accessing an empty heap')
empty = hp.Heap()
try:
    empty.peek()
except IndexError as exc:
    print(f'peek(): {exc}')

try:
    empty.pull_high()
except IndexError as exc:
    print(f'pull_high(): {exc}')
