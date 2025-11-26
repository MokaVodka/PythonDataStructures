import matplotlib.pyplot as plot
import sort_algorithms as sa

# If script doesn't run, check path in util.py
from util import estimate_ordo

# Using uniform list sizes for comparisons,
# So we're not using sort_size_test module


# -- Simplify sort_run --
# Run all sorts and cache their results
def run_sorts():
    labels = ['selection', 'bubble', 'insertion']
    algos = [sa.selection_sort, sa.bubble_sort, sa.insertion_sort]

    # Limit of bubble sort on my machine
    sizeRange = range(1000, 5401, 300)
    sizes = [i for i in sizeRange]
    times = []

    print('// Running and caching sort algorithm performance //')

    for i in range(0, 3):
        print(f'Running {labels[i]} sort...')
        _, time = sa.sort_run(algos[i], sizeRange, 3)
        times.append(time)

    print('')

    return sizes, times


# -- Experiment b --
# Evaluate the performance of the sortAlgo
# Compare them with each other
def compare_algo(sizeTimes):
    sizes, times = sizeTimes

    print('// Experiment: Compare selection/bubble/insertion sort //')
    print('List size | Selection |  Bubble  | Insertion | Time ratio')

    # Comparison table
    for i in range(0, len(sizes)):
        timeS = round(times[0][i], 3)
        timeB = round(times[1][i], 3)
        timeI = round(times[2][i], 3)

        # Calculate the time ratio between algos
        maxVal = max(timeS, timeB, timeI)
        ratios = timeS / maxVal, timeB / maxVal, timeI / maxVal
        ratio = f'{ratios[0]:.2f} : {ratios[1]:.2f} : {ratios[2]:.2f}'

        print(f'{sizes[i]:>9} | {timeS:>9} | {timeB:>8} | ', end='')
        print(f'{timeI:>9} | {ratio}')

    print('')


# -- Experiment c --
# Verify the time complexity using log-log and linear regression
def best_fit_and_ordo(sizeTimes):
    sizes, times = sizeTimes
    labels = ['selection', 'bubble', 'insertion']
    bestFitCalc = []

    print('// Experiment: Calculate best fit line and O() //')

    for i in range(0, 3):
        print(f'Ordo of {labels[i]} sort:')
        coefficient, bestFitLine = estimate_ordo(sizes, times[i])
        bestFitCalc.append((coefficient, bestFitLine))
        print('')

    return bestFitCalc


# -- Experiment d --
# 2 Plots: run times and log-log fit
def display_plot(sizeTimes, bestFitCalc):
    sizes, times = sizeTimes

    ks = []
    lineYs = []
    logSizes = []
    logTimes = []

    for calc in bestFitCalc:
        coefficient, bestFitLine = calc
        lineY, logSize, logTime = bestFitLine

        ks.append(coefficient)
        lineYs.append(lineY)
        logSizes.append(logSize)
        logTimes.append(logTime)

    _, plots = plot.subplots(1, 2, figsize=(13, 5))
    timePlot, logPlot = plots

    # Configure plot (data)
    labels = ['selection', 'bubble', 'insertion']
    markers = ['+', 'x', '|']
    colors = ['r', 'g', 'b']

    for i in range(0, 3):
        labe, mark, col = labels[i], markers[i], colors[i]

        # Run time plot
        timePlot.scatter(sizes, times[i], marker=mark, c=col, label=labe)

        # Log-Log plot
        logSize = logSizes[i]
        labe = labe + ' with k = ' + str(ks[i])

        logPlot.scatter(logSize, logTimes[i], marker=mark, c=col, label=labe)
        logPlot.plot(logSize, lineYs[i], c=col, alpha=0.3)

    # Configure plot (general)
    timePlot.set_title('Run times for O(n^2) sort algorithms')
    timePlot.set_xlabel('Input list size')
    timePlot.set_ylabel('Average time of 3 runs with random lists')
    timePlot.legend()

    logPlot.set_title('Log-log plot for O(n^2) sort algorithms')
    logPlot.set_xlabel('Logarithm of list sizes')
    logPlot.set_ylabel('Logarithm of run times')
    logPlot.legend()

    plot.tight_layout()
    plot.show()


# -- Excecute experiment --
def experiments():
    sizeTimes = run_sorts()
    compare_algo(sizeTimes)
    bestFitCalc = best_fit_and_ordo(sizeTimes)
    display_plot(sizeTimes, bestFitCalc)


experiments()
