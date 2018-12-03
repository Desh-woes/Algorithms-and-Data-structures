# Euclid’s Algorithm (Greatest common denominator)
def gcd(m, n):
    while m % n != 0:
        old_m = m
        old_n = n
        m = old_n
        n = old_m % old_n
    return n


class Fraction:

    def __init__(self, top, buttom):
        if top > 0 or top < 0:
            self.num = top
        else:
            raise ValueError

        if buttom > 0 or buttom < 0:
            self.den = buttom
        else:
            raise ValueError

        common = gcd(self.num, self.den)
        self.num = self.num//common
        self.den = self.den//common

    def __str__(self):
        return str(self.num) + '/' + str(self.den)

    def __add__(self, other):
        new_num = (self.num*other.den) + (other.num*self.den)
        new_den = self.den*other.den
        return Fraction(new_num, new_den)
    __radd__ = __add__

    def __sub__(self, other):
        new_num = (self.num * other.den) - (other.num * self.den)
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __mul__(self, other):
        new_num = self.num * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)

    def __iadd__(self, other):
        self.num = (self.num * other.den) + (other.num * self.den)
        self.den = self.den * other.den
        return Fraction(self.num, self.den)

    def __truediv__(self, other):
        new_num = self.num * other.den
        new_den = self.den * other.num
        return Fraction(new_num, new_den)

    def __eq__(self, other):
        first_num = self.num * other.den
        second_num = self.den * other.num

        return first_num == second_num

    def __gt__(self, other):
        first_num = self.num * other.den
        second_num = self.den * other.num

        return first_num > second_num

    def __ge__(self, other):
        first_num = self.num * other.den
        second_num = self.den * other.num

        return first_num >= second_num

    def __lt__(self, other):
        first_num = self.num * other.den
        second_num = self.den * other.num

        return first_num < second_num

    def __le__(self, other):
        first_num = self.num * other.den
        second_num = self.den * other.num

        return first_num <= second_num

    def __ne__(self, other):
        first_num = self.num * other.den
        second_num = self.den * other.num

        return first_num != second_num

    def __repr__(self):
        return 'Fraction'

    def get_num(self):
        return self.num

    def get_den(self):
        return self.den


fr_1 = Fraction(1, 4)
fr_2 = Fraction(1, 2)
fr_1 += fr_2

print(repr(fr_1))
