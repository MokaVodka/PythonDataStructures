import pytest
import random
from util_test import sort_algorithms
from util_test import gen_random_list


# Act and Assert
def act_assert(toSort, sort_algo):
    expect = sorted(toSort)
    result = sort_algo(toSort)
    assert result == expect, f"Exp {expect}, got {result}"


@pytest.fixture
def sort_algo():
    algos = sort_algorithms()
    return algos[0]


# List population
def populated_list():
    return gen_random_list(15)


# Test empty
def test_empty(sort_algo):
    toSort = []
    act_assert(toSort, sort_algo)


# Test 1 length list
def test_len1(sort_algo):
    toSort = [0]
    act_assert(toSort, sort_algo)


# Test random
def test_random(sort_algo):
    toSort = populated_list()
    act_assert(toSort, sort_algo)


# Test sorted
def test_sorted(sort_algo, reversed=False):
    toSort = sorted(populated_list())
    if reversed:
        toSort = toSort[::-1]
    act_assert(toSort, sort_algo)


# Test duplicates
def test_duplicate(sort_algo, dupeType=0):
    toSort = populated_list()

    # All dupes
    if dupeType == 0:
        for i in range(1, len(toSort)):
            toSort[i] = toSort[0]

    # Pair dupes
    elif dupeType == 1:
        for i in range(1, len(toSort), 2):
            toSort[i] = toSort[i - 1]

    # Varying dupes
    else:
        endDupe = 1
        for i in range(1, len(toSort)):
            if i == endDupe:
                endDupe += random.randint(1, 4)
            else:
                toSort[i] = toSort[i - 1]

    act_assert(toSort, sort_algo)


# Main test
def test_main(sort_algo):

    # Test list size of 0 | 1
    test_empty(sort_algo)
    test_len1(sort_algo)

    # Test duplicates All | Pair | Variable amount
    test_duplicate(sort_algo, 0)
    test_duplicate(sort_algo, 1)
    test_duplicate(sort_algo, 2)

    # Test random
    test_random(sort_algo)

    # Test sorted
    test_sorted(sort_algo, reversed=False)
    test_sorted(sort_algo, reversed=True)
