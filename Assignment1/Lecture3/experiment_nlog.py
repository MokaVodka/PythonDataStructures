import matplotlib.pyplot as plot
import sort_algorithms as sa

# If script doesn't run, check path in util.py
from util import filter_plot_data

# Using uniform list sizes for comparisons,
# So we're not using sort_size_test module


# -- Simplify sort_run --
# Run all sorts and cache their results
def run_sorts():
    labels = ['merge', 'quick']
    algos = [sa.merge_sort, sa.quick_sort]

    # Limit of merge sort on my machine
    sizeRange = range(2000, 13501, 800)
    sizes = [i for i in sizeRange]
    times = []

    print('// Running and caching sort algorithm performance //')

    for i in range(0, 2):
        print(f'Running {labels[i]} sort...')
        _, time = sa.sort_run(algos[i], sizeRange, 5)
        times.append(time)

    print('')

    return sizes, times


# -- Experiment b --
# Evaluate the performance of the sortAlgo
# Compare them with each other
def compare_algo(sizeTimes):
    sizes, times = sizeTimes

    print('// Experiment: Compare merge/quick sort //')
    print('List size | Merge | Quick | Time ratio')

    # Comparison table
    for i in range(0, len(sizes)):
        timeM = round(times[0][i], 3)
        timeQ = round(times[1][i], 3)

        # Calculate the time ratio between algos
        maxVal = max(timeM, timeQ)
        ratioM, ratioQ = timeM / maxVal, timeQ / maxVal

        # Write NULL in case of RecursionError (returns time = -1)
        timeM = 'NULL' if timeM < 0 else timeM
        timeQ = 'NULL' if timeQ < 0 else timeQ

        ratioM = 'NULL' if ratioM < 0 else f'{ratioM:.2f}'
        ratioQ = 'NULL' if ratioQ < 0 else f'{ratioQ:.2f}'
        ratio = ratioM + ' : ' + ratioQ

        print(f'{sizes[i]:>9} | {timeM:>5} | {timeQ:>5} | ', end='')
        print(f'{ratio}')

    print('')


def run_time_plot(sizeTimes):
    # Filter out invalid data (recursion exception)
    sizes, times = sizeTimes
    szM, tmM = filter_plot_data(sizes, times[0])
    szQ, tmQ = filter_plot_data(sizes, times[1])

    _, scatterPlot = plot.subplots(1, 1, figsize=(9, 5))
    scatterPlot.scatter(szM, tmM, marker='+', c='r')
    scatterPlot.scatter(szQ, tmQ, marker='x', c='b')

    scatterPlot.set_title('Run times for O(n*log(n)) sort algorithms')
    scatterPlot.set_xlabel('Input list size')
    scatterPlot.set_ylabel('Average time of 5 runs with random lists')
    scatterPlot.legend(['merge', 'quick'])
    plot.show()


# -- Excecute experiment --
def experiments():
    sizeTimes = run_sorts()
    compare_algo(sizeTimes)
    run_time_plot(sizeTimes)


experiments()
