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
	x19 = big_csp.Entity(encoder)

	big_csp.Constraint(2 <= x0 <= 25)
	big_csp.Constraint(1 <= x1 <= 16)
	big_csp.Constraint(2 <= x2 <= 28)
	big_csp.Constraint(0 <= x3 <= 26)
	big_csp.Constraint(5 <= x4 <= 14)
	big_csp.Constraint(3 <= x5 <= 31)
	big_csp.Constraint(1 <= x6 <= 11)
	big_csp.Constraint(3 <= x7 <= 32)
	big_csp.Constraint(0 <= x8 <= 27)
	big_csp.Constraint(2 <= x9 <= 10)
	big_csp.Constraint(5 <= x10 <= 11)
	big_csp.Constraint(0 <= x11 <= 25)
	big_csp.Constraint(0 <= x12 <= 10)
	big_csp.Constraint(3 <= x13 <= 29)
	big_csp.Constraint(0 <= x14 <= 14)
	big_csp.Constraint(0 <= x15 <= 17)
	big_csp.Constraint(6 <= x16 <= 25)
	big_csp.Constraint(1 <= x17 <= 9)
	big_csp.Constraint(2 <= x18 <= 25)
	big_csp.Constraint(2 <= x19 <= 14)

	big_csp.Constraint(optimal < x4 * x3 + 5 * x18 + x10 * x8 + x19 ** 3 + x18 * x8 + 4 * x1 + x15 * x7 + x10 ** 5 + x4 * x1 + 5 * x13 + x4 * x16 + 5 * x8 + x3 * x4 + x18 ** 3 + x10 + x16 * 4 * x4 + x3 * x9 + x6 ** 2 + x17 + x10 * x7 ** 2)

	big_csp.Constraint(x6 + x0 * x9 ** 2 + x0 * x17 + x17 ** 5 + x12 * x18 + x12 ** 5 + x0 * x16 + x15 ** 5 + x15 + x8 * 2 * x3 <= 276)

	big_csp.Constraint(x19 + x0 * x16 ** 2 + x7 + x9 * 4 * x11 + x9 * x16 + x4 ** 3 + x6 * x16 + 5 * x2 + x6 * x2 + x10 ** 5 <= 108)

	big_csp.Constraint(x10 * x4 + x4 ** 5 + x12 + x11 * x4 ** 5 + x10 * x11 + 4 * x11 + x6 * x2 + x15 ** 3 + x19 * x5 + x10 ** 4 <= 141)

	big_csp.Constraint(x0 + x13 * 3 * x13 + x15 * x1 + x10 ** 2 + x14 + x15 * 2 * x10 + x16 * x13 + 3 * x17 + x16 * x5 + 3 * x5 <= 237)

	big_csp.Constraint(x18 * x6 + x4 ** 3 + x18 + x3 * 3 * x8 + x8 * x19 + x5 ** 3 + x7 + x15 * x1 ** 3 + x17 * x5 + 5 * x18 <= 372)

	solver = big_csp.Solver()
	if solver.satisfy([x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19]):
		optimal = x4 * x3 + 5 * x18 + x10 * x8 + x19 ** 3 + x18 * x8 + 4 * x1 + x15 * x7 + x10 ** 5 + x4 * x1 + 5 * x13 + x4 * x16 + 5 * x8 + x3 * x4 + x18 ** 3 + x10 + x16 * 4 * x4 + x3 * x9 + x6 ** 2 + x17 + x10 * x7 ** 2 
		print(optimal, '=>', x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19)
	else:
		break

	solver.clear()
