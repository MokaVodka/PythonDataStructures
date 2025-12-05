import pytest
import random
from util_test import sort_algorithms
from util_test import get_random_list


# Act and Assert
def act_assert(toSort, sortAlgo):
    expect = sorted(toSort)
    result = sortAlgo(toSort)
    assert result == expect, f"Exp {expect}, got {result}"


# List population
def populated_list():
    return get_random_list(15)


def algorithms():
    return tuple(sort_algorithms())


# Test empty
@pytest.mark.parametrize('sortAlgo', algorithms())
def test_empty(sortAlgo):
    toSort = []
    act_assert(toSort, sortAlgo)


# Test 1 length list
@pytest.mark.parametrize('sortAlgo', algorithms())
def test_len1(sortAlgo):
    toSort = [0]
    act_assert(toSort, sortAlgo)


# Test random
@pytest.mark.parametrize('sortAlgo', algorithms())
def test_random(sortAlgo):
    toSort = populated_list()
    act_assert(toSort, sortAlgo)


# Test sorted
def sort_list(reversed=False):
    toSort = sorted(populated_list())
    if reversed:
        toSort = toSort[::-1]
    return toSort


@pytest.mark.parametrize('sortAlgo', algorithms())
def test_sorted(sortAlgo):
    toSort = sort_list(False)
    act_assert(toSort, sortAlgo)

    toSort = sort_list(True)
    act_assert(toSort, sortAlgo)


# Test duplicates
def duplify_list(dupeType=0):
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

    return toSort


@pytest.mark.parametrize('sortAlgo', algorithms())
def test_duplicate(sortAlgo):
    toSort = duplify_list(0)
    act_assert(toSort, sortAlgo)

    toSort = duplify_list(1)
    act_assert(toSort, sortAlgo)

    toSort = duplify_list(2)
    act_assert(toSort, sortAlgo)


# Main test
def main_test(sortAlgo):

    # Test list size of 0 | 1
    test_empty(sortAlgo)
    test_len1(sortAlgo)

    # Test duplicates All | Pair | Variable amount
    test_duplicate(sortAlgo)

    # Test random
    test_random(sortAlgo)

    # Test sorted
    test_sorted(sortAlgo)
