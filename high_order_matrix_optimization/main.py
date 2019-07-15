"""
///////////////////////////////////////////////////////////////////////////////
//        copyright (b) 2012-2019 Oscar Riveros. all rights reserved.        //
//                        oscar.riveros@peqnp.science                        //
//                                                                           //
//   without any restriction, Oscar Riveros reserved rights, patents and     //
//  commercialization of this knowledge or derived directly from this work.  //
///////////////////////////////////////////////////////////////////////////////
"""
import numpy

import big_csp

if __name__ == '__main__':
    o = 0
    p, q = 4, 4

    a = numpy.random.randint(1, 100, size=(p,))
    b = numpy.random.randint(1, 100, size=(q,))

    numpy.savetxt('a.txt', a, fmt='%i')
    numpy.savetxt('b.txt', b, fmt='%i')

    encoder = big_csp.Encoder(bits=16)

    while True:
        x = numpy.empty(shape=(p, q), dtype=big_csp.Entity)
        for i in range(p):
            for j in range(q):
                x[i, j] = big_csp.Entity(encoder)

        y = numpy.empty(shape=(p, q), dtype=big_csp.Entity)
        for i in range(p):
            for j in range(q):
                y[i, j] = big_csp.Entity(encoder)

        for i in range(p):
            big_csp.Constraint(numpy.linalg.matrix_power(x, 2)[i, :].sum() <= a.tolist()[i])
            big_csp.Constraint((y ** 2)[i, :].sum() <= b.tolist()[i])
        for j in range(q):
            big_csp.Constraint((x ** 2)[:, j].sum() <= a.tolist()[j])
            big_csp.Constraint(numpy.linalg.matrix_power(y, 2)[:, j].sum() <= b.tolist()[j])

        big_csp.Constraint(numpy.dot(x, y).diagonal().sum() > o)

        solver = big_csp.Solver()

        if solver.satisfy(x.flatten().tolist() + y.flatten().tolist()):
            o = numpy.dot(x, y).diagonal().sum()
            x = numpy.vectorize(int)(x)
            y = numpy.vectorize(int)(y)
            print(o)
            print(numpy.dot(x, y))
            print(x)
            print(y)
            print(80 * '-')
            numpy.savetxt('x.txt', numpy.vectorize(int)(x), fmt='%i')
            numpy.savetxt('y.txt', numpy.vectorize(int)(y), fmt='%i')
        else:
            solver.clear()
            break
