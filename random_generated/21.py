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

	big_csp.Constraint(4 <= x0 <= 27)
	big_csp.Constraint(1 <= x1 <= 24)
	big_csp.Constraint(1 <= x2 <= 11)
	big_csp.Constraint(3 <= x3 <= 17)
	big_csp.Constraint(0 <= x4 <= 45)
	big_csp.Constraint(0 <= x5 <= 56)
	big_csp.Constraint(2 <= x6 <= 44)
	big_csp.Constraint(6 <= x7 <= 8)
	big_csp.Constraint(5 <= x8 <= 36)
	big_csp.Constraint(0 <= x9 <= 29)
	big_csp.Constraint(5 <= x10 <= 11)
	big_csp.Constraint(3 <= x11 <= 24)
	big_csp.Constraint(1 <= x12 <= 43)
	big_csp.Constraint(1 <= x13 <= 56)
	big_csp.Constraint(3 <= x14 <= 51)
	big_csp.Constraint(6 <= x15 <= 47)
	big_csp.Constraint(3 <= x16 <= 15)
	big_csp.Constraint(4 <= x17 <= 53)
	big_csp.Constraint(6 <= x18 <= 42)
	big_csp.Constraint(3 <= x19 <= 8)
	big_csp.Constraint(0 <= x20 <= 47)

	big_csp.Constraint(optimal < x18 + x12 * 2 * x18 + x13 + x2 * x13 ** 4 + x4 * x8 + x6 ** 5 + x12 + x0 * 3 * x12 + x9 * x12 + x16 ** 4 + x3 + x12 * x18 ** 2 + x17 * x7 + x5 ** 4 + x0 + x13 * x18 ** 4 + x10 * x8 + 4 * x3 + x4 + x15 * 5 * x0)

	big_csp.Constraint(x6 * x17 + x18 ** 2 + x12 + x2 * x5 ** 4 + x10 + x15 * 3 * x2 + x4 + x12 * 3 * x16 + x15 + x11 * x10 ** 5 <= 249)

	big_csp.Constraint(x16 * x10 + 2 * x14 + x14 + x6 * 5 * x7 + x15 + x11 * x4 ** 4 + x10 + x4 * 3 * x4 + x12 * x2 + x6 ** 2 <= 105)

	big_csp.Constraint(x17 * x2 + 2 * x16 + x15 * x6 + 2 * x4 + x20 * x11 + x7 ** 2 + x5 * x9 + x8 ** 4 + x8 * x5 + 4 * x11 <= 169)

	big_csp.Constraint(x19 + x7 * x10 ** 2 + x9 + x12 * x7 ** 2 + x10 * x8 + x4 ** 3 + x7 * x0 + x9 ** 3 + x10 + x3 * x10 ** 5 <= 354)

	big_csp.Constraint(x14 + x8 * 4 * x14 + x1 * x6 + 2 * x19 + x12 * x16 + x18 ** 4 + x1 + x10 * 5 * x1 + x18 * x15 + x1 ** 4 <= 134)

	solver = big_csp.Solver()
	if solver.satisfy([x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20]):
		optimal = x18 + x12 * 2 * x18 + x13 + x2 * x13 ** 4 + x4 * x8 + x6 ** 5 + x12 + x0 * 3 * x12 + x9 * x12 + x16 ** 4 + x3 + x12 * x18 ** 2 + x17 * x7 + x5 ** 4 + x0 + x13 * x18 ** 4 + x10 * x8 + 4 * x3 + x4 + x15 * 5 * x0 
		print(optimal, '=>', x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20)
	else:
		break

	solver.clear()
