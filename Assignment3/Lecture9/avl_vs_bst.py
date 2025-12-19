import matplotlib.pyplot as plot
import random
import math
from util import create_BST
import AvlSet as AVL


# Computes the mean max depth of a BST
def mean_max_depth(h, create_tree):
    # Trees has 2h − 1 unique (non-duplicate) elements
    elements = (2 * h) - 1
    maxDepths = []

    for _ in range(0, 10):
        tree = create_tree()

        while tree.size() < elements:
            data = random.randint(0, 100)
            tree.add(data)

        maxDepths.append(tree.max_depth())

    return sum(maxDepths)/len(maxDepths)


def generate_dataset_for_plot():
    # h = 5, 6, ..., 19, 20
    treeDepths = [h for h in range(5, 21)]
    treeSizes = [(2 * h) - 1 for h in treeDepths]
    bstMeanDepths = []
    avlMeanDepths = []

    # Calculate mean over 10 runs
    for h in treeDepths:
        bstMeanDepths.append(mean_max_depth(h, create_BST))
        avlMeanDepths.append(mean_max_depth(h, AVL.AvlSet))

    return treeSizes, treeDepths, bstMeanDepths, avlMeanDepths


def log2_treeSizes(treeSizes):
    logTreeSizes = [math.log(size, 2) for size in treeSizes]
    return logTreeSizes


def plot_diagram(plotData, treeSizeLog):
    _, plots = plot.subplots(1, 2, figsize=(13, 5))
    meanDepthPlot, logDepthPlot = plots

    # Configure plot (visuals)
    markers = ['+', 'x', '|']
    colors = ['r', 'g', 'b']
    labels = ['Complete tree', 'BST', 'AVL']
    data = [plotData[1], plotData[2], plotData[3]]

    # Plot tree sizes vs Average of Max Depth
    for i in range(0, 3):
        meanDepthPlot.scatter(plotData[0], data[i], label=labels[i],
                              marker=markers[i], c=colors[i])
        meanDepthPlot.plot(plotData[0], data[i], c=colors[i], alpha=0.3)

    # Plot log tree sizes vs Average of Max Depth
    for i in range(0, 3):
        logDepthPlot.scatter(treeSizeLog, data[i], label=labels[i],
                             marker=markers[i], c=colors[i])
        logDepthPlot.plot(treeSizeLog, data[i], c=colors[i], alpha=0.3)

    # Configure plot (general)
    label = 'Depth of random input trees'

    meanDepthPlot.set_title(f'{label}')
    meanDepthPlot.set_xlabel('Tree size')
    meanDepthPlot.set_ylabel('Mean max depth of 10 runs with random lists')
    meanDepthPlot.legend()

    logDepthPlot.set_title(f'{label}')
    logDepthPlot.set_xlabel('Log base 2 tree size')
    logDepthPlot.set_ylabel('Mean max depth of 10 runs with random lists')
    logDepthPlot.legend()

    plot.tight_layout()
    plot.show()


def experiment():
    plotData = generate_dataset_for_plot()
    treeSizesLog = log2_treeSizes(plotData[0])
    plot_diagram(plotData, treeSizesLog)


experiment()
