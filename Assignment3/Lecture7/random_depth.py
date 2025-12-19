import matplotlib.pyplot as plot
import random
import math
import BstSet as BST


# Computes the mean max depth of a BST
def mean_max_depth(h):
    # Trees has 2^h − 1 unique (non-duplicate) elements
    elements = (2 ** h) - 1
    maxDepths = []

    for _ in range(0, 10):
        bst = BST.BstSet()

        while bst.size() < elements:
            data = random.randint(-elements * 2, elements * 2)
            bst.add(data)

        maxDepths.append(bst.max_depth())

    return sum(maxDepths)/len(maxDepths)


def generate_dataset_for_plot():
    # h = 5, 6, ..., 19, 20
    treeDepths = [h for h in range(5, 21)]
    treeSizes = [(2 ** h) - 1 for h in treeDepths]
    meanDepths = []

    # Calculate mean over 10 runs
    for h in treeDepths:
        print(f'Running {h} height trees...')
        meanDepths.append(mean_max_depth(h))
    print('Finished caculations!')

    return treeSizes, treeDepths, meanDepths


def log2_treeSizes(treeSizes):
    logTreeSizes = [math.log(size, 2) for size in treeSizes]
    return logTreeSizes


def plot_diagram(treeSizes, treeDepths, meanDepths, isLog):
    _, plots = plot.subplots(1, 2, figsize=(13, 5))
    meanDepthPlot, treeDepthPlot = plots

    # Configure plot (visuals)
    markers = ['+', 'x']
    colors = ['r', 'b']

    # Plot tree sizes vs Average of Max Depth
    meanDepthPlot.scatter(treeSizes, meanDepths,
                          marker=markers[0], c=colors[0])
    meanDepthPlot.plot(treeSizes, meanDepths, c=colors[0], alpha=0.3)

    # Plot tree sizes vs Depth of Complete Tree (i.e 5, 6, ..., 19, 20)
    treeDepthPlot.scatter(treeSizes, treeDepths,
                          marker=markers[1], c=colors[1])
    treeDepthPlot.plot(treeSizes, treeDepths, c=colors[1], alpha=0.3)

    # Configure plot (general)
    label = 'Log base 2 tree sizes' if isLog else 'Tree sizes'

    meanDepthPlot.set_title(f'{label} vs Mean max depth (BST)')
    meanDepthPlot.set_xlabel(f'{label}')
    meanDepthPlot.set_ylabel('Mean max depth of 10 runs with random lists')

    treeDepthPlot.set_title(f'{label} vs Tree depth (Complete)')
    treeDepthPlot.set_xlabel(f'{label}')
    treeDepthPlot.set_ylabel('Tree depths')

    plot.tight_layout()
    plot.show()


def experiment():
    treeSizes, treeDepths, meanDepths = generate_dataset_for_plot()
    plot_diagram(treeSizes, treeDepths, meanDepths, False)

    treeSizes = log2_treeSizes(treeSizes)
    plot_diagram(treeSizes, treeDepths, meanDepths, True)


experiment()
