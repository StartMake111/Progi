import math
import copy


class Rational:
    def __init__(self, numerator=0, denuminator=1):
        self.num = abs(numerator)
        self.denum = abs(denuminator)
        self.sign = -1 if numerator < 0 or denuminator < 0 else 1
        if numerator < 0 and denuminator < 0:
            self.sign = 1

    def isNaN(self):
        return self.num == self.denum == 0

    def gcd(a, b):
        if a == 0:
            return b
        if b == 0:
            return a
        if b > a:
            temp = a
            a = b
            b = temp
        for i in range(b, 1, -1):
            if a % i == 0 and b % i == 0:
                return i
        return 1

    def __eq__(self, other):
        if self.isNaN() or other.isNaN():
            return False
        if self.denum == other.denum == 0:
            return self.sign == other.sign
        return self.sign * self.num * other.denum == other.sign * other.num * self.denum

    def __add__(self, other):
        if self.isNaN() or other.isNaN():
            return Rational(0, 0)
        if self.denum == other.denum == 0:
            return self if self.sign == other.sign else Rational(0, 0)
        return Rational(
            (self.sign * self.num * other.denum)
            + (other.sign * other.num * self.denum),
            self.denum * other.denum,
        )

    def __sub__(self, other):
        clone = copy.deepcopy(other)
        clone.sign = -clone.sign
        return self + clone

    def __mul__(self, other):
        res = Rational(self.num * other.num, self.denum * other.denum)
        res.sign = self.sign * other.sign
        return res

    def __truediv__(self, other):
        res = Rational(self.num * other.denum, self.denum * other.num)
        res.sign = self.sign * other.sign
        return res

    def __float__(self):
        if self.denum == 0:
            return math.nan if self.num == 0 else math.inf * self.sign
        return self.sign * self.num / self.denum

    def __bool__(self):
        return self.num != 0 or self.denum == 0

    def numerator(self):
        return self.num

    def denuminator(self):
        return self.denum


def equal(a, b, e=1e-10):

    if -e < a - b < e:
        return True

    else:
        return False


if (
    Rational.gcd(91, 65) == 13
    and Rational.gcd(10, 3) == 1
    and Rational.gcd(-10, 3) == 1
    and Rational.gcd(10, -3) == 1
    and Rational.gcd(-10, -3) == 1
    and Rational.gcd(30, 10) == 10
    and Rational.gcd(10, 30) == 10
    and Rational.gcd(0, 10) == 10
    and Rational.gcd(10, 0) == 10
):
    print("gcd test passed")

else:
    print("gcd test failed")


if (
    not Rational(22, 0).isNaN()
    and not Rational(22, 9).isNaN()
    and not Rational(0, 9).isNaN()
    and not Rational(-22, 9).isNaN()
    and not Rational(-22, 0).isNaN()
    and Rational(0, 0).isNaN()
):
    print("isNaN test passed")

else:
    print("isNaN test failed")


if (
    Rational(22, 0) == Rational(22, 0)
    and Rational(22, 0) == Rational(9, 0)
    and not (Rational(22, 0) == Rational(22, 9))
    and not (Rational(22, 0) == Rational(-22, 9))
    and not (Rational(22, 0) == Rational(-22, 0))
    and not (Rational(22, 0) == Rational(0, 9))
    and not (Rational(22, 0) == Rational(0, 0))
    and Rational(22, 9) == Rational(22, 9)
    and Rational(22, 9) == Rational(-22, -9)
    and Rational(22, 9) == Rational(110, 45)
    and Rational(22, 9) == Rational(-110, -45)
    and not (Rational(22, 9) == Rational(-22, 9))
    and not (Rational(22, 9) == Rational(22, -9))
    and not (Rational(22, 9) == Rational(9, 22))
    and not (Rational(22, 9) == Rational(22, 0))
    and not (Rational(22, 9) == Rational(-22, 0))
    and not (Rational(22, 9) == Rational(0, 9))
    and not (Rational(22, 9) == Rational(0, 0))
    and Rational(0, 1) == Rational(0, 1)
    and Rational(0, 1) == Rational(0, 9)
    and Rational(0, 1) == Rational(0, -9)
    and not (Rational(0, 1) == Rational(22, 9))
    and not (Rational(0, 1) == Rational(-22, 9))
    and not (Rational(0, 1) == Rational(22, 0))
    and not (Rational(0, 1) == Rational(-22, 0))
    and not (Rational(0, 1) == Rational(0, 0))
    and Rational(-22, 9) == Rational(-22, 9)
    and Rational(-22, 9) == Rational(22, -9)
    and Rational(-22, 9) == Rational(-110, 45)
    and Rational(-22, 9) == Rational(110, -45)
    and not (Rational(-22, 9) == Rational(-22, -9))
    and not (Rational(-22, 9) == Rational(22, 9))
    and not (Rational(-22, 9) == Rational(9, -22))
    and not (Rational(-22, 9) == Rational(22, 0))
    and not (Rational(-22, 9) == Rational(-22, 0))
    and not (Rational(-22, 9) == Rational(0, 9))
    and not (Rational(-22, 9) == Rational(0, 0))
    and Rational(-22, 0) == Rational(-22, 0)
    and Rational(-22, 0) == Rational(-9, 0)
    and not (Rational(-22, 0) == Rational(22, 9))
    and not (Rational(-22, 0) == Rational(-22, 9))
    and not (Rational(-22, 0) == Rational(22, 0))
    and not (Rational(-22, 0) == Rational(0, 9))
    and not (Rational(-22, 0) == Rational(0, 0))
    and not (Rational(0, 0) == Rational(0, 0))
):
    print("Equality test passed")

