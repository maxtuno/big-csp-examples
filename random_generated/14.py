import big_csp

optimal = 0
while True:
	encoder = big_csp.Encoder(bits=32)

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

	big_csp.Constraint(0 <= x0 <= 34)
	big_csp.Constraint(0 <= x1 <= 23)
	big_csp.Constraint(1 <= x2 <= 17)
	big_csp.Constraint(1 <= x3 <= 16)
	big_csp.Constraint(0 <= x4 <= 20)
	big_csp.Constraint(1 <= x5 <= 16)
	big_csp.Constraint(1 <= x6 <= 24)
	big_csp.Constraint(1 <= x7 <= 6)
	big_csp.Constraint(1 <= x8 <= 25)
	big_csp.Constraint(0 <= x9 <= 34)
	big_csp.Constraint(1 <= x10 <= 6)
	big_csp.Constraint(0 <= x11 <= 28)
	big_csp.Constraint(0 <= x12 <= 29)
	big_csp.Constraint(1 <= x13 <= 19)

	big_csp.Constraint(optimal < x12 + x11 * 3 * x7 + x0 * x5 + 3 * x2 + x5 + x13 * 2 * x8 + x7 + x5 * 3 * x7 + x7 + x6 * 3 * x9 + x13 + x1 * 3 * x5 + x4 + x1 * x9 ** 3)

	big_csp.Constraint(x2 * x9 + 3 * x12 + x3 * x2 + 2 * x1 + x10 + x0 * 2 * x2 <= 118)

	big_csp.Constraint(x3 + x0 * x13 ** 3 + x4 * x0 + x8 ** 3 + x5 * x10 + 3 * x11 <= 41)

	big_csp.Constraint(x7 * x13 + x5 ** 3 + x12 + x11 * 3 * x4 + x13 * x4 + x12 ** 2 <= 43)

	solver = big_csp.Solver()
	if solver.satisfy([x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13]):
		optimal = x12 + x11 * 3 * x7 + x0 * x5 + 3 * x2 + x5 + x13 * 2 * x8 + x7 + x5 * 3 * x7 + x7 + x6 * 3 * x9 + x13 + x1 * 3 * x5 + x4 + x1 * x9 ** 3 
		print(optimal, '=>', x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13)
	else:
		break

	solver.clear()
