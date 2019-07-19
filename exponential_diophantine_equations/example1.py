from big_csp import *


def eq():
    return abs(x ** a - y ** b) == z ** c


if __name__ == '__main__':

    bits = Encoder(bits=16)

    x = Entity(bits)
    y = Entity(bits)
    z = Entity(bits)
    a = Entity(bits)
    b = Entity(bits)
    c = Entity(bits)

    assert (eq())
    assert (x > 1)
    assert (y > 1)
    assert (z > 1)
    assert (a > 1)
    assert (b > 1)
    assert (c > 1)

    solver = Solver()
    while solver.satisfy([x, y, z, a, b, c]):
        print('abs({0} ** {1} - {2} ** {3}) == {4} ** {5}'.format(x, a, y, b, z, c))
    solver.clear()
