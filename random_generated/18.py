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

	big_csp.Constraint(1 <= x0 <= 23)
	big_csp.Constraint(3 <= x1 <= 4)
	big_csp.Constraint(1 <= x2 <= 17)
	big_csp.Constraint(2 <= x3 <= 14)
	big_csp.Constraint(2 <= x4 <= 15)
	big_csp.Constraint(0 <= x5 <= 5)
	big_csp.Constraint(2 <= x6 <= 22)
	big_csp.Constraint(0 <= x7 <= 25)
	big_csp.Constraint(2 <= x8 <= 24)
	big_csp.Constraint(2 <= x9 <= 9)
	big_csp.Constraint(3 <= x10 <= 3)
	big_csp.Constraint(2 <= x11 <= 13)
	big_csp.Constraint(2 <= x12 <= 29)
	big_csp.Constraint(0 <= x13 <= 26)
	big_csp.Constraint(2 <= x14 <= 10)
	big_csp.Constraint(1 <= x15 <= 11)
	big_csp.Constraint(0 <= x16 <= 21)
	big_csp.Constraint(3 <= x17 <= 31)

	big_csp.Constraint(optimal < x8 + x8 * 3 * x5 + x11 * x13 + 3 * x9 + x9 * x1 + 2 * x12 + x5 * x16 + x2 ** 3 + x11 * x6 + 4 * x10 + x12 * x16 + 2 * x3 + x7 * x4 + 2 * x13 + x16 * x12 + x13 ** 4 + x5 * x8 + 3 * x15)

	big_csp.Constraint(x9 * x9 + x8 ** 3 + x10 + x13 * 3 * x1 + x12 * x3 + x5 ** 4 + x14 + x10 * 3 * x13 <= 200)

	big_csp.Constraint(x4 + x15 * 4 * x15 + x10 + x11 * 2 * x2 + x16 * x9 + 4 * x14 + x5 * x2 + x7 ** 3 <= 159)

	big_csp.Constraint(x12 + x17 * x7 ** 4 + x5 * x16 + x17 ** 2 + x16 * x5 + x4 ** 4 + x6 * x12 + x6 ** 4 <= 62)

	big_csp.Constraint(x4 + x6 * x17 ** 2 + x12 * x0 + 2 * x3 + x9 * x15 + 4 * x6 + x15 + x12 * x11 ** 4 <= 179)

	solver = big_csp.Solver()
	if solver.satisfy([x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17]):
		optimal = x8 + x8 * 3 * x5 + x11 * x13 + 3 * x9 + x9 * x1 + 2 * x12 + x5 * x16 + x2 ** 3 + x11 * x6 + 4 * x10 + x12 * x16 + 2 * x3 + x7 * x4 + 2 * x13 + x16 * x12 + x13 ** 4 + x5 * x8 + 3 * x15 
		print(optimal, '=>', x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17)
	else:
		break

	solver.clear()
