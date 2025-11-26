import nsum as ns


# -- Get default input sizeRange --
# These sizeRanges are based on previous find_input_size testings
# fast: Use a smaller sizeRange for faster testing
def get_default_sizeRange(nsumAlgo, fast=False):
    if nsumAlgo == ns.threesum_brute:
        return range(50, 351, 20) if fast else range(140, 441, 20)

    if nsumAlgo == ns.threesum_pointers:
        return range(200, 4601, 300) if fast else range(800, 5201, 300)

    if nsumAlgo == ns.threesum_caching:
        return range(200, 4401, 300) if fast else range(800, 5001, 300)


# -- Experiment i --
# Find a suitable range of input list sizes
# about 15 sizes and execution times from 0.1-5 seconds
def find_input_size(nsumAlgo, startSize=0, increment=0):
    label, sizeRange = None, None
    size, increase = startSize, increment
    time, min, max = 0, 0, 0

    # Set starting size to scan size for
    # Adjust increase to get more accurate times (smaller = slow)
    if nsumAlgo == ns.threesum_brute:
        label = 'brute'
        if startSize == 0 or increment == 0:
            size, increase = 100, 20

    if nsumAlgo == ns.threesum_pointers:
        label = 'pointers'
        if startSize == 0 or increment == 0:
            size, increase = 800, 200

    if nsumAlgo == ns.threesum_caching:
        label = 'caching'
        if startSize == 0 or increment == 0:
            size, increase = 800, 200

    print(f'// Testing suitable input for 3-sum ({label}) //')

    # End scan when max time margin is close to 0.15
    while 5 - time > 0.15:
        print(f'Testing list size: {size}', end='')
        # Repeat 3 times for more accurate measurement
        _, times = ns.nsum_run(nsumAlgo, range(size, size + 1, 1), 3)
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
    rerun = input('Rerun 3-sum with sizeRange and time printed? (y/ANY): ')
    if rerun == 'y':
        ns.nsum_run(nsumAlgo, sizeRange, 3, True)

    print('')

    return sizeRange
