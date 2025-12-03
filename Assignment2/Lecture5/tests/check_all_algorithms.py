import test_sorting
from util_test import sort_algorithms


def check_all_algorithms():
    algos = sort_algorithms()

    for algo in algos:
        print(f'Checking {algo.__name__}()...')
        test_sorting.test_main(algo)


check_all_algorithms()