else:
    print("Equality test failed")


if (
    Rational(22, 0) + Rational(22, 0) == Rational(22, 0)
    and Rational(22, 9) + Rational(22, 0) == Rational(22, 0)
    and Rational(0, 9) + Rational(22, 0) == Rational(22, 0)
    and Rational(-22, 9) + Rational(22, 0) == Rational(22, 0)
    and (Rational(-22, 0) + Rational(22, 0)).isNaN()
    and Rational(22, 0) + Rational(22, 9) == Rational(22, 0)
    and Rational(22, 9) + Rational(22, 9) == Rational(44, 9)
    and Rational(0, 9) + Rational(22, 9) == Rational(22, 9)
    and Rational(-22, 9) + Rational(22, 9) == Rational(0, 9)
    and Rational(-22, 0) + Rational(22, 9) == Rational(-22, 0)
    and Rational(22, 0) + Rational(0, 1) == Rational(22, 0)
    and Rational(22, 9) + Rational(0, 1) == Rational(22, 9)
    and Rational(0, 9) + Rational(0, 1) == Rational(0, 9)
    and Rational(-22, 9) + Rational(0, 1) == Rational(-22, 9)
    and Rational(-22, 0) + Rational(0, 1) == Rational(-22, 0)
    and Rational(22, 0) + Rational(-22, 9) == Rational(22, 0)
    and Rational(22, 9) + Rational(-22, 9) == Rational(0, 9)
    and Rational(0, 9) + Rational(-22, 9) == Rational(-22, 9)
    and Rational(-22, 9) + Rational(-22, 9) == Rational(-44, 9)
    and Rational(-22, 0) + Rational(-22, 9) == Rational(-22, 0)
    and (Rational(22, 0) + Rational(-22, 0)).isNaN()
    and Rational(22, 9) + Rational(-22, 0) == Rational(-22, 0)
    and Rational(0, 9) + Rational(-22, 0) == Rational(-22, 0)
    and Rational(-22, 9) + Rational(-22, 0) == Rational(-22, 0)
    and Rational(-22, 0) + Rational(-22, 0) == Rational(-22, 0)
    and (Rational(22, 0) + Rational(0, 0)).isNaN()
    and (Rational(22, 9) + Rational(0, 0)).isNaN()
    and (Rational(0, 9) + Rational(0, 0)).isNaN()
    and (Rational(-22, 9) + Rational(0, 0)).isNaN()
    and (Rational(-22, 0) + Rational(0, 0)).isNaN()
):
    print("Summation test passed")

else:
    print("Summation test failed")


