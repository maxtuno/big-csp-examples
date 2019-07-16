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

	big_csp.Constraint(0 <= x0 <= 48)
	big_csp.Constraint(0 <= x1 <= 40)
	big_csp.Constraint(2 <= x2 <= 74)
	big_csp.Constraint(2 <= x3 <= 61)
	big_csp.Constraint(0 <= x4 <= 10)
	big_csp.Constraint(1 <= x5 <= 77)
	big_csp.Constraint(1 <= x6 <= 8)
	big_csp.Constraint(0 <= x7 <= 78)
	big_csp.Constraint(1 <= x8 <= 5)
	big_csp.Constraint(2 <= x9 <= 58)

	big_csp.Constraint(optimal < x1 + x2 * x7 ** 2 + x0 * x1 + x2 ** 2 + x5 + x6 * 2 * x8 + x7 + x5 * x6 ** 2 + x9 * x0 + x1 ** 2)

	big_csp.Constraint(x5 * x5 + x5 ** 2 + x4 + x2 * 2 * x2 <= 82)

	big_csp.Constraint(x3 + x4 * 2 * x0 + x3 * x7 + x5 ** 2 <= 100)

	solver = big_csp.Solver()
	if solver.satisfy([x0, x1, x2, x3, x4, x5, x6, x7, x8, x9]):
		optimal = x1 + x2 * x7 ** 2 + x0 * x1 + x2 ** 2 + x5 + x6 * 2 * x8 + x7 + x5 * x6 ** 2 + x9 * x0 + x1 ** 2 
		print(optimal, '=>', x0, x1, x2, x3, x4, x5, x6, x7, x8, x9)
	else:
		break

	solver.clear()
