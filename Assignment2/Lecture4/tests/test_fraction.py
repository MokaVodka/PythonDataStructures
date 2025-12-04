import pytest
from util_test import Fraction


def assert_result(result, expect):
    assert result == expect, f'Exp {expect}, got {result}'


@pytest.fixture
def default_values():
    f1 = Fraction(4, 6)
    f2 = Fraction(-7, 2)
    i1 = 3
    s1 = '4'

    return f1, f2, i1, s1


# Test initialization
def test_Fraction():
    result = Fraction(4, 6)
    assert_result(str(result), '2/3')

    with pytest.raises(ValueError) as exc_info:
        Fraction(3.5, 6)
    result = str(exc_info.value)
    assert_result(str(result), 'Numerator must be an int')

    with pytest.raises(ValueError) as exc_info:
        Fraction(4, '6')
    result = str(exc_info.value)
    assert_result(str(result), 'Denominator must be an int')

    with pytest.raises(ValueError) as exc_info:
        Fraction(1, 0)
    result = str(exc_info.value)
    assert_result(str(result), 'Denominator cannot be 0')


def test_add(default_values):
    f1, f2, i1, s1 = default_values

    result = f1 + f2
    expect = '-17/6'
    assert_result(str(result), str(expect))

    result = f1 + i1
    expect = '11/3'
    assert_result(str(result), str(expect))

    with pytest.raises(ValueError) as exc_info:
        _ = f1 + s1
    result = str(exc_info.value)
    assert_result(str(result), 'Other value must be an int or Fraction')


def test_subtract(default_values):
    f1, f2, i1, s1 = default_values

    result = f1 - f2
    expect = '25/6'
    assert_result(str(result), str(expect))

    result = f1 - i1
    expect = '-7/3'
    assert_result(str(result), str(expect))

    with pytest.raises(ValueError) as exc_info:
        _ = f1 - s1
    result = str(exc_info.value)
    assert_result(str(result), 'Other value must be an int or Fraction')


def test_multiply(default_values):
    f1, f2, i1, s1 = default_values

    result = f1 * f2
    expect = '-7/3'
    assert_result(str(result), str(expect))

    result = f1 * i1
    expect = '2/1'
    assert_result(str(result), str(expect))

    with pytest.raises(ValueError) as exc_info:
        _ = f1 * s1
    result = str(exc_info.value)
    assert_result(str(result), 'Other value must be an int or Fraction')


def test_divide(default_values):
    f1, f2, i1, s1 = default_values

    result = f1 / f2
    expect = '-4/21'
    assert_result(str(result), str(expect))

    result = f1 / i1
    expect = '2/9'
    assert_result(str(result), str(expect))

    with pytest.raises(ValueError) as exc_info:
        _ = f1 / s1
    result = str(exc_info.value)
    assert_result(str(result), 'Other value must be an int or Fraction')

    # Zero division
    with pytest.raises(ValueError) as exc_info:
        _ = f1 / 0
    result = str(exc_info.value)
    assert_result(str(result), 'Cannot divide fraction by 0')

    with pytest.raises(ValueError) as exc_info:
        _ = f1 / Fraction(0, 3)
    result = str(exc_info.value)
    assert_result(str(result), 'Cannot divide fraction by 0')
