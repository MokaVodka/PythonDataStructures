import matplotlib.pyplot as plot
import util_sort as su
import Heap as hp


def heap_sort(lst):
    result = []

    # Add elements to heap
    heap = hp.Heap()
    for num in lst:
        heap.add(num)

    # Pull from heap
    while not heap.is_empty():
        result.append(heap.pull_high())

    return result[::-1]


# -- Simplify sort_run --
# Run all sorts and cache their results
def run_sorts():
    labels = ['merge', 'quick', 'heap']
    algos = su.sort_algorithms()
    algos.append(heap_sort)

    # Limit of merge sort on my machine
    sizeRange = range(10 * 1000, 160 * 1000, 10 * 1000)
    sizes = [i for i in sizeRange]
    times = []

    print('// Running and caching sort algorithm performance //')

    for i in range(0, 3):
        print(f'Running {labels[i]} sort...')
        _, time = su.sort_run(algos[i], sizeRange, 5)
        times.append(time)

    print('')

    return sizes, times


# -- Comparison --
# Evaluate the performance of the sortAlgo
def compare_algo(sizeTimes):
    sizes, times = sizeTimes

    print('// Experiment: Compare merge/quick/heap sort //')
    print('List size | Merge | Quick |  Heap | Time ratio')

    # Comparison table
    for i in range(0, len(sizes)):
        timeM = round(times[0][i], 3)
        timeQ = round(times[1][i], 3)
        timeH = round(times[2][i], 3)

        # Calculate the time ratio between algos
        maxVal = max(timeM, timeQ, timeH)
        ratioM, ratioQ = timeM / maxVal, timeQ / maxVal
        ratioH = timeH / maxVal

        # Write NULL in case of RecursionError (returns time = -1)
        timeM = 'NULL' if timeM < 0 else timeM
        timeQ = 'NULL' if timeQ < 0 else timeQ

        ratioM = 'NULL' if ratioM < 0 else f'{ratioM:.2f}'
        ratioQ = 'NULL' if ratioQ < 0 else f'{ratioQ:.2f}'
        ratio = ratioM + ' : ' + ratioQ + ':' + f'{ratioH:.2f}'

        print(f'{sizes[i]:>9} | {timeM:>5} | {timeQ:>5} | ', end='')
        print(f'{timeH:>5} | {ratio}')

    print('')


def run_time_plot(sizeTimes):
    # Filter out invalid data (recursion exception)
    sizes, times = sizeTimes
    szM, tmM = su.filter_data(sizes, times[0])
    szQ, tmQ = su.filter_data(sizes, times[1])
    szH, tmH = su.filter_data(sizes, times[2])

    _, scatterPlot = plot.subplots(1, 1, figsize=(9, 5))
    scatterPlot.scatter(szM, tmM, marker='+', c='r')
    scatterPlot.scatter(szQ, tmQ, marker='x', c='g')
    scatterPlot.scatter(szH, tmH, marker='|', c='b')

    scatterPlot.set_title('Run times for sort algorithms')
    scatterPlot.set_xlabel('Input list size')
    scatterPlot.set_ylabel('Average time of 5 runs with random lists')
    scatterPlot.legend(['merge', 'quick', 'heap'])
    plot.show()


# -- Excecute experiment --
def experiments():
    sizeTimes = run_sorts()
    compare_algo(sizeTimes)
    run_time_plot(sizeTimes)


experiments()
