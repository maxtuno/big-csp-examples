import big_csp

optimal = 0
while True:
	encoder = big_csp.Encoder(bits=16)

	x0 = big_csp.Entity(encoder)
	x1 = big_csp.Entity(encoder)
	x2 = big_csp.Entity(encoder)
	x3 = big_csp.Entity(encoder)
	x4 = big_csp.Entity(encoder)
	x5 = big_csp.Entity(encoder)
	x6 = big_csp.Entity(encoder)
	x7 = big_csp.Entity(encoder)
	x8 = big_csp.Entity(encoder)
	x9 = big_csp.Entity(encoder)
	x10 = big_csp.Entity(encoder)
	x11 = big_csp.Entity(encoder)
	x12 = big_csp.Entity(encoder)
	x13 = big_csp.Entity(encoder)
	x14 = big_csp.Entity(encoder)

	big_csp.Constraint(1 <= x0 <= 14)
	big_csp.Constraint(1 <= x1 <= 22)
	big_csp.Constraint(6 <= x2 <= 25)
	big_csp.Constraint(7 <= x3 <= 55)
	big_csp.Constraint(9 <= x4 <= 71)
	big_csp.Constraint(7 <= x5 <= 66)
	big_csp.Constraint(6 <= x6 <= 66)
	big_csp.Constraint(3 <= x7 <= 20)
	big_csp.Constraint(7 <= x8 <= 71)
	big_csp.Constraint(0 <= x9 <= 56)
	big_csp.Constraint(5 <= x10 <= 53)
	big_csp.Constraint(6 <= x11 <= 63)
	big_csp.Constraint(8 <= x12 <= 27)
	big_csp.Constraint(4 <= x13 <= 39)
	big_csp.Constraint(6 <= x14 <= 22)

	big_csp.Constraint(optimal < x10 * x0 + x2 ** 2 + x4 + x3 * x6 ** 3 + x2 + x10 * x4 ** 2 + x7 + x0 * 3 * x5 + x9 * x9 + 2 * x4 + x5 * x2 + 2 * x5 + x13 + x13 * 2 * x6)

	big_csp.Constraint(x2 * x10 + 3 * x12 + x9 + x5 * 2 * x2 + x2 * x9 + 2 * x3 <= 49)

	big_csp.Constraint(x6 * x1 + x0 ** 2 + x11 + x0 * 2 * x14 + x9 * x11 + x4 ** 3 <= 54)

	big_csp.Constraint(x1 + x4 * x0 ** 2 + x0 + x7 * x6 ** 2 + x8 + x4 * 2 * x1 <= 33)

	solver = big_csp.Solver()
	if solver.satisfy([x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14]):
		optimal = x10 * x0 + x2 ** 2 + x4 + x3 * x6 ** 3 + x2 + x10 * x4 ** 2 + x7 + x0 * 3 * x5 + x9 * x9 + 2 * x4 + x5 * x2 + 2 * x5 + x13 + x13 * 2 * x6 
		print(optimal, '=>', x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14)
	else:
		break

	solver.clear()
