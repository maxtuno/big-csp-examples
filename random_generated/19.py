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
	x17 = big_csp.Entity(encoder)
	x18 = big_csp.Entity(encoder)

	big_csp.Constraint(4 <= x0 <= 50)
	big_csp.Constraint(1 <= x1 <= 40)
	big_csp.Constraint(4 <= x2 <= 27)
	big_csp.Constraint(4 <= x3 <= 72)
	big_csp.Constraint(4 <= x4 <= 48)
	big_csp.Constraint(5 <= x5 <= 70)
	big_csp.Constraint(3 <= x6 <= 52)
	big_csp.Constraint(4 <= x7 <= 28)
	big_csp.Constraint(0 <= x8 <= 13)
	big_csp.Constraint(5 <= x9 <= 50)
	big_csp.Constraint(3 <= x10 <= 6)
	big_csp.Constraint(4 <= x11 <= 28)
	big_csp.Constraint(2 <= x12 <= 49)
	big_csp.Constraint(4 <= x13 <= 31)
	big_csp.Constraint(1 <= x14 <= 71)
	big_csp.Constraint(3 <= x15 <= 17)
	big_csp.Constraint(2 <= x16 <= 48)
	big_csp.Constraint(0 <= x17 <= 5)
	big_csp.Constraint(3 <= x18 <= 73)

	big_csp.Constraint(optimal < x4 + x18 * 2 * x7 + x5 * x15 + x15 ** 4 + x4 * x13 + 3 * x4 + x10 + x11 * x0 ** 4 + x4 * x11 + x11 ** 4 + x2 * x16 + 4 * x11 + x16 + x0 * x4 ** 2 + x0 + x17 * x14 ** 3 + x0 + x4 * x15 ** 3)

	big_csp.Constraint(x10 + x3 * x14 ** 3 + x18 * x11 + x10 ** 4 + x18 + x9 * 3 * x18 + x3 + x9 * x12 ** 4 <= 93)

	big_csp.Constraint(x5 * x10 + 2 * x12 + x2 + x6 * 2 * x7 + x3 + x14 * x16 ** 4 + x13 * x1 + 3 * x10 <= 37)

	big_csp.Constraint(x5 * x1 + x11 ** 2 + x1 * x13 + x3 ** 3 + x3 * x0 + 3 * x16 + x17 * x5 + x11 ** 3 <= 303)

	big_csp.Constraint(x3 + x6 * 4 * x14 + x9 + x14 * 4 * x16 + x17 + x15 * x14 ** 4 + x13 + x10 * 3 * x10 <= 165)

	solver = big_csp.Solver()
	if solver.satisfy([x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18]):
		optimal = x4 + x18 * 2 * x7 + x5 * x15 + x15 ** 4 + x4 * x13 + 3 * x4 + x10 + x11 * x0 ** 4 + x4 * x11 + x11 ** 4 + x2 * x16 + 4 * x11 + x16 + x0 * x4 ** 2 + x0 + x17 * x14 ** 3 + x0 + x4 * x15 ** 3 
		print(optimal, '=>', x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18)
	else:
		break

	solver.clear()
