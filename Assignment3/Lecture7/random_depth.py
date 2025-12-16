import matplotlib
import random
import BstSet as BST


def generate_data(h):
    # Trees has 2h − 1 unique (non-duplicate) elements
    elements = (2 * h) - 1
    data = set()
    while len(data) < elements:
        data.add(random.randint(0, 100))
    return data


# Computes the mean max depth of a BST
def mean_max_depth(h):
    maxDepths = []

    for _ in range(0, 10):
        bst = BST.BstSet()
        data = generate_data(h)

        for n in data:
            bst.add(n)
        maxDepths.append(bst.max_depth())

    return sum(maxDepths)/len(maxDepths)


def generate_dataset_for_plot():
    # h = 5, 6, ..., 19, 20
    treeSizes = [(2 * h) - 1 for h in range(5, 21)]
    depths = [h for h in range(5, 21)]
    meanDepths = []

    # Calculate mean over 10 runs
    for h in depths:
        meanDepths.append(mean_max_depth(h))

    return treeSizes, depths, meanDepths


def plot_treeSizes_meanDepths():

    # Plot tree sizes vs Average of Max Depth

    # Plot tree sizes vs Depth of Complete Tree (i.e 5, 6, ..., 19, 20)

    pass


def plot():
    # Plot log2 tree sizes vs Average of Max Depth

    # Plot log2 tree sizes vs Depth of Complete Tree (i.e 5, 6, ..., 19, 20)

    # Is it roughly a straight line?
    # We expect the two diagrams (in a single 2 × 1 pattern) to pop up.

    # expect a O(log(n)) behavior
    pass


def experiment():
    treeSizes, depths, meanDepths = generate_dataset_for_plot()
    plot_treeSizes_meanDepths()


experiment()
