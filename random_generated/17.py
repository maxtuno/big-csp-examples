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
	x16 = big_csp.Entity(encoder)

	big_csp.Constraint(0 <= x0 <= 13)
	big_csp.Constraint(3 <= x1 <= 23)
	big_csp.Constraint(1 <= x2 <= 23)
	big_csp.Constraint(2 <= x3 <= 10)
	big_csp.Constraint(0 <= x4 <= 13)
	big_csp.Constraint(0 <= x5 <= 14)
	big_csp.Constraint(2 <= x6 <= 11)
	big_csp.Constraint(2 <= x7 <= 6)
	big_csp.Constraint(1 <= x8 <= 22)
	big_csp.Constraint(3 <= x9 <= 27)
	big_csp.Constraint(1 <= x10 <= 11)
	big_csp.Constraint(2 <= x11 <= 21)
	big_csp.Constraint(1 <= x12 <= 10)
	big_csp.Constraint(0 <= x13 <= 6)
	big_csp.Constraint(2 <= x14 <= 4)
	big_csp.Constraint(0 <= x15 <= 5)
	big_csp.Constraint(0 <= x16 <= 24)

	big_csp.Constraint(optimal < x13 * x15 + 3 * x14 + x6 + x2 * 4 * x7 + x10 * x8 + 3 * x2 + x12 + x13 * x3 ** 2 + x16 * x14 + x5 ** 2 + x13 + x7 * x4 ** 3 + x16 * x4 + 2 * x14 + x16 * x9 + x11 ** 3)

	big_csp.Constraint(x7 + x8 * 3 * x5 + x13 * x10 + 2 * x1 + x13 + x16 * x9 ** 2 + x10 + x2 * 3 * x12 <= 256)

	big_csp.Constraint(x11 * x15 + 2 * x4 + x0 * x1 + 4 * x0 + x10 + x14 * 3 * x15 + x8 * x0 + 2 * x11 <= 182)

	big_csp.Constraint(x7 + x6 * x11 ** 3 + x13 + x3 * 4 * x16 + x11 * x7 + 4 * x12 + x10 + x10 * 3 * x1 <= 21)

	big_csp.Constraint(x7 + x14 * 3 * x1 + x8 * x3 + 2 * x7 + x3 + x6 * 3 * x1 + x2 + x7 * x12 ** 4 <= 135)

	solver = big_csp.Solver()
	if solver.satisfy([x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16]):
		optimal = x13 * x15 + 3 * x14 + x6 + x2 * 4 * x7 + x10 * x8 + 3 * x2 + x12 + x13 * x3 ** 2 + x16 * x14 + x5 ** 2 + x13 + x7 * x4 ** 3 + x16 * x4 + 2 * x14 + x16 * x9 + x11 ** 3 
		print(optimal, '=>', x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16)
	else:
		break

	solver.clear()
