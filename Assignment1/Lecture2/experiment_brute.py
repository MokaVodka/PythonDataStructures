import matplotlib.pyplot as plot
from nsum import nsum_run
from nsum import threesum_brute

from nsum_size_test import get_default_sizeRange
from nsum_size_test import find_input_size
from nsum_correct_test import nsum_correct_test

# If script doesn't run, check path in util.py
from util import estimate_ordo


# -- Simplify nsum_run --
# sizeRange: list sizes, use default sizeRange if None
# fast: Use smaller sizeRange for faster tests
# repeat: Repetition to get average runtime
# printAvgTime: Print recorded average time to console
def run(sizeRange=None, fast=False, repeat=1, printAvgTime=False):
    if sizeRange is None or fast is True:
        sizeRange = get_default_sizeRange(threesum_brute, fast)
    return nsum_run(threesum_brute, sizeRange, repeat, printAvgTime)


# -- Experiment i --
# Implemented in nsum_size_test


# -- Experiment ii --
# Plot 3 separate runs, see if results fluctuate from run to run
def three_separate_runs(sizeRange=None, fast=False):
    print('// Experiment: Run time of 3 separate runs //')

    runs = []
    for _ in range(0, 3):
        sizes, times = run(sizeRange, fast, printAvgTime=True)
        runs.append((sizes, times))
        print('')

    _, scatterPlot = plot.subplots(1, 1, figsize=(9, 5))
    scatterPlot.scatter(runs[0][0], runs[0][1], marker='+', c='r')
    scatterPlot.scatter(runs[1][0], runs[1][1], marker='x', c='b')
    scatterPlot.scatter(runs[2][0], runs[2][1], marker='|', c='g')

    scatterPlot.set_title('3 separated runs of threesum_brute()')
    scatterPlot.set_xlabel('Input list size')
    scatterPlot.set_ylabel('Run time with random lists')
    scatterPlot.legend(['Run 1', 'Run 2', 'Run 3'])
    plot.show()


# -- Experiment iii --
# Plot the average time of 3 repeated runs
def three_repeated_runs(sizeRange=None, fast=False):
    print('// Experiment: Average run time of 3 repeated runs //')
    sizes, times = run(sizeRange, fast, 3, printAvgTime=True)
    print('')

    _, scatterPlot = plot.subplots(1, 1, figsize=(9, 5))
    scatterPlot.scatter(sizes, times, c='r')

    # Line too long smh
    pTitle = 'Average run time of 3 repeated runs of threesum_brute()'
    scatterPlot.set_title(pTitle)
    scatterPlot.set_xlabel('Input list size')
    scatterPlot.set_ylabel('Run time with random lists')
    plot.show()

    return sizes, times


# -- Experiment iv, v --
# Implemented in Util.linear_regress
# Computes best fit line and time complexity
def best_fit_and_ordo(sizes, times):
    print('// Experiment: Calculate best fit line and O() //')
    coefficient, bestFitLine = estimate_ordo(sizes, times)
    print('')

    return coefficient, bestFitLine


# -- Experiment vi --
# Plot straight line fit with the log-log data
def best_line_fit_plot(bestFitCalc):
    coefficient, bestFitLine = bestFitCalc
    lineY, logSize, logTime = bestFitLine

    _, logPlot = plot.subplots(1, 1, figsize=(9, 5))
    logPlot.scatter(logSize, logTime, c='r')
    logPlot.plot(logSize, lineY)

    logPlot.set_title(f'Best fit line with k = {coefficient}')
    logPlot.set_xlabel('Logarithm of list sizes')
    logPlot.set_ylabel('Logarithm of run times')
    plot.show()


# -- Excecute experiment --
def experiments():
    # Toggle fastExperiment to use smaller default list sizes instead
    fastExperiment = False

    nsum_correct_test(threesum_brute)
    sizeRange = find_input_size(threesum_brute, 100, 20)

    three_separate_runs(sizeRange, fastExperiment)

    sizes, times = three_repeated_runs(sizeRange, fastExperiment)
    bestFitCalc = best_fit_and_ordo(sizes, times)
    best_line_fit_plot(bestFitCalc)


experiments()
