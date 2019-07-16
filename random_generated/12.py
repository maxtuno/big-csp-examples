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

	big_csp.Constraint(0 <= x0 <= 1)
	big_csp.Constraint(0 <= x1 <= 14)
	big_csp.Constraint(0 <= x2 <= 42)
	big_csp.Constraint(1 <= x3 <= 28)
	big_csp.Constraint(1 <= x4 <= 21)
	big_csp.Constraint(1 <= x5 <= 21)
	big_csp.Constraint(1 <= x6 <= 4)
	big_csp.Constraint(0 <= x7 <= 38)
	big_csp.Constraint(0 <= x8 <= 14)
	big_csp.Constraint(1 <= x9 <= 20)
	big_csp.Constraint(1 <= x10 <= 39)
	big_csp.Constraint(0 <= x11 <= 42)

	big_csp.Constraint(optimal < x8 + x6 * x11 ** 2 + x7 * x1 + 2 * x0 + x11 * x0 + x4 ** 3 + x0 + x0 * x8 ** 2 + x1 + x9 * x7 ** 2 + x2 * x3 + 2 * x2)

	big_csp.Constraint(x9 + x3 * 2 * x0 + x4 * x0 + 2 * x2 + x1 * x5 + x11 ** 3 <= 97)

	big_csp.Constraint(x7 + x2 * 3 * x7 + x5 + x2 * 2 * x7 + x10 * x11 + x4 ** 2 <= 79)

	big_csp.Constraint(x7 * x2 + 2 * x5 + x2 * x6 + 3 * x4 + x9 * x3 + x9 ** 2 <= 105)

	solver = big_csp.Solver()
	if solver.satisfy([x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11]):
		optimal = x8 + x6 * x11 ** 2 + x7 * x1 + 2 * x0 + x11 * x0 + x4 ** 3 + x0 + x0 * x8 ** 2 + x1 + x9 * x7 ** 2 + x2 * x3 + 2 * x2 
		print(optimal, '=>', x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11)
	else:
		break

	solver.clear()
