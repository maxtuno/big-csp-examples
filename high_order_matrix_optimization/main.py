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
    n = 4

    a = numpy.loadtxt('a.txt').tolist()
    b = numpy.loadtxt('b.txt').tolist()

    while True:
        encoder = big_csp.Encoder(bits=16)
        x = numpy.empty(shape=(n, n), dtype=big_csp.Entity)
        y = numpy.empty(shape=(n, n), dtype=big_csp.Entity)
        for i in range(n):
            for j in range(n):
                x[i, j] = big_csp.Entity(encoder)
                y[i, j] = big_csp.Entity(encoder)

        for k in range(n):
            big_csp.Constraint(numpy.linalg.matrix_power(x, 2)[k, :].sum() <= a[k])
            big_csp.Constraint((x ** 2)[:, k].sum() <= b[k])
            big_csp.Constraint(numpy.linalg.matrix_power(y, 2)[:, k].sum() <= a[k])
            big_csp.Constraint((y ** 2)[k, :].sum() <= b[k])

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
            solver.clear()
        else:
            break
