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
	x15 = big_csp.Entity(encoder)

	big_csp.Constraint(5 <= x0 <= 71)
	big_csp.Constraint(2 <= x1 <= 22)
	big_csp.Constraint(0 <= x2 <= 51)
	big_csp.Constraint(6 <= x3 <= 47)
	big_csp.Constraint(0 <= x4 <= 34)
	big_csp.Constraint(0 <= x5 <= 44)
	big_csp.Constraint(1 <= x6 <= 73)
	big_csp.Constraint(0 <= x7 <= 24)
	big_csp.Constraint(4 <= x8 <= 34)
	big_csp.Constraint(0 <= x9 <= 43)
	big_csp.Constraint(7 <= x10 <= 24)
	big_csp.Constraint(0 <= x11 <= 50)
	big_csp.Constraint(5 <= x12 <= 24)
	big_csp.Constraint(4 <= x13 <= 57)
	big_csp.Constraint(5 <= x14 <= 66)
	big_csp.Constraint(6 <= x15 <= 7)

	big_csp.Constraint(optimal < x15 + x9 * 2 * x5 + x11 * x1 + x11 ** 4 + x11 + x11 * x14 ** 3 + x0 * x10 + 4 * x4 + x6 * x14 + x7 ** 2 + x4 + x7 * 3 * x6 + x3 * x3 + 3 * x6 + x0 + x4 * 3 * x5)

	big_csp.Constraint(x3 * x3 + x3 ** 2 + x12 + x7 * 4 * x13 + x12 * x6 + 4 * x4 + x2 * x2 + x15 ** 3 <= 157)

	big_csp.Constraint(x9 + x11 * x10 ** 3 + x9 * x13 + x5 ** 3 + x6 + x10 * 2 * x5 + x3 + x15 * 3 * x12 <= 234)

	big_csp.Constraint(x2 + x5 * x3 ** 4 + x13 + x13 * x7 ** 4 + x8 * x4 + 3 * x1 + x1 * x13 + 2 * x10 <= 57)

	big_csp.Constraint(x9 * x6 + x13 ** 4 + x3 * x10 + 3 * x10 + x2 * x8 + x8 ** 2 + x2 + x1 * x0 ** 4 <= 80)

	solver = big_csp.Solver()
	if solver.satisfy([x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15]):
		optimal = x15 + x9 * 2 * x5 + x11 * x1 + x11 ** 4 + x11 + x11 * x14 ** 3 + x0 * x10 + 4 * x4 + x6 * x14 + x7 ** 2 + x4 + x7 * 3 * x6 + x3 * x3 + 3 * x6 + x0 + x4 * 3 * x5 
		print(optimal, '=>', x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15)
	else:
		break

	solver.clear()
