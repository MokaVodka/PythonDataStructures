import pytest
from util_test import create_Deque


# Assert
def assert_result(result, expect):
    assert result == expect, f"Exp {expect}, got {result}"


@pytest.fixture
def deque_add_first():
    deque = create_Deque()
    deque.add_first('Alpha')
    deque.add_first('Beta')
    deque.add_first('Gamma')
    return deque


@pytest.fixture
def deque_add_last():
    deque = create_Deque()
    deque.add_last('Alpha')
    deque.add_last('Beta')
    deque.add_last('Gamma')
    return deque


# Test add and get
def test_add_first(deque_add_first):
    deque = deque_add_first
    assert_result(deque.size, 3)
    assert_result(deque.get_first(), 'Gamma')
    assert_result(deque.get_last(), 'Alpha')


def test_add_last(deque_add_last):
    deque = deque_add_last
    assert_result(deque.size, 3)
    assert_result(deque.get_first(), 'Alpha')
    assert_result(deque.get_last(), 'Gamma')


# Test remove
def test_remove_first(deque_add_last):
    deque = deque_add_last
    removed = deque.remove_first()
    assert_result(removed, 'Alpha')
    assert_result(deque.get_first(), 'Beta')
    assert_result(deque.get_last(), 'Gamma')


def test_remove_last(deque_add_last):
    deque = deque_add_last
    removed = deque.remove_last()
    assert_result(removed, 'Gamma')
    assert_result(deque.get_first(), 'Alpha')
    assert_result(deque.get_last(), 'Beta')


# Test empty
def test_empty_deque():
    deque = create_Deque()
    assert_result(deque.size, 0)

    # Access node
    genericMessage = 'Queue is empty, nothing to '
    expect = genericMessage + 'access'

    with pytest.raises(IndexError) as exc_info:
        deque.get_first()
    result = str(exc_info.value)
    assert_result(result, expect)

    with pytest.raises(IndexError) as exc_info:
        deque.get_last()
    result = str(exc_info.value)
    assert_result(result, expect)

    # Remove node
    expect = genericMessage + 'remove'

    with pytest.raises(IndexError) as exc_info:
        deque.remove_first()
    result = str(exc_info.value)
    assert_result(result, expect)

    with pytest.raises(IndexError) as exc_info:
        deque.remove_last()
    result = str(exc_info.value)
    assert_result(result, expect)