if (
    (Rational(22, 0) - Rational(22, 0)).isNaN()
    and Rational(22, 9) - Rational(22, 0) == Rational(-22, 0)
    and Rational(0, 9) - Rational(22, 0) == Rational(-22, 0)
    and Rational(-22, 9) - Rational(22, 0) == Rational(-22, 0)
    and Rational(-22, 0) - Rational(22, 0) == Rational(-22, 0)
    and Rational(22, 0) - Rational(22, 9) == Rational(22, 0)
    and Rational(22, 9) - Rational(22, 9) == Rational(0, 9)
    and Rational(0, 9) - Rational(22, 9) == Rational(-22, 9)
    and Rational(-22, 9) - Rational(22, 9) == Rational(-44, 9)
    and Rational(-22, 0) - Rational(22, 9) == Rational(-22, 0)
    and Rational(22, 0) - Rational(0, 1) == Rational(22, 0)
    and Rational(22, 9) - Rational(0, 1) == Rational(22, 9)
    and Rational(0, 9) - Rational(0, 1) == Rational(0, 9)
    and Rational(-22, 9) - Rational(0, 1) == Rational(-22, 9)
    and Rational(-22, 0) - Rational(0, 1) == Rational(-22, 0)
    and Rational(22, 0) - Rational(-22, 9) == Rational(22, 0)
    and Rational(22, 9) - Rational(-22, 9) == Rational(44, 9)
    and Rational(0, 9) - Rational(-22, 9) == Rational(22, 9)
    and Rational(-22, 9) - Rational(-22, 9) == Rational(0, 9)
    and Rational(-22, 0) - Rational(-22, 9) == Rational(-22, 0)
    and Rational(22, 0) - Rational(-22, 0) == Rational(22, 0)
    and Rational(22, 9) - Rational(-22, 0) == Rational(22, 0)
    and Rational(0, 9) - Rational(-22, 0) == Rational(22, 0)
    and Rational(-22, 9) - Rational(-22, 0) == Rational(22, 0)
    and (Rational(-22, 0) - Rational(-22, 0)).isNaN()
    and (Rational(22, 0) - Rational(0, 0)).isNaN()
    and (Rational(22, 9) - Rational(0, 0)).isNaN()
    and (Rational(0, 9) - Rational(0, 0)).isNaN()
    and (Rational(-22, 9) - Rational(0, 0)).isNaN()
    and (Rational(-22, 0) - Rational(0, 0)).isNaN()
):
    print("Subtraction test passed")

else:
    print("Subtraction test failed")


if (
    Rational(22, 0) * Rational(22, 0) == Rational(22, 0)
    and Rational(22, 9) * Rational(22, 0) == Rational(22, 0)
    and (Rational(0, 9) * Rational(22, 0)).isNaN()
    and Rational(-22, 9) * Rational(22, 0) == Rational(-22, 0)
    and Rational(-22, 0) * Rational(22, 0) == Rational(-22, 0)
    and Rational(22, 0) * Rational(22, 9) == Rational(22, 0)
    and Rational(22, 9) * Rational(22, 9) == Rational(22 * 22, 9 * 9)
    and Rational(0, 9) * Rational(22, 9) == Rational(0, 9)
    and Rational(-22, 9) * Rational(22, 9) == Rational(-22 * 22, 9 * 9)
    and Rational(-22, 0) * Rational(22, 9) == Rational(-22, 0)
    and (Rational(22, 0) * Rational(0, 1)).isNaN()
    and Rational(22, 9) * Rational(0, 1) == Rational(0, 9)
    and Rational(0, 9) * Rational(0, 1) == Rational(0, 9)
    and Rational(-22, 9) * Rational(0, 1) == Rational(0, 9)
    and (Rational(-22, 0) * Rational(0, 1)).isNaN()
    and Rational(22, 0) * Rational(-22, 9) == Rational(-22, 0)
    and Rational(22, 9) * Rational(-22, 9) == Rational(-22 * 22, 9 * 9)
    and Rational(0, 9) * Rational(-22, 9) == Rational(0, 9)
    and Rational(-22, 9) * Rational(-22, 9) == Rational(22 * 22, 9 * 9)
    and Rational(-22, 0) * Rational(-22, 9) == Rational(22, 0)
    and Rational(22, 0) * Rational(-22, 0) == Rational(-22, 0)
    and Rational(22, 9) * Rational(-22, 0) == Rational(-22, 0)
    and (Rational(0, 9) * Rational(-22, 0)).isNaN()
    and Rational(-22, 9) * Rational(-22, 0) == Rational(22, 0)
    and Rational(-22, 0) * Rational(-22, 0) == Rational(22, 0)
    and (Rational(22, 0) * Rational(0, 0)).isNaN()
    and (Rational(22, 9) * Rational(0, 0)).isNaN()
    and (Rational(0, 9) * Rational(0, 0)).isNaN()
    and (Rational(-22, 9) * Rational(0, 0)).isNaN()
    and (Rational(-22, 0) * Rational(0, 0)).isNaN()
):
    print("Multiplication test passed")

