from big_csp import *

if __name__ == '__main__':

    bits = Encoder(bits=16)

    x = Entity(bits)
    y = Entity(bits)
    z = Entity(bits)
    a = Entity(bits)
    b = Entity(bits)
    c = Entity(bits)

    assert (a * x ** a + b * y ** b + c * z ** c == a * b * c * x * y * z)
    
    assert (x > 1)
    assert (y > 1)
    assert (z > 1)
    assert (a > 1)
    assert (b > 1)
    assert (c > 1)

    solver = Solver()
    while solver.satisfy([x, y, z, a, b, c]):
        print('{1}*{0}**{1} + {3}*{2}**{3} + {5}*{4}**{5} == {1}*{3}*{5}*{0}*{2}*{4}'.format(x, a, y, b, z, c))
    solver.clear()
