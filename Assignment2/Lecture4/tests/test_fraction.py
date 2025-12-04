import pytest
from util_test import Fraction


def assert_result(result, expect):
    assert result == expect, f'Exp {expect}, got {result}'


# Test initialization
def test_Fraction():
    result = Fraction(4, 6)
    assert_result(str(result), '2/3')


def test_add():
    result = ''
    expect = ''
    assert_result(str(result), str(expect))


def test_subtract():
    result = ''
    expect = ''
    assert_result(str(result), str(expect))


def test_multiply():
    result = ''
    expect = ''
    assert_result(str(result), str(expect))


def test_divide():
    result = ''
    expect = ''
    assert_result(str(result), str(expect))
