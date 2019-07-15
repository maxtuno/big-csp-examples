import numpy

if __name__ == '__main__':
    p, q = 4, 4

    a = numpy.loadtxt('a.txt')
    b = numpy.loadtxt('b.txt')

    x = numpy.loadtxt('x.txt')
    y = numpy.loadtxt('y.txt')

    for i in range(p):
        print(numpy.linalg.matrix_power(x, 2)[i, :].sum() <= a.tolist()[i])
        print((y ** 2)[i, :].sum() <= b.tolist()[i])
    for j in range(q):
        print((x ** 2)[:, j].sum() <= a.tolist()[j])
        print(numpy.linalg.matrix_power(y, 2)[:, j].sum() <= b.tolist()[j])

    print(numpy.dot(x, y).diagonal().sum())
