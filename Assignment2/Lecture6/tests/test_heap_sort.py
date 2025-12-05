import pytest
import random
import util_test_heap as tu


# Act and Assert
def act_assert(toSort, sortAlgo):
    expect = sorted(toSort)
    result = sortAlgo(toSort)
    assert result == expect, f"Exp {expect}, got {result}"


# List population
@pytest.fixture
def populated_list():
    return tu.get_random_list(15)


# Algorithms to test
def algorithms():
    return (tu.run_heap_sort, tu.run_fast_merge_sort)


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
def test_random(populated_list, sortAlgo):
    toSort = populated_list
    act_assert(toSort, sortAlgo)


# Test sorted
def sort_list(populated_list, reversed=False):
    toSort = sorted(populated_list)
    if reversed:
        toSort = toSort[::-1]
    return toSort


@pytest.mark.parametrize('sortAlgo', algorithms())
def test_sorted(populated_list, sortAlgo):
    toSort = sort_list(populated_list, False)
    act_assert(toSort, sortAlgo)

    toSort = sort_list(populated_list, True)
    act_assert(toSort, sortAlgo)


# Test duplicates
def duplify_list(populated_list, dupeType=0):
    toSort = populated_list

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
def test_duplicate(populated_list, sortAlgo):
    toSort = duplify_list(populated_list, 0)
    act_assert(toSort, sortAlgo)

    toSort = duplify_list(populated_list, 1)
    act_assert(toSort, sortAlgo)

    toSort = duplify_list(populated_list, 2)
    act_assert(toSort, sortAlgo)
