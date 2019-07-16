import numpy

if __name__ == '__main__':
    n = 4

    a = numpy.loadtxt('a.txt').tolist()
    b = numpy.loadtxt('b.txt').tolist()

    x = numpy.loadtxt('x.txt')
    y = numpy.loadtxt('y.txt')

    print(numpy.dot(x, y).diagonal().sum())

    for k in range(n):
        print(numpy.linalg.matrix_power(x, 2)[k, :].sum() <= a[k])
        print((x ** 2)[:, k].sum() <= b[k])
        print(numpy.linalg.matrix_power(y, 2)[:, k].sum() <= a[k])
        print((y ** 2)[k, :].sum() <= b[k])
