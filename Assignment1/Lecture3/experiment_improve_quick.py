import matplotlib.pyplot as plot
import sort_algorithms as sa

# If script doesn't run, check path in util.py
from util import gen_random_list
from util import filter_plot_data


# -- Simplify sort_run --
# Run all sorts and cache their results
# sizeRange: input sizeRange
# isRandom: Use random list or reversed sorted list
def run_sorts(sizeRange, isRandom):
    labels = ['quick', 'improved quick']
    algos = [sa.quick_sort, sa.improved_quick_sort]
    repeat = 10

    sizes = [i for i in sizeRange]
    times = []

    label = 'random' if isRandom else 'reverse sorted'
    print(f'// Sorting {label} lists and cache algorithm performance //')

    for i in range(0, 2):
        print(f'Running {labels[i]} sort...')

        time = None
        if isRandom:
            _, time = sa.sort_run(algos[i], sizeRange, repeat)
        else:
            time = sort_reveresed_list(algos[i], sizeRange, repeat)

        times.append(time)

    print('')

    return sizes, times


def sort_reveresed_list(sortAlgo, sizeRange, repeat):
    sizes = [size for size in sizeRange]
    avgTimes = []

    for size in sizes:
        # Repeat runs to get average time
        totalTime = 0

        for _ in range(0, repeat):

            # Use the default sort as it would be redundant to use our sorts
            reversedLst = gen_random_list(size)
            reversedLst = sorted(reversedLst)
            reversedLst = reversedLst[::-1]

            time = -1
            try:
                time = sa.sort_single_run(sortAlgo, reversedLst)
            except RecursionError:
                print(f'Exceeded max recursion depth at list size {size}')
                print('Stopping process')
                print('')

                while len(avgTimes) < len(sizes):
                    avgTimes.append(-1)
                return avgTimes

            totalTime += time

        avgTime = totalTime/repeat
        avgTimes.append(avgTime)

    return avgTimes


# Evaluate the performance of the sortAlgo
# Compare them with each other
def compare_algo(sizeTimes, isRandom=False):
    sizes, times = sizeTimes
    label = 'random' if isRandom else 'reverse sorted'
    print(f'// Experiment: Compare merge/quick sort with {label} lists //')
    print('List size | Quick | Improved | Time ratio')

    # Comparison table
    for i in range(0, len(sizes)):
        timeQ = round(times[0][i], 3)
        timeIQ = round(times[1][i], 3)

        # Calculate the time ratio between algos
        maxVal = max(timeQ, timeIQ)
        ratioQ, ratioIQ = timeQ / maxVal, timeIQ / maxVal

        # Write NULL in case of RecursionError (returns time = -1)
        timeQ = 'NULL' if timeQ < 0 else timeQ
        timeIQ = 'NULL' if timeIQ < 0 else timeIQ

        ratioQ = 'NULL' if ratioQ < 0 else f'{ratioQ:.2f}'
        ratioIQ = 'NULL' if ratioIQ < 0 else f'{ratioIQ:.2f}'
        ratio = ratioQ + ' : ' + ratioIQ

        print(f'{sizes[i]:>9} | {timeQ:>5} | {timeIQ:>8} | ', end='')
        print(f'{ratio}')

    print('')


def run_time_plot(sizeTimes, isRandom=False):
    # Filter out invalid data (recursion exception)
    sizes, times = sizeTimes
    szQ, tmQ = filter_plot_data(sizes, times[0])
    szIQ, tmIQ = filter_plot_data(sizes, times[1])

    label = 'random' if isRandom else 'reverse sorted'

    _, scatterPlot = plot.subplots(1, 1, figsize=(9, 5))
    scatterPlot.scatter(szQ, tmQ, marker='+', c='r', label='quick')
    scatterPlot.plot(szQ, tmQ, c='r', alpha=0.3)

    scatterPlot.scatter(szIQ, tmIQ, marker='x', c='b', label='improved quick')
    scatterPlot.plot(szIQ, tmIQ, c='b', alpha=0.3)

    scatterPlot.set_title('Run times for quick sort algorithms')
    scatterPlot.set_xlabel('Input list size')
    scatterPlot.set_ylabel(f'Average time of 10 runs with {label} lists')
    scatterPlot.legend()
    plot.show()


# -- Excecute experiment --
def experiments():
    # Limit of quick sort on my machine
    # Change values for better data
    sizeRange = range(50 * 1000, 5000 * 1000 + 1, 350 * 1000)
    sizeTimesRandom = run_sorts(sizeRange, True)
    compare_algo(sizeTimesRandom, True)
    run_time_plot(sizeTimesRandom, True)

    # Smaller list size because it takes way too long
    # Change values for better data
    sizeRange = range(1 * 1000, 250 * 1000 + 1, 17 * 1000)
    sizeTimesSorted = run_sorts(sizeRange, False)
    compare_algo(sizeTimesSorted, False)
    run_time_plot(sizeTimesSorted, False)


experiments()
