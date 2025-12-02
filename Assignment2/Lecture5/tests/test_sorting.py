import pytest
import random
from util_sort import gen_random_list


# Test correctness
def correct_test(sort_algo, listSize):
    toSort = gen_random_list(listSize)
    expect = sorted(toSort)
    result = sort_algo(toSort)
    assert result == expect, f"Exp {expect}, got {result}"


# Test sorted
def sorted_test(sort_algo, listSize, reversed=False):
    toSort = gen_random_list(listSize)
    toSort = sorted(toSort)
    expect = toSort

    if reversed:
        toSort = toSort[::-1]

    result = sort_algo(toSort)
    assert result == expect, f"Exp {expect}, got {result}"


# Test duplicates
def duplicate_test(sort_algo, listSize=15, lst=None):
    toSort = []

    if lst:
        toSort = lst
    else:
        while len(toSort) < listSize:
            toSort.append(random.randint(-listSize*10, listSize*10))
            toSort.append(toSort[len(toSort) - 1])

    expect = sorted(toSort)
    result = sort_algo(toSort)
    assert result == expect, f"Exp {expect}, got {result}"


# Main test
def main_test(sort_algo):

    # Test list size of 0 | 1
    correct_test(sort_algo, 0)
    correct_test(sort_algo, 1)

    # Test duplicates All | Pair | Variable amount
    duplicate_test(sort_algo, lst=[7, 7, 7, 7, 7, 7, 7, 7])
    duplicate_test(sort_algo, listSize=15)
    duplicate_test(sort_algo, lst=[9, 7, 7, 7, 7, 10, 10, 1, 5])

    # Test random
    correct_test(sort_algo, 15)

    # Test sorted
    sorted_test(sort_algo, 15, reversed=False)
    sorted_test(sort_algo, 15, reversed=True)
