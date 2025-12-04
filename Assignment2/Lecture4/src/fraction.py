class Fraction:
    def __init__(self, numerator, denominator):
        if numerator is None or type(numerator) is not int:
            raise ValueError('Numerator must be an int')
        if denominator is None or type(denominator) is not int:
            raise ValueError('Denominator must be an int')

        if denominator == 0:
            raise ValueError('Denominator cannot be 0')

        self.__numerator = numerator
        self.__denominator = denominator
        self.__simplify()

    def __simplify(self):
        # 4/-5 -> -4/5 | -4/-5 -> 4/5
        if self.__denominator < 0:
            self.__numerator = -self.__numerator
            self.__denominator = -self.__denominator

        # Find gcd()
        # 1. Assign a, b
        # 2. Find remainer
        # 3. Assign new a, b to b, remainder
        # 4. Repeat until remainder is 0 (new b = 0)

        a, b, = self.__numerator, self.__denominator
        while b != 0:
            a, b = b, a % b
        gcd = a

        # Simplify fraction
        self.__numerator //= gcd
        self.__denominator //= gcd

    def __check_type(self, other):
        otherType = type(other)
        isInt = otherType is int
        isFraction = otherType is Fraction
        isValidType = isInt or isFraction

        if other is None or not isValidType:
            raise ValueError('Value to be added must be an int or Fraction')
        return isInt, isFraction

    def __add__(self, other):
        isInt, isFraction = self.__check_type(other)

        # Don't modify inputs
        t_numerator = self.__numerator
        t_denominator = self.__denominator

        if isInt:
            o_int = other
            o_int *= t_denominator
            t_numerator += o_int
            return Fraction(t_numerator, t_denominator)

        elif isFraction:
            o_numerator = other.__numerator
            o_denominator = other.__denominator

            # Multiply for common denominator
            o_numerator *= t_denominator
            t_numerator *= o_denominator
            t_denominator *= o_denominator

            # Add and simplify resulting fraction
            t_numerator += o_numerator
            return Fraction(t_numerator, t_denominator)

        else:
            return None

    def __sub__(self, other):
        isInt, isFraction = self.__check_type(other)

        # Don't modify inputs
        t_numerator = self.__numerator
        t_denominator = self.__denominator

        if isInt:
            o_int = other
            o_int *= t_denominator
            t_numerator -= o_int
            return Fraction(t_numerator, t_denominator)

        elif isFraction:
            o_numerator = other.__numerator
            o_denominator = other.__denominator

            # Multiply for common denominator
            o_numerator *= t_denominator
            t_numerator *= o_denominator
            t_denominator *= o_denominator

            # Subtract and simplify resulting fraction
            t_numerator -= o_numerator
            return Fraction(t_numerator, t_denominator)

        else:
            return None

    def __mul__(self, other):
        isInt, isFraction = self.__check_type(other)

        # Don't modify inputs
        t_numerator = self.__numerator
        t_denominator = self.__denominator

        if isInt:
            t_numerator *= other
            return Fraction(t_numerator, t_denominator)

        elif isFraction:
            t_numerator *= other.__numerator
            t_denominator *= other.__denominator
            return Fraction(t_numerator, t_denominator)

        else:
            return None

    def __truediv__(self, other):
        isInt, isFraction = self.__check_type(other)

        # Don't modify inputs
        t_numerator = self.__numerator
        t_denominator = self.__denominator

        if isInt:
            if other == 0:
                raise ValueError('Cannot divide fraction by 0')

            t_denominator *= other
            return Fraction(t_numerator, t_denominator)

        elif isFraction:
            if other.__numerator == 0:
                raise ValueError('Cannot divide fraction by 0')

            t_numerator *= other.__denominator
            t_denominator *= other.__numerator
            return Fraction(t_numerator, t_denominator)

        else:
            return None

    def __str__(self):
        return '/'.join([str(self.__numerator), str(self.__denominator)])


# -- Example program --
def example():
    f1 = Fraction(5, -3)
    f2 = Fraction(-2, -8)

    print(f'f1 = {f1}')
    print(f'f2 = {f2}')
    print('')

    print('-- Calculations --')
    print(f'f1 + f2 = {f1 + f2}')
    print(f'f1 + 3 = {f1 + 3}')
    print('')

    print(f'f1 - f2 = {f1 - f2}')
    print(f'f2 - f1 = {f2 - f1}')
    print(f'f1 - 3 = {f1 - 3}')
    print('')

    print(f'f1 * f2 = {f1 * f2}')
    print(f'f1 * 3 = {f1 * 3}')
    print('')

    print(f'f1 / f2 = {f1 / f2}')
    print(f'f2 / f1 = {f2 / f1}')
    print(f'f1 / 3 = {f1 / 3}')
    print('')


try:
    example()
except Exception as e:
    print(f'An error occured: {e}')
