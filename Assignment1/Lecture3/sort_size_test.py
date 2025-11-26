import sort_algorithms as sa


# -- Get default input sizeRange --
# These sizeRanges are based on previous find_input_size testings
# fast: Use a smaller sizeRange for faster testing
def get_default_sizeRange(sortAlgo, fast=False):
    if sortAlgo == sa.selection_sort:
        return range(500, 8001, 500) if fast else range(1500, 10001, 600)

    if sortAlgo == sa.bubble_sort:
        return range(500, 4501, 275) if fast else range(1000, 5401, 300)

    if sortAlgo == sa.insertion_sort:
        return range(1000, 8001, 500) if fast else range(2000, 11501, 650)

    if sortAlgo == sa.merge_sort:
        return range(1000, 10001, 600) if fast else range(2000, 13501, 800)

    if sortAlgo == sa.quick_sort:
        if fast:
            return range(10000, 500000, 35000)
        else:
            return range(30000, 740001, 50000)

    if sortAlgo == sa.improved_quick_sort:
        if fast:
            return range(10000, 500000, 35000)
        else:
            return range(30000, 900001, 62000)


# Find a suitable range of input list sizes
# about 15 sizes and execution times from 0.1-5 seconds
# Somehow this function is really inconsistent (see line 78)
def find_input_size(sortAlgo, startSize=0, increment=0):
    label, sizeRange = None, None
    size, increase = startSize, increment
    time, min, max = 0, 0, 0

    # Set starting size to scan size for
    # Adjust increase to get more accurate times (smaller = slow)
    if sortAlgo == sa.selection_sort:
        label = 'selection'
        if startSize == 0 or increment == 0:
            size, increase = 1500, 500

    if sortAlgo == sa.bubble_sort:
        label = 'bubble'
        if startSize == 0 or increment == 0:
            size, increase = 1000, 250

    if sortAlgo == sa.insertion_sort:
        label = 'insertion'
        if startSize == 0 or increment == 0:
            size, increase = 1000, 500

    if sortAlgo == sa.merge_sort:
        label = 'merge'
        if startSize == 0 or increment == 0:
            size, increase = 2000, 800

    if sortAlgo == sa.quick_sort:
        label = 'quick'
        if startSize == 0 or increment == 0:
            size, increase = 30000, 50000

    if sortAlgo == sa.improved_quick_sort:
        label = 'improved quick'
        if startSize == 0 or increment == 0:
            size, increase = 30000, 50000

    print(f'// Testing suitable input for {label} sort //')

    # End scan when max time margin is close to 0.15
    while 5 - time > 0.15:
        print(f'Testing list size: {size}', end='')
        # Somehow this line runs slower than normal
        # Maybe because of range() size being 1?
        # Doesn't seem to be a problem with 3-sums, but it is with sorts
        _, times = sa.sort_run(sortAlgo, range(size, size + 1, 1), 3)
        time = round(times[0], 2)
        print(f' | Average runtime: {time}')

        # Set valid min and max size
        if time >= 0.1 and min == 0:
            min = size
        if time <= 5:
            max = size

        size += increase

    # Calculate approriate sizeRange
    increase = (max + 1 - min) // 14
    sizeRange = range(min, max + 1, increase)
    print(f'Found valid input size range: {sizeRange}')

    # Rerun and print the size range (for debugging)
    rerun = input('Rerun sort with sizeRange and time printed? (y/ANY): ')
    if rerun == 'y':
        sa.nsum_run(sortAlgo, sizeRange, 3, True)

    print('')

    return sizeRange
