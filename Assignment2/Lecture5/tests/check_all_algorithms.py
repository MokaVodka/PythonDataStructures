import test_sorting
import util_sort


def check_all_algorithms():
    algos = util_sort.sort_algorithms()

    for algo in algos:
        print(f'Checking {algo.__name__}()...')
        test_sorting.test_main(algo)


check_all_algorithms()
