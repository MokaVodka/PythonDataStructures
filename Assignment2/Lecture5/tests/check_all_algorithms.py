import test_sorting
import util_sort


def check_all_algorithms():
    algos = util_sort.sort_algorithms()

    for algo in algos:
        print(algo.__name__)


check_all_algorithms()
