import matplotlib.pyplot as plot
from nsum import nsum_run
from nsum import threesum_pointers
from nsum import threesum_caching

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
def run_pointers(sizeRange=None, fast=False, repeat=1, printAvgTime=False):
    if sizeRange is None or fast is True:
        sizeRange = get_default_sizeRange(threesum_pointers, fast)
    return nsum_run(threesum_pointers, sizeRange, repeat, printAvgTime)


def run_caching(sizeRange=None, fast=False, repeat=1, printAvgTime=False):
    if sizeRange is None or fast is True:
        sizeRange = get_default_sizeRange(threesum_caching, fast)
    return nsum_run(threesum_caching, sizeRange, repeat, printAvgTime)


# -- Experiment d --
# Plot the average time of 3 repeated runs
def three_repeated_runs(sizeRangeP=None, sizeRangeC=None, fast=False):
    print('// Experiment: Average run time of 3 repeated runs //')

    print('threesum_pointers()')
    sizesP, timesP = run_pointers(sizeRangeP, fast, 3, printAvgTime=True)
    print('')

    print('threesum_caching()')
    sizesC, timesC = run_caching(sizeRangeC, fast, 3, printAvgTime=True)
    print('')

    _, scatterPlot = plot.subplots(1, 1, figsize=(9, 5))
    scatterPlot.scatter(sizesP, timesP, marker='+', c='r')
    scatterPlot.scatter(sizesC, timesC, marker='x', c='b')

    # Line too long smh
    pTitle = 'Average run time of 3 repeated runs'
    scatterPlot.set_title(pTitle)
    scatterPlot.set_xlabel('Input list size')
    scatterPlot.set_ylabel('Run time with random lists')
    scatterPlot.legend(['threesum_pointers()', 'threesum_caching()'])
    plot.show()

    return sizesP, timesP, sizesC, timesC


# -- Experiment e --
# Computes best fit line and time complexity
def best_fit_and_ordo(sizeTimes):
    sizesP, timesP, sizesC, timesC = sizeTimes

    print('// Experiment: Calculate best fit line and O() //')

    print('threesum_pointers()')
    coefficientP, bestFitLineP = estimate_ordo(sizesP, timesP)
    print('')

    print('threesum_caching()')
    coefficientC, bestFitLineC = estimate_ordo(sizesC, timesC)
    print('')

    return coefficientP, bestFitLineP, coefficientC, bestFitLineC


# -- Experiment f --
# Plot straight line fit with the log-log data
def best_line_fit_plot(bestFitCalc):
    coefficientP, bestFitLineP, coefficientC, bestFitLineC = bestFitCalc
    lineYP, logSizeP, logTimeP = bestFitLineP
    lineYC, logSizeC, logTimeC = bestFitLineC

    _, logPlot = plot.subplots(1, 1, figsize=(9, 5))

    labe = f'3-sum pointers with k = {coefficientP}'
    logPlot.scatter(logSizeP, logTimeP, marker='+', c='r', label=labe)
    logPlot.plot(logSizeP, lineYP, c='r', alpha=0.3)

    labe = f'3-sum caching with k = {coefficientC}'
    logPlot.scatter(logSizeC, logTimeC, marker='x', c='b', label=labe)
    logPlot.plot(logSizeC, lineYC, c='b', alpha=0.3)

    logPlot.set_title('Log-log plot for O(n^2) 3-sum algorithms')
    logPlot.set_xlabel('Logarithm of list sizes')
    logPlot.set_ylabel('Logarithm of run times')
    logPlot.legend()

    plot.show()


# -- Excecute experiment --
def experiments():
    # Toggle fastExperiment to use smaller default list sizes instead
    fastExperiment = False

    nsum_correct_test(threesum_pointers)
    nsum_correct_test(threesum_caching)

    sizeRangeP, sizeRangeC = None, None
    sizeRangeP = find_input_size(threesum_pointers, 800, 200)
    sizeRangeC = find_input_size(threesum_caching, 800, 200)

    sizeTimes = three_repeated_runs(sizeRangeP, sizeRangeC, fastExperiment)

    bestFitCalc = best_fit_and_ordo(sizeTimes)
    best_line_fit_plot(bestFitCalc)


experiments()
