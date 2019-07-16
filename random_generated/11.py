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

	big_csp.Constraint(1 <= x0 <= 31)
	big_csp.Constraint(0 <= x1 <= 35)
	big_csp.Constraint(1 <= x2 <= 74)
	big_csp.Constraint(2 <= x3 <= 72)
	big_csp.Constraint(3 <= x4 <= 19)
	big_csp.Constraint(1 <= x5 <= 62)
	big_csp.Constraint(1 <= x6 <= 10)
	big_csp.Constraint(3 <= x7 <= 44)
	big_csp.Constraint(3 <= x8 <= 27)
	big_csp.Constraint(0 <= x9 <= 38)
	big_csp.Constraint(2 <= x10 <= 11)

	big_csp.Constraint(optimal < x5 * x2 + 2 * x0 + x5 + x5 * 2 * x7 + x1 + x2 * x0 ** 2 + x2 * x5 + x9 ** 2 + x6 + x5 * 2 * x3)

	big_csp.Constraint(x7 + x1 * x1 ** 2 + x2 + x5 * 2 * x1 <= 102)

	big_csp.Constraint(x3 * x7 + 2 * x2 + x7 * x3 + x4 ** 2 <= 15)

	solver = big_csp.Solver()
	if solver.satisfy([x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10]):
		optimal = x5 * x2 + 2 * x0 + x5 + x5 * 2 * x7 + x1 + x2 * x0 ** 2 + x2 * x5 + x9 ** 2 + x6 + x5 * 2 * x3 
		print(optimal, '=>', x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10)
	else:
		break

	solver.clear()
