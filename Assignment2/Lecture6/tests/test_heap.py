import pytest
from util_test_heap import create_Heap


# Assert
def assert_result(result, expect):
    assert result == expect, f"Exp {expect}, got {result}"


@pytest.fixture
def heap_add():
    heap = create_Heap()
    heap.add('Alpha')
    heap.add('Beta')
    heap.add('Gamma')
    return heap


# Test add and get
def test_add(heap_add):
    heap = heap_add
    assert_result(heap.get_size(), 3)
    assert_result(heap.peek(), 'Gamma')
    assert_result(heap.is_empty(), False)


# Test remove
def test_remove(heap_add):
    heap = heap_add
    removed = heap.pull_high()
    assert_result(removed, 'Gamma')
    assert_result(heap.peek(), 'Beta')
    assert_result(heap.get_size(), 2)
    assert_result(heap.is_empty(), False)

    while not heap.is_empty():
        heap.pull_high()

    assert_result(heap.get_size(), 0)
    assert_result(heap.is_empty(), True)


# Test empty
def test_empty_heap():
    heap = create_Heap()
    assert_result(heap.get_size(), 0)

    # Access node
    genericMessage = 'Heap is empty, nothing to '
    expect = genericMessage + 'peek'

    with pytest.raises(IndexError) as exc_info:
        heap.peek()
    result = str(exc_info.value)
    assert_result(result, expect)

    # Remove node
    expect = genericMessage + 'pull'

    with pytest.raises(IndexError) as exc_info:
        heap.pull_high()
    result = str(exc_info.value)
    assert_result(result, expect)
