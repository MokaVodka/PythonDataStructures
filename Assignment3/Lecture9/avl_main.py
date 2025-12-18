import AvlSet as AVL

# a ) Adds the numbers 1-20 (in that order) and prints the DOT text
print('\nAdd')
avl = AVL.AvlSet()
for num in range(1, 21):
    avl.add(num)

print('DOT printout')
print(avl.dot())

# b ) Deletes the numbers 1-0 (in that order) and prints the DOT text
print('\nDelete')
for num in range(1, 11):
    avl.delete(num)

print('DOT printout')
print(avl.dot())
