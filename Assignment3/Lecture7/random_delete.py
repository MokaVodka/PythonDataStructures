import random
import BstSet as BST
import os


# Generates a random tree with 1023 unique values
def generate_tree():
    elements = 1023

    bst = BST.BstSet()

    while bst.size() < elements:
        data = random.randint(0, 2048)
        bst.add(data)

    return bst


#  Save dot text of tree (before and after delete)
def write_tree(bst, isBeforeDelete):
    # This should work if opened directory is Assignment3
    filePath = os.path.normcase(os.getcwd() + '/lecture7/output/')
    if not os.path.exists(filePath):
        os.mkdir(filePath)

    fileName = 'before_delete' if isBeforeDelete else 'after_delete'
    with open(f'{filePath}{fileName}.txt', 'w', encoding='utf-8') as file:
        file.write(bst.dot())


def experiment():
    # (a) Generates a random tree with 1023 unique (non-duplicate) values
    bst = generate_tree()

    # (b) Saves the tree (the dot text) in a file before_delete.txt
    write_tree(bst, True)

    # (c) Repeats the following 2000 times
    for _ in range(0, 2000):
        elements = bst.lr_inorder()
        deletedElements = []

        # i. Delete 512 random elements
        for deleted in range(0, 512):
            index = random.randint(0, 1022 - deleted)
            element = elements[index]
            bst.delete(element)
            deletedElements.append(element)

            elements.pop(index)

        # ii. Add the same 512 deleted elements again
        for element in deletedElements:
            bst.add(element)

    # (d) Saves the tree (the dot text) in a file after_delete.txt
    write_tree(bst, False)


experiment()
