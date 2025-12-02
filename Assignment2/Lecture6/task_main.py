import Heap as hp
import Task as ts


# Start demo
print('Heap-Task demo')
heap = hp.Heap()
tasks = [ts.Task(100, 'Groceries'), ts.Task(5, 'Check mail'),
         ts.Task(80, 'Clean home'), ts.Task(50, 'Excercise'),
         ts.Task(30, 'Do laundry'), ts.Task(85, 'Do homework'),
         ts.Task(70, 'Schedule Christmas date'),
         ts.Task(40, 'Check email'), ts.Task(60, 'Fix lamp'),
         ts.Task(10, 'Decorate home')]


# Add tasks with add()
for task in tasks:
    heap.add(task)

# Print heap content with pull_high()
while not heap.is_empty():
    print(heap.pull_high())