else:
    print("Multiplication test failed")


if (
    (Rational(22, 0) / Rational(22, 0)).isNaN()
    and Rational(22, 9) / Rational(22, 0) == Rational(0, 9)
    and Rational(0, 9) / Rational(22, 0) == Rational(0, 9)
    and Rational(-22, 9) / Rational(22, 0) == Rational(0, 9)
    and (Rational(-22, 0) / Rational(22, 0)).isNaN()
    and Rational(22, 0) / Rational(22, 9) == Rational(22, 0)
    and Rational(22, 9) / Rational(22, 9) == Rational(9, 9)
    and Rational(0, 9) / Rational(22, 9) == Rational(0, 9)
    and Rational(-22, 9) / Rational(22, 9) == Rational(-9, 9)
    and Rational(-22, 0) / Rational(22, 9) == Rational(-22, 0)
    and Rational(22, 0) / Rational(0, 1) == Rational(22, 0)
    and Rational(22, 9) / Rational(0, 1) == Rational(22, 0)
    and (Rational(0, 9) / Rational(0, 1)).isNaN()
    and Rational(-22, 9) / Rational(0, 1) == Rational(-22, 0)
    and Rational(-22, 0) / Rational(0, 1) == Rational(-22, 0)
    and Rational(22, 0) / Rational(-22, 9) == Rational(-22, 0)
    and Rational(22, 9) / Rational(-22, 9) == Rational(-9, 9)
    and Rational(0, 9) / Rational(-22, 9) == Rational(0, 9)
    and Rational(-22, 9) / Rational(-22, 9) == Rational(9, 9)
    and Rational(-22, 0) / Rational(-22, 9) == Rational(22, 0)
    and (Rational(22, 0) / Rational(-22, 0)).isNaN()
    and Rational(22, 9) / Rational(-22, 0) == Rational(0, 9)
    and Rational(0, 9) / Rational(-22, 0) == Rational(0, 9)
    and Rational(-22, 9) / Rational(-22, 0) == Rational(0, 9)
    and (Rational(-22, 0) / Rational(-22, 0)).isNaN()
    and (Rational(22, 0) / Rational(0, 0)).isNaN()
    and (Rational(22, 9) / Rational(0, 0)).isNaN()
    and (Rational(0, 9) / Rational(0, 0)).isNaN()
    and (Rational(-22, 9) / Rational(0, 0)).isNaN()
    and (Rational(-22, 0) / Rational(0, 0)).isNaN()
):
    print("Division test passed")

else:
    print("Division test failed")


if (
    equal(float(Rational(-22, -9)), 22 / 9.0)
    and equal(float(Rational(-9, -9)), 1)
    and equal(float(Rational(-6, -9)), 6 / 9.0)
    and equal(float(Rational(0, -9)), 0)
    and equal(float(Rational(6, -9)), -6 / 9.0)
    and equal(float(Rational(9, -9)), -1)
    and equal(float(Rational(22, -9)), -22 / 9.0)
    and math.isinf(float(Rational(-9, 0)))
    and math.isnan(float(Rational(0, 0)))
    and math.isinf(float(Rational(9, 0)))
    and equal(float(Rational(-22, 9)), -22 / 9.0)
    and equal(float(Rational(-9, 9)), -1)
    and equal(float(Rational(-6, 9)), -6 / 9.0)
    and equal(float(Rational(0, 9)), 0)
    and equal(float(Rational(6, 9)), 6 / 9.0)
    and equal(float(Rational(9, 9)), 1)
    and equal(float(Rational(22, 9)), 22 / 9.0)
):
    print("Conversion to double test passed")

else:
    print("Conversion to double test failed")


if (
    bool(Rational(-22, -9))
    and bool(Rational(-9, -9))
    and bool(Rational(-6, -9))
    and not bool(Rational(0, -9))
    and bool(Rational(6, -9))
    and bool(Rational(9, -9))
    and bool(Rational(22, -9))
    and bool(Rational(-9, 0))
    and bool(Rational(0, 0))
    and bool(Rational(9, 0))
    and bool(Rational(-22, 9))
    and bool(Rational(-9, 9))
    and bool(Rational(-6, 9))
    and not bool(Rational(0, 9))
    and bool(Rational(6, 9))
    and bool(Rational(9, 9))
    and bool(Rational(22, 9))
):
    print("Conversion to bool test passed")

else:
    print("Conversion to bool test failed")
