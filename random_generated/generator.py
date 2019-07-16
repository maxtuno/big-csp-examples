import sys
import random

if __name__ == '__main__':
    n = int(sys.argv[1])
    with open('{}.txt'.format(n), 'w') as description_file:
        m = n // 2
        e = n // 4
        bits = 16
        print('import big_csp')
        print()
        print('optimal = 0')
        print('while True:')
        print('\tencoder = big_csp.Encoder(bits={})'.format(bits))
        print()
        xs = []
        for i in range(n):
            xs.append('x{}'.format(i))
            print('\tx{} = big_csp.Entity(encoder)'.format(i))
        print()
        a, b = sorted((random.randint(0, 10), random.randint(10, 100)))
        bounds = [sorted((random.randint(0, a), random.randint(a, b))) for _ in range(n)]
        for i, (a, b) in enumerate(bounds):
            print('\tbig_csp.Constraint({} <= x{} <= {})'.format(a, i, b))
        print()

        eq_master = ''
        for _ in range(m):
            eq_master += 'x{}'.format(random.randint(0, n - 1))
            if random.choice([True, False]):
                eq_master += ' + x{} *'.format(random.randint(0, n - 1))
            else:
                eq_master += ' * x{} +'.format(random.randint(0, n - 1))
            if random.choice([True, False]):
                eq_master += ' x{} ** {} + '.format(random.randint(0, n - 1), random.randint(2, e))
            else:
                eq_master += ' {} * x{} + '.format(random.randint(2, e), random.randint(0, n - 1))
        print('\tbig_csp.Constraint(optimal < {})'.format(eq_master[:-3]))
        print('max : {}'.format(eq_master[:-3]), file=description_file)
        print()

        for _ in range(m // 2):
            eq = ''
            for _ in range(m // 2):
                eq += 'x{}'.format(random.randint(0, n - 1))
                if random.choice([True, False]):
                    eq += ' + x{} *'.format(random.randint(0, n - 1))
                else:
                    eq += ' * x{} +'.format(random.randint(0, n - 1))
                if random.choice([True, False]):
                    eq += ' x{} ** {} + '.format(random.randint(0, n - 1), random.randint(2, e))
                else:
                    eq += ' {} * x{} + '.format(random.randint(2, e), random.randint(0, n - 1))
            print('\tbig_csp.Constraint({}<= {})'.format(eq[:-2], random.randint(n, n ** 2)))
            print('{}<= {}'.format(eq[:-2], random.randint(n, n ** 2)), file=description_file)
            print()

        for i, (a, b) in enumerate(bounds):
            print('{} <= x{} <= {}'.format(a, i, b), file=description_file)

        print('\tsolver = big_csp.Solver()')
        print('\tif solver.satisfy([{}]):'.format(', '.join(xs)))
        print('\t\toptimal = {}'.format(eq_master[:-2]))
        print('\t\tprint(optimal, \'=>\', {})'.format(', '.join(xs)))
        print('\telse:')
        print('\t\tbreak')
        print()
        print('\tsolver.clear()')
