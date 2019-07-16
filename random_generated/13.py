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

	big_csp.Constraint(9 <= x0 <= 30)
	big_csp.Constraint(1 <= x1 <= 65)
	big_csp.Constraint(9 <= x2 <= 17)
	big_csp.Constraint(0 <= x3 <= 54)
	big_csp.Constraint(1 <= x4 <= 18)
	big_csp.Constraint(10 <= x5 <= 31)
	big_csp.Constraint(1 <= x6 <= 60)
	big_csp.Constraint(1 <= x7 <= 33)
	big_csp.Constraint(6 <= x8 <= 30)
	big_csp.Constraint(9 <= x9 <= 36)
	big_csp.Constraint(8 <= x10 <= 26)
	big_csp.Constraint(7 <= x11 <= 31)
	big_csp.Constraint(4 <= x12 <= 10)

	big_csp.Constraint(optimal < x2 * x0 + x11 ** 2 + x9 + x3 * x4 ** 3 + x9 + x9 * 3 * x3 + x4 * x2 + 2 * x1 + x5 + x9 * 2 * x10 + x2 + x6 * 3 * x9)

	big_csp.Constraint(x4 + x7 * x4 ** 3 + x0 * x12 + x8 ** 3 + x8 + x8 * 2 * x4 <= 15)

	big_csp.Constraint(x10 + x6 * x4 ** 2 + x2 + x12 * 3 * x10 + x2 * x10 + x1 ** 2 <= 147)

	big_csp.Constraint(x9 + x8 * 3 * x7 + x4 * x11 + x0 ** 2 + x11 + x11 * 2 * x2 <= 130)

	solver = big_csp.Solver()
	if solver.satisfy([x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12]):
		optimal = x2 * x0 + x11 ** 2 + x9 + x3 * x4 ** 3 + x9 + x9 * 3 * x3 + x4 * x2 + 2 * x1 + x5 + x9 * 2 * x10 + x2 + x6 * 3 * x9 
		print(optimal, '=>', x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12)
	else:
		break

	solver.clear()
