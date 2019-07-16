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
	x20 = big_csp.Entity(encoder)
	x21 = big_csp.Entity(encoder)

	big_csp.Constraint(7 <= x0 <= 23)
	big_csp.Constraint(2 <= x1 <= 68)
	big_csp.Constraint(5 <= x2 <= 51)
	big_csp.Constraint(7 <= x3 <= 55)
	big_csp.Constraint(0 <= x4 <= 42)
	big_csp.Constraint(6 <= x5 <= 18)
	big_csp.Constraint(4 <= x6 <= 36)
	big_csp.Constraint(7 <= x7 <= 53)
	big_csp.Constraint(7 <= x8 <= 89)
	big_csp.Constraint(7 <= x9 <= 21)
	big_csp.Constraint(8 <= x10 <= 27)
	big_csp.Constraint(5 <= x11 <= 18)
	big_csp.Constraint(1 <= x12 <= 62)
	big_csp.Constraint(0 <= x13 <= 51)
	big_csp.Constraint(5 <= x14 <= 59)
	big_csp.Constraint(4 <= x15 <= 27)
	big_csp.Constraint(3 <= x16 <= 70)
	big_csp.Constraint(6 <= x17 <= 17)
	big_csp.Constraint(2 <= x18 <= 16)
	big_csp.Constraint(7 <= x19 <= 60)
	big_csp.Constraint(0 <= x20 <= 61)
	big_csp.Constraint(6 <= x21 <= 32)

	big_csp.Constraint(optimal < x4 + x14 * x19 ** 4 + x11 * x7 + 2 * x16 + x7 * x13 + 3 * x8 + x7 + x9 * 3 * x1 + x9 * x19 + x21 ** 3 + x1 + x0 * x8 ** 2 + x21 + x16 * x20 ** 4 + x12 + x16 * x16 ** 3 + x2 * x8 + 3 * x7 + x8 * x20 + x18 ** 4 + x8 * x15 + x14 ** 3)

	big_csp.Constraint(x19 + x9 * x1 ** 5 + x6 * x2 + x11 ** 4 + x15 * x19 + x10 ** 4 + x15 + x15 * x14 ** 5 + x14 * x13 + x1 ** 2 <= 69)

	big_csp.Constraint(x4 + x21 * x0 ** 5 + x21 * x7 + x17 ** 3 + x15 * x12 + 4 * x10 + x14 + x9 * x8 ** 5 + x12 + x10 * 4 * x1 <= 429)

	big_csp.Constraint(x8 + x3 * x16 ** 3 + x10 + x13 * x9 ** 5 + x18 + x20 * 4 * x12 + x13 * x4 + 2 * x1 + x9 + x13 * 4 * x16 <= 169)

	big_csp.Constraint(x4 + x11 * x20 ** 5 + x8 + x18 * 4 * x3 + x1 * x4 + 3 * x7 + x5 + x20 * x18 ** 4 + x7 * x12 + x21 ** 4 <= 364)

	big_csp.Constraint(x20 * x21 + 3 * x0 + x5 * x5 + x20 ** 4 + x3 + x1 * x2 ** 3 + x20 + x0 * 3 * x0 + x7 * x10 + 3 * x12 <= 68)

	solver = big_csp.Solver()
	if solver.satisfy([x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21]):
		optimal = x4 + x14 * x19 ** 4 + x11 * x7 + 2 * x16 + x7 * x13 + 3 * x8 + x7 + x9 * 3 * x1 + x9 * x19 + x21 ** 3 + x1 + x0 * x8 ** 2 + x21 + x16 * x20 ** 4 + x12 + x16 * x16 ** 3 + x2 * x8 + 3 * x7 + x8 * x20 + x18 ** 4 + x8 * x15 + x14 ** 3 
		print(optimal, '=>', x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21)
	else:
		break

	solver.clear()
