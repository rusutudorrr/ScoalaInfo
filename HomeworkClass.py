class Fraction:

    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __add__(self, add_fraction):
        add_num = self.num * add_fraction.den + self.den * add_fraction.num
        add_den = self.den * add_fraction.den

        return Fraction(add_num, add_den)

    def __sub__(self, sub_fraction):
        sub_num = self.num * sub_fraction.den - self.den * sub_fraction.num
        sub_den = self.den * sub_fraction.den

        return Fraction(sub_num, sub_den)

    def inverse(self, top, bottom):
        self.num = bottom
        self.den = top

        return str(self.num) + "/" + str(self.den)


my_fraction = Fraction(3, 5)
print(my_fraction)

f1 = Fraction(1, 4)
f2 = Fraction(1, 6)

my_add = f1 + f2

print(my_add)

f3 = Fraction(1, 4)
f4 = Fraction(1, 6)

my_sub = f3 - f4

print(my_sub)

print(my_fraction.inverse(3, 5))